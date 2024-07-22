**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-bert-base-squad).**



Automatically generated README for this automation recipe: **get-ml-model-bert-base-squad**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-bert-base-squad,b3b10b452ce24c5f) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-base-squad)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ml-model,raw,bert,bert-base,bert-squad,language,language-processing*
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

````cmr "get ml-model raw bert bert-base bert-squad language language-processing" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ml-model,raw,bert,bert-base,bert-squad,language,language-processing`

`cm run script --tags=get,ml-model,raw,bert,bert-base,bert-squad,language,language-processing[,variations] `

*or*

`cmr "get ml-model raw bert bert-base bert-squad language language-processing"`

`cmr "get ml-model raw bert bert-base bert-squad language language-processing [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,raw,bert,bert-base,bert-squad,language,language-processing'
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

```cmr "cm gui" --script="get,ml-model,raw,bert,bert-base,bert-squad,language,language-processing"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,raw,bert,bert-base,bert-squad,language,language-processing) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model raw bert bert-base bert-squad language language-processing[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse,int8`
      - Environment variables:
        - *CM_ML_MODEL_F1*: `87.89`
        - *CM_ML_MODEL_FILE*: `model.onnx`
        - *CM_PRUNING_PERCENTAGE*: `95`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,zoo,deepsparse,_pruned95_obs_quant-none
             * CM names: `--adr.['neural-magic-zoo-downloader']...`
             - *Warning: no scripts found*

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse`
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `deepsparse`
        - *CM_ML_MODEL_INPUT_IDS_NAME*: `input_ids`
        - *CM_ML_MODEL_INPUT_MASK_NAME*: `input_mask`
        - *CM_ML_MODEL_INPUT_SEGMENTS_NAME*: `segment_ids`
        - *CM_ML_MODEL_OUTPUT_END_LOGITS_NAME*: `output_end_logits`
        - *CM_ML_MODEL_OUTPUT_START_LOGITS_NAME*: `output_start_logits`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_ML_MODEL_PRECISION*: `fp32`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_ML_MODEL_PRECISION*: `int8`
        - *CM_ML_MODEL_QUANTIZED*: `yes`
      - Workflow:

    </details>


#### Default variations

`_fp32`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-base-squad/_cm.json)
  1. Run "preprocess" function from customize.py
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-base-squad/_cm.json)***
     * download-and-extract
       * `if (CM_TMP_ML_MODEL_REQUIRE_DOWNLOAD in yes)`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-base-squad/_cm.json)
  1. Run "postrocess" function from customize.py
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-base-squad/_cm.json)***
     * get,bert,squad,vocab
       - CM script: [get-bert-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-bert-squad-vocab)

___
### Script output
`cmr "get ml-model raw bert bert-base bert-squad language language-processing [,variations]"  -j`
#### New environment keys (filter)

* `CM_ML_MODEL*`
#### New environment keys auto-detected from customize
