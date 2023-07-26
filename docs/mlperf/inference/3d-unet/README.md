[ [Back to MLPerf inference benchmarks index](../README.md) ]

## MLPerf inference: medical imaging with 3D U-Net

### Notes

3d-unet has two variants - `3d-unet-99` and `3d-unet-99.9` where the `99` and `99.9` specifies the required accuracy constraint 
with respect to the reference floating point model. Both models can be submitter under edge as well as datacenter category.

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
