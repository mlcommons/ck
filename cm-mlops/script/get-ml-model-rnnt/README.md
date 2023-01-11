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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,ml-model,rnnt,librispeech,speech-recognition

___
### Variations
#### All variations
* **fp32** (default)
  - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
  - *ENV CM_ML_MODEL_PRECISION*: `fp32`
  - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
* **pytorch** (default)
  - *ENV CM_ML_MODEL_FRAMEWORK*: `pytorch`
* pytorch,fp32
  - *ENV CM_ML_MODEL_ACCURACY*: `0.07452253714852645`
  - *ENV CM_PACKAGE_URL*: `https://zenodo.org/record/3662521/files/DistributedDataParallel_1576581068.9962234-epoch-100.pt?download=1`
* weights
  - *ENV CM_MODEL_WEIGHTS_FILE*: `yes`

#### Variations by groups

  * framework
    * **pytorch** (default)
      - *ENV CM_ML_MODEL_FRAMEWORK*: `pytorch`

  * precision
    * **fp32** (default)
      - *ENV CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
      - *ENV CM_ML_MODEL_PRECISION*: `fp32`
      - *ENV CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
___
### Default environment

___
### CM script workflow

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt/_cm.json)
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
`cm run script --tags="get,ml-model,rnnt,librispeech,speech-recognition"`

*or*

`cm run script "get ml-model rnnt librispeech speech-recognition"`

*or*

`cm run script 8858f18b89774d28`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,rnnt,librispeech,speech-recognition'
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