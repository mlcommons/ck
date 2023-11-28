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
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,dataset,openimages,open-images,object-detection,preprocessed*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,dataset,openimages,open-images,object-detection,preprocessed[,variations] [--input_flags]`

2. `cmr "get dataset openimages open-images object-detection preprocessed[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,openimages,open-images,object-detection,preprocessed'
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

```cmr "cm gui" --script="get,dataset,openimages,open-images,object-detection,preprocessed"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,openimages,open-images,object-detection,preprocessed) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset openimages open-images object-detection preprocessed[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_nvidia`
      - Environment variables:
        - *CM_PREPROCESSING_BY_NVIDIA*: `yes`
      - Workflow:

    </details>


  * Group "**annotations**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_custom-annotations`
      - Workflow:
    * **`_default-annotations`** (default)
      - Workflow:

    </details>


  * Group "**dataset-count**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_50`** (default)
      - Environment variables:
        - *CM_DATASET_SIZE*: `50`
      - Workflow:
    * `_500`
      - Environment variables:
        - *CM_DATASET_SIZE*: `500`
      - Workflow:
    * `_full`
      - Environment variables:
        - *CM_DATASET_SIZE*: `0`
      - Workflow:
    * `_size.#`
      - Environment variables:
        - *CM_DATASET_SIZE*: `#`
      - Workflow:

    </details>


  * Group "**dataset-layout**"
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


  * Group "**dataset-precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_DATASET_DTYPE*: `fp32`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_DATASET_DTYPE*: `int8`
      - Workflow:

    </details>


  * Group "**dataset-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calibration`
      - Environment variables:
        - *CM_DATASET_PATH*: `<<<CM_CALIBRATION_DATASET_PATH>>>`
      - Workflow:
    * **`_validation`** (default)
      - Workflow:

    </details>


#### Default variations

`_50,_NCHW,_default-annotations,_fp32,_validation`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_PATH=value`
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

* CM_DATASET: `OPENIMAGES`
* CM_DATASET_DTYPE: `fp32`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)***
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,dataset,object-detection,openimages,original
       * CM names: `--adr.['original-dataset']...`
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
       - CM script: [get-dataset-coco](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco)
     * mlperf,mlcommons,inference,source,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,generic-python-lib,_pycocotools
       * CM names: `--adr.['pycocotools']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_opencv-python
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_pillow
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_numpy
       * CM names: `--adr.['numpy']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)
</details>

___
### Script output
`cmr "get dataset openimages open-images object-detection preprocessed[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_DATASET_*`
#### New environment keys auto-detected from customize

* `CM_DATASET_ANNOTATIONS_DIR_PATH`
* `CM_DATASET_ANNOTATIONS_FILE_PATH`
* `CM_DATASET_PREPROCESSED_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)