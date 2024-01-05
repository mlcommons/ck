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
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-calibration)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *get,dataset,openimages,calibration*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,dataset,openimages,calibration[,variations] `

2. `cmr "get dataset openimages calibration[ variations]" `

* `variations` can be seen [here](#variations)

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

`cm docker script "get dataset openimages calibration[ variations]" `

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
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-calibration/_cm.yaml)***
     * download,file
       * CM names: `--adr.['calibration-file-downloader']...`
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-calibration/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-calibration/_cm.yaml)
  1. ***Run native script if exists***
     * [run-filter.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-calibration/run-filter.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-calibration/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-calibration/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-calibration/_cm.yaml)
</details>

___
### Script output
`cmr "get dataset openimages calibration[,variations]"  -j`
#### New environment keys (filter)

* `CM_MLPERF_OPENIMAGES_CALIBRATION_LIST_FILE_WITH_PATH`
#### New environment keys auto-detected from customize

* `CM_MLPERF_OPENIMAGES_CALIBRATION_LIST_FILE_WITH_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)