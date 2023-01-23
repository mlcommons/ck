**[ [TOC](../README.md) ]**

## Pull MLOps automation repo

```bash
ck pull repo:mlcommons@ck-mlops
```

## Install CK packages (CPU)

```bash
ck install package --tags=lib,python-package,pytorch,1.9.0
ck install package --tags=lib,python-package,torchvision,0.10.0
```

*Note that MLPerf v1.1 doesn't work with pytorch > 1.5.0. You need to install the working version as follows:*

```bash
ck install package --tags=lib,python-package,pytorch,1.5.0
ck install package --tags=lib,python-package,torchvision,0.6.0
```

## Install CK packages (CUDA)

Follow [this guide](compiler-cuda.md) to plug CUDA into CK.

```bash
ck install package --tags=lib,python-package,pytorch-cuda,1.9.0+cu111
ck install package --tags=lib,python-package,torchvision-cuda,0.10.0+cu111
```

*Note that MLPerf v1.1 doesn't work with pytorch > 1.5.0. You need to install the working version as follows:*

```bash
ck install package --tags=lib,python-package,pytorch-cuda,1.5.0+cu101
ck install package --tags=lib,python-package,torchvision-cuda,0.6.0+cu101
```

## Tested configurations

### 20210723

Note that MLPerf reference image classification v1.1 fails with PyTorch > 1.5 (seg fault in MLPerf inference)

Grigori testsed the following configuration:
* CK workflow: https://github.com/mlcommons/ck-mlops/tree/main/program/mlperf-inference-bench-image-classification-pytorch-onnx-cpu
* PyTorch 1.5.0
* TorchVision 0.6.0 (works with PyTorch 1.5.0)
* ONNX 1.8.1
* RESNET50 model opset-8

