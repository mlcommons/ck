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
  * [ Script input flags mapped to environment](#script-input-flags-mapped-to-environment)
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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,dataset,openimages,open-images,object-detection,preprocessed

___
### Variations
#### All variations
* 1
  - *ENV CM_DATASET_SIZE: 1*
* 5
  - *ENV CM_DATASET_SIZE: 5*
* **50** (default)
  - *ENV CM_DATASET_SIZE: 50*
* 500
  - *ENV CM_DATASET_SIZE: 500*
* **NCHW** (default)
  - *ENV CM_ML_MODEL_DATA_LAYOUT: NCHW*
* NHWC
  - *ENV CM_ML_MODEL_DATA_LAYOUT: NHWC*
* calibration
  - *ENV CM_DATASET_PATH: <<<CM_CALIBRATION_DATASET_PATH>>>*
* **fp32** (default)
  - *ENV CM_DATASET_DTYPE: fp32*
* full
  - *ENV CM_DATASET_SIZE: *
* int8
  - *ENV CM_DATASET_DTYPE: int8*
* nvidia
  - *ENV CM_PREPROCESSING_BY_NVIDIA: yes*
* **validation** (default)

#### Variations by groups

  * dataset-count
    * 1
      - *ENV CM_DATASET_SIZE: 1*
    * 5
      - *ENV CM_DATASET_SIZE: 5*
    * **50** (default)
      - *ENV CM_DATASET_SIZE: 50*
    * 500
      - *ENV CM_DATASET_SIZE: 500*
    * full
      - *ENV CM_DATASET_SIZE: *

  * dataset-layout
    * **NCHW** (default)
      - *ENV CM_ML_MODEL_DATA_LAYOUT: NCHW*
    * NHWC
      - *ENV CM_ML_MODEL_DATA_LAYOUT: NHWC*

  * dataset-precision
    * **fp32** (default)
      - *ENV CM_DATASET_DTYPE: fp32*
    * int8
      - *ENV CM_DATASET_DTYPE: int8*

  * dataset-type
    * calibration
      - *ENV CM_DATASET_PATH: <<<CM_CALIBRATION_DATASET_PATH>>>*
    * **validation** (default)
___
### Default environment

* CM_DATASET: **OPENIMAGES**
* CM_DATASET_DTYPE: **fp32**
___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)***
     * get,python3
       - CM script [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,dataset,object-detection,openimages,original
       - CM script [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
     * mlperf,mlcommons,inference,source,src
       - CM script [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,generic-python-lib,_pycocotools
       - CM script [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_opencv-python
       - CM script [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_pillow
       - CM script [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_numpy
       - CM script [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)
___
### New environment export

* **CM_DATASET_***
___
### New environment detected from customize

* **CM_DATASET_ANNOTATIONS_DIR_PATH**
* **CM_DATASET_ANNOTATIONS_FILE_PATH**
* **CM_DATASET_PREPROCESSED_PATH**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,dataset,openimages,open-images,object-detection,preprocessed"`

*or*

`cm run script "get dataset openimages open-images object-detection preprocessed"`

*or*

`cm run script 9842f1be8cba4c7b`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,openimages,open-images,object-detection,preprocessed'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* dir --> **CM_DATASET_PREPROCESSED_PATH**
* threads --> **CM_NUM_PREPROCESS_THREADS**

Examples:

```bash
cm run script "get dataset openimages open-images object-detection preprocessed" --dir=...
```
```python
r=cm.access({... , "dir":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)