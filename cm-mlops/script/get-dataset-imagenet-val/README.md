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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,val,validation,dataset,imagenet,ILSVRC,image-classification,original

___
### Variations
#### All variations
* 2012-1
  - *ENV CM_DATASET_SIZE*: `1`
  - *ENV CM_DATASET_VER*: `2012`
* **2012-500** (default)
  - *ENV CM_DATASET_SIZE*: `500`
  - *ENV CM_DATASET_VER*: `2012`
* 2012-full
  - *ENV CM_DATASET_SIZE*: `50000`
  - *ENV CM_DATASET_VER*: `2012`
  - *ENV CM_IMAGENET_FULL*: `yes`
* full
  - *ENV CM_DATASET_SIZE*: `50000`
  - *ENV CM_DATASET_VER*: `2012`
  - *ENV CM_IMAGENET_FULL*: `yes`
* size.#
  - *ENV CM_DATASET_SIZE*: `#`
___
### Default environment

___
### CM script workflow

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)
___
### New environment export

* **CM_DATASET_***
___
### New environment detected from customize

* **CM_DATASET_IMAGENET_PATH**
* **CM_DATASET_PATH**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,val,validation,dataset,imagenet,ILSVRC,image-classification,original"`

*or*

`cm run script "get val validation dataset imagenet ILSVRC image-classification original"`

*or*

`cm run script 7afd58d287fe4f11`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,val,validation,dataset,imagenet,ILSVRC,image-classification,original'
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