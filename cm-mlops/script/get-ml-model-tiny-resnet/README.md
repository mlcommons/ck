**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-tiny-resnet).**



Automatically generated README for this automation recipe: **get-ml-model-tiny-resnet**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-tiny-resnet,dd5ec11c3f6e49eb) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-tiny-resnet)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,raw,ml-model,resnet,pretrained,tiny,model,ic,ml-model-tiny-resnet,image-classification*
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

````cmr "get raw ml-model resnet pretrained tiny model ic ml-model-tiny-resnet image-classification" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,raw,ml-model,resnet,pretrained,tiny,model,ic,ml-model-tiny-resnet,image-classification`

`cm run script --tags=get,raw,ml-model,resnet,pretrained,tiny,model,ic,ml-model-tiny-resnet,image-classification[,variations] `

*or*

`cmr "get raw ml-model resnet pretrained tiny model ic ml-model-tiny-resnet image-classification"`

`cmr "get raw ml-model resnet pretrained tiny model ic ml-model-tiny-resnet image-classification [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,raw,ml-model,resnet,pretrained,tiny,model,ic,ml-model-tiny-resnet,image-classification'
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

```cmr "cm gui" --script="get,raw,ml-model,resnet,pretrained,tiny,model,ic,ml-model-tiny-resnet,image-classification"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,raw,ml-model,resnet,pretrained,tiny,model,ic,ml-model-tiny-resnet,image-classification) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get raw ml-model resnet pretrained tiny model ic ml-model-tiny-resnet image-classification[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_batch_size.#`
      - Environment variables:
        - *CM_ML_MODEL_BATCH_SIZE*: `#`
      - Workflow:
    * `_tflite,int8`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://github.com/mlcommons/tiny/raw/master/benchmark/training/image_classification/trained_models/pretrainedResnet_quant.tflite`
        - *CM_DOWNLOAD_CHECKSUM*: `2d6dd48722471313e4c4528249205ae3`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_onnx`
      - Environment variables:
        - *CM_TMP_ML_MODEL_TF2ONNX*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,python3
             * CM names: `--adr.['python,python3']...`
             - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
           * get,tiny,model,resnet,_tflite
             * CM names: `--adr.['tflite-resnet-model', 'dependent-model']...`
             - CM script: [get-ml-model-tiny-resnet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-tiny-resnet)
           * get,generic-python-lib,_package.tf2onnx
             * CM names: `--adr.['tf2onnx']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * **`_tflite`** (default)
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `85`
        - *CM_ML_MODEL_DATA_LAYOUT*: `NHWC`
        - *CM_ML_MODEL_FRAMEWORK*: `tflite`
        - *CM_ML_MODEL_GIVEN_CHANNEL_MEANS*: ``
        - *CM_ML_MODEL_INPUT_LAYERS*: ``
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: ``
        - *CM_ML_MODEL_INPUT_SHAPES*: ``
        - *CM_ML_MODEL_NORMALIZE_DATA*: `0`
        - *CM_ML_MODEL_OUTPUT_LAYERS*: ``
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: ``
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `<<<CM_PACKAGE_URL>>>`
        - *CM_ML_MODEL_SUBTRACT_MEANS*: `YES`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_fp32`
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
        - *CM_ML_MODEL_PRECISION*: `fp32`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
      - Workflow:
    * **`_int8`** (default)
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `int8`
        - *CM_ML_MODEL_PRECISION*: `int8`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `int8`
      - Workflow:
    * `_uint8`
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `uint8`
        - *CM_ML_MODEL_PRECISION*: `uint8`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `uint8`
      - Workflow:

    </details>


#### Default variations

`_int8,_tflite`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-tiny-resnet/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-tiny-resnet/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-tiny-resnet/_cm.json)***
     * download-and-extract
       * `if (CM_PACKAGE_URL  == on)`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-tiny-resnet/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-tiny-resnet/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-tiny-resnet/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-tiny-resnet/_cm.json)

___
### Script output
`cmr "get raw ml-model resnet pretrained tiny model ic ml-model-tiny-resnet image-classification [,variations]"  -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`