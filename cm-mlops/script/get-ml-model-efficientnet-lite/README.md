**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-efficientnet-lite).**



Automatically generated README for this automation recipe: **get-ml-model-efficientnet-lite**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-efficientnet-lite,1041f681977d4b7c) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-efficientnet-lite)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ml-model,efficientnet,raw,ml-model-efficientnet,ml-model-efficientnet-lite,lite,tflite,image-classification*
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

````cmr "get ml-model efficientnet raw ml-model-efficientnet ml-model-efficientnet-lite lite tflite image-classification" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ml-model,efficientnet,raw,ml-model-efficientnet,ml-model-efficientnet-lite,lite,tflite,image-classification`

`cm run script --tags=get,ml-model,efficientnet,raw,ml-model-efficientnet,ml-model-efficientnet-lite,lite,tflite,image-classification[,variations] `

*or*

`cmr "get ml-model efficientnet raw ml-model-efficientnet ml-model-efficientnet-lite lite tflite image-classification"`

`cmr "get ml-model efficientnet raw ml-model-efficientnet ml-model-efficientnet-lite lite tflite image-classification [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,efficientnet,raw,ml-model-efficientnet,ml-model-efficientnet-lite,lite,tflite,image-classification'
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

```cmr "cm gui" --script="get,ml-model,efficientnet,raw,ml-model-efficientnet,ml-model-efficientnet-lite,lite,tflite,image-classification"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,efficientnet,raw,ml-model-efficientnet,ml-model-efficientnet-lite,lite,tflite,image-classification) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model efficientnet raw ml-model-efficientnet ml-model-efficientnet-lite lite tflite image-classification[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_tflite`
      - Workflow:

    </details>


  * Group "**kind**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_lite0`** (default)
      - Environment variables:
        - *CM_ML_MODEL_EFFICIENTNET_LITE_KIND*: `lite0`
      - Workflow:
    * `_lite1`
      - Environment variables:
        - *CM_ML_MODEL_EFFICIENTNET_LITE_KIND*: `lite1`
      - Workflow:
    * `_lite2`
      - Environment variables:
        - *CM_ML_MODEL_EFFICIENTNET_LITE_KIND*: `lite2`
      - Workflow:
    * `_lite3`
      - Environment variables:
        - *CM_ML_MODEL_EFFICIENTNET_LITE_KIND*: `lite3`
      - Workflow:
    * `_lite4`
      - Environment variables:
        - *CM_ML_MODEL_EFFICIENTNET_LITE_KIND*: `lite4`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_ML_MODEL_EFFICIENTNET_LITE_PRECISION*: `fp32`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_PRECISION*: `fp32`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `fp32`
      - Workflow:
    * `_uint8`
      - Aliases: `_int8`
      - Environment variables:
        - *CM_ML_MODEL_EFFICIENTNET_LITE_PRECISION*: `int8`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `uint8`
        - *CM_ML_MODEL_PRECISION*: `uint8`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `uint8`
      - Workflow:

    </details>


  * Group "**resolution**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_resolution-224`** (default)
      - Environment variables:
        - *CM_ML_MODEL_IMAGE_HEIGHT*: `224`
        - *CM_ML_MODEL_IMAGE_WIDTH*: `224`
        - *CM_ML_MODEL_MOBILENET_RESOLUTION*: `224`
        - *CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS*: `_resolution.224`
      - Workflow:
    * `_resolution-240`
      - Environment variables:
        - *CM_ML_MODEL_IMAGE_HEIGHT*: `240`
        - *CM_ML_MODEL_IMAGE_WIDTH*: `240`
        - *CM_ML_MODEL_MOBILENET_RESOLUTION*: `240`
        - *CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS*: `_resolution.240`
      - Workflow:
    * `_resolution-260`
      - Environment variables:
        - *CM_ML_MODEL_IMAGE_HEIGHT*: `260`
        - *CM_ML_MODEL_IMAGE_WIDTH*: `260`
        - *CM_ML_MODEL_MOBILENET_RESOLUTION*: `260`
        - *CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS*: `_resolution.260`
      - Workflow:
    * `_resolution-280`
      - Environment variables:
        - *CM_ML_MODEL_IMAGE_HEIGHT*: `280`
        - *CM_ML_MODEL_IMAGE_WIDTH*: `280`
        - *CM_ML_MODEL_MOBILENET_RESOLUTION*: `280`
        - *CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS*: `_resolution.280`
      - Workflow:
    * `_resolution-300`
      - Environment variables:
        - *CM_ML_MODEL_IMAGE_HEIGHT*: `300`
        - *CM_ML_MODEL_IMAGE_WIDTH*: `300`
        - *CM_ML_MODEL_MOBILENET_RESOLUTION*: `300`
        - *CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS*: `_resolution.300`
      - Workflow:

    </details>


#### Default variations

`_fp32,_lite0,_resolution-224`

#### Valid variation combinations checked by the community



* `_lite0,_resolution-224`
* `_lite1,_resolution-240`
* `_lite2,_resolution-260`
* `_lite3,_resolution-280`
* `_lite4,_resolution-300`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
* CM_ML_MODEL_PRECISION: `fp32`
* CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`

</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-efficientnet-lite/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-efficientnet-lite/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-efficientnet-lite/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-efficientnet-lite/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-efficientnet-lite/_cm.json)

___
### Script output
`cmr "get ml-model efficientnet raw ml-model-efficientnet ml-model-efficientnet-lite lite tflite image-classification [,variations]"  -j`
#### New environment keys (filter)

* `CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS`
* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`
* `CM_ML_MODEL_PATH`
* `CM_ML_MODEL_STARTING_WEIGHTS_FILENAME`