## Setup
Please follow the MLCommons CK [installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md) to install CM.

Install MLCommons CK repository with automation workflows for MLPerf.

```
cm pull repo mlcommons@ck
```

GPT-J has two variants - `gptj-99` and `gptj-99.9` where the `99` and `99.9` specifies the required accuracy constraint with respect to the reference floating point model. `gptj-99.9` model is applicable only on a datacenter system.

In the edge category, gptj-99 has Offline and SingleStream scenarios and in the datacenter category, both `gptj-99` and `gptj-99.9` have Offline and Server scenarios.


## Run Commands
Please follow the below readmes to run the command specific to a given implementation

* [MLCommons Reference implementation in Python](README_reference.md)
