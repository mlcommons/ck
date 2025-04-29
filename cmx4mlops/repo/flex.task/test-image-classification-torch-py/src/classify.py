#!/usr/bin/env python3

import json
import time
import os
import shutil
import numpy as np


import torch
from torchvision import models
from torchvision import transforms
from PIL import Image

def main():
    pytorch_device = os.environ['CMX_PYTORCH_DEVICE']

    print ('')
    print (f'Target torch device: {pytorch_device}')

    if pytorch_device == 'cuda':
        if not torch.cuda.is_available():
            print ('ERROR: CUDA is not available in your PyTorch')
            exit(1)

        print(f'CUDA version used: {torch.version.cuda}')

        cuda_devices = torch.cuda.device_count()
        print (f'Number of CUDA devices: {cuda_devices}')

        print ('')
        for n in range(0, cuda_devices):
            name = torch.cuda.get_device_name(n)
            print (f'CUDA device name: {n+1} - {name}')


    device = torch.device(pytorch_device)

    model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
    model.to(device)

    transform = transforms.Compose([            #[1]
     transforms.Resize(256),                    #[2]
     transforms.CenterCrop(224),                #[3]
     transforms.ToTensor(),                     #[4]
     transforms.Normalize(                      #[5]
     mean=[0.485, 0.456, 0.406],                #[6]
     std=[0.229, 0.224, 0.225]                  #[7]
     )])

    image = os.environ['CMX_IMAGE_WITH_PATH']

    print ('')
    print (f'Analyzing image {image} ...')

    img = Image.open(image)

    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0).to(device=device, dtype=torch.float)

    model.eval()

    out = model(batch_t)
    print(out.shape)

    classes_with_path = os.environ['CMX_CLASSES_WITH_PATH']

    with open(classes_with_path) as f:
      labels = [line.strip() for line in f.readlines()]

    _, index = torch.max(out, 1)
     
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
     
    print ('')
    print ('Classification:')
    print (labels[index[0]], percentage[index[0]].item())

    _, indices = torch.sort(out, descending=True)
    predictions = ([(labels[idx], percentage[idx].item()) for idx in indices[0][:5]])

    print ('')
    for p in predictions:
        print (p)

if __name__ == '__main__':
    main()
