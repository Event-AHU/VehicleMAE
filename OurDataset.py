from PIL import Image
from torch.utils.data import Dataset
import pickle
import os
import torch
from typing import Tuple, Optional, Union

class OurDataset(Dataset):
    def __init__(self, pkl_path, transform = None):
        dataset_info = pickle.load(open(pkl_path, 'rb+'))

        self.transform=transform
        self.rgb_image_name = dataset_info.image_rgb_name
        self.lunkuo_image_name = dataset_info.image_lunkuo_name
    def __getitem__(self, index)-> Tuple[torch.Tensor, ...]:

        seed = torch.randint(0, 100000, (1,)).item()
        rgb_image= self.rgb_image_name[index]
        lunkuo_image= self.lunkuo_image_name[index]

        rgb_img_pil = Image.open(rgb_image)
        lunkuo_img_pil = Image.open(lunkuo_image).convert('RGB')

        if self.transform is not None:
            torch.manual_seed(seed)
            rgb_image = self.transform(rgb_img_pil)
            torch.manual_seed(seed)
            lunkuo_image = self.transform(lunkuo_img_pil)

        return rgb_image,lunkuo_image
    def __len__(self):
        return len(self.rgb_image_name) 
