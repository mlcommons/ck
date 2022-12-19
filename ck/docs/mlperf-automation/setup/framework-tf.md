**[ [TOC](../README.md) ]**

## Pull MLOps automation repo

```bash
ck pull repo:mlcommons@ck-mlops
```

## Install CK packages with TensorFlow (CPU)

```bash
ck install package --tags=lib,python-package,tensorflow-cpu,2.5.0
```

### Install any available version
```bash
ck install package --tags=lib,python-package,tensorflow-cpu
```

## Install CK packages with TensorFlow (GPU)

Follow [this guide](compiler-cuda.md) to plug CUDA into CK.

```bash
ck install package --tags=lib,python-package,tensorflow-gpu,2.5.0
```

You can check you CUDA capabilities via CK as follows:
```bash
ck detect platform.gpgpu --cuda
```

### Install any available version
```bash
ck install package --tags=lib,python-package,tensorflow-gpu
```


## Tested configurations

### 20210806

Grigori tested the following configuration for MLPerf inference v1.1 benchmark (image classification):
* Ubuntu 18.04
* CUDA 11.1
* cuDNN 8.1.0
* TF 2.5.0
