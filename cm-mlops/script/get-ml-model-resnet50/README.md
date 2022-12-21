*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Variations](#variations)
  * [ All variations](#all-variations)
  * [ Variations by groups](#variations-by-groups)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

ML/AI models.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,raw,ml-model,resnet50,ml-model-resnet50,image-classification

___
### Variations
#### All variations
* **fp32** (default)
  - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
  - *ENV CM_ML_MODEL_PRECISION*: `fp32`
  - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
* int8
  - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `int8`
  - *ENV CM_ML_MODEL_PRECISION*: `int8`
  - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `int8`
* **onnx** (default)
  - *ENV CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
  - *ENV CM_ML_MODEL_FRAMEWORK*: `onnx`
  - *ENV CM_ML_MODEL_INPUT_LAYERS*: `input_tensor:0`
  - *ENV CM_ML_MODEL_INPUT_LAYER_NAME*: `input_tensor:0`
  - *ENV CM_ML_MODEL_OUTPUT_LAYERS*: `softmax_tensor:0`
  - *ENV CM_ML_MODEL_INPUT_SHAPES*: `\"input_tensor:0\": (BATCH_SIZE, 3, 224, 224)`
  - *ENV CM_ML_MODEL_OUTPUT_LAYER_NAME*: `softmax_tensor:0`
  - *ENV CM_ML_MODEL_VER*: `1.5`
* onnx,opset-11
  - *ENV CM_PACKAGE_URL*: `https://zenodo.org/record/4735647/files/resnet50_v1.onnx`
* onnx,opset-8
  - *ENV CM_PACKAGE_URL*: `https://zenodo.org/record/2592612/files/resnet50_v1.onnx`
* onnxruntime
* opset-11
  - *ENV CM_ML_MODEL_ONNX_OPSET*: `11`
* opset-8
  - *ENV CM_ML_MODEL_ONNX_OPSET*: `8`
* pytorch
  - *ENV CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
  - *ENV CM_ML_MODEL_FRAMEWORK*: `pytorch`
  - *ENV CM_ML_MODEL_INPUT_LAYER_NAME*: `?`
  - *ENV CM_ML_MODEL_OUTPUT_LAYERS*: `output`
  - *ENV CM_ML_MODEL_OUTPUT_LAYER_NAME*: `?`
  - *ENV CM_ML_MODEL_INPUT_SHAPES*: `(\"input_tensor:0\", [BATCH_SIZE, 3, 224, 224])`
  - *ENV CM_ML_MODEL_GIVEN_CHANNEL_MEANS*: `?`
  - *ENV CM_ML_STARTING_WEIGHTS_FILENAME*: `<<<CM_PACKAGE_URL>>>`
* pytorch,fp32
  - *ENV CM_PACKAGE_URL*: `https://zenodo.org/record/4588417/files/resnet50-19c8e357.pth`
* pytorch,int8
  - *ENV CM_PACKAGE_URL*: `https://zenodo.org/record/4589637/files/resnet50_INT8bit_quantized.pt`
* tensorflow
  - *ENV CM_ML_MODEL_ACCURACY*: `76.456`
  - *ENV CM_ML_MODEL_DATA_LAYOUT*: `NHWC`
  - *ENV CM_ML_MODEL_FRAMEWORK*: `tensorflow`
  - *ENV CM_ML_MODEL_GIVEN_CHANNEL_MEANS*: `123.68 116.78 103.94`
  - *ENV CM_ML_MODEL_INPUT_LAYERS*: `input_tensor`
  - *ENV CM_ML_MODEL_INPUT_LAYER_NAME*: `input_tensor`
  - *ENV CM_ML_MODEL_NORMALIZE_DATA*: `0`
  - *ENV CM_ML_MODEL_OUTPUT_LAYERS*: `softmax_tensor`
  - *ENV CM_ML_MODEL_OUTPUT_LAYER_NAME*: `softmax_tensor`
  - *ENV CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `<<<CM_PACKAGE_URL>>>`
  - *ENV CM_ML_MODEL_SUBTRACT_MEAN*: `YES`
  - *ENV CM_PACKAGE_URL*: `https://zenodo.org/record/2535873/files/resnet50_v1.pb`
* tf
* tflite
* uint8
  - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `uint8`
  - *ENV CM_ML_MODEL_PRECISION*: `uint8`
  - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `uint8`

#### Variations by groups

  * framework
    * **onnx** (default)
      - *ENV CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
      - *ENV CM_ML_MODEL_FRAMEWORK*: `onnx`
      - *ENV CM_ML_MODEL_INPUT_LAYERS*: `input_tensor:0`
      - *ENV CM_ML_MODEL_INPUT_LAYER_NAME*: `input_tensor:0`
      - *ENV CM_ML_MODEL_OUTPUT_LAYERS*: `softmax_tensor:0`
      - *ENV CM_ML_MODEL_INPUT_SHAPES*: `\"input_tensor:0\": (BATCH_SIZE, 3, 224, 224)`
      - *ENV CM_ML_MODEL_OUTPUT_LAYER_NAME*: `softmax_tensor:0`
      - *ENV CM_ML_MODEL_VER*: `1.5`
    * pytorch
      - *ENV CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
      - *ENV CM_ML_MODEL_FRAMEWORK*: `pytorch`
      - *ENV CM_ML_MODEL_INPUT_LAYER_NAME*: `?`
      - *ENV CM_ML_MODEL_OUTPUT_LAYERS*: `output`
      - *ENV CM_ML_MODEL_OUTPUT_LAYER_NAME*: `?`
      - *ENV CM_ML_MODEL_INPUT_SHAPES*: `(\"input_tensor:0\", [BATCH_SIZE, 3, 224, 224])`
      - *ENV CM_ML_MODEL_GIVEN_CHANNEL_MEANS*: `?`
      - *ENV CM_ML_STARTING_WEIGHTS_FILENAME*: `<<<CM_PACKAGE_URL>>>`
    * tensorflow
      - *ENV CM_ML_MODEL_ACCURACY*: `76.456`
      - *ENV CM_ML_MODEL_DATA_LAYOUT*: `NHWC`
      - *ENV CM_ML_MODEL_FRAMEWORK*: `tensorflow`
      - *ENV CM_ML_MODEL_GIVEN_CHANNEL_MEANS*: `123.68 116.78 103.94`
      - *ENV CM_ML_MODEL_INPUT_LAYERS*: `input_tensor`
      - *ENV CM_ML_MODEL_INPUT_LAYER_NAME*: `input_tensor`
      - *ENV CM_ML_MODEL_NORMALIZE_DATA*: `0`
      - *ENV CM_ML_MODEL_OUTPUT_LAYERS*: `softmax_tensor`
      - *ENV CM_ML_MODEL_OUTPUT_LAYER_NAME*: `softmax_tensor`
      - *ENV CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `<<<CM_PACKAGE_URL>>>`
      - *ENV CM_ML_MODEL_SUBTRACT_MEAN*: `YES`
      - *ENV CM_PACKAGE_URL*: `https://zenodo.org/record/2535873/files/resnet50_v1.pb`

  * opset-version
    * opset-11
      - *ENV CM_ML_MODEL_ONNX_OPSET*: `11`
    * opset-8
      - *ENV CM_ML_MODEL_ONNX_OPSET*: `8`

  * precision
    * **fp32** (default)
      - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
      - *ENV CM_ML_MODEL_PRECISION*: `fp32`
      - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
    * int8
      - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `int8`
      - *ENV CM_ML_MODEL_PRECISION*: `int8`
      - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `int8`
    * uint8
      - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `uint8`
      - *ENV CM_ML_MODEL_PRECISION*: `uint8`
      - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `uint8`
___
### Default environment

___
### CM script workflow

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50/_cm.json)
___
### New environment export

* **CM_ML_MODEL_***
___
### New environment detected from customize

* **CM_ML_MODEL_FILE**
* **CM_ML_MODEL_FILE_WITH_PATH**
* **CM_ML_MODEL_PATH**
* **CM_STARTING_WEIGHTS_FILENAME**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,raw,ml-model,resnet50,ml-model-resnet50,image-classification"`

*or*

`cm run script "get raw ml-model resnet50 ml-model-resnet50 image-classification"`

*or*

`cm run script 56203e4e998b4bc0`

#### CM Python API

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

#### CM modular Docker container
*TBD*
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)