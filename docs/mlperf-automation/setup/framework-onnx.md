**[ [TOC](../README.md) ]**

## Pull MLOps automation repo

```bash
ck pull repo:octoml@mlops
```

## Install CK packages with ONNX (CPU)

```bash
ck install package --tags=lib,python-package,onnxruntime-cpu,1.8.0
ck install package --tags=lib,python-package,onnx,1.8.0
```

## Install any available version (CPU)
```bash
ck install package --tags=lib,python-package,onnxruntime-cpu
ck install package --tags=lib,python-package,onnx
```

## Notes
CK makes it possible to install multiple versions of different packages at the same time.
CK workflows can then automatically plug in different versions of packages (frameworks, libraries, models, data sets)
to enable collaborating testing, benchmarking and optimization of ML Systems.
