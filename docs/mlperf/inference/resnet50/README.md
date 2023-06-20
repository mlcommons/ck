## Setup
Please follow the MLCommons CK [installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md) to install CM.

Install MLCommons CK repository with automation workflows for MLPerf.
```
cm pull repo mlcommons@ck
```

## Get Imagenet Dataset

We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset and register in CM.

In the edge category, ResNet50 has Offline, SingleStream, and MultiStream scenarios and in the datacenter category, it has Offline and Server scenarios. The below commands are assuming an edge category system. 

## Run Commands
Please follow the below readmes to run the command specific to a given implementation

* [MLCommons Reference implementation in Python](README_reference.md)
* [NVIDIA implementation](README_nvidia.md)
* [TFLite C++ implementation](README_tflite.md)
