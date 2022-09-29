# Get ML Model Resnet50 Tensorflow
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/tutorial-scripts.md) downloads the Resnet50 Tensorflow model and adds it to CM cache with relevant meta data.

## How To
```bash
cm run script --tags=get,ml-model,resnet50-tf
```

## Exported Variables
* `CM_ML_MODEL_FILE:` Model filename
* `CM_ML_MODEL_FILE_WITH_PATH:` Full path to model file
* `CM_ML_MODEL_PATH:` Path to folder containing the model file
* More env variables being exported are given in [cm.json file](_cm.json)

