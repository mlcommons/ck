# Get MLCommons Power-dev Source
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/tutorial-scripts.md) git clones the [MLCommons Power-dev repository](https://github.com/mlcommons/power-dev).

## Commands
To install
```
cm run script --tags=get,mlperf,power-dev,src,[VARIATION] --version=[VERSION] 
```
where [VARIATION] is one of
* `default:` Works with the official MLCommons inference repository. Uses `short-history` variation

[VERSION] is one of
* `main:` Uses the main branch 

## Exported Variables
* `CM_MLPERF_POWER_SOURCE`: Directory path of the cloned inference repository

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9
