**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-openimages).**



Automatically generated README for this automation recipe: **get-dataset-openimages**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-dataset-openimages,0a9d49b644cf4142) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,dataset,openimages,open-images,object-detection,original*
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

````cmr "get dataset openimages open-images object-detection original" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,dataset,openimages,open-images,object-detection,original`

`cm run script --tags=get,dataset,openimages,open-images,object-detection,original[,variations] `

*or*

`cmr "get dataset openimages open-images object-detection original"`

`cmr "get dataset openimages open-images object-detection original [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,openimages,open-images,object-detection,original'
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

```cmr "cm gui" --script="get,dataset,openimages,open-images,object-detection,original"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,openimages,open-images,object-detection,original) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset openimages open-images object-detection original[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_filter`
      - Workflow:
    * `_filter,calibration`
      - Workflow:
    * `_filter-size.#`
      - Workflow:
    * `_using-fiftyone`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_fiftyone
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,openssl,lib
             - CM script: [get-openssl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openssl)

    </details>


  * Group "**annotations**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_custom-annotations`
      - Environment variables:
        - *CM_DATASET_OPENIMAGES_CUSTOM_ANNOTATIONS*: `yes`
      - Workflow:
    * **`_default-annotations`** (default)
      - Environment variables:
        - *CM_DATASET_OPENIMAGES_CUSTOM_ANNOTATIONS*: `no`
      - Workflow:

    </details>


  * Group "**dataset-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calibration`
      - Environment variables:
        - *CM_DATASET_CALIBRATION*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,openimages,calibration
             * CM names: `--adr.['openimages-calibration']...`
             - CM script: [get-dataset-openimages-calibration](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-calibration)
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


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages/_cm.json)***
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_requests
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * mlperf,inference,source
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,generic-python-lib,_boto3
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_tqdm
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_numpy
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_opencv-python
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_pandas
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_pycocotools
       * CM names: `--adr.['pycocotools']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages/run.sh)
  1. ***Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages/_cm.json)***
     * get,openimages,annotations
       * `if (CM_DATASET_OPENIMAGES_CUSTOM_ANNOTATIONS  == yes)`
       - CM script: [get-dataset-openimages-annotations](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-annotations)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages/_cm.json)

___
### Script output
`cmr "get dataset openimages open-images object-detection original [,variations]"  -j`
#### New environment keys (filter)

* `CM_CALIBRATION_DATASET_PATH`
* `CM_DATASET_ANNOTATIONS_DIR_PATH`
* `CM_DATASET_ANNOTATIONS_FILE_PATH`
* `CM_DATASET_CALIBRATION_ANNOTATIONS_FILE_PATH`
* `CM_DATASET_PATH`
* `CM_DATASET_PATH_ROOT`
* `CM_DATASET_VALIDATION_ANNOTATIONS_FILE_PATH`
#### New environment keys auto-detected from customize

* `CM_CALIBRATION_DATASET_PATH`
* `CM_DATASET_ANNOTATIONS_DIR_PATH`
* `CM_DATASET_ANNOTATIONS_FILE_PATH`
* `CM_DATASET_CALIBRATION_ANNOTATIONS_FILE_PATH`
* `CM_DATASET_PATH`
* `CM_DATASET_PATH_ROOT`
* `CM_DATASET_VALIDATION_ANNOTATIONS_FILE_PATH`