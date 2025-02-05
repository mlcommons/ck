# Get MLCommons Inference Results
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) git clones the [MLCommons Inference results repository](https://github.com/mlcommons/inference_v2.1).

## Commands
To install
```
cm run script --tags=get,mlperf,inference,results --version=[VERSION] 
```

[VERSION] is one of
* `v2.1:` MLCommons inference 2.1 round results

## Exported Variables
* `CM_MLPERF_INFERENCE_RESULTS_PATH`: Directory path to the inference results repository

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9
