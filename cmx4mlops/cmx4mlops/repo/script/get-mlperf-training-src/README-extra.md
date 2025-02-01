# Get MLCommons Training Source
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) git clones the [MLCommons Training repository](https://github.com/mlcommons/training).

## Commands
To install
```
cm run script --tags=get,mlperf,training,src,[VARIATION] --version=[VERSION] 
```
where [VARIATION] is one of
* `default:` Works with the official MLCommons inference repository. Uses `short-history` variation
* `patch:` Applies the `git.patch` to the cloned git repository
* `octoml:` Works with the OctoML fork of the MLCommons inference repository. Uses `short-history` variation
* `short-history:` Uses a git depth of last 10 commits (significantly reduces the download size)
* `full-history:` Uses the full git history
* `no-recurse-submodules:` Only download the main repository

[VERSION] is one of
* `master:` Uses the master branch 
* `r2.1:`  Uses the release branch used for MLCommons training 2.1 round

## Exported Variables
* `CM_MLPERF_TRAINING_SOURCE`: Directory path of the cloned inference repository
* `PYTHONPATH`: Is appended with the paths to vision module and the submission tools module

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9
