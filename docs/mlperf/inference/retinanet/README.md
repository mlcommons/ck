[ [Back to MLPerf inference benchmarks index](../README.md) ]

## MLPerf inference: object detection with RetinaNet

### Notes

In the edge category, RetinaNet has Offline, SingleStream and MultiStream scenarios and in the datacenter category, it has Offline and Server scenarios. 

Please check [MLPerf inference GitHub](https://github.com/mlcommons/inference) for more details.

### Install CM

Please follow this [guide](../README.md#install-cm-automation-language) 
to install the [MLCommons CM automation language](https://doi.org/10.5281/zenodo.8105339),
pull the repository with the CM automation recipes for MLPerf and 
set up virtual environment to run MLPerf benchmarks.

### Run MLPerf via CM

The following guides explain how to run different implementations of this benchmark via CM:

* [MLCommons Reference implementation in Python](README_reference.md)
* [NVIDIA implementation](README_nvidia.md)
