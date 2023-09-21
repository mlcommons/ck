[ [Back to MLPerf inference benchmarks index](../README.md) ]

## MLPerf inference: language processing with BERT

### Notes

Bert has two variants - `bert-99` and `bert-99.9` where the `99` and `99.9` specifies the required accuracy constraint 
with respect to the reference floating point model. `bert-99.9` model is applicable only on a datacenter system.

In the edge category, bert-99 has Offline and SingleStream scenarios and in the datacenter category, 
both `bert-99` and `bert-99.9` have Offline and Server scenarios.

Please check [MLPerf inference GitHub](https://github.com/mlcommons/inference) for more details.
 
### Install CM 

Please follow this [guide](../README.md#install-cm-automation-language) 
to install the [MLCommons CM automation language](https://doi.org/10.5281/zenodo.8105339),
pull the repository with the CM automation recipes for MLPerf and 
set up virtual environment to run MLPerf benchmarks.

### Run MLPerf via CM

The following guides explain how to run different implementations of this benchmark via CM:

* [MLCommons reference implementation in Python (CPU & GPU)](README_reference.md)
* [NVIDIA optimized implementation (GPU)](README_nvidia.md)
