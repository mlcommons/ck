**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/create-fpgaconvnet-config-tinyml).**



Automatically generated README for this automation recipe: **create-fpgaconvnet-config-tinyml**

Category: **TinyML automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=create-fpgaconvnet-config-tinyml,f6cdad166cfa47bc) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-config-tinyml)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *create,config,fpgaconvnet*
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

````cmr "create config fpgaconvnet" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=create,config,fpgaconvnet`

`cm run script --tags=create,config,fpgaconvnet[,variations] `

*or*

`cmr "create config fpgaconvnet"`

`cmr "create config fpgaconvnet [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'create,config,fpgaconvnet'
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

```cmr "cm gui" --script="create,config,fpgaconvnet"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=create,config,fpgaconvnet) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "create config fpgaconvnet[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_zc706,ic`
      - Environment variables:
        - *CM_TINY_NETWORK_NAME*: `zc706-resnet`
      - Workflow:

    </details>


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


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-config-tinyml/_cm.json)***
     * get,python3
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,ml-model,tiny
       * CM names: `--adr.['ml-model']...`
       - CM script: [get-ml-model-tiny-resnet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-tiny-resnet)
     * get,git,repo,_repo.https://github.com/mlcommons/submissions_tiny_v1.1
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-config-tinyml/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-config-tinyml/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-config-tinyml/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-config-tinyml/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-config-tinyml/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-config-tinyml/_cm.json)

___
### Script output
`cmr "create config fpgaconvnet [,variations]"  -j`
#### New environment keys (filter)

* `CM_TINY_FPGACONVNET*`
#### New environment keys auto-detected from customize

* `CM_TINY_FPGACONVNET_' + network_env_name + '_CODE_PATH`
* `CM_TINY_FPGACONVNET_' + network_env_name + '_RUN_DIR`
* `CM_TINY_FPGACONVNET_CONFIG_FILE_' + network_env_name + '_PATH`
* `CM_TINY_FPGACONVNET_NETWORK_ENV_NAME`
* `CM_TINY_FPGACONVNET_NETWORK_NAME`