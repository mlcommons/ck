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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,ml-model,ml-model-tvm,tvm-model,resnet50,ml-model-resnet50,image-classification

___
### Variations
#### All variations
* bs.1
  - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 1*
* bs.16
  - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 16*
* bs.2
  - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 2*
* bs.32
  - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 32*
* bs.4
  - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 4*
* bs.64
  - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 64*
* **bs.8** (default)
  - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 8*
* **fp32** (default)
* int8
* **onnx** (default)
* pytorch
* tensorflow
* tf
* tflite
* uint8

#### Variations by groups

  * batchsize
    * bs.1
      - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 1*
    * bs.16
      - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 16*
    * bs.2
      - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 2*
    * bs.32
      - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 32*
    * bs.4
      - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 4*
    * bs.64
      - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 64*
    * **bs.8** (default)
      - *ENV CM_ML_MODEL_MAX_BATCH_SIZE: 8*

  * framework
    * **onnx** (default)
    * pytorch
    * tensorflow

  * precision
    * **fp32** (default)
    * int8
    * uint8
___
### Default environment

___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm/_cm.json)***
     * get,python
       - CM script [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,tvm
       - CM script [get-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm/_cm.json)
___
### New environment export

* **CM_ML_MODEL_***
___
### New environment detected from customize

* **CM_ML_MODEL_FILE**
* **CM_ML_MODEL_FILE_WITH_PATH**
* **CM_ML_MODEL_FRAMEWORK**
* **CM_ML_MODEL_INPUT_SHAPES**
* **CM_ML_MODEL_ORIGINAL_FILE_WITH_PATH**
* **CM_ML_MODEL_PATH**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,ml-model,ml-model-tvm,tvm-model,resnet50,ml-model-resnet50,image-classification"`

*or*

`cm run script "get ml-model ml-model-tvm tvm-model resnet50 ml-model-resnet50 image-classification"`

*or*

`cm run script c1b7b656b6224307`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,ml-model-tvm,tvm-model,resnet50,ml-model-resnet50,image-classification'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)