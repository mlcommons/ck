# Get ML Model Resnet50 optimized by TVM
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) optimizes the Resnet50 model using TVM.

## How To
```bash
cm run script --tags=get,ml-model-tvm,resnet50,_[VARIATION]
```
where,
* `[VARIATION]` is one of `onnx` (alias `onnxruntime`), `pytorch`, `tensorflow` (alias `tf`) , `fp32`, `int8`.

## Exported Variables
* `CM_ML_MODEL_FILE:` Model filename
* `CM_ML_MODEL_FILE_WITH_PATH:` Full path to model file
* `CM_ML_MODEL_PATH:` Path to folder containing the model file
* More env variables being exported are given in [cm.json file](_cm.json)
