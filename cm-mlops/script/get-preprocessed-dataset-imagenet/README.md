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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,dataset,imagenet,ILSVRC,image-classification,preprocessed

___
### Variations
#### All variations
* 1
  - *ENV CM_DATASET_SIZE*: `1`
* 500
  - *ENV CM_DATASET_SIZE*: `500`
* NCHW
  - *ENV CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
* NHWC
  - *ENV CM_ML_MODEL_DATA_LAYOUT*: `NHWC`
* for.mobilenet
  - *ENV CM_IMAGENET_QUANTIZED*: `no`
  - *ENV CM_MODEL*: `mobilenet`
* for.mobilenet-quantized
  - *ENV CM_IMAGENET_QUANTIZED*: `yes`
* for.resnet50
  - *ENV CM_IMAGENET_QUANTIZED*: `no`
  - *ENV CM_MODEL*: `resnet50`
* for.resnet50-quantized
  - *ENV CM_IMAGENET_QUANTIZED*: `yes`
  - *ENV CM_MODEL*: `resnet50`
  - *ENV CM_NEW_EXTENSION*: `rgb8`
  - *ENV CM_NORMALIZE_DATA*: `0`
  - *ENV CM_SUBTRACT_MEAN*: `YES`
  - *ENV CM_GIVEN_CHANNEL_MEANS*: `123.68 116.78 103.94`
  - *ENV CM_INTERPOLATION_METHOD*: `INTER_AREA`
  - *ENV CM_QUANT_SCALE*: `1.18944883`
  - *ENV CM_QUANT_OFFSET*: `0`
  - *ENV CM_QUANTIZE*: `1`
  - *ENV CM_CONVERT_TO_UNSIGNED*: `1`
* full
  - *ENV CM_DATASET_SIZE*: `50000`
___
### Default environment

* CM_IMAGENET_QUANTIZED: **no**
* CM_INPUT_SQUARE_SIDE: **224**
* CM_CROP_FACTOR: **87.5**
* CM_ML_MODEL_DATA_TYPE: **float32**
* CM_QUANT_SCALE: **1**
* CM_QUANT_OFFSET: **0**
* CM_CONVERT_TO_UNSIGNED: **0**
___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/_cm.json)***
     * get,python3
       * `if (CM_IMAGENET_PREPROCESSED_PATH  != on)`
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,dataset,image-classification,original
       * `if (CM_IMAGENET_PREPROCESSED_PATH  != on)`
       * CM names: `--adr.['original-dataset']...`
       - CM script: [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)
     * get,dataset-aux,image-classification,imagenet-aux
       * `if (CM_IMAGENET_PREPROCESSED_PATH  != on)`
       - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
     * mlperf,mlcommons,inference,source,src
       * `if (CM_IMAGENET_QUANTIZED  == no) AND (CM_IMAGENET_PREPROCESSED_PATH  != on)`
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,generic-python-lib,_opencv-python
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_pillow
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/_cm.json)
___
### New environment export

* **CM_DATASET_***
___
### New environment detected from customize

* **CM_DATASET_PREPROCESSED_IMAGES_LIST**
* **CM_DATASET_PREPROCESSED_PATH**
* **CM_QUANTIZE**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,dataset,imagenet,ILSVRC,image-classification,preprocessed"`

*or*

`cm run script "get dataset imagenet ILSVRC image-classification preprocessed"`

*or*

`cm run script f259d490bbaf45f5`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,imagenet,ILSVRC,image-classification,preprocessed'
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

#### Script input flags mapped to environment

* dir --> **CM_DATASET_PREPROCESSED_PATH**
* threads --> **CM_NUM_PREPROCESS_THREADS**
* imagenet_path --> **CM_IMAGENET_PATH**
* imagenet_preprocessed_path --> **CM_IMAGENET_PREPROCESSED_PATH**

Examples:

```bash
cm run script "get dataset imagenet ILSVRC image-classification preprocessed" --dir=...
```
```python
r=cm.access({... , "dir":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)