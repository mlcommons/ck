**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/build-dockerfile).**



Automatically generated README for this automation recipe: **build-dockerfile**

Category: **Docker automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=build-dockerfile,e66a7483230d4641) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-dockerfile)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *build,dockerfile*
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

````cmr "build dockerfile" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=build,dockerfile`

`cm run script --tags=build,dockerfile[,variations] [--input_flags]`

*or*

`cmr "build dockerfile"`

`cmr "build dockerfile [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'build,dockerfile'
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

```cmr "cm gui" --script="build,dockerfile"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=build,dockerfile) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "build dockerfile[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_slim`
      - Environment variables:
        - *CM_DOCKER_BUILD_SLIM*: `yes`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--build=value`  &rarr;  `CM_BUILD_DOCKER_IMAGE=value`
* `--cache=value`  &rarr;  `CM_DOCKER_CACHE=value`
* `--cm_repo=value`  &rarr;  `CM_MLOPS_REPO=value`
* `--cm_repo_flags=value`  &rarr;  `CM_DOCKER_ADD_FLAG_TO_CM_MLOPS_REPO=value`
* `--cm_repos=value`  &rarr;  `CM_DOCKER_EXTRA_CM_REPOS=value`
* `--comments=value`  &rarr;  `CM_DOCKER_RUN_COMMENTS=value`
* `--copy_files=value`  &rarr;  `CM_DOCKER_COPY_FILES=value`
* `--docker_base_image=value`  &rarr;  `CM_DOCKER_IMAGE_BASE=value`
* `--docker_os=value`  &rarr;  `CM_DOCKER_OS=value`
* `--docker_os_version=value`  &rarr;  `CM_DOCKER_OS_VERSION=value`
* `--extra_sys_deps=value`  &rarr;  `CM_DOCKER_EXTRA_SYS_DEPS=value`
* `--fake_docker_deps=value`  &rarr;  `CM_DOCKER_FAKE_DEPS=value`
* `--fake_run_option=value`  &rarr;  `CM_DOCKER_FAKE_RUN_OPTION=value`
* `--file_path=value`  &rarr;  `CM_DOCKERFILE_WITH_PATH=value`
* `--gh_token=value`  &rarr;  `CM_GH_TOKEN=value`
* `--image_repo=value`  &rarr;  `CM_DOCKER_IMAGE_REPO=value`
* `--image_tag=value`  &rarr;  `CM_DOCKER_IMAGE_TAG=value`
* `--package_manager_update_cmd=value`  &rarr;  `CM_PACKAGE_MANAGER_UPDATE_CMD=value`
* `--pip_extra_flags=value`  &rarr;  `CM_DOCKER_PIP_INSTALL_EXTRA_FLAGS=value`
* `--post_file=value`  &rarr;  `DOCKER_IMAGE_POST_FILE=value`
* `--post_run_cmds=value`  &rarr;  `CM_DOCKER_POST_RUN_COMMANDS=value`
* `--pre_run_cmds=value`  &rarr;  `CM_DOCKER_PRE_RUN_COMMANDS=value`
* `--real_run=value`  &rarr;  `CM_REAL_RUN=value`
* `--run_cmd=value`  &rarr;  `CM_DOCKER_RUN_CMD=value`
* `--run_cmd_extra=value`  &rarr;  `CM_DOCKER_RUN_CMD_EXTRA=value`
* `--script_tags=value`  &rarr;  `CM_DOCKER_RUN_SCRIPT_TAGS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "build":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_DOCKER_BUILD_SLIM: `no`
* CM_DOCKER_OS: `ubuntu`
* CM_DOCKER_IMAGE_EOL: `
`

</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-dockerfile/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-dockerfile/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-dockerfile/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-dockerfile/_cm.json)
  1. Run "postrocess" function from customize.py
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-dockerfile/_cm.json)***
     * build,docker,image
       * `if (CM_BUILD_DOCKER_IMAGE in ['yes', '1'])`
       * CM names: `--adr.['build-docker-image']...`
       - CM script: [build-docker-image](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image)

___
### Script output
`cmr "build dockerfile [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_DOCKERFILE_*`
#### New environment keys auto-detected from customize

* `CM_DOCKERFILE_WITH_PATH`