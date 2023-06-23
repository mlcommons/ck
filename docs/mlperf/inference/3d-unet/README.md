## Setup
Please follow the MLCommons CK [installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md) to install CM.

Install MLCommons CK repository with automation workflows for MLPerf.

```
cm pull repo mlcommons@ck
```


3d-unet has two variants - `3d-unet-99` and `3d-unet-99.9` where the `99` and `99.9` specifies the required accuracy constraint with respect to the reference floating point model. Both models can be submitter under edge as well as datacenter category.


## Run Commands
Please follow the below readmes to run the command specific to a given implementation

* [MLCommons Reference implementation in Python](README_reference.md)
* [NVIDIA implementation](README_nvidia.md)
