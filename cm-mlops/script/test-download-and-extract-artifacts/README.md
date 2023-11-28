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

* Category: *Tests.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-download-and-extract-artifacts)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *test,download-and-extract-artifacts*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=test,download-and-extract-artifacts `

2. `cmr "test download-and-extract-artifacts" `

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'test,download-and-extract-artifacts'
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

```cmr "cm gui" --script="test,download-and-extract-artifacts"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=test,download-and-extract-artifacts) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "test download-and-extract-artifacts" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-download-and-extract-artifacts/_cm.yaml)***
     * download,file,_url.https://zenodo.org/record/4735647/files/resnet50_v1.onnx
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
     * download-and-extract,_extract,_url.https://zenodo.org/record/5597155/files/3dunet_kits19_128x128x128.tf.zip?download=1
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-download-and-extract-artifacts/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-download-and-extract-artifacts/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-download-and-extract-artifacts/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-download-and-extract-artifacts/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-download-and-extract-artifacts/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-download-and-extract-artifacts/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-download-and-extract-artifacts/_cm.yaml)
</details>

___
### Script output
`cmr "test download-and-extract-artifacts"  -j`
#### New environment keys (filter)

* `CM_REPRODUCE_PAPER_XYZ*`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)