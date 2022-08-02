#! /bin/bash

export CK_REPOS=$PWD/CK
export CK_TOOLS=$PWD/CK-TOOLS

cb setup
cb publish solution:mlperf-inference-v0.5-image-classification-openvino-resnet50-imagenet-val-500-linux --force --version=1.0.1

