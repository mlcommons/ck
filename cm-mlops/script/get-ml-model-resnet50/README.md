<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Default environment](#default-environment)
  * [ Variations](#variations)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys](#new-environment-keys)
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *ML/AI models.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,raw,ml-model,resnet50,ml-model-resnet50,image-classification*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=get,raw,ml-model,resnet50,ml-model-resnet50,image-classification(,variations from below) (flags from below)`

*or*

`cm run script "get raw ml-model resnet50 ml-model-resnet50 image-classification (variations from below)" (flags from below)`

*or*

`cm run script 56203e4e998b4bc0`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,raw,ml-model,resnet50,ml-model-resnet50,image-classification'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>

#### CM modular Docker container
*TBD*
___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.


</details>


#### Variations

  * *No group (any variation can be selected)*
<details>
<summary>Click here to expand this section.</summary>

    * `_onnx,opset-11`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/4735647/files/resnet50_v1.onnx`
      - Workflow:
    * `_onnx,opset-8`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/2592612/files/resnet50_v1.onnx`
      - Workflow:
    * `_pytorch,fp32`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/4588417/files/resnet50-19c8e357.pth`
      - Workflow:
    * `_pytorch,int8`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/4589637/files/resnet50_INT8bit_quantized.pt`
      - Workflow:
    * `_tflite,argmax`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://www.dropbox.com/s/cvv2zlfo80h54uz/resnet50_v1.tflite.gz?dl=1`
        - *CM_UNZIP*: `yes`
        - *CM_ML_MODEL_FILE*: `resnet50_v1.tflite`
      - Workflow:
    * `_tflite,no-argmax`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://www.dropbox.com/s/vhuqo0wc39lky0a/resnet50_v1.no-argmax.tflite?dl=1`
        - *CM_ML_MODEL_FILE*: `resnet50_v1.no-argmax.tflite`
      - Workflow:

</details>


  * Group "**framework**"
<details>
<summary>Click here to expand this section.</summary>

    * **`_onnx`** (default)
      - Aliases: `_onnxruntime`
      - Environment variables:
        - *CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
        - *CM_ML_MODEL_FRAMEWORK*: `onnx`
        - *CM_ML_MODEL_INPUT_LAYERS*: `input_tensor:0`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `input_tensor:0`
        - *CM_ML_MODEL_OUTPUT_LAYERS*: `softmax_tensor:0`
        - *CM_ML_MODEL_INPUT_SHAPES*: `\"input_tensor:0\": (BATCH_SIZE, 3, 224, 224)`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `softmax_tensor:0`
        - *CM_ML_MODEL_VER*: `1.5`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
        - *CM_ML_MODEL_FRAMEWORK*: `pytorch`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `?`
        - *CM_ML_MODEL_OUTPUT_LAYERS*: `output`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `?`
        - *CM_ML_MODEL_INPUT_SHAPES*: `(\"input_tensor:0\", [BATCH_SIZE, 3, 224, 224])`
        - *CM_ML_MODEL_GIVEN_CHANNEL_MEANS*: `?`
        - *CM_ML_STARTING_WEIGHTS_FILENAME*: `<<<CM_PACKAGE_URL>>>`
      - Workflow:
    * `_tensorflow`
      - Aliases: `_tf`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `76.456`
        - *CM_ML_MODEL_DATA_LAYOUT*: `NHWC`
        - *CM_ML_MODEL_FRAMEWORK*: `tensorflow`
        - *CM_ML_MODEL_GIVEN_CHANNEL_MEANS*: `123.68 116.78 103.94`
        - *CM_ML_MODEL_INPUT_LAYERS*: `input_tensor`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `input_tensor`
        - *CM_ML_MODEL_NORMALIZE_DATA*: `0`
        - *CM_ML_MODEL_OUTPUT_LAYERS*: `softmax_tensor`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `softmax_tensor`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `<<<CM_PACKAGE_URL>>>`
        - *CM_ML_MODEL_SUBTRACT_MEAN*: `YES`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/2535873/files/resnet50_v1.pb`
      - Workflow:
    * `_tflite`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `76.456`
        - *CM_ML_MODEL_DATA_LAYOUT*: `NHWC`
        - *CM_ML_MODEL_FRAMEWORK*: `tflite`
        - *CM_ML_MODEL_GIVEN_CHANNEL_MEANS*: `123.68 116.78 103.94`
        - *CM_ML_MODEL_INPUT_LAYERS*: `input_tensor`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `input_tensor`
        - *CM_ML_MODEL_NORMALIZE_DATA*: `0`
        - *CM_ML_MODEL_OUTPUT_LAYERS*: `softmax_tensor`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `softmax_tensor`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `<<<CM_PACKAGE_URL>>>`
        - *CM_ML_MODEL_SUBTRACT_MEAN*: `YES`
        - *CM_PACKAGE_URL*: `https://www.dropbox.com/s/cvv2zlfo80h54uz/resnet50_v1.tflite.gz`
      - Workflow:

</details>


  * Group "**model-output**"
<details>
<summary>Click here to expand this section.</summary>

    * **`_argmax`** (default)
      - Environment variables:
        - *CM_ML_MODEL_OUTPUT_LAYER_ARGMAX*: `yes`
      - Workflow:
    * `_no-argmax`
      - Environment variables:
        - *CM_ML_MODEL_OUTPUT_LAYER_ARGMAX*: `no`
      - Workflow:

</details>


  * Group "**opset-version**"
<details>
<summary>Click here to expand this section.</summary>

    * `_opset-11`
      - Environment variables:
        - *CM_ML_MODEL_ONNX_OPSET*: `11`
      - Workflow:
    * `_opset-8`
      - Environment variables:
        - *CM_ML_MODEL_ONNX_OPSET*: `8`
      - Workflow:

</details>


  * Group "**precision**"
<details>
<summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
        - *CM_ML_MODEL_PRECISION*: `fp32`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
      - Workflow:
    * `_int8`
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

___
### Script workflow, dependencies and native scripts

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50/_cm.json)
___
### Script output
#### New environment keys

* **CM_ML_MODEL_***
#### New environment keys auto-detected from customize

* **CM_ML_MODEL_FILE**
* **CM_ML_MODEL_FILE_WITH_PATH**
* **CM_ML_MODEL_PATH**
* **CM_STARTING_WEIGHTS_FILENAME**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)