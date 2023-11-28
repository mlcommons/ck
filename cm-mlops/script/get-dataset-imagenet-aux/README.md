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

* Category: *AI/ML datasets.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,aux,dataset-aux,image-classification,imagenet-aux*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,aux,dataset-aux,image-classification,imagenet-aux[,variations] `

2. `cmr "get aux dataset-aux image-classification imagenet-aux[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,aux,dataset-aux,image-classification,imagenet-aux'
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

```cmr "cm gui" --script="get,aux,dataset-aux,image-classification,imagenet-aux"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,aux,dataset-aux,image-classification,imagenet-aux) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get aux dataset-aux image-classification imagenet-aux[ variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_2012`
      - Environment variables:
        - *CM_DATASET_AUX_VER*: `2012`
      - Workflow:

    </details>


  * Group "**download-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_from.berkeleyvision`
      - Environment variables:
        - *CM_WGET_URL*: `http://dl.caffe.berkeleyvision.org/caffe_ilsvrc12.tar.gz`
      - Workflow:
    * **`_from.dropbox`** (default)
      - Environment variables:
        - *CM_WGET_URL*: `https://www.dropbox.com/s/92n2fyej3lzy3s3/caffe_ilsvrc12.tar.gz`
      - Workflow:

    </details>


#### Default variations

`_from.dropbox`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)
</details>

___
### Script output
`cmr "get aux dataset-aux image-classification imagenet-aux[,variations]"  -j`
#### New environment keys (filter)

* `CM_DATASET_AUX_*`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)