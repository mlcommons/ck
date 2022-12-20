*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
  * [ Script input flags mapped to environment](#script-input-flags-mapped-to-environment)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Docker automation.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
build,docker,image,docker-image,dockerimage

___
### Default environment

___
### CM script workflow

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image/_cm.json)***
     * build,dockerfile
       - CM script [build-dockerfile](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image/_cm.json)
___
### New environment export

___
### New environment detected from customize

___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="build,docker,image,docker-image,dockerimage"`

*or*

`cm run script "build docker image docker-image dockerimage"`

*or*

`cm run script 2c3c4ba2413442e7`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'build,docker,image,docker-image,dockerimage'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* cache --> **CM_DOCKER_CACHE**
* cm_repo --> **CM_MLOPS_REPO**
* docker_os --> **CM_DOCKER_OS**
* docker_os_version --> **CM_DOCKER_OS_VERSION**
* dockerfile --> **CM_DOCKERFILE_WITH_PATH**
* gh_token --> **CM_GH_TOKEN**
* image_repo --> **CM_DOCKER_IMAGE_REPO**
* image_name --> **CM_DOCKER_IMAGE_NAME**
* image_tag --> **CM_DOCKER_IMAGE_TAG**
* script_tags --> **CM_DOCKER_RUN_SCRIPT_TAGS**
* real_run --> **CM_REAL_RUN**
* pre_run_cmds --> **CM_DOCKER_PRE_RUN_COMMANDS**
* post_run_cmds --> **CM_DOCKER_POST_RUN_COMMANDS**

Examples:

```bash
cm run script "build docker image docker-image dockerimage" --cache=...
```
```python
r=cm.access({... , "cache":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)