**[ [TOC](../README.md) ]**

## Pull MLOps automation repo

```bash
ck pull repo:octoml@mlops
```

## Install CK packages

```bash
ck install package --tags=lib,python-package,pytorch
```

## Tested configurations

Note that MLPerf reference image classification v1.1 fails with PyTorch > 1.5 (seg fault in MLPerf inference)

Grigori testsed the following configuration (20210723):
* CK workflow: https://github.com/octoml/mlops/tree/main/program/mlperf-inference-bench-image-classification-pytorch-onnx-cpu
* PyTorch 1.5.0
* ONNX 1.8.1
* RESNET50 model opset-8

