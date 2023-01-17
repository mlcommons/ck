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
  * [ Variations](#variations)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *ML/AI models.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,ml-model,mobilenet,ml-model-mobilenet,image-classification*
* Output cached?: *True*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=get,ml-model,mobilenet,ml-model-mobilenet,image-classification(,variations from below) (flags from below)`

*or*

`cm run script "get ml-model mobilenet ml-model-mobilenet image-classification (variations from below)" (flags from below)`

*or*

`cm run script ce46675a3ab249e4`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

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

</details>

#### CM modular Docker container
*TBD*
___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_onnx`** (default)
      - Environment variables:
        - *CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
        - *CM_ML_MODEL_FRAMEWORK*: `onnx`
      - Workflow:
    * `_onnx,fp32`
      - Environment variables:
        - *CM_ML_MODEL_NORMALIZE_DATA*: `yes`
        - *CM_ML_MODEL_SUBTRACT_MEAN*: `no`
        - *CM_ML_MODEL_VER*: `1_1.0_224`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `input:0`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `MobilenetV1/Predictions/Reshape_1:0`
      - Workflow:
    * `_onnx,int8`
      - Environment variables:
        - *CM_ML_MODEL_NORMALIZE_DATA*: `no`
        - *CM_ML_MODEL_SUBTRACT_MEAN*: `yes`
        - *CM_ML_MODEL_GIVEN_CHANNEL_MEANS*: `128.0 128.0 128.0`
        - *CM_ML_MODEL_VER*: `1_1.0_224_quant`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `0`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `169`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3353417/files/Quantized%20MobileNet.zip`
        - *CM_ML_MODEL_FILE*: `mobilenet_sym_no_bn.onnx`
        - *CM_UNZIP*: `yes`
      - Workflow:
    * `_onnx,opset-11,fp32`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/4735651/files/mobilenet_v1_1.0_224.onnx`
      - Workflow:
    * `_onnx,opset-8,fp32`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3157894/files/mobilenet_v1_1.0_224.onnx`
      - Workflow:
    * `_tf`
      - Environment variables:
        - *CM_ML_MODEL_DATA_LAYOUT*: `NHWC`
        - *CM_ML_MODEL_NORMALIZE_DATA*: `yes`
        - *CM_ML_MODEL_SUBTRACT_MEAN*: `no`
        - *CM_ML_MODEL_VER*: `1_1.0_224_2018_08_02`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `input`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `MobilenetV1/Predictions/Reshape_1`
        - *CM_ML_MODEL_WEIGHTS_FILE*: `mobilenet_v1_1.0_224.ckpt`
      - Workflow:
    * `_tf,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `71.676`
        - *CM_ML_MODEL_FILE*: `mobilenet_v1_1.0_224.tflite`
        - *CM_UNTAR*: `yes`
      - Workflow:
    * `_tf,fp32,from.google`
      - Environment variables:
        - *CM_PACKAGE_URL*: `http://download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224.tgz`
      - Workflow:
    * `_tf,fp32,from.zenodo`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/2269307/files/mobilenet_v1_1.0_224.tgz`
      - Workflow:
    * `_tf,int8`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `70.762`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/2269307/files/mobilenet_v1_1.0_224_quant.tgz`
      - Workflow:
    * `_tflite`
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

    * `_fp32`
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

    </details>


  * Group "**source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_from.google`
      - Environment variables:
        - *CM_DOWNLOAD_SOURCE*: `google`
      - Workflow:
    * `_from.zenodo`
      - Environment variables:
        - *CM_DOWNLOAD_SOURCE*: `zenodo`
      - Workflow:

    </details>


#### Default variations

`_onnx`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet/_cm.json)
___
### Script output
#### New environment keys (filter)

* **CM_ML_MODEL_***
#### New environment keys auto-detected from customize

* **CM_ML_MODEL_FILE**
* **CM_ML_MODEL_FILE_WITH_PATH**
* **CM_ML_MODEL_PATH**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)