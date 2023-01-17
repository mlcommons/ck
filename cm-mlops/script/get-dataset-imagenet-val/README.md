<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
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

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *ML/AI datasets.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,val,validation,dataset,imagenet,ILSVRC,image-classification,original*
* Output cached?: *True*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=get,val,validation,dataset,imagenet,ILSVRC,image-classification,original(,variations from below) (flags from below)`

*or*

`cm run script "get val validation dataset imagenet ILSVRC image-classification original (variations from below)" (flags from below)`

*or*

`cm run script 7afd58d287fe4f11`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,val,validation,dataset,imagenet,ILSVRC,image-classification,original'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>

#### CM modular Docker container
*TBD*
___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_2012-1`
      - Environment variables:
        - *CM_DATASET_SIZE*: `1`
        - *CM_DATASET_VER*: `2012`
      - Workflow:
    * **`_2012-500`** (default)
      - Environment variables:
        - *CM_DATASET_SIZE*: `500`
        - *CM_DATASET_VER*: `2012`
      - Workflow:
    * `_2012-full`
      - Environment variables:
        - *CM_DATASET_SIZE*: `50000`
        - *CM_DATASET_VER*: `2012`
        - *CM_IMAGENET_FULL*: `yes`
      - Workflow:
    * `_full`
      - Environment variables:
        - *CM_DATASET_SIZE*: `50000`
        - *CM_DATASET_VER*: `2012`
        - *CM_IMAGENET_FULL*: `yes`
      - Workflow:
    * `_size.#`
      - Environment variables:
        - *CM_DATASET_SIZE*: `#`
      - Workflow:

    </details>


#### Default variations

`_2012-500`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)
___
### Script output
#### New environment keys (filter)

* **CM_DATASET_IMAGENET_PATH**
* **CM_DATASET_PATH**
* **CM_DATASET_SIZE**
* **CM_DATASET_VER**
#### New environment keys auto-detected from customize

* **CM_DATASET_IMAGENET_PATH**
* **CM_DATASET_PATH**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)