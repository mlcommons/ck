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
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-stable-diffusion)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,raw,ml-model,stable-diffusion,sdxl,text-to-image*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,raw,ml-model,stable-diffusion,sdxl,text-to-image[,variations] [--input_flags]`

2. `cmr "get raw ml-model stable-diffusion sdxl text-to-image[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,raw,ml-model,stable-diffusion,sdxl,text-to-image'
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

```cmr "cm gui" --script="get,raw,ml-model,stable-diffusion,sdxl,text-to-image"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,raw,ml-model,stable-diffusion,sdxl,text-to-image) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get raw ml-model stable-diffusion sdxl text-to-image[ variations]" [--input_flags]`

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
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0`
      - Workflow:
    * `_rclone,fp16`
      - Environment variables:
        - *CM_DOWNLOAD_URL*: `mlc-inference:mlcommons-inference-wg-public/stable_diffusion_fp16`
      - Workflow:
    * `_rclone,fp32`
      - Environment variables:
        - *CM_DOWNLOAD_URL*: `mlc-inference:mlcommons-inference-wg-public/stable_diffusion_fp32`
      - Workflow:

    </details>


  * Group "**download-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_huggingface`
      - Workflow:
    * **`_mlcommons`** (default)
      - Workflow:

    </details>


  * Group "**download-tool**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_git`
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `git`
      - Workflow:
    * `_rclone`
      - Environment variables:
        - *CM_RCLONE_CONFIG_CMD*: `rclone config create mlc-inference s3 provider=Cloudflare access_key_id=f65ba5eef400db161ea49967de89f47b secret_access_key=fbea333914c292b854f14d3fe232bad6c5407bf0ab1bebf78833c2b359bdfd2b endpoint=https://c2686074cb2caf5cbaf6d134bdba8b47.r2.cloudflarestorage.com`
        - *CM_DOWNLOAD_TOOL*: `rclone`
      - Workflow:
    * `_wget`
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `wget`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_pytorch`** (default)
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `pytorch`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_fp16`
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `fp16`
        - *CM_ML_MODEL_PRECISION*: `fp16`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp16`
      - Workflow:
    * **`_fp32`** (default)
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
        - *CM_ML_MODEL_PRECISION*: `fp32`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
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

`_fp32,_mlcommons,_pytorch`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--checkpoint=value`  &rarr;  `SDXL_CHECKPOINT_PATH=value`
* `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--to=value`  &rarr;  `CM_DOWNLOAD_PATH=value`

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

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-stable-diffusion/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-stable-diffusion/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-stable-diffusion/_cm.json)***
     * get,ml-model,huggingface,zoo,_clone-repo,_model-stub.stabilityai/stable-diffusion-xl-base-1.0
       * `if (CM_TMP_REQUIRE_DOWNLOAD  == yes AND CM_DOWNLOAD_TOOL  == git)`
       * CM names: `--adr.['hf-zoo']...`
       - CM script: [get-ml-model-huggingface-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-huggingface-zoo)
     * download-and-extract
       * `if (CM_TMP_REQUIRE_DOWNLOAD  == yes AND CM_DOWNLOAD_TOOL  == rclone)`
       * CM names: `--adr.['dae']...`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-stable-diffusion/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-stable-diffusion/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-stable-diffusion/_cm.json)
</details>

___
### Script output
`cmr "get raw ml-model stable-diffusion sdxl text-to-image[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
* `SDXL_CHECKPOINT_PATH`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)