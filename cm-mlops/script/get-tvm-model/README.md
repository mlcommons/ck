**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm-model).**



Automatically generated README for this automation recipe: **get-tvm-model**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-tvm-model,c1b7b656b6224307) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tvm-model)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ml-model-tvm,tvm-model*
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

````cmr "get ml-model-tvm tvm-model" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ml-model-tvm,tvm-model`

`cm run script --tags=get,ml-model-tvm,tvm-model[,variations] `

*or*

`cmr "get ml-model-tvm tvm-model"`

`cmr "get ml-model-tvm tvm-model [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model-tvm,tvm-model'
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

```cmr "cm gui" --script="get,ml-model-tvm,tvm-model"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model-tvm,tvm-model) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model-tvm tvm-model[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_tune-model`
      - Environment variables:
        - *CM_TUNE_TVM_MODEL*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_xgboost
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_pandas
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_tornado
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * Group "**batchsize**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_batch_size.#`
      - Environment variables:
        - *CM_ML_MODEL_MAX_BATCH_SIZE*: `#`
      - Workflow:

    </details>


  * Group "**frontend**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_onnx`** (default)
      - Environment variables:
        - *CM_TVM_FRONTEND_FRAMEWORK*: `onnx`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_onnx
             * CM names: `--adr.['onnx']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_pytorch`
      - Aliases: `_torch`
      - Environment variables:
        - *CM_TVM_FRONTEND_FRAMEWORK*: `pytorch`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torch
             * CM names: `--adr.['pytorch', 'torch']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torchvision
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_tensorflow`
      - Aliases: `_tf`
      - Environment variables:
        - *CM_TVM_FRONTEND_FRAMEWORK*: `tensorflow`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_tensorflow
             * CM names: `--adr.['tensorflow']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_tflite`
      - Environment variables:
        - *CM_TVM_FRONTEND_FRAMEWORK*: `tflite`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_tflite
             * CM names: `--adr.['tflite']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_model.#`
      - Environment variables:
        - *CM_ML_MODEL*: `#`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Workflow:
    * `_int8`
      - Workflow:
    * `_uint8`
      - Workflow:

    </details>


  * Group "**runtime**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_graph_executor`
      - Environment variables:
        - *CM_TVM_USE_VM*: `no`
      - Workflow:
    * **`_virtual_machine`** (default)
      - Environment variables:
        - *CM_TVM_USE_VM*: `yes`
      - Workflow:

    </details>


#### Default variations

`_fp32,_onnx,_virtual_machine`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_ML_MODEL_MAX_BATCH_SIZE: `1`
* CM_TUNE_TVM_MODEL: `no`
* CM_TVM_USE_VM: `yes`
* CM_TVM_FRONTEND_FRAMEWORK: `onnx`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tvm-model/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,tvm
       * CM names: `--adr.['tvm']...`
       - CM script: [get-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)
     * get,generic-python-lib,_decorator
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_psutil
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_scipy
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_attrs
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tvm-model/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tvm-model/_cm.json)***
     * get,ml-model,raw
       * CM names: `--adr.['original-model']...`
       - CM script: [get-ml-model-3d-unet-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-3d-unet-kits19)
       - CM script: [get-ml-model-bert-base-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-base-squad)
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
       - CM script: [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)
       - CM script: [get-ml-model-efficientnet-lite](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-efficientnet-lite)
       - CM script: [get-ml-model-gptj](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj)
       - CM script: [get-ml-model-huggingface-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-huggingface-zoo)
       - CM script: [get-ml-model-llama2](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-llama2)
       - CM script: [get-ml-model-mobilenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
       - CM script: [get-ml-model-rnnt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt)
       - CM script: [get-ml-model-stable-diffusion](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-stable-diffusion)
       - CM script: [get-ml-model-tiny-resnet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-tiny-resnet)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tvm-model/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tvm-model/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tvm-model/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tvm-model/_cm.json)

___
### Script output
`cmr "get ml-model-tvm tvm-model [,variations]"  -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
* `CM_TUNE_TVM_*`
* `CM_TVM_*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`
* `CM_ML_MODEL_FRAMEWORK`
* `CM_ML_MODEL_INPUT_SHAPES`
* `CM_ML_MODEL_ORIGINAL_FILE_WITH_PATH`
* `CM_ML_MODEL_PATH`
* `CM_TUNE_TVM_MODEL`
* `CM_TVM_FRONTEND_FRAMEWORK`