**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-gptj).**



Automatically generated README for this automation recipe: **get-ml-model-gptj**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-gptj,a41166210f294fbf) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,raw,ml-model,gptj,gpt-j,large-language-model*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "get raw ml-model gptj gpt-j large-language-model" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,raw,ml-model,gptj,gpt-j,large-language-model`

`cm run script --tags=get,raw,ml-model,gptj,gpt-j,large-language-model[,variations] [--input_flags]`

*or*

`cmr "get raw ml-model gptj gpt-j large-language-model"`

`cmr "get raw ml-model gptj gpt-j large-language-model [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

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

`cm docker script "get raw ml-model gptj gpt-j large-language-model[variations]" [--input_flags]`

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
    * `_saxml,fp32`
      - Environment variables:
        - *CM_TMP_MODEL_SAXML*: `fp32`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,gptj,_pytorch,_fp32
             - CM script: [get-ml-model-gptj](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj)
           * get,python3
             * CM names: `--adr.['python', 'python3']...`
             - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
           * get,generic-python-lib,_package.jax[cpu]
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.paxml
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.praxis
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.transformers
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.accelerate
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_saxml,int8`
      - Environment variables:
        - *CM_TMP_MODEL_SAXML*: `int8`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,gptj,_saxml,_fp32
             - CM script: [get-ml-model-gptj](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj)
           * get,python3
             * CM names: `--adr.['python', 'python3']...`
             - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
           * get,generic-python-lib,_package.praxis
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.apache-beam
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,git,repo,_repo.https://github.com/google/saxml
             * CM names: `--adr.['saxml']...`
             - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)

    </details>


  * Group "**download-tool**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_rclone`** (default)
      - Environment variables:
        - *CM_DOWNLOAD_FILENAME*: `checkpoint`
        - *CM_DOWNLOAD_URL*: `<<<CM_RCLONE_URL>>>`
      - Workflow:
    * `_wget`
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
    * `_saxml`
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

`_mlcommons,_pytorch,_rclone`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--checkpoint=value`  &rarr;  `GPTJ_CHECKPOINT_PATH=value`
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
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj/_cm.json)***
     * download-and-extract
       * `if (CM_TMP_REQUIRE_DOWNLOAD  == yes)`
       * CM names: `--adr.['dae']...`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
     * [run-int4-calibration.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj/run-int4-calibration.sh)
     * [run-intel.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj/run-intel.sh)
     * [run-saxml-quantized.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj/run-saxml-quantized.sh)
     * [run-saxml.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj/run-saxml.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj/_cm.json)

___
### Script output
`cmr "get raw ml-model gptj gpt-j large-language-model [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
* `GPTJ_CHECKPOINT_PATH`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`
* `CM_ML_MODEL_WEIGHT_DATA_TYPES`