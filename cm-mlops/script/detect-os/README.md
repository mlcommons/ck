**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/detect-os).**



Automatically generated README for this automation recipe: **detect-os**

Category: **Platform information**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=detect-os,863735b7db8c44fc) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-os)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *detect-os,detect,os,info*
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

````cmr "detect-os detect os info" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=detect-os,detect,os,info`

`cm run script --tags=detect-os,detect,os,info `

*or*

`cmr "detect-os detect os info"`

`cmr "detect-os detect os info " `


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
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-os/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-os/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-os/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-os/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-os/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-os/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-os/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-os/_cm.json)***
     * get,sys-utils-min
       * `if (CM_HOST_OS_TYPE  == windows)`
       - CM script: [get-sys-utils-min](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min)

___
### Script output
`cmr "detect-os detect os info "  -j`
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