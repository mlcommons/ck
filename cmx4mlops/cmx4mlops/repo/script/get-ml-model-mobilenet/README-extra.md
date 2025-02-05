# Get ML Model MobileNet
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) downloads the MobileNet model and adds it to CM cache with relevant meta data.

## How To
```bash
cm run script --tags=get,ml-model,mobilenet,_[VARIATION]
```
where,
* `[VARIATION]` is one of  `tf-fp32`, `tf-int8`, `onnx-v1-opset-8`, `onnx-v1-opset-11`, `onnx-int8`.

## Exported Variables
* `CM_ML_MODEL_FILE:` Model filename
* `CM_ML_MODEL_FILE_WITH_PATH:` Full path to model file
* `CM_ML_MODEL_PATH:` Path to folder containing the model file
* More env variables being exported are given in [cm.json file](_cm.json)
