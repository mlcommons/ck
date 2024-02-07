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

* Category: *AI/ML models.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,raw,ml-model,gptj,gpt-j,large-language-model*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,raw,ml-model,gptj,gpt-j,large-language-model[,variations] [--input_flags]`

2. `cmr "get raw ml-model gptj gpt-j large-language-model[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,raw,ml-model,gptj,gpt-j,large-language-model'
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

```cmr "cm gui" --script="get,raw,ml-model,gptj,gpt-j,large-language-model"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,raw,ml-model,gptj,gpt-j,large-language-model) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get raw ml-model gptj gpt-j large-language-model[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_batch_size.#`
      - Environment variables:
        - *CM_ML_MODEL_BATCH_SIZE*: `#`
      - Workflow:
    * `_pytorch,fp32`
      - Environment variables:
        - *CM_DOWNLOAD_EXTRA_OPTIONS*: ` --output-document checkpoint.zip`
        - *CM_UNZIP*: `yes`
        - *CM_DOWNLOAD_CHECKSUM_NOT_USED*: `e677e28aaf03da84584bb3073b7ee315`
        - *CM_PACKAGE_URL*: `https://cloud.mlcommons.org/index.php/s/QAZ2oM94MkFtbQx/download`
        - *CM_RCLONE_CONFIG_CMD*: `rclone config create mlc-inference s3 provider=Cloudflare access_key_id=f65ba5eef400db161ea49967de89f47b secret_access_key=fbea333914c292b854f14d3fe232bad6c5407bf0ab1bebf78833c2b359bdfd2b endpoint=https://c2686074cb2caf5cbaf6d134bdba8b47.r2.cloudflarestorage.com`
        - *CM_RCLONE_URL*: `mlc-inference:mlcommons-inference-wg-public/gpt-j`
      - Workflow:
    * `_pytorch,fp32,wget`
      - Workflow:
    * `_pytorch,int4,intel`
      - Workflow:
    * `_pytorch,int8,intel`
      - Workflow:
    * `_pytorch,intel`
      - Environment variables:
        - *CM_GPTJ_INTEL_MODEL*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,mlperf,inference,results
             - CM script: [get-mlperf-inference-results](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results)
             - CM script: [get-mlperf-inference-results-dir](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results-dir)
           * get,ml-model,gpt-j,_fp32,_pytorch
             - CM script: [get-ml-model-gptj](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj)
           * get,conda,_name.gptj-pt
             - CM script: [get-conda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-conda)
           * get,python,_conda.gptj-pt
             - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
           * get,generic,conda-package,_package.intel-openmp,_source.intel
             * CM names: `--adr.['conda-package', 'intel-openmp']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.jemalloc,_source.conda-forge
             * CM names: `--adr.['conda-package', 'jemalloc']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * install,ipex,from.src,_for-intel-mlperf-inference-v3.1-gptj
             - CM script: [install-ipex-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-ipex-from-src)
           * get,dataset,cnndm,_calibration
             - CM script: [get-dataset-cnndm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-cnndm)

    </details>


  * Group "**download-tool**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_rclone`
      - Environment variables:
        - *CM_DOWNLOAD_FILENAME*: `checkpoint`
        - *CM_DOWNLOAD_URL*: `<<<CM_RCLONE_URL>>>`
      - Workflow:
    * **`_wget`** (default)
      - Environment variables:
        - *CM_DOWNLOAD_URL*: `<<<CM_PACKAGE_URL>>>`
        - *CM_DOWNLOAD_FILENAME*: `checkpoint.zip`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_pytorch`** (default)
      - Environment variables:
        - *CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
        - *CM_ML_MODEL_FRAMEWORK*: `pytorch`
        - *CM_ML_STARTING_WEIGHTS_FILENAME*: `<<<CM_PACKAGE_URL>>>`
      - Workflow:

    </details>


  * Group "**model-provider**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_intel`
      - Workflow:
    * **`_mlcommons`** (default)
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_fp32`
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
        - *CM_ML_MODEL_PRECISION*: `fp32`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
      - Workflow:
    * `_int4`
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `int4`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `int4`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `int8`
        - *CM_ML_MODEL_PRECISION*: `int8`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `int8`
      - Workflow:
    * `_uint8`
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `uint8`
        - *CM_ML_MODEL_PRECISION*: `uint8`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `uint8`
      - Workflow:

    </details>


#### Default variations

`_mlcommons,_pytorch,_wget`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--checkpoint=value`  &rarr;  `GPTJ_CHECKPOINT_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "checkpoint":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj/_cm.json)***
     * download-and-extract
       * `if (CM_TMP_REQUIRE_DOWNLOAD  == yes)`
       * CM names: `--adr.['dae']...`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
     * [run-int4-calibration.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj/run-int4-calibration.sh)
     * [run-intel.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj/run-intel.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj/_cm.json)
</details>

___
### Script output
`cmr "get raw ml-model gptj gpt-j large-language-model[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
* `GPTJ_CHECKPOINT_PATH`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`
* `CM_ML_MODEL_WEIGHT_DATA_TYPES`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)