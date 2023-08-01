import os

import torch

if __name__ == "__main__":

    print ('')
    print ('Main script:')
    print ('ENV CM_VAR1: {}'.format(os.environ.get('CM_VAR1','')))
    print ('ENV USE_CUDA: {}'.format(os.environ.get('USE_CUDA','')))
    print ('')
    print ('PyTorch version: {}'.format(torch.__version__))
    print ('')

    exit(0)
