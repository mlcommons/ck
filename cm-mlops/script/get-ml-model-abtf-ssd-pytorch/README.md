Automatically generated README for this automation recipe: **get-ml-model-abtf-ssd-pytorch**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-abtf-ssd-pytorch,59cfc2a22f5d4f46) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-abtf-ssd-pytorch)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ml-model,abtf-ssd-pytorch*
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

````cmr "get ml-model abtf-ssd-pytorch" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ml-model,abtf-ssd-pytorch`

`cm run script --tags=get,ml-model,abtf-ssd-pytorch[,variations] `

*or*

`cmr "get ml-model abtf-ssd-pytorch"`

`cmr "get ml-model abtf-ssd-pytorch [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,abtf-ssd-pytorch'
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

```cmr "cm gui" --script="get,ml-model,abtf-ssd-pytorch"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,abtf-ssd-pytorch) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model abtf-ssd-pytorch[variations]" `

___
### Customization


#### Variations

  * Group "**epoch**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_e01`
      - Environment variables:
        - *CM_ML_MODEL_CHECKSUM*: `31d177228308bbe43917c912b01c2d67`
        - *CM_ML_MODEL_FILENAME*: `SSD_e1.pth`
        - *CM_ML_MODEL_URL*: `https://www.dropbox.com/scl/fi/7nqt5z8gplgeaveo933eo/SSD_e1.pth?rlkey=7lyb4qs2hzg491bfprwcuvx54&dl=0`
        - *CM_ML_MODEL*: `abtf-ssd-pytorch`
        - *CM_ML_MODEL_DATASET*: `coco`
        - *CM_ML_MODEL_IMAGE_HEIGHT*: `300`
        - *CM_ML_MODEL_IMAGE_WIDTH*: `300`
      - Workflow:
    * **`_e65`** (default)
      - Environment variables:
        - *CM_ML_MODEL_CHECKSUM*: `f769eb0321ac7fc1c16f982db6131d2f`
        - *CM_ML_MODEL_FILENAME*: `SSD_e65.pth`
        - *CM_ML_MODEL_URL*: `https://www.dropbox.com/scl/fi/wkegl2qxvm8cefbqq00o3/SSD_e65.pth?rlkey=ez26jafjdcly665npl6pdqxl8&dl=0`
        - *CM_ML_MODEL*: `abtf-ssd-pytorch`
        - *CM_ML_MODEL_DATASET*: `coco`
        - *CM_ML_MODEL_IMAGE_HEIGHT*: `300`
        - *CM_ML_MODEL_IMAGE_WIDTH*: `300`
      - Workflow:
    * `_local.#`
      - Environment variables:
        - *CM_ML_MODEL_FILENAME*: `#`
        - *CM_ML_MODEL_LOCAL*: `yes`
        - *CM_SKIP_DOWNLOAD*: `yes`
      - Workflow:

    </details>


#### Default variations

`_e65`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-abtf-ssd-pytorch/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * download,file,_wget
       * `if (CM_SKIP_DOWNLOAD  != yes)`
       * CM names: `--adr.['get-ml-model']...`
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-abtf-ssd-pytorch/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-abtf-ssd-pytorch/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-abtf-ssd-pytorch/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-abtf-ssd-pytorch/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-abtf-ssd-pytorch/_cm.json)

___
### Script output
`cmr "get ml-model abtf-ssd-pytorch [,variations]"  -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`