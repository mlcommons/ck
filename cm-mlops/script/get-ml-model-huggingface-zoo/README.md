**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-huggingface-zoo).**



Automatically generated README for this automation recipe: **get-ml-model-huggingface-zoo**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-huggingface-zoo,53cf8252a443446a) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-huggingface-zoo)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ml-model,huggingface,zoo*
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

````cmr "get ml-model huggingface zoo" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ml-model,huggingface,zoo`

`cm run script --tags=get,ml-model,huggingface,zoo[,variations] [--input_flags]`

*or*

`cmr "get ml-model huggingface zoo"`

`cmr "get ml-model huggingface zoo [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,huggingface,zoo'
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

```cmr "cm gui" --script="get,ml-model,huggingface,zoo"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,huggingface,zoo) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model huggingface zoo[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_model-stub.#`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `#`
      - Workflow:
    * `_onnx-subfolder`
      - Environment variables:
        - *CM_HF_SUBFOLDER*: `onnx`
      - Workflow:
    * `_pierreguillou_bert_base_cased_squad_v1.1_portuguese`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `pierreguillou/bert-base-cased-squad-v1.1-portuguese`
      - Workflow:
    * `_prune`
      - Environment variables:
        - *CM_MODEL_TASK*: `prune`
      - Workflow:

    </details>


  * Group "**download-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_clone-repo`
      - Environment variables:
        - *CM_GIT_CLONE_REPO*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,git,repo,_lfs
             - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--env_key=value`  &rarr;  `CM_MODEL_ZOO_ENV_KEY=value`
* `--full_subfolder=value`  &rarr;  `CM_HF_FULL_SUBFOLDER=value`
* `--model_filename=value`  &rarr;  `CM_MODEL_ZOO_FILENAME=value`
* `--revision=value`  &rarr;  `CM_HF_REVISION=value`
* `--subfolder=value`  &rarr;  `CM_HF_SUBFOLDER=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "download_path":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-huggingface-zoo/_cm.json)***
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_huggingface_hub
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-huggingface-zoo/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-huggingface-zoo/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-huggingface-zoo/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-huggingface-zoo/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-huggingface-zoo/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-huggingface-zoo/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-huggingface-zoo/_cm.json)

___
### Script output
`cmr "get ml-model huggingface zoo [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_ML_MODEL*`
* `CM_MODEL_ZOO_STUB`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_'+env_key+'_FILE_WITH_PATH`
* `CM_ML_MODEL_'+env_key+'_PATH`
* `CM_ML_MODEL_PATH`