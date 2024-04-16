**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-coco2014).**



Automatically generated README for this automation recipe: **get-dataset-coco2014**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-dataset-coco2014,3f7ad9d42f4040f8) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco2014)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *get,dataset,coco2014,object-detection,original*
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

````cmr "get dataset coco2014 object-detection original" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,dataset,coco2014,object-detection,original`

`cm run script --tags=get,dataset,coco2014,object-detection,original[,variations] `

*or*

`cmr "get dataset coco2014 object-detection original"`

`cmr "get dataset coco2014 object-detection original [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,coco2014,object-detection,original'
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

```cmr "cm gui" --script="get,dataset,coco2014,object-detection,original"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,coco2014,object-detection,original) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset coco2014 object-detection original[variations]" `

___
### Customization


#### Variations

  * Group "**annotations**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_custom-annotations`
      - Environment variables:
        - *CM_DATASET_COCO2014_CUSTOM_ANNOTATIONS*: `yes`
      - Workflow:
    * **`_default-annotations`** (default)
      - Environment variables:
        - *CM_DATASET_COCO2014_CUSTOM_ANNOTATIONS*: `no`
      - Workflow:

    </details>


  * Group "**dataset-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calibration`
      - Environment variables:
        - *CM_DATASET_CALIBRATION*: `yes`
      - Workflow:
    * **`_validation`** (default)
      - Environment variables:
        - *CM_DATASET_CALIBRATION*: `no`
      - Workflow:

    </details>


  * Group "**size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_50`** (default)
      - Environment variables:
        - *CM_DATASET_SIZE*: `50`
      - Workflow:
    * `_500`
      - Environment variables:
        - *CM_DATASET_SIZE*: `500`
      - Workflow:
    * `_full`
      - Environment variables:
        - *CM_DATASET_SIZE*: ``
      - Workflow:
    * `_size.#`
      - Environment variables:
        - *CM_DATASET_SIZE*: `#`
      - Workflow:

    </details>


#### Default variations

`_50,_default-annotations,_validation`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_DATASET_CALIBRATION: `no`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco2014/_cm.yaml)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_package.tqdm
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * mlperf,inference,source
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco2014/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco2014/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco2014/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco2014/run.sh)
  1. ***Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco2014/_cm.yaml)***
     * get,coco2014,annotations
       * `if (CM_DATASET_COCO2014_CUSTOM_ANNOTATIONS  == yes)`
       - *Warning: no scripts found*
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco2014/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco2014/_cm.yaml)

___
### Script output
`cmr "get dataset coco2014 object-detection original [,variations]"  -j`
#### New environment keys (filter)

* `CM_CALIBRATION_DATASET_PATH`
* `CM_DATASET_ANNOTATIONS_DIR_PATH`
* `CM_DATASET_ANNOTATIONS_FILE_PATH`
* `CM_DATASET_PATH`
* `CM_DATASET_PATH_ROOT`
#### New environment keys auto-detected from customize

* `CM_CALIBRATION_DATASET_PATH`
* `CM_DATASET_PATH`
* `CM_DATASET_PATH_ROOT`