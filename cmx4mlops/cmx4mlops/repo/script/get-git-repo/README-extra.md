# Get GIT Repository
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) git clones any specified GIT repository.

## Commands
To install
```
cm run script --tags=get,git,repo,_repo.<repo_name>,[VARIATION] 
```
where [VARIATION] is one of
* `patch:` Applies the `git.patch` to the cloned git repository
* `short-history:` Uses a git depth of last 10 commits (significantly reduces the download size)
* `full-history:` Uses the full git history
* `no-recurse-submodules:` Only download the main repository

## Exported Variables
* `CM_GIT_CHECKOUT_PATH`: Directory path of the cloned git repository

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9
