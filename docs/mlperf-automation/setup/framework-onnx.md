**[ [TOC](../README.md) ]**

## Pull MLOps automation repo

```bash
ck pull repo:mlcommons@ck-mlops
```

## Install CK packages with ONNX (CPU)

```bash
ck install package --tags=lib,python-package,onnxruntime-cpu,1.8.1
ck install package --tags=lib,python-package,onnx,1.8.1
```

### Install any available version
```bash
ck install package --tags=lib,python-package,onnxruntime-cpu
ck install package --tags=lib,python-package,onnx
```

## Install CK packages with ONNX (GPU)

Follow [this guide](compiler-cuda.md) to plug CUDA into CK.

*Note that CK will attempt to automatically detect your CUDA installation and plug it into CK*

```bash
ck install package --tags=lib,python-package,onnxruntime-gpu,1.8.1
ck install package --tags=lib,python-package,onnx,1.8.1
```

You can check you CUDA capabilities via CK as follows:
```bash
ck detect platform.gpgpu --cuda
```

### Install any available version
```bash
ck install package --tags=lib,python-package,onnxruntime-gpu

ck install package --tags=lib,python-package,onnx
```


## Notes
CK makes it possible to install multiple versions of different packages at the same time.
CK workflows can then automatically plug in different versions of packages (frameworks, libraries, models, data sets)
to enable collaborating testing, benchmarking and optimization of ML Systems.
