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

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm-model)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,ml-model-tvm,tvm-model*
* Output cached?: *True*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=get,ml-model-tvm,tvm-model[,variations] `

2. `cm run script "get ml-model-tvm tvm-model[,variations]" `

3. `cm run script c1b7b656b6224307 `

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

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


#### CM GUI

```cm run script --tags=gui --script="get,ml-model-tvm,tvm-model"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model-tvm,tvm-model) to generate CM CMD.

#### CM modular Docker container

*TBD*

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
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm-model/_cm.json)***
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
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm-model/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm-model/_cm.json)***
     * get,ml-model,raw
       * CM names: `--adr.['original-model']...`
       - CM script: [get-ml-model-3d-unet-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-3d-unet-kits19)
       - CM script: [get-ml-model-bert-base-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-base-squad)
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
       - CM script: [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)
       - CM script: [get-ml-model-efficientnet-lite](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-efficientnet-lite)
       - CM script: [get-ml-model-gptj](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj)
       - CM script: [get-ml-model-mobilenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
       - CM script: [get-ml-model-rnnt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt)
       - CM script: [get-ml-model-tiny-resnet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-tiny-resnet)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm-model/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm-model/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm-model/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm-model/_cm.json)
</details>

___
### Script output
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
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)