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
* [Versions](#versions)
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

* Category: *CUDA automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda[,variations] [--input_flags]`

2. `cmr "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda'
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

```cmr "cm gui" --script="install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * Group "**install-driver**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_driver`
      - Environment variables:
        - *CM_CUDA_INSTALL_DRIVER*: `yes`
      - Workflow:
    * **`_no-driver`** (default)
      - Environment variables:
        - *CM_CUDA_INSTALL_DRIVER*: `no`
      - Workflow:

    </details>


#### Default variations

`_no-driver`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--local_run_file_path=value`  &rarr;  `CUDA_RUN_FILE_LOCAL_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "local_run_file_path":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_SUDO: `sudo`

</details>

#### Versions
Default version: `11.8.0`

* `11.7.0`
* `11.8.0`
* `12.0.0`
* `12.1.1`
* `12.2.0`
* `12.3.2`
___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt/_cm.json)***
     * download,file
       * CM names: `--adr.['download-script']...`
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt/_cm.json)
  1. Run "postrocess" function from customize.py
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt/_cm.json)***
     * get,cuda
       * `if (CM_REQUIRE_INSTALL  != yes)`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
</details>

___
### Script output
`cmr "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_CUDA_*`
* `CM_NVCC_*`
#### New environment keys auto-detected from customize

* `CM_CUDA_INSTALLED_PATH`
* `CM_NVCC_BIN_WITH_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)