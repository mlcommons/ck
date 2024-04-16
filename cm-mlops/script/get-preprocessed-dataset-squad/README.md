**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-squad).**



Automatically generated README for this automation recipe: **get-preprocessed-dataset-squad**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-preprocessed-dataset-squad,7cd1d9b7e8af4788) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-squad)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *get,dataset,preprocessed,tokenized,squad*
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

````cmr "get dataset preprocessed tokenized squad" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,dataset,preprocessed,tokenized,squad`

`cm run script --tags=get,dataset,preprocessed,tokenized,squad[,variations] `

*or*

`cmr "get dataset preprocessed tokenized squad"`

`cmr "get dataset preprocessed tokenized squad [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

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

`cm docker script "get dataset preprocessed tokenized squad[variations]" `

___
### Customization


#### Variations

  * Group "**calibration-set**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calib1`
      - Environment variables:
        - *CM_DATASET_SQUAD_CALIBRATION_SET*: `one`
      - Workflow:
    * `_calib2`
      - Environment variables:
        - *CM_DATASET_SQUAD_CALIBRATION_SET*: `two`
      - Workflow:
    * **`_no-calib`** (default)
      - Environment variables:
        - *CM_DATASET_SQUAD_CALIBRATION_SET*: ``
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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-squad/_cm.yaml)***
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
     * get,generic-python-lib,_package.transformers
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.tensorflow
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-squad/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-squad/_cm.yaml)
  1. ***Run native script if exists***
     * [run-packed.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-squad/run-packed.sh)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-squad/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-squad/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-squad/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-squad/_cm.yaml)

___
### Script output
`cmr "get dataset preprocessed tokenized squad [,variations]"  -j`
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