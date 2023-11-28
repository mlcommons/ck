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
  * [ Variations](#variations)
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

* Category: *TinyML automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-fpgaconvnet-app-tinyml)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *create,app,fpgaconvnet*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=create,app,fpgaconvnet[,variations] `

2. `cmr "create app fpgaconvnet[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'create,app,fpgaconvnet'
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

```cmr "cm gui" --script="create,app,fpgaconvnet"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=create,app,fpgaconvnet) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "create app fpgaconvnet[ variations]" `

___
### Customization


#### Variations

  * Group "**benchmark**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_ic`** (default)
      - Workflow:

    </details>


  * Group "**board**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_zc706`** (default)
      - Environment variables:
        - *CM_TINY_BOARD*: `zc706`
      - Workflow:

    </details>


#### Default variations

`_ic,_zc706`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-fpgaconvnet-app-tinyml/_cm.json)***
     * create,fpgaconvnet,config
       * CM names: `--adr.['config-generator']...`
       - CM script: [create-fpgaconvnet-config-tinyml](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-fpgaconvnet-config-tinyml)
     * get,xilinx,sdk
       * CM names: `--adr.['xilinx-sdk']...`
       - CM script: [get-xilinx-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-xilinx-sdk)
     * get,tensorflow
       * CM names: `--adr.['tensorflow']...`
       - CM script: [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-fpgaconvnet-app-tinyml/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-fpgaconvnet-app-tinyml/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-fpgaconvnet-app-tinyml/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-fpgaconvnet-app-tinyml/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-fpgaconvnet-app-tinyml/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-fpgaconvnet-app-tinyml/_cm.json)
</details>

___
### Script output
`cmr "create app fpgaconvnet[,variations]"  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)