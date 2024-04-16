**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-coco).**



Automatically generated README for this automation recipe: **get-dataset-coco**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-dataset-coco,c198e1f60ac6445c) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,dataset,object-detection,coco*
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

````cmr "get dataset object-detection coco" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,dataset,object-detection,coco`

`cm run script --tags=get,dataset,object-detection,coco[,variations] [--input_flags]`

*or*

`cmr "get dataset object-detection coco"`

`cmr "get dataset object-detection coco [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,object-detection,coco'
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

```cmr "cm gui" --script="get,dataset,object-detection,coco"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,object-detection,coco) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset object-detection coco[variations]" [--input_flags]`

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
* `--home=value`  &rarr;  `CM_HOME_DIR=value`
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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco/_cm.json)***
     * download-and-extract,file,_wget,_extract
       * `if (CM_DATASET_COCO_DETECTED  != yes)`
       * CM names: `--adr.['get-dataset-coco-data', '746e5dad5e784ad6']...`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
     * download-and-extract,file,_wget,_extract
       * `if (CM_DATASET_COCO_DETECTED  != yes)`
       * CM names: `--adr.['get-dataset-coco-annotations', 'edb6cd092ff64171']...`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco/_cm.json)

___
### Script output
`cmr "get dataset object-detection coco [,variations]" [--input_flags] -j`
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