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

* Category: *AI/ML datasets.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *get,dataset,preprocessed,tokenized,squad*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,dataset,preprocessed,tokenized,squad[,variations] `

2. `cmr "get dataset preprocessed tokenized squad[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,preprocessed,tokenized,squad'
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

```cmr "cm gui" --script="get,dataset,preprocessed,tokenized,squad"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,preprocessed,tokenized,squad) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset preprocessed tokenized squad[ variations]" `

___
### Customization


#### Variations

  * Group "**calibration-set**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calib1`
      - Environment variables:
        - *CM_SQUAD_CALIBRATION_SET*: `one`
      - Workflow:
    * `_calib2`
      - Environment variables:
        - *CM_SQUAD_CALIBRATION_SET*: `two`
      - Workflow:
    * **`_no-calib`** (default)
      - Environment variables:
        - *CM_SQUAD_CALIBRATION_SET*: ``
      - Workflow:

    </details>


  * Group "**doc-stride**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_doc-stride.#`
      - Environment variables:
        - *CM_DATASET_DOC_STRIDE*: `#`
      - Workflow:
    * **`_doc-stride.128`** (default)
      - Environment variables:
        - *CM_DATASET_DOC_STRIDE*: `128`
      - Workflow:

    </details>


  * Group "**packing**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_packed`
      - Environment variables:
        - *CM_DATASET_SQUAD_PACKED*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,preprocessed,squad,_pickle
             - CM script: [get-preprocessed-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad)

    </details>


  * Group "**raw**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_pickle`
      - Environment variables:
        - *CM_DATASET_RAW*: `no`
      - Workflow:
    * **`_raw`** (default)
      - Environment variables:
        - *CM_DATASET_RAW*: `yes`
      - Workflow:

    </details>


  * Group "**seq-length**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_seq-length.#`
      - Environment variables:
        - *CM_DATASET_MAX_SEQ_LENGTH*: `#`
      - Workflow:
    * **`_seq-length.384`** (default)
      - Environment variables:
        - *CM_DATASET_MAX_SEQ_LENGTH*: `384`
      - Workflow:

    </details>


#### Default variations

`_doc-stride.128,_no-calib,_raw,_seq-length.384`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad/_cm.yaml)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlperf,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,squad,dataset,original
       * CM names: `--adr.['squad-dataset']...`
       - CM script: [get-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)
     * get,squad,vocab
       * CM names: `--adr.['squad-vocab']...`
       - CM script: [get-bert-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-bert-squad-vocab)
     * get,generic-python-lib,_package.tokenization
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad/_cm.yaml)
  1. ***Run native script if exists***
     * [run-packed.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad/run-packed.sh)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad/_cm.yaml)
</details>

___
### Script output
`cmr "get dataset preprocessed tokenized squad[,variations]"  -j`
#### New environment keys (filter)

* `CM_DATASET_SQUAD_TOKENIZED_*`
#### New environment keys auto-detected from customize

* `CM_DATASET_SQUAD_TOKENIZED_DOC_STRIDE`
* `CM_DATASET_SQUAD_TOKENIZED_INPUT_IDS`
* `CM_DATASET_SQUAD_TOKENIZED_INPUT_MASK`
* `CM_DATASET_SQUAD_TOKENIZED_MAX_QUERY_LENGTH`
* `CM_DATASET_SQUAD_TOKENIZED_MAX_SEQ_LENGTH`
* `CM_DATASET_SQUAD_TOKENIZED_PACKED_FILENAMES_FILE`
* `CM_DATASET_SQUAD_TOKENIZED_PICKLE_FILE`
* `CM_DATASET_SQUAD_TOKENIZED_ROOT`
* `CM_DATASET_SQUAD_TOKENIZED_SEGMENT_IDS`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)