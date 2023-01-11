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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
run,docker,container

___
### Default environment

___
### CM script workflow

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/_cm.json)***
     * build,docker,image
       * `if (CM_DOCKER_IMAGE_EXISTS  != yes)`
       * CM names: `--adr.['build-docker-image']...`
       - CM script: [build-docker-image](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/_cm.json)
___
### New environment export

___
### New environment detected from customize

* **CM_DOCKER_IMAGE_EXISTS**
* **CM_DOCKER_IMAGE_RECREATE**
* **CM_DOCKER_RUN_CMD**
* **CM_DOCKER_RUN_SCRIPT_TAGS**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="run,docker,container"`

*or*

`cm run script "run docker container"`

*or*

`cm run script 1e0c884107514b46`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,docker,container'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* base --> **CM_DOCKER_IMAGE_BASE**
* cm_repo --> **CM_MLOPS_REPO**
* recreate --> **CM_DOCKER_IMAGE_RECREATE**
* gh_token --> **CM_GH_TOKEN**
* image_repo --> **CM_DOCKER_IMAGE_REPO**
* image_tag --> **CM_DOCKER_IMAGE_TAG**
* docker_os --> **CM_DOCKER_OS**
* docker_os_version --> **CM_DOCKER_OS_VERSION**
* script_tags --> **CM_DOCKER_RUN_SCRIPT_TAGS**
* run_cmd_extra --> **CM_DOCKER_RUN_CMD_EXTRA**
* real_run --> **CM_REAL_RUN**
* run_cmd --> **CM_DOCKER_RUN_CMD**
* pre_run_cmds --> **CM_DOCKER_PRE_RUN_COMMANDS**
* post_run_cmds --> **CM_DOCKER_POST_RUN_COMMANDS**
* pass_user_group --> **CM_DOCKER_PASS_USER_GROUP**
* mounts --> **CM_DOCKER_VOLUME_MOUNTS**
* port_maps --> **CM_DOCKER_PORT_MAPS**
* device --> **CM_DOCKER_ADD_DEVICE**
* cache --> **CM_DOCKER_CACHE**

Examples:

```bash
cm run script "run docker container" --base=...
```
```python
r=cm.access({... , "base":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)