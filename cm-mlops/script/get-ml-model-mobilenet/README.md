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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,ml-model,mobilenet,ml-model-mobilenet,image-classification

___
### Variations
#### All variations
* fp32
  - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
  - *ENV CM_ML_MODEL_PRECISION*: `fp32`
  - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
* from.google
  - *ENV CM_DOWNLOAD_SOURCE*: `google`
* from.zenodo
  - *ENV CM_DOWNLOAD_SOURCE*: `zenodo`
* int8
  - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `int8`
  - *ENV CM_ML_MODEL_PRECISION*: `int8`
  - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `int8`
* **onnx** (default)
  - *ENV CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
  - *ENV CM_ML_MODEL_FRAMEWORK*: `onnx`
* onnx,fp32
  - *ENV CM_ML_MODEL_NORMALIZE_DATA*: `yes`
  - *ENV CM_ML_MODEL_SUBTRACT_MEAN*: `no`
  - *ENV CM_ML_MODEL_VER*: `1_1.0_224`
  - *ENV CM_ML_MODEL_INPUT_LAYER_NAME*: `input:0`
  - *ENV CM_ML_MODEL_OUTPUT_LAYER_NAME*: `MobilenetV1/Predictions/Reshape_1:0`
* onnx,int8
  - *ENV CM_ML_MODEL_NORMALIZE_DATA*: `no`
  - *ENV CM_ML_MODEL_SUBTRACT_MEAN*: `yes`
  - *ENV CM_ML_MODEL_GIVEN_CHANNEL_MEANS*: `128.0 128.0 128.0`
  - *ENV CM_ML_MODEL_VER*: `1_1.0_224_quant`
  - *ENV CM_ML_MODEL_INPUT_LAYER_NAME*: `0`
  - *ENV CM_ML_MODEL_OUTPUT_LAYER_NAME*: `169`
  - *ENV CM_PACKAGE_URL*: `https://zenodo.org/record/3353417/files/Quantized%20MobileNet.zip`
  - *ENV CM_ML_MODEL_FILE*: `mobilenet_sym_no_bn.onnx`
  - *ENV CM_UNZIP*: `yes`
* onnx,opset-11,fp32
  - *ENV CM_PACKAGE_URL*: `https://zenodo.org/record/4735651/files/mobilenet_v1_1.0_224.onnx`
* onnx,opset-8,fp32
  - *ENV CM_PACKAGE_URL*: `https://zenodo.org/record/3157894/files/mobilenet_v1_1.0_224.onnx`
* opset-11
  - *ENV CM_ML_MODEL_ONNX_OPSET*: `11`
* opset-8
  - *ENV CM_ML_MODEL_ONNX_OPSET*: `8`
* tf
  - *ENV CM_ML_MODEL_DATA_LAYOUT*: `NHWC`
  - *ENV CM_ML_MODEL_NORMALIZE_DATA*: `yes`
  - *ENV CM_ML_MODEL_SUBTRACT_MEAN*: `no`
  - *ENV CM_ML_MODEL_VER*: `1_1.0_224_2018_08_02`
  - *ENV CM_ML_MODEL_INPUT_LAYER_NAME*: `input`
  - *ENV CM_ML_MODEL_OUTPUT_LAYER_NAME*: `MobilenetV1/Predictions/Reshape_1`
  - *ENV CM_ML_MODEL_WEIGHTS_FILE*: `mobilenet_v1_1.0_224.ckpt`
* tf,fp32
  - *ENV CM_ML_MODEL_ACCURACY*: `71.676`
  - *ENV CM_ML_MODEL_FILE*: `mobilenet_v1_1.0_224.tflite`
  - *ENV CM_UNTAR*: `yes`
* tf,fp32,from.google
  - *ENV CM_PACKAGE_URL*: `http://download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224.tgz`
* tf,fp32,from.zenodo
  - *ENV CM_PACKAGE_URL*: `https://zenodo.org/record/2269307/files/mobilenet_v1_1.0_224.tgz`
* tf,int8
  - *ENV CM_ML_MODEL_ACCURACY*: `70.762`
  - *ENV CM_PACKAGE_URL*: `https://zenodo.org/record/2269307/files/mobilenet_v1_1.0_224_quant.tgz`
* tflite

#### Variations by groups

  * opset-version
    * opset-11
      - *ENV CM_ML_MODEL_ONNX_OPSET*: `11`
    * opset-8
      - *ENV CM_ML_MODEL_ONNX_OPSET*: `8`

  * precision
    * fp32
      - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
      - *ENV CM_ML_MODEL_PRECISION*: `fp32`
      - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
    * int8
      - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `int8`
      - *ENV CM_ML_MODEL_PRECISION*: `int8`
      - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `int8`

  * source
    * from.google
      - *ENV CM_DOWNLOAD_SOURCE*: `google`
    * from.zenodo
      - *ENV CM_DOWNLOAD_SOURCE*: `zenodo`
___
### Default environment

___
### CM script workflow

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet/_cm.json)
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
`cm run script --tags="get,ml-model,mobilenet,ml-model-mobilenet,image-classification"`

*or*

`cm run script "get ml-model mobilenet ml-model-mobilenet image-classification"`

*or*

`cm run script ce46675a3ab249e4`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,mobilenet,ml-model-mobilenet,image-classification'
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