import torch
from torch import nn
#from datatxt import HICO_INTERACTIONS
from datahouneed import HICO_INTERACTIONS
from models.clip import clip
import torch.nn.functional as F
 


def build_clip(args):

    device = torch.device(args.device)

    # build_clip
    model_path = args.clip_pre_model 

    clip_model, preprocess = clip.load(model_path, device=device)   #加载预训练好的模型

    print("Turning off gradients in both the image and the text encoder")
    for name, param in clip_model.named_parameters():
        # if "prompt_learner" not in name:
        param.requires_grad_(False)
    #提取特征
    ao_pair = [(d['brand'], d['color'], d['energy'], d['level'], d['long'], d['width'], d['high'], d['doors'], d['seats'], d['wheelbase'], d['years']) for d in HICO_INTERACTIONS]
    #生成clip文本
    text_inputs = torch.cat(        #将多个tensor拼接
        [clip.tokenize("a picture of a {} {} {} car ,it is a {} {} ,its length is {}, its width is {}, its height is {}, its wheelbase is {}, it has {} doors and {} seats".format(c,y,b,e,le,lo,w,h,w,d,s,w)) for b, c,e,le,lo,w,h,d,s,w,y in ao_pair]).to(device)     #类别构建
    #生成每个文本的特征
    text_features = clip_model.encode_text(text_inputs)
    #归一化特征
    text_features = text_features / text_features.norm(dim=-1, keepdim=True)
    #将text_features加载到GPU中
    text_features = text_features.to(device)


    return clip_model,preprocess,text_features



class ClipBaseModel(nn.Module):
    """
    Perform forward pass separately on each resolution input.
    The inputs corresponding to a single resolution are clubbed and single
    forward is run on the same resolution inputs. Hence we do several
    forward passes = number of different resolutions used. We then
    concatenate all the output features and run the head forward on these
    concatenated features.
    """
    def __init__(self, clip_model ,text_features):
        super(ClipBaseModel, self).__init__()
        # disable layers dedicated to ImageNet labels classification
        self.clip = clip_model
        #self.preprocess = preprocess
        self.text_features = text_features
        #self.batch_size = batch_size
        #self.register_buffer("temperature", torch.tensor(temperature))
    

    def Clip_Loss(self,image_features,student_image_features):
        #对学生网络输出特征进行处理，变为[B,P]
        #student_image_features = student_image_features[:,:,0:1]
        student_image_features = student_image_features.reshape(len(image_features),-1)
        
        #将特征l2归一化
        image_features_l2 = F.normalize(image_features, p=2, dim=1, eps=1e-12, out=None)
        student_image_features_l2 = F.normalize(student_image_features, p=2, dim=1, eps=1e-12, out=None)
        #((inputs - targets) ** 2).sum() / inputs.size(0)
        #计算相似性loss
        similarity_loss = torch.sum((image_features_l2-student_image_features_l2)** 2)/ image_features_l2.size(0)
        #F.kl_div(inputs, targets, reduction='batchmean')
        #计算图像及文本的交叉模态loss        
        #余弦相似度作为 logits
        logit_scale = self.clip.logit_scale.exp()
        #计算每张图片和文本的余弦相似度
        logits_clip = logit_scale * image_features_l2 @ self.text_features.t()
        logits_mae = logit_scale * student_image_features_l2 @ self.text_features.t()

        #probs_clip = logits_clip.softmax(dim=-1).cpu().numpy()
        #probs_mae = logits_mae.softmax(dim=-1).cpu().detach().numpy()
        #计算教师网络和学生网络的KLloss
        kl_loss = nn.KLDivLoss(reduction='batchmean')
        #归一化
        temp = 1
        input = F.log_softmax(logits_mae/temp, dim=-1)
        target = F.softmax(logits_clip/temp, dim=-1)
        #target = F.log_softmax(logits_clip, dim=-1)
        kl_distance_loss = kl_loss(input, target)

        '''
        representations = torch.cat([image_features_l2, image_features], dim=0)
        similarity_matrix = F.cosine_similarity(representations.unsqueeze(1), representations.unsqueeze(0), dim=2)
        #if self.verbose: print("Similarity matrix\n", similarity_matrix, "\n")

        sim_ij = torch.diag(similarity_matrix, self.batch_size)
        sim_ji = torch.diag(similarity_matrix, -self.batch_size)
        positives = torch.cat([sim_ij, sim_ji], dim=0)
        
        nominator = torch.exp(positives / self.temperature)
        denominator = self.negatives_mask * torch.exp(similarity_matrix / self.temperature)
    
        loss_partial = -torch.log(nominator / torch.sum(denominator, dim=1))
        loss = torch.sum(loss_partial) / (2 * self.batch_size)
        '''

        return similarity_loss,kl_distance_loss





    def forward(self,image,student_image_features):
        #图像处理
        #image = self.preprocess(image).unsqueeze(0)
        #生成图像特征
        image_features = self.clip.encode_image(image)

        #对图像特征进行归一化
        image_features = image_features / image_features.norm(dim=-1, keepdim=True)
        #计算每张图片和文本的余弦相似度
        similarity_loss,kl_distance_loss = self.Clip_Loss(image_features,student_image_features)

        return  similarity_loss,kl_distance_loss
