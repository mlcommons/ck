**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-resnet50).**



Automatically generated README for this automation recipe: **get-ml-model-resnet50**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-resnet50,56203e4e998b4bc0) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-resnet50)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,raw,ml-model,resnet50,ml-model-resnet50,image-classification*
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

````cmr "get raw ml-model resnet50 ml-model-resnet50 image-classification" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,raw,ml-model,resnet50,ml-model-resnet50,image-classification`

`cm run script --tags=get,raw,ml-model,resnet50,ml-model-resnet50,image-classification[,variations] `

*or*

`cmr "get raw ml-model resnet50 ml-model-resnet50 image-classification"`

`cmr "get raw ml-model resnet50 ml-model-resnet50 image-classification [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="get,raw,ml-model,resnet50,ml-model-resnet50,image-classification"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,raw,ml-model,resnet50,ml-model-resnet50,image-classification) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get raw ml-model resnet50 ml-model-resnet50 image-classification[variations]" `

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
    * `_batch_size.1`
      - Environment variables:
        - *CM_ML_MODEL_BATCH_SIZE*: `1`
      - Workflow:
    * `_fix-input-shape`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,python3
             * CM names: `--adr.['python', 'python3']...`
             - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
    * `_from-tf`
      - Workflow:
    * `_huggingface_default`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://huggingface.co/ctuning/mlperf-inference-resnet50-onnx-fp32-imagenet2012-v1.0/resolve/main/resnet50_v1.onnx`
      - Workflow:
    * `_ncnn,fp32`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/8073420/files/resnet50_v1.bin?download=1`
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * download-and-extract,_url.https://zenodo.org/record/8073420/files/resnet50_v1.param?download=
             - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
    * `_onnx,from-tf`
      - Environment variables:
        - *CM_ML_MODEL_DATA_LAYOUT*: `NHWC`
        - *CM_ML_MODEL_FRAMEWORK*: `onnx`
        - *CM_ML_MODEL_INPUT_LAYERS*: `input_tensor`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `input_tensor`
        - *CM_ML_MODEL_INPUT_SHAPES*: `\"input_tensor\": (BATCH_SIZE, 224, 224, 3)`
        - *CM_ML_MODEL_OUTPUT_LAYERS*: `softmax_tensor`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `softmax_tensor`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/2535873/files/resnet50_v1.pb`
      - Workflow:
    * `_onnx,from-tf,fp32`
      - Environment variables:
        - *CM_DOWNLOAD_FILENAME*: `resnet50_v1_modified.onnx`
        - *CM_PACKAGE_URL*: `https://drive.google.com/uc?id=15wZ_8Vt12cb10IEBsln8wksD1zGwlbOM`
      - Workflow:
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
    * `_tensorflow,fix-input-shape`
      - Environment variables:
        - *CM_ML_MODEL_TF_FIX_INPUT_SHAPE*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_package.tensorflow
             * CM names: `--adr.['tensorflow']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_tflite,argmax`
      - Environment variables:
        - *CM_DAE_EXTRACT_DOWNLOADED*: `yes`
        - *CM_DOWNLOAD_FINAL_ENV_NAME*: ``
        - *CM_EXTRACT_FINAL_ENV_NAME*: `CM_ML_MODEL_FILE_WITH_PATH`
        - *CM_ML_MODEL_FILE*: `resnet50_v1.tflite`
        - *CM_ML_MODEL_INPUT_SHAPES*: `\"input_tensor 2\": (BATCH_SIZE, 224, 224, 3)`
        - *CM_PACKAGE_URL*: `https://www.dropbox.com/s/cvv2zlfo80h54uz/resnet50_v1.tflite.gz?dl=1`
      - Workflow:
    * `_tflite,int8,no-argmax`
      - Environment variables:
        - *CM_DOWNLOAD_FINAL_ENV_NAME*: `CM_ML_MODEL_FILE_WITH_PATH`
        - *CM_ML_MODEL_FILE*: `resnet50_quant_full_mlperf_edgetpu.tflite`
        - *CM_ML_MODEL_INPUT_SHAPES*: `\"input_tensor 2\": (BATCH_SIZE, 224, 224, 3)`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/8234946/files/resnet50_quant_full_mlperf_edgetpu.tflite?download=1`
      - Workflow:
    * `_tflite,no-argmax`
      - Environment variables:
        - *CM_ML_MODEL_FILE*: `resnet50_v1.no-argmax.tflite`
        - *CM_ML_MODEL_INPUT_SHAPES*: `\"input_tensor 2\": (BATCH_SIZE, 224, 224, 3)`
        - *CM_PACKAGE_URL*: `https://www.dropbox.com/s/vhuqo0wc39lky0a/resnet50_v1.no-argmax.tflite?dl=1`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_ncnn`
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `ncnn`
      - Workflow:
    * **`_onnx`** (default)
      - Aliases: `_onnxruntime`
      - Environment variables:
        - *CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
        - *CM_ML_MODEL_FRAMEWORK*: `onnx`
        - *CM_ML_MODEL_INPUT_LAYERS*: `input_tensor:0`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `input_tensor:0`
        - *CM_ML_MODEL_INPUT_SHAPES*: `\"input_tensor:0\": (BATCH_SIZE, 3, 224, 224)`
        - *CM_ML_MODEL_OUTPUT_LAYERS*: `softmax_tensor:0`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `softmax_tensor:0`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `<<<CM_PACKAGE_URL>>>`
        - *CM_ML_MODEL_VER*: `1.5`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
        - *CM_ML_MODEL_FRAMEWORK*: `pytorch`
        - *CM_ML_MODEL_GIVEN_CHANNEL_MEANS*: `?`
        - *CM_ML_MODEL_INPUT_LAYER_NAME*: `input_tensor:0`
        - *CM_ML_MODEL_INPUT_SHAPES*: `\"input_tensor:0\": [BATCH_SIZE, 3, 224, 224]`
        - *CM_ML_MODEL_OUTPUT_LAYERS*: `output`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `?`
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
        - *CM_ML_MODEL_INPUT_SHAPES*: `\"input_tensor:0\": (BATCH_SIZE, 3, 224, 224)`
        - *CM_ML_MODEL_NORMALIZE_DATA*: `0`
        - *CM_ML_MODEL_OUTPUT_LAYERS*: `softmax_tensor`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `softmax_tensor`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `<<<CM_PACKAGE_URL>>>`
        - *CM_ML_MODEL_SUBTRACT_MEANS*: `YES`
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
        - *CM_ML_MODEL_INPUT_SHAPES*: `\"input_tensor 2\": (BATCH_SIZE, 224, 224, 3)`
        - *CM_ML_MODEL_NORMALIZE_DATA*: `0`
        - *CM_ML_MODEL_OUTPUT_LAYERS*: `softmax_tensor`
        - *CM_ML_MODEL_OUTPUT_LAYER_NAME*: `softmax_tensor`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `<<<CM_PACKAGE_URL>>>`
        - *CM_ML_MODEL_SUBTRACT_MEANS*: `YES`
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


#### Default variations

`_argmax,_fp32,_onnx`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-resnet50/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-resnet50/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-resnet50/_cm.json)***
     * download-and-extract
       * CM names: `--adr.['model-downloader']...`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
     * [run-fix-input.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-resnet50/run-fix-input.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-resnet50/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-resnet50/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-resnet50/_cm.json)

___
### Script output
`cmr "get raw ml-model resnet50 ml-model-resnet50 image-classification [,variations]"  -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`
* `CM_ML_MODEL_STARTING_FILE_PATH`