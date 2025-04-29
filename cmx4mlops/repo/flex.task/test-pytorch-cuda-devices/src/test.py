#!/usr/bin/env python3

import os
import torch


def main():
    pytorch_device = os.environ['CMX_PYTORCH_DEVICE']

    print ('')
    print (f'Target torch device: {pytorch_device}')

#    if pytorch_device == 'cuda':
    print(f'CUDA version used: {torch.version.cuda}')
    print(f'CUDA device count: {torch.cuda.device_count()}')

if __name__ == '__main__':
    main()
