# MLPerf automation and reproducibility report

**Tags:** MLPerf inference v2.1; Image Classification; Resnet50; ONNX 1.11.1; Ubuntu 22.04; x8664

[Back to MLPerf reproducibility studies](reproducibility.md)

## Current status

*[20220927] Working.*

## Setup

* [System dependencies](../../cm/docs/installation.md#ubuntu--debian)
* [CK installation](../../cm/docs/installation.md#cm-installation)

## CM automation workflow

To be improved!

```bash
cm run script --tags=app,mlperf,_resnet50,_onnxruntime,_cpu,_cpp    --add_deps_recursive.inference-src.tags=_octoml
cm run script --tags=app,mlperf,inference,python,_cpp,_resnet50,_onnxruntime,_cpu  --add_deps_recursive.inference-src.tags=_octoml --env.OUTPUT_BASE_DIR=$HOME/result --env.CM_TEST_QUERY_COUNT=100 --env.CM_RERUN=yes
```

## Reusable CM components

* [LLVM](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
* [Resnet50 model (ONNX)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-onnx)
* [ImageNet validation set](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-imagenet-val)
* [ONNX run-time](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime)
* [MLPerf inference benchmark workflow with Python FE](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-vision-reference)

* [Other reusable CM components](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)*

## Report problems

* [Open GitHub issue](https://github.com/mlcommons/ck/issues)
* [Discuss during weekly conf-calls](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)