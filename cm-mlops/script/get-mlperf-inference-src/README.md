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
  * [ Default environment](#default-environment)
* [Versions](#versions)
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

* Category: *MLPerf benchmark support.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,src,source,inference,inference-src,inference-source,mlperf,mlcommons*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,src,source,inference,inference-src,inference-source,mlperf,mlcommons[,variations] `

2. `cmr "get src source inference inference-src inference-source mlperf mlcommons[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,src,source,inference,inference-src,inference-source,mlperf,mlcommons'
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

```cmr "cm gui" --script="get,src,source,inference,inference-src,inference-source,mlperf,mlcommons"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,src,source,inference,inference-src,inference-source,mlperf,mlcommons) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get src source inference inference-src inference-source mlperf mlcommons[ variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_3d-unet`
      - Environment variables:
        - *CM_SUBMODULE_3D_UNET*: `yes`
      - Workflow:
    * `_deeplearningexamples`
      - Environment variables:
        - *CM_SUBMODULE_DEEPLEARNINGEXAMPLES*: `yes`
      - Workflow:
    * `_deepsparse`
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/neuralmagic/inference`
        - *CM_GIT_CHECKOUT*: `deepsparse`
        - *CM_MLPERF_LAST_RELEASE*: `v3.0`
      - Workflow:
    * `_gn`
      - Environment variables:
        - *CM_SUBMODULE_GN*: `yes`
      - Workflow:
    * `_no-recurse-submodules`
      - Environment variables:
        - *CM_GIT_RECURSE_SUBMODULES*: ``
      - Workflow:
    * `_nvidia-pycocotools`
      - Environment variables:
        - *CM_GIT_PATCH_FILENAME*: `coco.patch`
      - Workflow:
    * `_octoml`
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/octoml/inference`
      - Workflow:
    * `_openimages-nvidia-pycocotools`
      - Environment variables:
        - *CM_GIT_PATCH_FILENAME*: `openimages-pycocotools.patch`
      - Workflow:
    * `_patch`
      - Environment variables:
        - *CM_GIT_PATCH*: `yes`
      - Workflow:
    * `_pybind`
      - Environment variables:
        - *CM_SUBMODULE_PYBIND*: `yes`
      - Workflow:
    * `_recurse-submodules`
      - Environment variables:
        - *CM_GIT_RECURSE_SUBMODULES*: ` --recurse-submodules`
      - Workflow:
    * `_repo.#`
      - Environment variables:
        - *CM_GIT_URL*: `#`
      - Workflow:
    * `_submodules.#`
      - Environment variables:
        - *CM_GIT_SUBMODULES*: `#`
      - Workflow:

    </details>


  * Group "**checkout**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_branch.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT*: `#`
      - Workflow:
    * `_sha.#`
      - Environment variables:
        - *CM_GIT_SHA*: `#`
      - Workflow:

    </details>


  * Group "**git-history**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_full-history`
      - Environment variables:
        - *CM_GIT_DEPTH*: ``
      - Workflow:
    * **`_short-history`** (default)
      - Environment variables:
        - *CM_GIT_DEPTH*: `--depth 10`
      - Workflow:

    </details>


#### Default variations

`_short-history`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_DEPTH: `--depth 4`
* CM_GIT_PATCH: `no`
* CM_GIT_URL: `https://github.com/mlcommons/inference.git`
* CM_GIT_RECURSE_SUBMODULES: ``
* CM_GIT_CHECKOUT_FOLDER: `inference`

</details>

#### Versions
Default version: `master`

* `custom`
* `deepsparse`
* `master`
* `pybind_fix`
* `r2.1`
* `r3.0`
* `r3.1`
* `tvm`
___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)***
     * get,git,repo
       * CM names: `--adr.['inference-git-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)
</details>

___
### Script output
`cmr "get src source inference inference-src inference-source mlperf mlcommons[,variations]"  -j`
#### New environment keys (filter)

* `+PYTHONPATH`
* `CM_MLPERF_INFERENCE_3DUNET_PATH`
* `CM_MLPERF_INFERENCE_BERT_PATH`
* `CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH`
* `CM_MLPERF_INFERENCE_CONF_PATH`
* `CM_MLPERF_INFERENCE_DLRM_PATH`
* `CM_MLPERF_INFERENCE_DLRM_V2_PATH`
* `CM_MLPERF_INFERENCE_GPTJ_PATH`
* `CM_MLPERF_INFERENCE_RNNT_PATH`
* `CM_MLPERF_INFERENCE_SOURCE`
* `CM_MLPERF_INFERENCE_VERSION`
* `CM_MLPERF_INFERENCE_VISION_PATH`
* `CM_MLPERF_LAST_RELEASE`
#### New environment keys auto-detected from customize

* `CM_MLPERF_INFERENCE_3DUNET_PATH`
* `CM_MLPERF_INFERENCE_BERT_PATH`
* `CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH`
* `CM_MLPERF_INFERENCE_CONF_PATH`
* `CM_MLPERF_INFERENCE_DLRM_PATH`
* `CM_MLPERF_INFERENCE_DLRM_V2_PATH`
* `CM_MLPERF_INFERENCE_GPTJ_PATH`
* `CM_MLPERF_INFERENCE_RNNT_PATH`
* `CM_MLPERF_INFERENCE_VISION_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)