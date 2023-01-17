<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *Docker automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *build,dockerfile*
* Output cached?: *False*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=build,dockerfile(,variations from below) (flags from below)`

*or*

`cm run script "build dockerfile (variations from below)" (flags from below)`

*or*

`cm run script e66a7483230d4641`

#### CM Python API

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

#### CM modular Docker container
*TBD*
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

* --**build**=value --> **CM_BUILD_DOCKER_IMAGE**=value
* --**cache**=value --> **CM_DOCKER_CACHE**=value
* --**cm_repo**=value --> **CM_MLOPS_REPO**=value
* --**comments**=value --> **CM_DOCKER_RUN_COMMENTS**=value
* --**docker_os**=value --> **CM_DOCKER_OS**=value
* --**docker_os_version**=value --> **CM_DOCKER_OS_VERSION**=value
* --**file_path**=value --> **CM_DOCKERFILE_WITH_PATH**=value
* --**gh_token**=value --> **CM_GH_TOKEN**=value
* --**image_repo**=value --> **CM_DOCKER_IMAGE_REPO**=value
* --**image_tag**=value --> **CM_DOCKER_IMAGE_TAG**=value
* --**post_run_cmds**=value --> **CM_DOCKER_POST_RUN_COMMANDS**=value
* --**pre_run_cmds**=value --> **CM_DOCKER_PRE_RUN_COMMANDS**=value
* --**real_run**=value --> **CM_REAL_RUN**=value
* --**run_cmd**=value --> **CM_DOCKER_RUN_CMD**=value
* --**run_cmd_extra**=value --> **CM_DOCKER_RUN_CMD_EXTRA**=value
* --**script_tags**=value --> **CM_DOCKER_RUN_SCRIPT_TAGS**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "build":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_DOCKER_BUILD_SLIM: **no**
* CM_DOCKER_OS: **ubuntu**
* CM_DOCKER_IMAGE_EOL: **
**

</details>

___
### Script workflow, dependencies and native scripts

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile/_cm.json)
  1. Run "postrocess" function from customize.py
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile/_cm.json)***
     * build,docker,image
       * `if (CM_BUILD_DOCKER_IMAGE in ['yes', '1'])`
       * CM names: `--adr.['build-docker-image']...`
       - CM script: [build-docker-image](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image)
___
### Script output
#### New environment keys (filter)

* **CM_DOCKERFILE_***
#### New environment keys auto-detected from customize

* **CM_DOCKERFILE_WITH_PATH**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)