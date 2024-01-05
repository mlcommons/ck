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
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
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

* Category: *AI/ML datasets.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,dataset,coco*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,dataset,coco[,variations] [--input_flags]`

2. `cmr "get dataset coco[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,coco'
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

```cmr "cm gui" --script="get,dataset,coco"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,coco) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset coco[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * Group "**size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_complete`** (default)
      - Environment variables:
        - *CM_DATASET_COCO_SIZE*: `complete`
      - Workflow:
    * `_small`
      - Environment variables:
        - *CM_DATASET_COCO_SIZE*: `small`
      - Workflow:

    </details>


  * Group "**type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_train`
      - Environment variables:
        - *CM_DATASET_COCO_TYPE*: `train`
      - Workflow:
    * **`_val`** (default)
      - Environment variables:
        - *CM_DATASET_COCO_TYPE*: `val`
      - Workflow:

    </details>


  * Group "**version**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_2017`** (default)
      - Environment variables:
        - *CM_DATASET_COCO_VERSION*: `2017`
      - Workflow:

    </details>


#### Default variations

`_2017,_complete,_val`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--from=value`  &rarr;  `CM_FROM=value`
* `--store=value`  &rarr;  `CM_STORE=value`
* `--to=value`  &rarr;  `CM_TO=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "from":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco/_cm.json)***
     * download-and-extract,file,_wget,_extract
       * `if (CM_DATASET_COCO_DETECTED  != yes)`
       * CM names: `--adr.['get-dataset-coco-data', '746e5dad5e784ad6']...`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
     * download-and-extract,file,_wget,_extract
       * `if (CM_DATASET_COCO_DETECTED  != yes)`
       * CM names: `--adr.['get-dataset-coco-annotations', 'edb6cd092ff64171']...`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco/_cm.json)
</details>

___
### Script output
`cmr "get dataset coco[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_DATASET_COCO*`
* `CM_DATASET_PATH`
* `CM_DATASET_PATH_ROOT`
#### New environment keys auto-detected from customize

* `CM_DATASET_COCO_ANNOTATIONS_PATH`
* `CM_DATASET_COCO_DATA_PATH`
* `CM_DATASET_COCO_DETECTED`
* `CM_DATASET_COCO_MD5SUM_ANN`
* `CM_DATASET_COCO_MD5SUM_DATA`
* `CM_DATASET_COCO_PATH`
* `CM_DATASET_COCO_TYPE`
* `CM_DATASET_COCO_TYPE_AND_VERSION`
* `CM_DATASET_COCO_URL_ANNOTATIONS_FULL`
* `CM_DATASET_COCO_URL_DATA_FULL`
* `CM_DATASET_COCO_VERSION`
* `CM_DATASET_PATH`
* `CM_DATASET_PATH_ROOT`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)