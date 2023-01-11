*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,ml-model,dlrm,terabyte,criteo-terabyte,criteo,recommendation

___
### Variations
#### All variations
* debug
  - *ENV CM_ML_MODEL_DEBUG*: `yes`
* **fp32** (default)
  - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
  - *ENV CM_ML_MODEL_PRECISION*: `fp32`
  - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
* onnx
  - *ENV CM_ML_MODEL_FRAMEWORK*: `onnx`
* onnx,fp32
  - *ENV CM_ML_MODEL_ACCURACY*: `0.8025`
  - *ENV CM_PACKAGE_URL*: `https://dlrm.s3-us-west-1.amazonaws.com/models/tb00_40M.onnx.tar`
  - *ENV CM_UNTAR*: `yes`
  - *ENV CM_ML_MODEL_FILE*: `tb00_40M.onnx`
  - *ENV CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `40000000`
* onnx,fp32,debug
  - *ENV CM_ML_MODEL_ACCURACY*: `0.8107`
  - *ENV CM_PACKAGE_URL*: `https://dlrm.s3-us-west-1.amazonaws.com/models/tb0875_10M.onnx.tar`
  - *ENV CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `10000000`
  - *ENV CM_UNTAR*: `yes`
  - *ENV CM_ML_MODEL_FILE*: `tb0875_10M.onnx`
* **pytorch** (default)
  - *ENV CM_ML_MODEL_FRAMEWORK*: `pytorch`
  - *ENV CM_TMP_MODEL_ADDITIONAL_NAME*: `dlrm_terabyte.pytorch`
* pytorch,fp32
  - *ENV CM_ML_MODEL_ACCURACY*: `0.8025`
  - *ENV CM_PACKAGE_URL*: `https://dlrm.s3-us-west-1.amazonaws.com/models/tb00_40M.pt`
  - *ENV CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `40000000`
* pytorch,fp32,debug
  - *ENV CM_ML_MODEL_ACCURACY*: `0.8107`
  - *ENV CM_PACKAGE_URL*: `https://dlrm.s3-us-west-1.amazonaws.com/models/tb0875_10M.pt`
  - *ENV CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `10000000`

#### Variations by groups

  * framework
    * onnx
      - *ENV CM_ML_MODEL_FRAMEWORK*: `onnx`
    * **pytorch** (default)
      - *ENV CM_ML_MODEL_FRAMEWORK*: `pytorch`
      - *ENV CM_TMP_MODEL_ADDITIONAL_NAME*: `dlrm_terabyte.pytorch`

  * precision
    * **fp32** (default)
      - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
      - *ENV CM_ML_MODEL_PRECISION*: `fp32`
      - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
___
### Default environment

___
### CM script workflow

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte/_cm.json)
___
### New environment export

* **CM_ML_MODEL_***
___
### New environment detected from customize

* **CM_ML_MODEL_FILE**
* **CM_ML_MODEL_FILE_WITH_PATH**
* **CM_ML_MODEL_PATH**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,ml-model,dlrm,terabyte,criteo-terabyte,criteo,recommendation"`

*or*

`cm run script "get ml-model dlrm terabyte criteo-terabyte criteo recommendation"`

*or*

`cm run script 8fa7582c603a4db3`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,dlrm,terabyte,criteo-terabyte,criteo,recommendation'
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