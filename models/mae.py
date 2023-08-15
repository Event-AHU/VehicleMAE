
# Copyright (c) ByteDance, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
# --------------------------------------------------------
# References:
# timm: https://github.com/rwightman/pytorch-image-models/tree/master/timm
# MAE: https://github.com/facebookresearch/mae 
# --------------------------------------------------------

from functools import partial
import torch
import numpy as np
import math
import random
import torch.nn as nn

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
# --------------------------------------------------------
# References:
# timm: https://github.com/rwightman/pytorch-image-models/tree/master/timm
# DeiT: https://github.com/facebookresearch/deit
# --------------------------------------------------------

from functools import partial

import torch
import torch.nn as nn

from timm.models.vision_transformer import PatchEmbed, Block

from pos_embed import get_2d_sincos_pos_embed

class MaskedAutoencoderViT(nn.Module):#基于vit实现的mae
    """ Masked Autoencoder with VisionTransformer backbone
    img_size：输入图像宽和高。patch_size：每一个patch的宽和高。in_chans：输入通道数。
    embed_dim：mse编码器的Hidden size。depth：mae中transform的块数Layers的层数。num_heads编码器的头数
    解码器的三个参数
    编码器的输出需要降维
    """

    def __init__(self, img_size=224, patch_size=16, in_chans=3,
                 embed_dim=768, depth=12, num_heads=16,
                 decoder_embed_dim=512, decoder_depth=8, decoder_num_heads=16,
                 mlp_ratio=4., norm_layer=nn.LayerNorm, norm_pix_loss=False,mask_ratio=0.75,use_learnable_pos_emb=True):
        super().__init__()

        # --------------------------------------------------------------------------
        # MAE encoder specifics
        #图片喂入就可以得到patch的序列
        self.patch_embed = PatchEmbed(img_size, patch_size, in_chans, embed_dim)#实例化需要传入照片的大小，patch的大小，照片输入的通道数，embed_dim
        #num_patches：得到块的数量
        num_patches = self.patch_embed.num_patches
        #实例化两个参数cls_token和pos_embed
        self.cls_token = nn.Parameter(torch.zeros(1, 1, embed_dim))#可训练的
        self.pos_embed = nn.Parameter(torch.zeros(1, num_patches + 1, embed_dim), requires_grad=False)  # fixed sin-cos embedding不可训练的，位置编码requires_grad不可训练
        #定义编码器的transform blocks，使用Module的列表，不能使用普通列表，不然无法被Module识别
        self.blocks = nn.ModuleList([
            Block(embed_dim, num_heads, mlp_ratio, qkv_bias=True, norm_layer=norm_layer)#多头注意力头数num_heads,, qk_scale=None
            for i in range(depth)])#最新版timm要注释掉qk_scale
        self.norm = norm_layer(embed_dim)#对encode output做归一化
        # --------------------------------------------------------------------------

        # --------------------------------------------------------------------------
        # MAE decoder specifics
        self.decoder_embed = nn.Linear(embed_dim, decoder_embed_dim, bias=True)#构建一个线性映射层，将编码器的输出映射到解码器的特征维度上
        '''
        # Probability prediction network 概率预测网络
        self.pos_embed_probs = nn.Parameter(torch.zeros(1, num_patches, embed_dim))
        self.get_token_probs = nn.Sequential(
                                Block(dim=embed_dim, num_heads=8, mlp_ratio=4., qkv_bias=False, 
                                 norm_layer=nn.LayerNorm),
                                nn.Linear(embed_dim, 1),
                                torch.nn.Flatten(start_dim=1),
                                )       #轻量级的多头注意网络（MHA）
        self.softmax =  nn.Softmax(dim=-1)      #mask中的softmax激活
        '''
        #self.visible_patches = int(num_patches*(1-mask_ratio))#计算未被掩码的pach数
        
        self.apply(self._init_weights)
        
        self.mask_token = nn.Parameter(torch.zeros(1, 1, decoder_embed_dim))#可训练的token，用于替换掉那些被mask的块

        self.decoder_pos_embed = nn.Parameter(torch.zeros(1, num_patches + 1, decoder_embed_dim), requires_grad=False)  # fixed sin-cos embedding
        
        #定义解码器的transform blocks
        self.decoder_blocks = nn.ModuleList([
            Block(decoder_embed_dim, decoder_num_heads, mlp_ratio, qkv_bias=True,  norm_layer=norm_layer)#qk_scale=None,
            for i in range(decoder_depth)])
        
        self.decoder_norm = norm_layer(decoder_embed_dim)#对decoder output做归一化
        #patch_size**2 * in_chans，patch的面积乘上通道数，映射层
        self.decoder_pred = nn.Linear(decoder_embed_dim, patch_size**2 * in_chans, bias=True) # decoder to patch
        self.decoder_image = nn.Linear(196, 1, bias=True)
        #self.decode_clip = nn.Linear(1024, 768, bias=True)
        # --------------------------------------------------------------------------

        self.norm_pix_loss = norm_pix_loss#是否要对像素做归一化再去算loss
        self.use_learnable_pos_emb = use_learnable_pos_emb
        self.initialize_weights()
    #初始化权重
    def initialize_weights(self):
        # initialization
        # initialize (and freeze) pos_embed by sin-cos embedding对pos_embed进行初始化
        pos_embed = get_2d_sincos_pos_embed(self.pos_embed.shape[-1], int(self.patch_embed.num_patches**.5), cls_token=True)
        self.pos_embed.data.copy_(torch.from_numpy(pos_embed).float().unsqueeze(0))

        #对decode的pos_embed进行初始化
        decoder_pos_embed = get_2d_sincos_pos_embed(self.decoder_pos_embed.shape[-1], int(self.patch_embed.num_patches**.5), cls_token=True)
        self.decoder_pos_embed.data.copy_(torch.from_numpy(decoder_pos_embed).float().unsqueeze(0))

        # initialize patch_embed like nn.Linear (instead of nn.Conv2d)均匀分布的初始化
        w = self.patch_embed.proj.weight.data
        torch.nn.init.xavier_uniform_(w.view([w.shape[0], -1]))

        # timm's trunc_normal_(std=.02) is effectively normal_(std=0.02) as cutoff is too big (2.)高斯分布的初始化
        torch.nn.init.normal_(self.cls_token, std=.02)
        torch.nn.init.normal_(self.mask_token, std=.02)

        # initialize nn.Linear and nn.LayerNorm
        self.apply(self._init_weights)#接受的参数是一个函数，函数会作用在当前这个Module和当前这个Module的子Module

    def _init_weights(self, m):
        if isinstance(m, nn.Linear):#如果进入这个模块的是nn.Linear的实例，则会对权重做均匀分布的初始化
            # we use xavier_uniform following official JAX ViT:
            torch.nn.init.xavier_uniform_(m.weight)
            if isinstance(m, nn.Linear) and m.bias is not None:#如果有bias则做一个bias为0的初始化
                nn.init.constant_(m.bias, 0)
        elif isinstance(m, nn.LayerNorm):#对层归一化逻辑进行判断，如果是则将权重和偏置做常数初始化
            nn.init.constant_(m.bias, 0)
            nn.init.constant_(m.weight, 1.0)

    def patchify(self, imgs):#把图片划分成块
        """
        imgs: (N, 3, H, W)
        x: (N, L, patch_size**2 *3)     patch_size**2 *3:单张图像的像素点个数,L:为图像尺寸，N为batch的大小
        """
        p = self.patch_embed.patch_size[0]  #p=patch_size的大小
        assert imgs.shape[2] == imgs.shape[3] and imgs.shape[2] % p == 0    #若img图像尺寸相对于patch_size不整除则跳出

        h = w = imgs.shape[2] // p
        x = imgs.reshape(shape=(imgs.shape[0], 3, h, p, w, p))
        x = torch.einsum('nchpwq->nhwpqc', x)
        x = x.reshape(shape=(imgs.shape[0], h * w, p**2 * 3))#batch_size*patch的数目*patch的大小
        return x

    def unpatchify(self, x):#把块的图片还原成图片
        """
        x: (N, L, patch_size**2 *3) #
        imgs: (N, 3, H, W)
        """
        p = self.patch_embed.patch_size[0]
        h = w = int(x.shape[1]**.5)
        assert h * w == x.shape[1]
        
        x = x.reshape(shape=(x.shape[0], h, w, p, p, 3))
        x = torch.einsum('nhwpqc->nchpwq', x)
        imgs = x.reshape(shape=(x.shape[0], 3, h * p, h * p))
        return imgs

    def random_masking(self, x, mask_ratio):#随机掩码
        """
        Perform per-sample random masking by per-sample shuffling.
        Per-sample shuffling is done by argsort random noise.
        x: [N, L, D], sequence
        """
        N, L, D = x.shape  # batch, length, dim
        len_keep = int(L * (1 - mask_ratio))#算出保留块的数目
        
        noise = torch.rand(N, L, device=x.device)  # noise in [0, 1]生成随机矩阵，均匀分布 batch_size*length
        
        # sort noise for each sample 对每个样本的噪声进行排序
        ids_shuffle = torch.argsort(noise, dim=1)  # ascend: small is keep, large is remove排序从小到大取掩码和被掩码时用的
        ids_restore = torch.argsort(ids_shuffle, dim=1)#对索引进行排序，还原序列时要用到的

        # keep the first subset 保留第一个子集
        ids_keep = ids_shuffle[:, :len_keep]#
        x_masked = torch.gather(x, dim=1, index=ids_keep.unsqueeze(-1).repeat(1, 1, D))#dim:维度。未被掩码的序列

        # generate the binary mask: 0 is keep, 1 is remove
        mask = torch.ones([N, L], device=x.device)#batch_size*lenth大小的提供给decode使用的全一矩阵
        mask[:, :len_keep] = 0#对未掩码设置为0
        # unshuffle to get the binary mask
        mask = torch.gather(mask, dim=1, index=ids_restore)#在原图中被掩码的位置

        return x_masked, mask, ids_restore

    def forward_encoder(self, x, mask_ratio):#x：输入图像。mask_ratio：掩码比例
        # embed patches
        x = self.patch_embed(x)

        # add pos embed w/o cls token
        x = x + self.pos_embed[:, 1:, :]

        x, mask, ids_restore = self.random_masking(x, mask_ratio)#随机掩码ids_restore：恢复的索引

        # append cls token
        cls_token = self.cls_token + self.pos_embed[:, :1, :]
        cls_tokens = cls_token.expand(x.shape[0], -1, -1)
        x = torch.cat((cls_tokens, x), dim=1)#encode的输入

        # apply Transformer blocks
        for blk in self.blocks:
            x = blk(x)
        x = self.norm(x)#encode的输出

        return x, mask, ids_restore
    
    def forward_decoder(self, x, ids_restore):
        # embed tokens
        x = self.decoder_embed(x)
        # append mask tokens to sequence
        mask_tokens = self.mask_token.repeat(x.shape[0], ids_restore.shape[1] + 1 - x.shape[1], 1)#扩维
        x_ = torch.cat([x[:, 1:, :], mask_tokens], dim=1)  # no cls token，拼接
        x_ = torch.gather(x_, dim=1, index=ids_restore.unsqueeze(-1).repeat(1, 1, x.shape[2]))  # unshuffle，得到被还原后的顺序
        x = torch.cat([x[:, :1, :], x_], dim=1)  # append cls token

        # add pos embed加上位置编码
        x = x + self.decoder_pos_embed


        # apply Transformer blocks对decode的所有block进行递归的调用
        for blk in self.decoder_blocks:
            x = blk(x)
        x = self.decoder_norm(x)#得到decode输出

        tezheng = x

        clip_tezheng = tezheng
        clip_tezheng = clip_tezheng[:, 1:, :]
        clip_tezheng = clip_tezheng.transpose(1,2)
        clip_tezheng = self.decoder_image(clip_tezheng)
        
        # predictor projection映射到像素的特征上
        x = self.decoder_pred(x)

        # remove cls token移除cls token
        x = x[:, 1:, :]

        return x ,tezheng,clip_tezheng

    def forward_loss(self, imgs, pred, mask):#平方差loss
        """
        imgs: [N, 3, H, W]
        pred: [N, L, p*p*3]
        mask: [N, L], 0 is keep, 1 is remove, 
        """
        target = self.patchify(imgs)    #原始图像patch后
        if self.norm_pix_loss:
            mean = target.mean(dim=-1, keepdim=True)#计算均值
            var = target.var(dim=-1, keepdim=True)#计算方差
            target = (target - mean) / (var + 1.e-6)**.5#对target做均值方差的归一化，1.e-6：防止方差为0

        loss = (pred - target) ** 2 #计算均方损失函数
        loss = loss.mean(dim=-1)     # [N, L], mean loss per patch，均值
        #loss = (loss * mask).sum() / mask.sum()  # 将每个mask后的patch累加

        return loss
    

    def del_tensor_ele_n(self,arr, index, n):
        """
        arr: 输入tensor
        index: 需要删除位置的索引
        n: 从index开始，需要删除的行数
        """
        arr1 = arr[0:index]
        arr2 = arr[index+n:]
        return torch.cat((arr1,arr2),dim=0)

    @torch.jit.ignore
    def no_weight_decay(self):
        return {'pos_embed', 'cls_token', 'mask_token'}
    
    def forward(self, imgs,mask_ratio=0.75):#结合返回
        latent, mask, ids_restore = self.forward_encoder(imgs, mask_ratio)
        pred,tezheng,clip_tezheng = self.forward_decoder(latent, ids_restore)  # [N, L, p*p*3]

        loss= self.forward_loss(imgs, pred, mask)
        return tezheng,loss,mask,ids_restore,clip_tezheng

#三种mae，mae_vit_base，mae_vit_large，mae_vit_huge
def mae_vit_base_patch16_dec512d8b(**kwargs):
    model = MaskedAutoencoderViT(
        patch_size=16, embed_dim=768, depth=12, num_heads=12,
        decoder_embed_dim=512,  decoder_num_heads=16,
        mlp_ratio=4, norm_layer=partial(nn.LayerNorm, eps=1e-6), **kwargs)
    return model

#decoder_depth=8,
def mae_vit_large_patch16_dec512d8b(**kwargs):
    model = MaskedAutoencoderViT(
        patch_size=16, embed_dim=1024, depth=24, num_heads=16,
        decoder_embed_dim=512,  decoder_num_heads=16,
        mlp_ratio=4, norm_layer=partial(nn.LayerNorm, eps=1e-6), **kwargs)
    return model


def mae_vit_huge_patch14_dec512d8b(**kwargs):
    model = MaskedAutoencoderViT(
        patch_size=14, embed_dim=1280, depth=32, num_heads=16,
        decoder_embed_dim=512, decoder_depth=8, decoder_num_heads=16,
        mlp_ratio=4, norm_layer=partial(nn.LayerNorm, eps=1e-6), **kwargs)
    return model


# set recommended archs
mae_vit_base_patch16 = mae_vit_base_patch16_dec512d8b  # decoder: 512 dim, 8 blocks
mae_vit_large_patch16 = mae_vit_large_patch16_dec512d8b  # decoder: 512 dim, 8 blocks
mae_vit_huge_patch14 = mae_vit_huge_patch14_dec512d8b  # decoder: 512 dim, 8 blocks
