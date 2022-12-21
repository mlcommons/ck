*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Versions](#versions)
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

ML/AI datasets.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,dataset,squad,language-processing,validation,training,original

___
### Versions
Default version: *1.1*

* 1.1
* 2.0
___
### Default environment

___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad/_cm.json)***
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad/_cm.json)
___
### New environment export

* **CM_DATASET_***
___
### New environment detected from customize

* **CM_DATASET_PATH**
* **CM_DATASET_SQUAD_PATH**
* **CM_DATASET_SQUAD_TRAIN_PATH**
* **CM_DATASET_SQUAD_VAL_PATH**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,dataset,squad,language-processing,validation,training,original"`

*or*

`cm run script "get dataset squad language-processing validation training original"`

*or*

`cm run script 6651c119c3ae49b3`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,squad,language-processing,validation,training,original'
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