**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-kits19).**



Automatically generated README for this automation recipe: **get-dataset-kits19**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-dataset-kits19,79992bb221024ac5) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-kits19)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,dataset,medical-imaging,kits,original,kits19*
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

````cmr "get dataset medical-imaging kits original kits19" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,dataset,medical-imaging,kits,original,kits19`

`cm run script --tags=get,dataset,medical-imaging,kits,original,kits19[,variations] `

*or*

`cmr "get dataset medical-imaging kits original kits19"`

`cmr "get dataset medical-imaging kits original kits19 [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,medical-imaging,kits,original,kits19'
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

```cmr "cm gui" --script="get,dataset,medical-imaging,kits,original,kits19"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,medical-imaging,kits,original,kits19) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset medical-imaging kits original kits19[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calibration`
      - Environment variables:
        - *CM_DATASET_CALIBRATION*: `yes`
      - Workflow:
    * `_default`
      - Environment variables:
        - *CM_GIT_PATCH*: `no`
      - Workflow:
    * `_full-history`
      - Environment variables:
        - *CM_GIT_DEPTH*: ``
      - Workflow:
    * `_no-recurse-submodules`
      - Environment variables:
        - *CM_GIT_RECURSE_SUBMODULES*: ``
      - Workflow:
    * `_patch`
      - Environment variables:
        - *CM_GIT_PATCH*: `yes`
      - Workflow:
    * `_short-history`
      - Environment variables:
        - *CM_GIT_DEPTH*: `--depth 5`
      - Workflow:
    * `_validation`
      - Environment variables:
        - *CM_DATASET_VALIDATION*: `yes`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_CHECKOUT: `master`
* CM_GIT_DEPTH: `--depth 2`
* CM_GIT_PATCH: `no`
* CM_GIT_RECURSE_SUBMODULES: ``
* CM_GIT_URL: `https://github.com/neheller/kits19`

</details>

#### Versions
Default version: `master`

* `custom`
* `master`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-kits19/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-kits19/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-kits19/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-kits19/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-kits19/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-kits19/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-kits19/_cm.json)

___
### Script output
`cmr "get dataset medical-imaging kits original kits19 [,variations]"  -j`
#### New environment keys (filter)

* `CM_DATASET_*`
#### New environment keys auto-detected from customize

* `CM_DATASET_PATH`