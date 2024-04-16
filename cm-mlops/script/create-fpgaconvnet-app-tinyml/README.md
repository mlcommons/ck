**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/create-fpgaconvnet-app-tinyml).**



Automatically generated README for this automation recipe: **create-fpgaconvnet-app-tinyml**

Category: **TinyML automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=create-fpgaconvnet-app-tinyml,618f3520e98e4728) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-app-tinyml)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *create,app,fpgaconvnet*
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

````cmr "create app fpgaconvnet" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=create,app,fpgaconvnet`

`cm run script --tags=create,app,fpgaconvnet[,variations] `

*or*

`cmr "create app fpgaconvnet"`

`cmr "create app fpgaconvnet [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

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

`cm docker script "create app fpgaconvnet[variations]" `

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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-app-tinyml/_cm.json)***
     * create,fpgaconvnet,config
       * CM names: `--adr.['config-generator']...`
       - CM script: [create-fpgaconvnet-config-tinyml](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-fpgaconvnet-config-tinyml)
     * get,xilinx,sdk
       * CM names: `--adr.['xilinx-sdk']...`
       - CM script: [get-xilinx-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-xilinx-sdk)
     * get,tensorflow
       * CM names: `--adr.['tensorflow']...`
       - CM script: [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-app-tinyml/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-app-tinyml/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-app-tinyml/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-app-tinyml/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-app-tinyml/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-app-tinyml/_cm.json)

___
### Script output
`cmr "create app fpgaconvnet [,variations]"  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
