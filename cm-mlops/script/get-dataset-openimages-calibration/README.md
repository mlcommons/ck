**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-openimages-calibration).**



Automatically generated README for this automation recipe: **get-dataset-openimages-calibration**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-dataset-openimages-calibration,27228976bb084dd0) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages-calibration)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *get,dataset,openimages,calibration*
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

````cmr "get dataset openimages calibration" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,dataset,openimages,calibration`

`cm run script --tags=get,dataset,openimages,calibration[,variations] `

*or*

`cmr "get dataset openimages calibration"`

`cmr "get dataset openimages calibration [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,openimages,calibration'
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

```cmr "cm gui" --script="get,dataset,openimages,calibration"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,openimages,calibration) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset openimages calibration[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_filter`
      - Environment variables:
        - *CM_CALIBRATE_FILTER*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,python3
             * CM names: `--adr.['python', 'python3']...`
             - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
           * get,openimages,dataset,original,_calibration
             - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)

    </details>


  * Group "**calibration-option**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_mlperf.option1`** (default)
      - Environment variables:
        - *CM_MLPERF_OPENIMAGES_CALIBRATION_OPTION*: `one`
        - *CM_DOWNLOAD_CHECKSUM1*: `f09719174af3553119e2c621157773a6`
      - Workflow:

    </details>


  * Group "**filter-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_filter-size.#`
      - Environment variables:
        - *CM_CALIBRATION_FILTER_SIZE*: `#`
      - Workflow:
    * `_filter-size.400`
      - Environment variables:
        - *CM_CALIBRATION_FILTER_SIZE*: `400`
      - Workflow:

    </details>


#### Default variations

`_mlperf.option1`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages-calibration/_cm.yaml)***
     * download,file
       * CM names: `--adr.['calibration-file-downloader']...`
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages-calibration/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages-calibration/_cm.yaml)
  1. ***Run native script if exists***
     * [run-filter.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages-calibration/run-filter.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages-calibration/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages-calibration/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages-calibration/_cm.yaml)

___
### Script output
`cmr "get dataset openimages calibration [,variations]"  -j`
#### New environment keys (filter)

* `CM_MLPERF_OPENIMAGES_CALIBRATION_LIST_FILE_WITH_PATH`
#### New environment keys auto-detected from customize

* `CM_MLPERF_OPENIMAGES_CALIBRATION_LIST_FILE_WITH_PATH`