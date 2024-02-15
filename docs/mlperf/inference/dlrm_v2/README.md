[ [Back to MLPerf inference benchmarks index](../README.md) ]

## MLPerf inference: recommendation with DLRMv2

### Notes

DLRMv2 has two variants - `dlrm_v2-99` and `dlrm_v2-99.9` where the `99` and `99.9` specify the required accuracy constraint 
with respect to the reference fp32 model. DLRMv2 applies only to datacenter category and includes both Offline and Server scenarios.

Please check [MLPerf inference GitHub](https://github.com/mlcommons/inference) for more details.

### Install CM

Please follow this [guide](../README.md#install-cm-automation-language) 
to install the [MLCommons CM automation language](https://doi.org/10.5281/zenodo.8105339),
pull the repository with the CM automation recipes for MLPerf and set up virtual environment to run MLPerf benchmarks.

### Run MLPerf via CM

The following guides explain how to run different implementations of this benchmark via CM:

* [MLCommons Reference implementation in Python](README_reference.md)
