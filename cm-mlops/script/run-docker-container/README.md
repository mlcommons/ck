**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/run-docker-container).**



Automatically generated README for this automation recipe: **run-docker-container**

Category: **Docker automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=run-docker-container,1e0c884107514b46) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-docker-container)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *run,docker,container*
* Output cached? *False*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "run docker container" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=run,docker,container`

`cm run script --tags=run,docker,container [--input_flags]`

*or*

`cmr "run docker container"`

`cmr "run docker container " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

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

</details>


#### Run this script via GUI

```cmr "cm gui" --script="run,docker,container"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,docker,container) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run docker container" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--all_gpus=value`  &rarr;  `CM_DOCKER_ADD_ALL_GPUS=value`
* `--base=value`  &rarr;  `CM_DOCKER_IMAGE_BASE=value`
* `--cache=value`  &rarr;  `CM_DOCKER_CACHE=value`
* `--cm_repo=value`  &rarr;  `CM_MLOPS_REPO=value`
* `--detached=value`  &rarr;  `CM_DOCKER_DETACHED_MODE=value`
* `--device=value`  &rarr;  `CM_DOCKER_ADD_DEVICE=value`
* `--docker_image_base=value`  &rarr;  `CM_DOCKER_IMAGE_BASE=value`
* `--docker_os=value`  &rarr;  `CM_DOCKER_OS=value`
* `--docker_os_version=value`  &rarr;  `CM_DOCKER_OS_VERSION=value`
* `--extra_run_args=value`  &rarr;  `CM_DOCKER_EXTRA_RUN_ARGS=value`
* `--fake_run_option=value`  &rarr;  `CM_DOCKER_FAKE_RUN_OPTION=value`
* `--gh_token=value`  &rarr;  `CM_GH_TOKEN=value`
* `--image_name=value`  &rarr;  `CM_DOCKER_IMAGE_NAME=value`
* `--image_repo=value`  &rarr;  `CM_DOCKER_IMAGE_REPO=value`
* `--image_tag=value`  &rarr;  `CM_DOCKER_IMAGE_TAG=value`
* `--interactive=value`  &rarr;  `CM_DOCKER_INTERACTIVE_MODE=value`
* `--it=value`  &rarr;  `CM_DOCKER_INTERACTIVE=value`
* `--mounts=value`  &rarr;  `CM_DOCKER_VOLUME_MOUNTS=value`
* `--pass_user_group=value`  &rarr;  `CM_DOCKER_PASS_USER_GROUP=value`
* `--port_maps=value`  &rarr;  `CM_DOCKER_PORT_MAPS=value`
* `--post_run_cmds=value`  &rarr;  `CM_DOCKER_POST_RUN_COMMANDS=value`
* `--pre_run_cmds=value`  &rarr;  `CM_DOCKER_PRE_RUN_COMMANDS=value`
* `--real_run=value`  &rarr;  `CM_REAL_RUN=value`
* `--recreate=value`  &rarr;  `CM_DOCKER_IMAGE_RECREATE=value`
* `--run_cmd=value`  &rarr;  `CM_DOCKER_RUN_CMD=value`
* `--run_cmd_extra=value`  &rarr;  `CM_DOCKER_RUN_CMD_EXTRA=value`
* `--save_script=value`  &rarr;  `CM_DOCKER_SAVE_SCRIPT=value`
* `--script_tags=value`  &rarr;  `CM_DOCKER_RUN_SCRIPT_TAGS=value`
* `--shm_size=value`  &rarr;  `CM_DOCKER_SHM_SIZE=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "all_gpus":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_DOCKER_DETACHED_MODE: `yes`

</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-docker-container/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-docker-container/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-docker-container/_cm.json)***
     * build,docker,image
       * `if (CM_DOCKER_IMAGE_EXISTS  != yes)`
       * CM names: `--adr.['build-docker-image']...`
       - CM script: [build-docker-image](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-docker-container/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-docker-container/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-docker-container/_cm.json)

___
### Script output
`cmr "run docker container " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
