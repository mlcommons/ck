<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *AI/ML datasets.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,dataset,imagenet,ILSVRC,image-classification,preprocessed*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,dataset,imagenet,ILSVRC,image-classification,preprocessed[,variations] [--input_flags]`

2. `cmr "get dataset imagenet ILSVRC image-classification preprocessed[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

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

</details>


#### Run this script via GUI

```cmr "cm gui" --script="get,dataset,imagenet,ILSVRC,image-classification,preprocessed"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,imagenet,ILSVRC,image-classification,preprocessed) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset imagenet ILSVRC image-classification preprocessed[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_mobilenet_`
      - Environment variables:
        - *CM_MODEL*: `mobilenet`
      - Workflow:
    * `_resnet50_`
      - Environment variables:
        - *CM_MODEL*: `resnet50`
      - Workflow:

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_500,validation`
      - Workflow:
    * **`_default`** (default)
      - Environment variables:
        - *CM_PREPROCESS_VGG*: `yes`
        - *CM_MODEL*: `resnet50`
      - Workflow:
    * `_for.mobilenet,float32`
      - Environment variables:
        - *CM_DATASET_QUANTIZE*: `0`
        - *CM_DATASET_GIVEN_CHANNEL_MEANS*: ``
        - *CM_DATASET_NORMALIZE_DATA*: `1`
        - *CM_DATASET_SUBTRACT_MEANS*: `0`
      - Workflow:
    * `_for.mobilenet,rgb8`
      - Environment variables:
        - *CM_DATASET_GIVEN_CHANNEL_MEANS*: ``
        - *CM_DATASET_SUBTRACT_MEANS*: `0`
        - *CM_DATASET_QUANTIZE*: `0`
        - *CM_DATASET_NORMALIZE_DATA*: `0`
        - *CM_DATASET_DATA_TYPE*: `uint8`
      - Workflow:
    * `_for.resnet50,float32`
      - Environment variables:
        - *CM_DATASET_GIVEN_CHANNEL_MEANS*: `123.68 116.78 103.94`
        - *CM_DATASET_SUBTRACT_MEANS*: `1`
        - *CM_DATASET_NORMALIZE_DATA*: `0`
      - Workflow:
    * `_for.resnet50,rgb8`
      - Environment variables:
        - *CM_DATASET_GIVEN_CHANNEL_MEANS*: ``
        - *CM_DATASET_SUBTRACT_MEANS*: `0`
        - *CM_DATASET_NORMALIZE_DATA*: `0`
        - *CM_DATASET_QUANTIZE*: `0`
        - *CM_DATASET_DATA_TYPE*: `uint8`
      - Workflow:
    * `_for.resnet50,uint8`
      - Environment variables:
        - *CM_DATASET_NORMALIZE_DATA*: `0`
        - *CM_DATASET_SUBTRACT_MEANS*: `1`
        - *CM_DATASET_GIVEN_CHANNEL_MEANS*: `123.68 116.78 103.94`
        - *CM_DATASET_INTERPOLATION_METHOD*: `INTER_AREA`
        - *CM_DATASET_QUANT_SCALE*: `1.18944883`
        - *CM_DATASET_QUANT_OFFSET*: `0`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_PREPROCESS_PYTORCH*: `yes`
        - *CM_MODEL*: `resnet50`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torchvision
             * CM names: `--adr.['torchvision']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_tflite_tpu`
      - Environment variables:
        - *CM_MODEL*: `resnet50`
        - *CM_PREPROCESS_TFLITE_TPU*: `yes`
      - Workflow:

    </details>


  * Group "**calibration-option**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_mlperf.option1`
      - Environment variables:
        - *CM_DATASET_CALIBRATION_OPTION*: `one`
      - Workflow:
    * `_mlperf.option2`
      - Environment variables:
        - *CM_DATASET_CALIBRATION_OPTION*: `two`
      - Workflow:

    </details>


  * Group "**dataset-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calibration`
      - Environment variables:
        - *CM_DATASET_TYPE*: `calibration`
      - Workflow:
    * **`_validation`** (default)
      - Environment variables:
        - *CM_DATASET_TYPE*: `validation`
      - Workflow:

    </details>


  * Group "**extension**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_rgb32`
      - Environment variables:
        - *CM_DATASET_PREPROCESSED_EXTENSION*: `rgb32`
      - Workflow:
    * `_rgb8`
      - Environment variables:
        - *CM_DATASET_PREPROCESSED_EXTENSION*: `rgb8`
      - Workflow:

    </details>


  * Group "**interpolation-method**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_inter.area`
      - Environment variables:
        - *CM_DATASET_INTERPOLATION_METHOD*: `INTER_AREA`
      - Workflow:
    * `_inter.linear`
      - Environment variables:
        - *CM_DATASET_INTERPOLATION_METHOD*: `INTER_LINEAR`
      - Workflow:

    </details>


  * Group "**layout**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_NCHW`** (default)
      - Environment variables:
        - *CM_DATASET_DATA_LAYOUT*: `NCHW`
      - Workflow:
    * `_NHWC`
      - Environment variables:
        - *CM_DATASET_DATA_LAYOUT*: `NHWC`
      - Workflow:

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_for.mobilenet`
      - Workflow:
    * `_for.resnet50`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_float32`
      - Environment variables:
        - *CM_DATASET_DATA_TYPE*: `float32`
        - *CM_DATASET_QUANTIZE*: `0`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_DATASET_DATA_TYPE*: `int8`
        - *CM_DATASET_QUANTIZE*: `1`
        - *CM_DATASET_CONVERT_TO_UNSIGNED*: `0`
      - Workflow:
    * `_uint8`
      - Environment variables:
        - *CM_DATASET_DATA_TYPE*: `uint8`
        - *CM_DATASET_QUANTIZE*: `1`
        - *CM_DATASET_CONVERT_TO_UNSIGNED*: `1`
      - Workflow:

    </details>


  * Group "**preprocessing-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_generic-preprocessor`
      - Environment variables:
        - *CM_DATASET_REFERENCE_PREPROCESSOR*: `0`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * get,generic,image-preprocessor
             - CM script: [get-preprocesser-script-generic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocesser-script-generic)
    * `_mlcommons-reference-preprocessor`
      - Environment variables:
        - *CM_DATASET_REFERENCE_PREPROCESSOR*: `1`
      - Workflow:

    </details>


  * Group "**resolution**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_resolution.#`
      - Environment variables:
        - *CM_DATASET_INPUT_SQUARE_SIDE*: `#`
      - Workflow:
    * **`_resolution.224`** (default)
      - Environment variables:
        - *CM_DATASET_INPUT_SQUARE_SIDE*: `224`
      - Workflow:

    </details>


  * Group "**size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_1`
      - Environment variables:
        - *CM_DATASET_SIZE*: `1`
      - Workflow:
    * `_500`
      - Environment variables:
        - *CM_DATASET_SIZE*: `500`
      - Workflow:
    * `_full`
      - Environment variables:
        - *CM_DATASET_SIZE*: `50000`
      - Workflow:
    * `_size.#`
      - Environment variables:
        - *CM_DATASET_SIZE*: `#`
      - Workflow:

    </details>


#### Default variations

`_NCHW,_default,_resolution.224,_validation`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_PATH=value`
* `--imagenet_path=value`  &rarr;  `CM_IMAGENET_PATH=value`
* `--imagenet_preprocessed_path=value`  &rarr;  `CM_IMAGENET_PREPROCESSED_PATH=value`
* `--threads=value`  &rarr;  `CM_NUM_PREPROCESS_THREADS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_DATASET_CROP_FACTOR: `87.5`
* CM_DATASET_DATA_TYPE: `float32`
* CM_DATASET_DATA_LAYOUT: `NCHW`
* CM_DATASET_QUANT_SCALE: `1`
* CM_DATASET_QUANTIZE: `0`
* CM_DATASET_QUANT_OFFSET: `0`
* CM_DATASET_PREPROCESSED_EXTENSION: `npy`
* CM_DATASET_CONVERT_TO_UNSIGNED: `0`
* CM_DATASET_REFERENCE_PREPROCESSOR: `1`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

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
       * `if (CM_DATASET_TYPE in validation) AND (CM_IMAGENET_PREPROCESSED_PATH  != on)`
       - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
     * get,dataset,imagenet,calibration
       * `if (CM_DATASET_TYPE in calibration) AND (CM_IMAGENET_PREPROCESSED_PATH  != on)`
       - *Warning: no scripts found*
     * get,generic-python-lib,_package.opencv-python-headless
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_pillow
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * mlperf,mlcommons,inference,source,src
       * `if (CM_DATASET_REFERENCE_PREPROCESSOR  == 1) AND (CM_IMAGENET_PREPROCESSED_PATH  != on)`
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/_cm.json)
</details>

___
### Script output
`cmr "get dataset imagenet ILSVRC image-classification preprocessed[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_DATASET_*`
#### New environment keys auto-detected from customize

* `CM_DATASET_IMAGES_LIST`
* `CM_DATASET_PREPROCESSED_IMAGES_LIST`
* `CM_DATASET_PREPROCESSED_PATH`
* `CM_DATASET_SIZE`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)