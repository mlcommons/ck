**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-llama2).**



Automatically generated README for this automation recipe: **get-ml-model-llama2**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-llama2,5db97be9f61244c6) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-llama2)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,raw,ml-model,language-processing,llama2,llama2-70b,text-summarization*
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

````cmr "get raw ml-model language-processing llama2 llama2-70b text-summarization" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,raw,ml-model,language-processing,llama2,llama2-70b,text-summarization`

`cm run script --tags=get,raw,ml-model,language-processing,llama2,llama2-70b,text-summarization[,variations] [--input_flags]`

*or*

`cmr "get raw ml-model language-processing llama2 llama2-70b text-summarization"`

`cmr "get raw ml-model language-processing llama2 llama2-70b text-summarization [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,raw,ml-model,language-processing,llama2,llama2-70b,text-summarization'
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

```cmr "cm gui" --script="get,raw,ml-model,language-processing,llama2,llama2-70b,text-summarization"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,raw,ml-model,language-processing,llama2,llama2-70b,text-summarization) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get raw ml-model language-processing llama2 llama2-70b text-summarization[variations]" [--input_flags]`

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


  * Group "**huggingface-stub**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_meta-llama/Llama-2-70b-chat-hf`** (default)
      - Environment variables:
        - *CM_GIT_CHECKOUT_FOLDER*: `Llama-2-70b-chat-hf`
        - *CM_MODEL_ZOO_ENV_KEY*: `LLAMA2`
      - Workflow:
    * `_meta-llama/Llama-2-7b-chat-hf`
      - Environment variables:
        - *CM_GIT_CHECKOUT_FOLDER*: `Llama-2-7b-chat-hf`
        - *CM_MODEL_ZOO_ENV_KEY*: `LLAMA2`
      - Workflow:
    * `_stub.#`
      - Environment variables:
        - *CM_MODEL_ZOO_ENV_KEY*: `LLAMA2`
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

`_fp32,_meta-llama/Llama-2-70b-chat-hf,_pytorch`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--checkpoint=value`  &rarr;  `LLAMA2_CHECKPOINT_PATH=value`

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


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-llama2/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-llama2/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-llama2/_cm.json)***
     * get,ml-model,huggingface,zoo,_clone-repo
       * `if (CM_TMP_REQUIRE_DOWNLOAD  == yes)`
       * CM names: `--adr.['hf-zoo']...`
       - CM script: [get-ml-model-huggingface-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-huggingface-zoo)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-llama2/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-llama2/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-llama2/_cm.json)

___
### Script output
`cmr "get raw ml-model language-processing llama2 llama2-70b text-summarization [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
* `LLAMA2_CHECKPOINT_PATH`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_PATH`