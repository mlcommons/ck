#! /bin/bash

export CK_REPOS=$PWD/CK
export CK_TOOLS=$PWD/CK-TOOLS

ck find module:program

cb benchmark mlperf-inference-v0.5-image-classification-openvino-resnet50-imagenet-val-500-linux
