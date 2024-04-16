**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-calibration).**



Automatically generated README for this automation recipe: **get-dataset-imagenet-calibration**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-dataset-imagenet-calibration,30361fad3dff49ff) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-calibration)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *get,dataset,imagenet,calibration*
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

````cmr "get dataset imagenet calibration" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,dataset,imagenet,calibration`

`cm run script --tags=get,dataset,imagenet,calibration[,variations] `

*or*

`cmr "get dataset imagenet calibration"`

`cmr "get dataset imagenet calibration [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,imagenet,calibration'
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

```cmr "cm gui" --script="get,dataset,imagenet,calibration"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,imagenet,calibration) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset imagenet calibration[variations]" `

___
### Customization


#### Variations

  * Group "**calibration-option**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_mlperf.option1`** (default)
      - Environment variables:
        - *CM_MLPERF_IMAGENET_CALIBRATION_OPTION*: `one`
        - *CM_DOWNLOAD_CHECKSUM*: `f09719174af3553119e2c621157773a6`
      - Workflow:
    * `_mlperf.option2`
      - Environment variables:
        - *CM_MLPERF_IMAGENET_CALIBRATION_OPTION*: `two`
        - *CM_DOWNLOAD_CHECKSUM*: `e44582af00e3b4fc3fac30efd6bdd05f`
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


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-calibration/_cm.yaml)***
     * download,file
       * CM names: `--adr.['calibration-file-downloader']...`
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-calibration/_cm.yaml)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-calibration/_cm.yaml)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-calibration/_cm.yaml)

___
### Script output
`cmr "get dataset imagenet calibration [,variations]"  -j`
#### New environment keys (filter)

* `CM_MLPERF_IMAGENET_CALIBRATION_LIST_FILE_WITH_PATH`
#### New environment keys auto-detected from customize
