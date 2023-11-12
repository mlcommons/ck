<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM GUI](#cm-gui)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! Use `README-extra.md` to add more info.*

### Description

#### Information

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *get,dataset,preprocessed,tokenized,squad*
* Output cached?: *True*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=get,dataset,preprocessed,tokenized,squad[,variations] `

2. `cm run script "get dataset preprocessed tokenized squad[,variations]" `

3. `cm run script 7cd1d9b7e8af4788 `

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

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


#### CM GUI

```cm run script --tags=gui --script="get,dataset,preprocessed,tokenized,squad"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,preprocessed,tokenized,squad) to generate CM CMD.

#### CM modular Docker container

*TBD*

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
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad/_cm.yaml)
</details>

___
### Script output
#### New environment keys (filter)

* `CM_DATASET_SQUAD_TOKENIZED_*`
#### New environment keys auto-detected from customize

* `CM_DATASET_SQUAD_TOKENIZED_DOC_STRIDE`
* `CM_DATASET_SQUAD_TOKENIZED_INPUT_IDS`
* `CM_DATASET_SQUAD_TOKENIZED_INPUT_MASK`
* `CM_DATASET_SQUAD_TOKENIZED_MAX_QUERY_LENGTH`
* `CM_DATASET_SQUAD_TOKENIZED_MAX_SEQ_LENGTH`
* `CM_DATASET_SQUAD_TOKENIZED_ROOT`
* `CM_DATASET_SQUAD_TOKENIZED_SEGMENT_IDS`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)