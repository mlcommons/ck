**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cmsis_5).**



Automatically generated README for this automation recipe: **get-cmsis_5**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-cmsis_5,2258c212b11443f5) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cmsis_5)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,cmsis,cmsis_5,arm-software*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "get cmsis cmsis_5 arm-software" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,cmsis,cmsis_5,arm-software`

`cm run script --tags=get,cmsis,cmsis_5,arm-software[,variations] `

*or*

`cmr "get cmsis cmsis_5 arm-software"`

`cmr "get cmsis cmsis_5 arm-software [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,cmsis,cmsis_5,arm-software'
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

```cmr "cm gui" --script="get,cmsis,cmsis_5,arm-software"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,cmsis,cmsis_5,arm-software) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get cmsis cmsis_5 arm-software[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_recurse-submodules`
      - Environment variables:
        - *CM_GIT_RECURSE_SUBMODULES*: `--recurse-submodules`
      - Workflow:
    * `_short-history`
      - Environment variables:
        - *CM_GIT_DEPTH*: `--depth 10`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_DEPTH: ``
* CM_GIT_PATCH: `no`
* CM_GIT_URL: `https://github.com/ARM-software/CMSIS_5.git`

</details>

#### Versions
Default version: `custom`

* `custom`
* `develop`
* `master`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cmsis_5/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cmsis_5/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cmsis_5/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cmsis_5/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cmsis_5/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cmsis_5/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cmsis_5/_cm.json)

___
### Script output
`cmr "get cmsis cmsis_5 arm-software [,variations]"  -j`
#### New environment keys (filter)

* `CMSIS*`
#### New environment keys auto-detected from customize
