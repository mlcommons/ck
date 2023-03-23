<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM GUI](#cm-gui)
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
* CM "database" tags to find this script: *get,ml-model,mobilenet,raw,ml-model-mobilenet,image-classification*
* Output cached?: *True*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help

```cm run script --help```

#### CM CLI

`cm run script --tags=get,ml-model,mobilenet,raw,ml-model-mobilenet,image-classification(,variations from below) (flags from below)`

*or*

`cm run script "get ml-model mobilenet raw ml-model-mobilenet image-classification (variations from below)" (flags from below)`

*or*

`cm run script ce46675a3ab249e4`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,mobilenet,raw,ml-model-mobilenet,image-classification'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### CM GUI

```cm run script --tags=gui --script="get,ml-model,mobilenet,raw,ml-model-mobilenet,image-classification"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,mobilenet,raw,ml-model-mobilenet,image-classification) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_quantized_`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_NAME_SUFFIX*: `_quant`
      - Workflow:
    * `_tf,from.google,v2,quantized_`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://storage.googleapis.com/mobilenet_v2/checkpoints/<<<CM_ML_MODEL_MOBILENET_NAME_PREFIX>>>_v2_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE>>>.tgz`
        - *CM_ML_MODEL_WEIGHTS_FILE*: `<<<CM_ML_MODEL_MOBILENET_NAME_PREFIX>>>_v2_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE>>>.ckpt.data-00000-of-00001`
        - *CM_ML_MODEL_FILE*: `model.tflite`
        - *CM_EXTRACT_FOLDER*: `v2_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE>>>`
        - *CM_UNTAR*: `yes`
      - Workflow:

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_onnx,fp32,v1`
      - Environment variables:
        - *CM_ML_MODEL_NORMALIZE_DATA*: `yes`
        - *CM_ML_MODEL_SUBTRACT_MEANS*: `no`
        - *CM_ML_MODEL_VER*: `1_1.0_224`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `input:0`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `MobilenetV1/Predictions/Reshape_1:0`
      - Workflow:
    * `_onnx,int8,v1`
      - Environment variables:
        - *CM_ML_MODEL_NORMALIZE_DATA*: `no`
        - *CM_ML_MODEL_SUBTRACT_MEANS*: `yes`
        - *CM_ML_MODEL_GIVEN_CHANNEL_MEANS*: `128.0 128.0 128.0`
        - *CM_ML_MODEL_VER*: `1_1.0_224_quant`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `0`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `169`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3353417/files/Quantized%20MobileNet.zip`
        - *CM_ML_MODEL_FILE*: `mobilenet_sym_no_bn.onnx`
        - *CM_UNZIP*: `yes`
      - Workflow:
    * `_onnx,opset-11,fp32,v1`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/4735651/files/mobilenet_v1_1.0_224.onnx`
      - Workflow:
    * `_onnx,opset-8,fp32,v1`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3157894/files/mobilenet_v1_1.0_224.onnx`
      - Workflow:
    * `_tf,fp32,v1,resolution-224,multiplier-1.0`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `71.676`
      - Workflow:
    * `_tf,from.google,v1`
      - Environment variables:
        - *CM_PACKAGE_URL*: `http://download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>><<<CM_ML_MODEL_MOBILENET_NAME_SUFFIX>>>.tgz`
        - *CM_UNTAR*: `yes`
      - Workflow:
    * `_tf,from.google,v2,fp32`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://storage.googleapis.com/mobilenet_v2/checkpoints/mobilenet_v2_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>.tgz`
        - *CM_ML_MODEL_WEIGHTS_FILE*: `mobilenet_v2_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>.ckpt.data-00000-of-00001`
        - *CM_ML_MODEL_FILE*: `mobilenet_v2_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>.tflite`
        - *CM_UNTAR*: `yes`
      - Workflow:
    * `_tf,from.google,v3`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://storage.googleapis.com/mobilenet_v3/checkpoints/v3-<<<CM_ML_MODEL_MOBILENET_KIND>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_PRECISION>>>.tgz`
        - *CM_EXTRACT_FOLDER*: `v3-<<<CM_ML_MODEL_MOBILENET_KIND>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_PRECISION>>>`
        - *CM_ML_MODEL_FILE*: `v3-<<<CM_ML_MODEL_MOBILENET_KIND>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_PRECISION>>>.tflite`
        - *CM_UNTAR*: `yes`
      - Workflow:
    * `_tf,from.zenodo,v1`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/2269307/files/mobilenet_v1_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>><<<CM_ML_MODEL_MOBILENET_NAME_SUFFIX>>>.tgz`
        - *CM_UNTAR*: `yes`
      - Workflow:
    * `_tf,int8,v1,resolution-224,multiplier-1.0`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `70.762`
      - Workflow:
    * `_tf,v1`
      - Environment variables:
        - *CM_ML_MODEL_VER*: `1_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>><<<CM_ML_MODEL_MOBILENET_NAME_SUFFIX>>>_2018_08_02`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `MobilenetV1/Predictions/Reshape_1`
        - *CM_ML_MODEL_WEIGHTS_FILE*: `mobilenet_v1_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>><<<CM_ML_MODEL_MOBILENET_NAME_SUFFIX>>>.ckpt.data-00000-of-00001`
        - *CM_ML_MODEL_FILE*: `mobilenet_v1_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>><<<CM_ML_MODEL_MOBILENET_NAME_SUFFIX>>>.tflite`
      - Workflow:
    * `_tf,v1,fp32`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_NAME_PREFIX*: ``
      - Workflow:
    * `_tf,v1,int8`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_NAME_SUFFIX*: `_quant`
      - Workflow:
    * `_tf,v1,uint8`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_NAME_SUFFIX*: `_quant`
      - Workflow:
    * `_tf,v2,fp32`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_NAME_PREFIX*: ``
        - *CM_ML_MODEL_VER*: `2_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `MobilenetV2/Predictions/Reshape_1`
      - Workflow:
    * `_tf,v2,int8`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_NAME_PREFIX*: `quantized`
        - *CM_ML_MODEL_VER*: `2_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `MobilenetV2/Predictions/Softmax`
      - Workflow:
    * `_tf,v2,uint8`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_NAME_PREFIX*: `quantized`
        - *CM_ML_MODEL_VER*: `2_<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `MobilenetV2/Predictions/Softmax`
      - Workflow:
    * `_tf,v3`
      - Environment variables:
        - *CM_ML_MODEL_VER*: `3_<<<CM_ML_MODEL_MOBILENET_KIND>>>_<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `MobilenetV3/Predictions/Softmax`
      - Workflow:
    * `_tflite`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_onnx`
      - Environment variables:
        - *CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
        - *CM_ML_MODEL_FRAMEWORK*: `onnx`
      - Workflow:
    * **`_tf`** (default)
      - Environment variables:
        - *CM_ML_MODEL_DATA_LAYOUT*: `NHWC`
        - *CM_ML_MODEL_NORMALIZE_DATA*: `yes`
        - *CM_ML_MODEL_SUBTRACT_MEANS*: `no`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `input`
      - Workflow:

    </details>


  * Group "**kind**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_large`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_KIND*: `large`
      - Workflow:
    * `_large-minimalistic`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_KIND*: `large-minimalistic`
      - Workflow:
    * `_small`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_KIND*: `small`
      - Workflow:
    * `_small-minimalistic`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_KIND*: `small-minimalistic`
      - Workflow:

    </details>


  * Group "**multiplier**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_multiplier-0.25`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_MULTIPLIER*: `0.25`
        - *CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE*: `25`
      - Workflow:
    * `_multiplier-0.35`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_MULTIPLIER*: `0.35`
        - *CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE*: `35`
      - Workflow:
    * `_multiplier-0.5`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_MULTIPLIER*: `0.5`
        - *CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE*: `50`
      - Workflow:
    * `_multiplier-0.75`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_MULTIPLIER*: `0.75`
        - *CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE*: `75`
      - Workflow:
    * `_multiplier-1.0`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_MULTIPLIER*: `1.0`
        - *CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE*: `100`
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
        - *CM_ML_MODEL_MOBILENET_PRECISION*: `float`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `int8`
        - *CM_ML_MODEL_PRECISION*: `int8`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `int8`
        - *CM_ML_MODEL_MOBILENET_PRECISION*: `int8`
      - Workflow:
    * `_uint8`
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `uint8`
        - *CM_ML_MODEL_PRECISION*: `uint8`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `uint8`
        - *CM_ML_MODEL_MOBILENET_PRECISION*: `uint8`
      - Workflow:

    </details>


  * Group "**resolution**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_resolution-128`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_RESOLUTION*: `128`
        - *CM_ML_MODEL_IMAGE_HEIGHT*: `128`
        - *CM_ML_MODEL_IMAGE_WIDTH*: `128`
        - *CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS*: `_resolution.128`
      - Workflow:
    * `_resolution-160`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_RESOLUTION*: `160`
        - *CM_ML_MODEL_IMAGE_HEIGHT*: `160`
        - *CM_ML_MODEL_IMAGE_WIDTH*: `160`
        - *CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS*: `_resolution.160`
      - Workflow:
    * `_resolution-192`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_RESOLUTION*: `192`
        - *CM_ML_MODEL_IMAGE_HEIGHT*: `192`
        - *CM_ML_MODEL_IMAGE_WIDTH*: `192`
        - *CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS*: `_resolution.192`
      - Workflow:
    * `_resolution-224`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_RESOLUTION*: `224`
        - *CM_ML_MODEL_IMAGE_HEIGHT*: `224`
        - *CM_ML_MODEL_IMAGE_WIDTH*: `224`
        - *CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS*: `_resolution.224`
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


  * Group "**version**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_v1`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_VERSION*: `1`
        - *CM_ML_MODEL_FULL_NAME*: `mobilenet-v1-precision_<<<CM_ML_MODEL_MOBILENET_PRECISION>>>-<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>-<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>`
      - Workflow:
    * `_v2`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_VERSION*: `2`
        - *CM_ML_MODEL_VER*: `2`
        - *CM_ML_MODEL_FULL_NAME*: `mobilenet-v2-precision_<<<CM_ML_MODEL_MOBILENET_PRECISION>>>-<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>-<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>`
      - Workflow:
    * **`_v3`** (default)
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_VERSION*: `3`
        - *CM_ML_MODEL_VER*: `3`
        - *CM_ML_MODEL_FULL_NAME*: `mobilenet-v3-precision_<<<CM_ML_MODEL_MOBILENET_PRECISION>>>-<<<CM_ML_MODEL_MOBILENET_KIND>>>-<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>`
      - Workflow:

    </details>


#### Default variations

`_fp32,_tf,_v3`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_ML_MODEL: **mobilenet**
* CM_ML_MODEL_DATASET: **imagenet2012-val**
* CM_ML_MODEL_RETRAINING: **no**
* CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: **no**
* CM_ML_MODEL_MOBILENET_NAME_SUFFIX: ****

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

* **CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS**
* **CM_ML_MODEL_***
#### New environment keys auto-detected from customize

* **CM_ML_MODEL_FILE**
* **CM_ML_MODEL_FILE_WITH_PATH**
* **CM_ML_MODEL_PATH**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)