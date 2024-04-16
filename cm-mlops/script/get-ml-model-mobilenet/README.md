**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-mobilenet).**



Automatically generated README for this automation recipe: **get-ml-model-mobilenet**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-mobilenet,ce46675a3ab249e4) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-mobilenet)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ml-model,mobilenet,raw,ml-model-mobilenet,image-classification*
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

````cmr "get ml-model mobilenet raw ml-model-mobilenet image-classification" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ml-model,mobilenet,raw,ml-model-mobilenet,image-classification`

`cm run script --tags=get,ml-model,mobilenet,raw,ml-model-mobilenet,image-classification[,variations] `

*or*

`cmr "get ml-model mobilenet raw ml-model-mobilenet image-classification"`

`cmr "get ml-model mobilenet raw ml-model-mobilenet image-classification [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="get,ml-model,mobilenet,raw,ml-model-mobilenet,image-classification"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,mobilenet,raw,ml-model-mobilenet,image-classification) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model mobilenet raw ml-model-mobilenet image-classification[variations]" `

___
### Customization


#### Variations

  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_quantized_`
      - Environment variables:
        - *CM_ML_MODEL_MOBILENET_NAME_SUFFIX*: `_quant`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `yes`
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
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_PRECISION*: `fp32`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_MOBILENET_PRECISION*: `float`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `int8`
        - *CM_ML_MODEL_PRECISION*: `int8`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int8`
        - *CM_ML_MODEL_MOBILENET_PRECISION*: `int8`
      - Workflow:
    * `_uint8`
      - Environment variables:
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `uint8`
        - *CM_ML_MODEL_PRECISION*: `uint8`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `uint8`
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

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_ML_MODEL: `mobilenet`
* CM_ML_MODEL_DATASET: `imagenet2012-val`
* CM_ML_MODEL_RETRAINING: `no`
* CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `no`
* CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
* CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
* CM_ML_MODEL_MOBILENET_NAME_SUFFIX: ``

</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-mobilenet/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-mobilenet/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-mobilenet/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-mobilenet/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-mobilenet/_cm.json)

___
### Script output
`cmr "get ml-model mobilenet raw ml-model-mobilenet image-classification [,variations]"  -j`
#### New environment keys (filter)

* `CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS`
* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`
* `CM_ML_MODEL_PATH`
* `CM_ML_MODEL_STARTING_WEIGHTS_FILENAME`