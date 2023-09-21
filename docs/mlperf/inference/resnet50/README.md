[ [Back to MLPerf inference benchmarks index](../README.md) ]

## MLPerf inference: image classification with ResNet50

### Notes
 
In the edge category, ResNet50 has Offline, SingleStream, and MultiStream scenarios and in the datacenter category, it has Offline and Server scenarios. 

Please check [MLPerf inference GitHub](https://github.com/mlcommons/inference) for more details.

### Install CM

Please follow this [guide](../README.md#install-cm-automation-language) 
to install the [MLCommons CM automation language](https://doi.org/10.5281/zenodo.8105339),
pull the repository with the CM automation recipes for MLPerf and 
set up virtual environment to run MLPerf benchmarks.

### Get Imagenet Dataset

We need to get full ImageNet dataset to make image-classification submissions for MLPerf inference. 
Since this dataset is not publicly available via a URL please follow the instructions 
given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) 
to download the dataset and register in CM.

### Run MLPerf via CM

The following guides explain how to run different implementations of this benchmark via CM:

* [MLCommons Reference implementation in Python](README_reference.md)
* [NVIDIA implementation](README_nvidia.md)
* [TFLite C++ implementation](README_tflite.md)
