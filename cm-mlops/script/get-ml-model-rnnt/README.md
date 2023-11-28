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
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,ml-model,rnnt,raw,librispeech,speech-recognition*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,ml-model,rnnt,raw,librispeech,speech-recognition[,variations] `

2. `cmr "get ml-model rnnt raw librispeech speech-recognition[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,rnnt,raw,librispeech,speech-recognition'
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

```cmr "cm gui" --script="get,ml-model,rnnt,raw,librispeech,speech-recognition"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,rnnt,raw,librispeech,speech-recognition) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model rnnt raw librispeech speech-recognition[ variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_pytorch,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.07452253714852645`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3662521/files/DistributedDataParallel_1576581068.9962234-epoch-100.pt?download=1`
      - Workflow:
    * `_pytorch,fp32,amazon-s3`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://mlperf-public.s3.us-west-2.amazonaws.com/DistributedDataParallel_1576581068.9962234-epoch-100.pt`
      - Workflow:
    * `_pytorch,fp32,zenodo`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3662521/files/DistributedDataParallel_1576581068.9962234-epoch-100.pt?download=1`
      - Workflow:
    * `_weights`
      - Environment variables:
        - *CM_MODEL_WEIGHTS_FILE*: `yes`
      - Workflow:

    </details>


  * Group "**download-src**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_amazon-s3`** (default)
      - Workflow:
    * `_zenodo`
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

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
        - *CM_ML_MODEL_PRECISION*: `fp32`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
      - Workflow:

    </details>


#### Default variations

`_amazon-s3,_fp32,_pytorch`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt/_cm.json)
</details>

___
### Script output
`cmr "get ml-model rnnt raw librispeech speech-recognition[,variations]"  -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`
* `CM_ML_MODEL_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)