# Get MLCommons Inference Loadgen

This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) builds and installs 
the Loadgen library from [MLCommons Inference repository](https://github.com/mlcommons/inference).

## Commands
To install
```
cm run script --tags=get,mlperf,inference,loadgen --version=[VERSION] 
```
where 
[VERSION] is one of
* `master:` Uses the master branch of inference source repository to build loadgen
* `r2.1:`  Uses the release branch used for MLCommons inference 2.1 round to build loadgen

## Exported Variables
* `C_INCLUDE_PATH`
* `CPLUS_INCLUDE_PATH`
* `LD_LIBRARY_PATH`
* `DYLD_FALLBACK_LIBRARY_PATH`
* `PYTHONPATH`

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9
3. Windows (installs into Python distro directly)
