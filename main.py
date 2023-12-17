# Copyright (c) ByteDance, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import argparse
import os
import sys
import datetime
import time
import math
import json
import numpy as np
import utils
import models
import torch
import torch.nn as nn
import torch.distributed as dist
import torch.backends.cudnn as cudnn
import torch.nn.functional as F

from pathlib import Path
from PIL import Image
from torchvision import datasets, transforms
from torchvision.transforms import InterpolationMode
from tensorboardX import SummaryWriter
from models.head import Head
from models.clipmodel import ClipBaseModel,build_clip


def get_args_parser():
    parser = argparse.ArgumentParser('VehicleMAE', add_help=False)

    # Model parameters
    parser.add_argument('--arch', default='mae_vit_base_patch16', type=str,
        choices=['mae_vit_base_patch16', 'mae_vit_large_patch16', 'mae_vit_huge_patch14'],
        help="""Name of architecture to train. For quick experiments with ViTs,
        we recommend using vit_tiny or vit_small.""")
    parser.add_argument('--patch_size', default=16, type=int, help="""Size in pixels
        of input square patches - default 16 (for 16x16 patches). Using smaller
        values leads to better performance but requires more memory. Applies only
        for ViTs (vit_tiny, vit_small and vit_base). If <16, we recommend disabling
        mixed precision training (--use_fp16 false) to avoid unstabilities.""")
    parser.add_argument('--out_dim', default=8192, type=int, help="""Dimensionality of
        output for [CLS] token.""")
    parser.add_argument('--patch_out_dim', default=8192, type=int, help="""Dimensionality of
        output for patch tokens.""")
    parser.add_argument('--shared_head', default=False, type=utils.bool_flag, help="""Wether to share 
        the same head for [CLS] token output and patch tokens output. When set to false, patch_out_dim
        is ignored and enforced to be same with out_dim. (Default: False)""")
    parser.add_argument('--shared_head_teacher', default=True, type=utils.bool_flag, help="""See above.
        Only works for teacher model. (Defeault: True)""")
    parser.add_argument('--norm_last_layer', default=True, type=utils.bool_flag,
        help="""Whether or not to weight normalize the last layer of the head.
        Not normalizing leads to better performance but can make the training unstable.
        In our experiments, we typically set this paramater to False with vit_small and True with vit_base.""")
    parser.add_argument('--momentum_teacher', default=0.996, type=float, help="""Base EMA
        parameter for teacher update. The value is increased to 1 during training with cosine schedule.
        We recommend setting a higher value with small batches: for example use 0.9995 with batch size of 256.""")
    parser.add_argument('--norm_in_head', default=None,
        help="Whether to use batch normalizations in projection head (Default: None)")
    parser.add_argument('--act_in_head', default='gelu',
        help="Whether to use batch normalizations in projection head (Default: gelu)")
    parser.add_argument('--use_masked_im_modeling', default=True, type=utils.bool_flag,
        help="Whether to use masked image modeling (mim) in backbone (Default: True)")
    parser.add_argument('--pred_ratio', default=0.3, type=float, nargs='+', help="""Ratio of partial prediction.
        If a list of ratio is specified, one of them will be randomly choosed for each patch.""")
    parser.add_argument('--pred_ratio_var', default=0, type=float, nargs='+', help="""Variance of partial prediction
        ratio. Length should be indentical to the length of pred_ratio. 0 for disabling. """)
    parser.add_argument('--pred_shape', default='block', type=str, help="""Shape of partial prediction.""")
    parser.add_argument('--pred_start_epoch', default=0, type=int, help="""Start epoch to perform masked
        image prediction. We typically set this to 50 for swin transformer. (Default: 0)""")
    parser.add_argument('--lambda1', default=1.0, type=float, help="""loss weight for dino
        loss over [CLS] tokens (Default: 1.0)""")
    parser.add_argument('--lambda2', default=1.0, type=float, help="""loss weight for beit 
        loss over masked patch tokens (Default: 1.0)""")
    parser.add_argument('--norm_pix_loss', action='store_true',
                        help='Use (per-patch) normalized pixels as targets for computing loss')
    parser.set_defaults(norm_pix_loss=False)
    parser.add_argument('--input_size', default=224, type=int,
                        help='images input size')
    parser.add_argument('--pin_mem', action='store_true',
                        help='Pin CPU memory in DataLoader for more efficient (sometimes) transfer to GPU.')
    parser.add_argument('--no_pin_mem', action='store_false', dest='pin_mem')
    parser.set_defaults(pin_mem=True)
    parser.add_argument('--mask_ratio', default=0.75, type=float,
                        help='Masking ratio (percentage of removed patches).')
    parser.add_argument('--use_learnable_pos_emb', default=False,
                        type=str, help='masked strategy of video tokens/patches False')


    # Temperature teacher parameters
    parser.add_argument('--warmup_teacher_temp', default=0.04, type=float,
        help="""Initial value for the teacher temperature: 0.04 works well in most cases.
        Try decreasing it if the training loss does not decrease.""")
    parser.add_argument('--teacher_temp', default=0.04, type=float, help="""Final value (after linear warmup)
        of the teacher temperature. For most experiments, anything above 0.07 is unstable. We recommend
        starting with the default value of 0.04 and increase this slightly if needed.""")
    parser.add_argument('--warmup_teacher_patch_temp', default=0.04, type=float, help="""See 
        `--warmup_teacher_temp`""")
    parser.add_argument('--teacher_patch_temp', default=0.07, type=float, help=""""See 
        `--teacher_temp`""")
    parser.add_argument('--warmup_teacher_temp_epochs', default=30, type=int,
        help='Number of warmup epochs for the teacher temperature (Default: 30).')
    parser.add_argument('--tlayernorm', type=int, default=0, choices=[0, 1],
                        help="0: without teache rlayernorm \
                            1:with vit original self.norm")

    # Training/Optimization parameters
    parser.add_argument('--use_fp16', type=utils.bool_flag, default=True, help="""Whether or not
        to use half precision for training. Improves training time and memory requirements,
        but can provoke instability and slight decay of performance. We recommend disabling
        mixed precision if the loss is unstable, if reducing the patch size or if training with bigger ViTs.""")    #True
    parser.add_argument('--weight_decay', type=float, default=0.04, help="""Initial value of the
        weight decay. With ViT, a smaller value at the beginning of training works well.""")
    parser.add_argument('--weight_decay_end', type=float, default=0.4, help="""Final value of the
        weight decay. We use a cosine schedule for WD and using a larger decay by
        the end of training improves performance for ViTs.""")
    parser.add_argument('--clip_grad', type=float, default=3.0, help="""Maximal parameter
        gradient norm if using gradient clipping. Clipping with norm .3 ~ 1.0 can
        help optimization for larger ViT architectures. 0 for disabling.""")
    parser.add_argument('--batch_size_per_gpu', default=128, type=int,
        help='Per-GPU batch-size : number of distinct images loaded on one GPU.')
    parser.add_argument('--epochs', default=300, type=int, help='Number of epochs of training.')
    parser.add_argument('--freeze_last_layer', default=1, type=int, help="""Number of epochs
        during which we keep the output layer fixed. Typically doing so during
        the first epoch helps training. Try increasing this value if the loss does not decrease.""")
    parser.add_argument("--lr", default=0.00025, type=float, help="""Learning rate at the end of  #0.0005
        linear warmup (highest LR used during training). The learning rate is linearly scaled
        with the batch size, and specified here for a reference batch size of 256.""")
    parser.add_argument("--warmup_epochs", default=10, type=int,
        help="Number of epochs for the linear learning-rate warm up.")
    parser.add_argument('--min_lr', type=float, default=1e-6, help="""Target LR at the      #1e-6
        end of optimization. We use a cosine LR schedule with linear warmup.""")
    parser.add_argument('--optimizer', default='adamw', type=str,
        choices=['adamw', 'sgd', 'lars'], help="""Type of optimizer. We recommend using adamw with ViTs.""")
    parser.add_argument('--load_from', default=None, help="""Path to load checkpoints to resume training.""")       #训练中断后加载之前训好的模型
    parser.add_argument('--drop_path', type=float, default=0.1, help="""Drop path rate for student network.""")

    #CLIP
    parser.add_argument('--clip_backbone', default='ViT-B-16', choices=['RN50', 'RN50x16', 'RN101', 'ViT-B-32', 'ViT-B-16'])


    # Multi-crop parameters
    parser.add_argument('--global_crops_number', type=int, default=2, help="""Number of global
        views to generate. Default is to use two global crops. """)
    parser.add_argument('--global_crops_scale', type=float, nargs='+', default=(0.14, 1.),
        help="""Scale range of the cropped image before resizing, relatively to the origin image.
        Used for large global view cropping. When disabling multi-crop (--local_crops_number 0), we
        recommand using a wider range of scale ("--global_crops_scale 0.14 1." for example)""")
    parser.add_argument('--local_crops_number', type=int, default=0, help="""Number of small
        local views to generate. Set this parameter to 0 to disable multi-crop training.
        When disabling multi-crop we recommend to use "--global_crops_scale 0.14 1." """)
    parser.add_argument('--local_crops_scale', type=float, nargs='+', default=(0.05, 0.4),
        help="""Scale range of the cropped image before resizing, relatively to the origin image.
        Used for small local view cropping of multi-crop.""")
    parser.add_argument('--device', default='cuda',
                        help='device to use for training / testing')

    # Learnable masking parameters
    parser.add_argument('--softmax_temp', type=float, default=1e-2, metavar='Learnable_Mask',
                        help='Softmax temp used to compute probability values for each patch')

    # Misc
    parser.add_argument('--data_path', default='/home/lcl_d/wuwentao/data', type=str,help='Please specify path to the ImageNet training data.')
    parser.add_argument('--output_dir', default="/home/lcl_d/wuwentao/VehicleMAE/output", type=str, help='Path to save logs and checkpoints.')
    parser.add_argument('--clip_pre_model', default="/home/lcl_d/wuwentao/maeclip/clip_pre_model/ViT-B-16.pt", type=str, help='clip pretrain model.')
    parser.add_argument('--saveckp_freq', default=50, type=int, help='Save checkpoint every x epochs.')
    parser.add_argument('--seed', default=0, type=int, help='Random seed.')
    parser.add_argument('--num_workers', default=8, type=int, help='Number of data loading workers per GPU.')
    parser.add_argument("--dist_url", default="env://", type=str, help="""url used to set up distributed training; see https://pytorch.org/docs/stable/distributed.html""")
    parser.add_argument("--local_rank", default=0, type=int, help="Please ignore and do not set this argument.")
    return parser

def train_vehicle(args):
    utils.init_distributed_mode(args)
    utils.fix_random_seeds(args.seed)
    print("git:\n  {}\n".format(utils.get_sha()))
    print("\n".join("%s: %s" % (k, str(v)) for k, v in sorted(dict(vars(args)).items())))
    cudnn.benchmark = True

    device = torch.device(args.device)
    
    # ============ preparing data ... ============
    transform_train = transforms.Compose([
            #随机截取一部分，然后Resize成224*224
            transforms.RandomResizedCrop(args.input_size, scale=(0.2, 1.0), interpolation=InterpolationMode.BICUBIC),   # 3 is bicubic
            #transforms.Resize([224,224]),
            #随机翻转
            transforms.RandomHorizontalFlip(),
            #将图像变为0~1的浮点数
            transforms.ToTensor(),
            #进行特定的均值，方差归一化（in）
            transforms.Normalize(mean=[0.446, 0.452, 0.466], std=[0.277, 0.278, 0.276])])   #[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
    #轮廓图像
    transform_lunkuo = transforms.Compose([
            #随机截取一部分，然后Resize成224*224
            transforms.RandomResizedCrop(args.input_size, scale=(0.2, 1.0), interpolation=InterpolationMode.BICUBIC),  # 3 is bicubic
            #transforms.Resize([224,224]),
            #随机翻转
            transforms.RandomHorizontalFlip(),
            #将图像变为0~1的浮点数
            transforms.ToTensor(),
            #将图像根目录传进去，将transform的操作传过去，dataset_train为正态分布后的数据
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    dataset_train = datasets.ImageFolder(os.path.join(args.data_path,'ourdata'), transform=transform_train)    #构建rgb数据
    dataset_lunkuo = datasets.ImageFolder(os.path.join(args.data_path,'oudata_lunkuo'), transform=transform_lunkuo)    #构建轮廓数据

    sampler_rgb = torch.utils.data.DistributedSampler(dataset_train, shuffle=True)
    sampler_lunkuo =  torch.utils.data.DistributedSampler(dataset_lunkuo, shuffle=True)
    np.random.seed(args.seed)
    data_loader_train = torch.utils.data.DataLoader(
        dataset_train, sampler=sampler_rgb,
        batch_size=args.batch_size_per_gpu,
        num_workers=args.num_workers,
        pin_memory=args.pin_mem,
        drop_last=True,
    )#从这拿到的都是minibatch
    np.random.seed(args.seed)
    data_loader_train_lunkuo = torch.utils.data.DataLoader(
        dataset_lunkuo, sampler=sampler_lunkuo,
        batch_size=args.batch_size_per_gpu,
        num_workers=args.num_workers,
        pin_memory=args.pin_mem,
        drop_last=True,
    )#从这拿到的都是minibatch


    print(f"Data loaded: there are {len(dataset_train)} images.")
    print(f"Data loaded: there are {len(dataset_lunkuo)} images.")

    # ============ building student,teacher_clip and teacher networks ... ============
    # we changed the name DeiT-S for ViT-S to avoid confusions

    clip_model, preprocess, text_features = build_clip(args)

    student = models.__dict__[args.arch](decoder_depth = 8,norm_pix_loss=args.norm_pix_loss)

    teacher = models.__dict__[args.arch](decoder_depth = 0,mask_ratio = 0)
    
    embed_dim = 512
    
    # multi-crop wrapper handles forward with inputs of different resolutions
    student = utils.MultiCropWrapper(student, Head(
        embed_dim,
        args.out_dim,
        patch_out_dim=args.patch_out_dim,
        norm=args.norm_in_head,
        act=args.act_in_head,
        norm_last_layer=args.norm_last_layer,
        shared_head=args.shared_head,
        use_learnable_pos_emb = args.use_learnable_pos_emb
    ))
    teacher = utils.MultiCropWrapper(teacher,Head(
        embed_dim, 
        args.out_dim,
        patch_out_dim=args.patch_out_dim,
        norm=args.norm_in_head,
        act=args.act_in_head,
        shared_head=args.shared_head_teacher,
    ),)
    teacher_clip = ClipBaseModel(
        clip_model,
        text_features,
    )

    student.to(device)
    teacher.to(device)
    teacher_clip.to(device)
    
    student_without_ddp = student
    
    if utils.has_batchnorms(student):
        student = nn.SyncBatchNorm.convert_sync_batchnorm(student)
        teacher = nn.SyncBatchNorm.convert_sync_batchnorm(teacher)
        teacher_clip = nn.SyncBatchNorm.convert_sync_batchnorm(teacher_clip)

        # we need DDP wrapper to have synchro batch norms working...我们需要 DDP 包装器才能使同步批处理规范正常工作...
        teacher = nn.parallel.DistributedDataParallel(teacher, device_ids=[args.gpu], broadcast_buffers=False,find_unused_parameters=False) 
        teacher_without_ddp = teacher.module
        student_without_ddp = student.module
        teacher_clip = nn.parallel.DistributedDataParallel(teacher_clip, device_ids=[args.gpu], broadcast_buffers=False,find_unused_parameters=False) 
        teacher_clip_without_ddp = teacher_clip.module
    else:
        # teacher_without_ddp and teacher are the same thing
        teacher_without_ddp = teacher
        teacher_clip_without_ddp = teacher_clip
    student = nn.parallel.DistributedDataParallel(student, device_ids=[args.gpu], broadcast_buffers=False,find_unused_parameters=False) 
    #教师和学生从相同权重开始
    teacher_without_ddp.load_state_dict(student.module.state_dict(), strict=False)
    #没有通过老师的反向传播，所以不需要梯度
    for p in teacher.parameters():
        p.requires_grad = False
    for p in teacher_clip.parameters():
        p.requires_grad = False
    print(f"Student and Teacher are built: they are both {args.arch} network.")

    # ============ preparing loss ... ============
    same_dim = args.shared_head or args.shared_head_teacher
    VehicleMAE_loss = VehicleMAELoss(
        args.out_dim,
        args.out_dim if same_dim else args.patch_out_dim,
        args.global_crops_number,
        args.local_crops_number,
        args.warmup_teacher_temp,
        args.teacher_temp,
        args.warmup_teacher_patch_temp,
        args.teacher_patch_temp,
        args.warmup_teacher_temp_epochs,
        args.epochs,
        lambda1=args.lambda1,
        lambda2=args.lambda2,
        mim_start_epoch=args.pred_start_epoch,
    ).cuda()

    if utils.is_main_process(): # Tensorboard configuration
        local_runs = os.path.join(args.output_dir, 'tf_logs')
        writer = SummaryWriter(logdir=local_runs)
        
    # ============ preparing optimizer ... ============
    params_groups = utils.get_params_groups(student)
    if args.optimizer == "adamw":
        optimizer = torch.optim.AdamW(params_groups)  # to use with ViTs
    elif args.optimizer == "sgd":
        optimizer = torch.optim.SGD(params_groups, lr=0, momentum=0.9)  # lr is set by scheduler
    elif args.optimizer == "lars":
        optimizer = utils.LARS(params_groups)  # to use with convnet and large batches
    # for mixed precision training
    fp16_scaler = None
    if args.use_fp16:
        fp16_scaler = torch.cuda.amp.GradScaler()

    # ============ init schedulers ... ============
    lr_schedule = utils.cosine_scheduler(
        args.lr * (args.batch_size_per_gpu * utils.get_world_size()) / 256,  # linear scaling rule
        args.min_lr,
        args.epochs, len(data_loader_train),
        warmup_epochs=args.warmup_epochs,
    )
    wd_schedule = utils.cosine_scheduler(
        args.weight_decay,
        args.weight_decay_end,
        args.epochs, len(data_loader_train),
    )
    # momentum parameter is increased to 1. during training with a cosine schedule
    momentum_schedule = utils.cosine_scheduler(args.momentum_teacher, 1,
                                            args.epochs, len(data_loader_train))
                  
    print(f"Loss, optimizer and schedulers ready.")

    # ============ optionally resume training ... ============
    to_restore = {"epoch": 0}
    if args.load_from:
        utils.restart_from_checkpoint(
            os.path.join(args.output_dir, args.load_from),
            run_variables=to_restore,
            student=student,
            teacher=teacher,
            optimizer=optimizer,
            fp16_scaler=fp16_scaler,
            vehiclemae_loss=VehicleMAE_loss,
        )
    start_epoch = to_restore["epoch"]

    start_time = time.time()
    print("Starting our training!")
    for epoch in range(start_epoch, args.epochs):
        data_loader_train.sampler.set_epoch(epoch)
        data_loader_train_lunkuo.sampler.set_epoch(epoch)

        # ============ training one epoch of iBOT ... ============
        
        train_stats = train_one_epoch(student, teacher,teacher_clip, teacher_without_ddp,teacher_clip_without_ddp, VehicleMAE_loss,
            data_loader_train,data_loader_train_lunkuo, optimizer, device,lr_schedule, wd_schedule, momentum_schedule,
            epoch, fp16_scaler, args)
        

        # ============ writing logs ... ============
        save_dict = {
            'student': student.state_dict(),
            'teacher': teacher.state_dict(),
            'teacher_clip': teacher_clip.state_dict(),
            'optimizer': optimizer.state_dict(),
            'epoch': epoch + 1,
            'args': args,
            'VehicleMAE_loss': VehicleMAE_loss.state_dict(),
        }
        if fp16_scaler is not None:
            save_dict['fp16_scaler'] = fp16_scaler.state_dict()
        utils.save_on_master(save_dict, os.path.join(args.output_dir, 'checkpoint.pth'))
        if args.output_dir and (epoch % 10 == 0 or epoch == args.epochs -1):
            utils.save_model(
                args=args, model=student, model_without_ddp=student_without_ddp, optimizer=optimizer,
                #args=args, model=student,  optimizer=optimizer,
                loss_scaler=VehicleMAE_loss, epoch=epoch)
        log_stats = {**{f'train_{k}': v for k, v in train_stats.items()},
                     'epoch': epoch}
        
        
        if utils.is_main_process():
            with (Path(args.output_dir) / "log.txt").open("a") as f:
                f.write(json.dumps(log_stats) + "\n")
                for k, v in train_stats.items():
                    writer.add_scalar(k, v, epoch)
        
    total_time = time.time() - start_time
    total_time_str = str(datetime.timedelta(seconds=int(total_time)))
    print('Training time {}'.format(total_time_str))


def train_one_epoch(student, teacher,teacher_clip, teacher_without_ddp,teacher_clip_without_ddp, VehicleMAE_loss, data_loader,data_loader_lunkuo,
                    optimizer, device: torch.device,lr_schedule, wd_schedule, momentum_schedule,epoch,
                    fp16_scaler, args):
  
    metric_logger = utils.MetricLogger(delimiter="  ")
    header = 'Epoch: [{}]'.format(epoch)
    
    # common params
    names_q, params_q, names_k, params_k,names_p,params_p = [], [], [], [],[],[]
    for name_q, param_q in student.module.named_parameters():
        names_q.append(name_q)
        params_q.append(param_q)
    for name_k, param_k in teacher_without_ddp.named_parameters():
        names_k.append(name_k)
        params_k.append(param_k)
    for name_p, param_p in teacher_clip_without_ddp.named_parameters():
        names_p.append(name_p)
        params_p.append(param_p)
    names_common = list(set(names_q) & set(names_k) & set(names_p))
    params_q = [param_q for name_q, param_q in zip(names_q, params_q) if name_q in names_common]
    params_k = [param_k for name_k, param_k in zip(names_k, params_k) if name_k in names_common]
    params_p = [param_p for name_p, param_p in zip(names_p, params_p) if name_p in names_common]

    for (it, (images, _)),( _, (images_lunkuo, _)) in zip(enumerate(metric_logger.log_every(data_loader, 20, header)),enumerate(metric_logger.log_every(data_loader_lunkuo, 20, header))):
        # update weight decay and learning rate according to their schedule
        it = len(data_loader) * epoch + it  # global training iteration
        for i, param_group in enumerate(optimizer.param_groups):
            param_group["lr"] = lr_schedule[it]
            if i == 0:  # only the first group is regularized
                param_group["weight_decay"] = wd_schedule[it]

        # move images to gpu      
        images = images.to(device, non_blocking=True)
        images_lunkuo =images_lunkuo.to(device, non_blocking=True)
        
        with torch.cuda.amp.autocast(fp16_scaler is not None):
            student_output,student_loss,masks,_,_,tezheng = student(images, mask_ratio=args.mask_ratio)
            teacher_output,_,_,_,_,_ = teacher(images_lunkuo,mask_ratio = 0)
            similarity_loss,kl_distance_loss = teacher_clip(images,tezheng)

            student_loss = ((student_loss * masks).sum() / masks.sum())*4

            masks = masks.type(torch.bool)
            all_loss = VehicleMAE_loss(student_output, teacher_output, masks, epoch,student_loss,similarity_loss,kl_distance_loss)
            loss = all_loss.pop('loss')

            #loss_value = loss.item()    #取具体的数值
            

        if not math.isfinite(loss.item()):
            print("Loss is {}, stopping training".format(loss.item()), force=True)
            sys.exit(1)

        # log statistics
        probs1 = teacher_output[0].chunk(args.global_crops_number)
        probs2 = student_output[0].chunk(args.global_crops_number)
        pred1 = utils.concat_all_gather(probs1[0].max(dim=1)[1]) 
        pred2 = utils.concat_all_gather(probs2[1].max(dim=1)[1])
        acc = (pred1 == pred2).sum() / pred1.size(0)

        optimizer.zero_grad()

        param_norms = None
        if fp16_scaler is None:
            loss.backward()
            if args.clip_grad:
                param_norms = utils.clip_gradients(student, args.clip_grad)
            utils.cancel_gradients_last_layer(epoch, student,
                                              args.freeze_last_layer)
            optimizer.step()
        else:
            fp16_scaler.scale(loss).backward()
            if args.clip_grad:
                
                fp16_scaler.unscale_(optimizer)  # unscale the gradients of optimizer's assigned params in-place
                param_norms = utils.clip_gradients(student, args.clip_grad)
            utils.cancel_gradients_last_layer(epoch, student,
                                              args.freeze_last_layer)
            fp16_scaler.step(optimizer)
            fp16_scaler.update()
        
        # EMA update for the teacher动态更新教师网络
        with torch.no_grad():
            m = momentum_schedule[it]  # momentum parameter
            for param_q, param_k in zip(params_q, params_k):
                param_k.data.mul_(m).add_((1 - m) * param_q.detach().data)
            for param_q, param_p in zip(params_q, params_p):
                param_p.data.mul_(m).add_((1 - m) * param_q.detach().data)

        # logging
        torch.cuda.synchronize()
        metric_logger.update(loss=loss.item())
        for key, value in all_loss.items():
            metric_logger.update(**{key: value.item()})
        metric_logger.update(lr=optimizer.param_groups[0]["lr"])
        metric_logger.update(wd=optimizer.param_groups[0]["weight_decay"])
        metric_logger.update(acc=acc)

    metric_logger.synchronize_between_processes()
    print("Averaged stats:", metric_logger)
    return_dict = {k: meter.global_avg for k, meter in metric_logger.meters.items()}
    return return_dict


class VehicleMAELoss(nn.Module):
    def __init__(self, out_dim, patch_out_dim, ngcrops, nlcrops, warmup_teacher_temp, 
                 teacher_temp, warmup_teacher_temp2, teacher_temp2, 
                 warmup_teacher_temp_epochs, nepochs, student_temp=0.1, 
                 center_momentum=0.9, center_momentum2=0.9,
                 lambda1=1.0, lambda2=1.0, mim_start_epoch=0):
        super().__init__()
        self.student_temp = student_temp
        self.center_momentum = center_momentum
        self.center_momentum2 = center_momentum2
        self.ngcrops = ngcrops
        self.nlcrops = nlcrops
        self.ncrops = ngcrops + nlcrops
        self.register_buffer("center", torch.zeros(1, out_dim))
        self.register_buffer("center2", torch.zeros(1, 1, patch_out_dim))
        self.lambda1 = lambda1
        self.lambda2 = lambda2

        # we apply a warm up for the teacher temperature because
        # a too high temperature makes the training instable at the beginning
        self.teacher_temp_schedule = np.concatenate((
            np.linspace(warmup_teacher_temp,
                        teacher_temp, warmup_teacher_temp_epochs),
            np.ones(nepochs - warmup_teacher_temp_epochs) * teacher_temp
        ))
        self.teacher_temp2_schedule = np.concatenate((
            np.linspace(warmup_teacher_temp2,
                        teacher_temp2, warmup_teacher_temp_epochs),
            np.ones(nepochs - warmup_teacher_temp_epochs) * teacher_temp2
        )) if mim_start_epoch == 0 else np.concatenate((
            np.ones(mim_start_epoch) * warmup_teacher_temp2,
            np.linspace(warmup_teacher_temp2,
                        teacher_temp2, warmup_teacher_temp_epochs),
            np.ones(nepochs - warmup_teacher_temp_epochs - mim_start_epoch) * teacher_temp2
        ))

    def forward(self, student_output, teacher_output, student_mask, epoch,mae_loss,similarity_loss,kl_distance_loss):
        """
        Cross-entropy between softmax outputs of the teacher and student networks.
        """
        
        student_cls, student_patch = student_output
        teacher_cls, teacher_patch = teacher_output

        # [CLS] and patch for global patches
        student_cls = student_cls / self.student_temp
        student_cls_c = student_cls.chunk(self.ncrops)
        student_patch = student_patch / self.student_temp
        student_patch_c = student_patch.chunk(self.ngcrops)
        
        # teacher centering and sharpening
        temp = self.teacher_temp_schedule[epoch]
        temp2 = self.teacher_temp2_schedule[epoch]
        teacher_cls_c = F.softmax((teacher_cls - self.center) / temp, dim=-1)
        teacher_cls_c = teacher_cls_c.detach().chunk(self.ngcrops)
        teacher_patch_c = F.softmax((teacher_patch - self.center2) / temp2, dim=-1)
        teacher_patch_c = teacher_patch_c.detach().chunk(self.ngcrops)


        total_loss1, n_loss_terms1 = 0, 0
        total_loss2, n_loss_terms2 = 0, 0
        for q in range(len(teacher_patch_c)):
            for v in range(len(student_patch_c)):
                if v == q:
                    loss2 = torch.sum(-teacher_patch_c[q] * F.log_softmax(student_patch_c[v], dim=-1), dim=-1)
                    mask = student_mask[v]
                    mask = ~mask
                    loss2 = torch.sum(loss2 * mask.float(), dim=-1) / mask.sum(dim=-1).clamp(min=1.0)
                    total_loss2 += loss2.mean()     #mean均值函数
                    n_loss_terms2 += 1
                else:
                    loss1 = torch.sum(-teacher_cls_c[q] * F.log_softmax(student_cls_c[v], dim=-1), dim=-1)
                    total_loss1 += loss1.mean()
                    n_loss_terms1 += 1
            
        total_loss1 = total_loss1 / n_loss_terms1 * self.lambda1*0.02
        total_loss2 = total_loss2 / n_loss_terms2 * self.lambda2*0.02
        
        kl_distance_loss = kl_distance_loss*0.1
        similarity_loss = similarity_loss*2

        total_loss = dict( cls =total_loss1, patch=total_loss2,mae =mae_loss,similarity = similarity_loss,kl = kl_distance_loss, loss=total_loss1+total_loss2+ mae_loss+similarity_loss+kl_distance_loss)

        self.update_center(teacher_cls, teacher_patch)           
        return total_loss

    @torch.no_grad()
    
    def update_center(self, teacher_cls, teacher_patch):
        """
        Update center used for teacher output.
        """
        cls_center = torch.sum(teacher_cls, dim=0, keepdim=True)
        dist.all_reduce(cls_center)
        cls_center = cls_center / (len(teacher_cls) * dist.get_world_size())
        self.center = self.center * self.center_momentum + cls_center * (1 - self.center_momentum)

        patch_center = torch.sum(teacher_patch.mean(1), dim=0, keepdim=True)
        dist.all_reduce(patch_center)
        patch_center = patch_center / (len(teacher_patch) * dist.get_world_size())
        self.center2 = self.center2 * self.center_momentum2 + patch_center * (1 - self.center_momentum2)



if __name__ == '__main__':
    parser = argparse.ArgumentParser('VehicleMAE', parents=[get_args_parser()])
    args = parser.parse_args()
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    train_vehicle(args)
