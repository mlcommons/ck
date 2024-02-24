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
* [Versions](#versions)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

#### Summary

* Category: *AI/ML frameworks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp[,variations] `

2. `cmr "install onnxruntime get prebuilt lib lang-c lang-cpp[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp'
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

```cmr "cm gui" --script="install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install onnxruntime get prebuilt lib lang-c lang-cpp[ variations]" `

___
### Customization


#### Variations

  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_ONNXRUNTIME_DEVICE*: ``
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_ONNXRUNTIME_DEVICE*: `gpu`
      - Workflow:

    </details>


#### Default variations

`_cpu`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `1.16.3`

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt/_cm.json)
</details>

___
### Script output
`cmr "install onnxruntime get prebuilt lib lang-c lang-cpp[,variations]"  -j`
#### New environment keys (filter)

* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+DYLD_FALLBACK_LIBRARY_PATH`
* `+LD_LIBRARY_PATH`
* `+PATH`
* `CM_ONNXRUNTIME_INCLUDE_PATH`
* `CM_ONNXRUNTIME_LIB_PATH`
#### New environment keys auto-detected from customize

* `CM_ONNXRUNTIME_INCLUDE_PATH`
* `CM_ONNXRUNTIME_LIB_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)