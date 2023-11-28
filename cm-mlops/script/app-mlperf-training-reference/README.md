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

#### Summary

* Category: *Modular MLPerf training benchmark pipeline.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-training-reference)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *app,vision,language,mlcommons,mlperf,training,reference,ref*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=app,vision,language,mlcommons,mlperf,training,reference,ref[,variations] [--input_flags]`

2. `cmr "app vision language mlcommons mlperf training reference ref[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,vision,language,mlcommons,mlperf,training,reference,ref'
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

```cmr "cm gui" --script="app,vision,language,mlcommons,mlperf,training,reference,ref"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=app,vision,language,mlcommons,mlperf,training,reference,ref) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "app vision language mlcommons mlperf training reference ref[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert`
      - Environment variables:
        - *CM_MLPERF_MODEL*: `bert`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_protobuf
             * `if (CM_MLPERF_BACKEND in ['tf', 'tflite'])`
             * CM names: `--adr.['protobuf']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torch
             * CM names: `--adr.['ml-engine-pytorch']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cuda`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cuda`
        - *USE_CUDA*: `True`
      - Workflow:
    * `_tpu`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `tpu`
        - *CUDA_VISIBLE_DEVICES*: ``
        - *USE_CUDA*: `False`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_pytorch`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `pytorch`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TORCH_VERSION>>>`
      - Workflow:
    * `_tf`
      - Aliases: `_tensorflow`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tf`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TENSORFLOW_VERSION>>>`
      - Workflow:

    </details>


#### Default variations

`_cuda`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_SUBMISSION_DIR=value`
* `--docker=value`  &rarr;  `CM_RUN_DOCKER_CONTAINER=value`
* `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
* `--model=value`  &rarr;  `CM_MLPERF_CUSTOM_MODEL_PATH=value`
* `--num_threads=value`  &rarr;  `CM_NUM_THREADS=value`
* `--output_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "clean":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `reference`
* CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX: ``

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-training-reference/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlperf,training,src
       * CM names: `--adr.['training-src']...`
       - CM script: [get-mlperf-training-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src)
     * get,cuda
       * `if (CM_MLPERF_DEVICE  == cuda)`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,generic-python-lib,_torchvision_cuda
       * `if (CM_MLPERF_BACKEND  == pytorch AND CM_MLPERF_DEVICE  == cuda)`
       * CM names: `--adr.['ml-engine-torchvision']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_mlperf_logging
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * prepare,mlperf,training,data,bert,_reference
       * `if (CM_MLPERF_MODEL  == bert)`
       * CM names: `--adr.['prepare-data', 'bert-model']...`
       - CM script: [prepare-training-data-bert](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-bert)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-training-reference/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-training-reference/_cm.yaml)
  1. ***Run native script if exists***
     * [run-bert-training.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-training-reference/run-bert-training.sh)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-training-reference/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-training-reference/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-training-reference/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-training-reference/_cm.yaml)
</details>

___
### Script output
`cmr "app vision language mlcommons mlperf training reference ref[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_DATASET_*`
* `CM_HW_NAME`
* `CM_MLPERF_*`
* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)