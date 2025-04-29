#!/usr/bin/env python3

import os
import torch
from flash_attn import flash_attn_func


def main():
    pytorch_device = os.environ['CMX_PYTORCH_DEVICE']

    print ('')
    print (f'Target torch device: {pytorch_device}')

    if pytorch_device == 'cuda':
        print(f'CUDA version used: {torch.version.cuda}')

    q, k, v = torch.randn(1, 128, 3, 16, 64, dtype=torch.float16, device=pytorch_device).unbind(2)

    out = flash_attn_func(q, k, v)

    print ('SUCCESS')

if __name__ == '__main__':
    main()
