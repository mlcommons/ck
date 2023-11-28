<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
* [Customization](#customization)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

#### Summary

* Category: *Platform information.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *detect-os,detect,os,info*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=detect-os,detect,os,info `

2. `cmr "detect-os detect os info" `

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'detect-os,detect,os,info'
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

```cmr "cm gui" --script="detect-os,detect,os,info"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=detect-os,detect,os,info) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "detect-os detect os info" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/_cm.json)***
     * get,sys-utils-min
       * `if (CM_HOST_OS_TYPE  == windows)`
       - CM script: [get-sys-utils-min](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min)
</details>

___
### Script output
`cmr "detect-os detect os info"  -j`
#### New environment keys (filter)

* `+CM_HOST_OS_*`
* `+PATH`
* `CM_HOST_OS_*`
* `CM_HOST_PLATFORM_*`
* `CM_HOST_PYTHON_*`
* `CM_HOST_SYSTEM_NAME`
* `CM_RUN_STATE_DOCKER`
#### New environment keys auto-detected from customize

* `CM_HOST_OS_BITS`
* `CM_HOST_OS_MACHINE`
* `CM_HOST_OS_PACKAGE_MANAGER`
* `CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD`
* `CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD`
* `CM_HOST_OS_TYPE`
* `CM_HOST_PYTHON_BITS`
* `CM_HOST_SYSTEM_NAME`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)