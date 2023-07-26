[ [Back to MLPerf inference benchmarks index](../README.md) ]

## MLPerf inference: language processing with GPT-J

### Notes

GPT-J has two variants - `gptj-99` and `gptj-99.9` where the `99` and `99.9` specifies the required accuracy constraint 
with respect to the reference floating point model. `gptj-99.9` model is applicable only on a datacenter system.

In the edge category, gptj-99 has Offline and SingleStream scenarios and in the datacenter category, both `gptj-99` and `gptj-99.9` have Offline and Server scenarios.

Please check [MLPerf inference GitHub](https://github.com/mlcommons/inference) for more details.

### Install CM

Please follow this [guide](../README.md#install-cm-automation-language) 
to install the [MLCommons CM automation language](https://doi.org/10.5281/zenodo.8105339),
pull the repository with the CM automation recipes for MLPerf and 
set up virtual environment to run MLPerf benchmarks.

### Run MLPerf via CM

The following guides explain how to run different implementations of this benchmark via CM:

* [MLCommons Reference implementation in Python](README_reference.md)
