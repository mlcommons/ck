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
  * [ Input description](#input-description)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
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

* Category: *Tests.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-abtf-ssd-pytorch)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *test,abtf,ssd,pytorch,ssd-pytorch*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=test,abtf,ssd,pytorch,ssd-pytorch[,variations] [--input_flags]`

2. `cmr "test abtf ssd pytorch ssd-pytorch[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'test,abtf,ssd,pytorch,ssd-pytorch'
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

```cmr "cm gui" --script="test,abtf,ssd,pytorch,ssd-pytorch"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=test,abtf,ssd,pytorch,ssd-pytorch) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "test abtf ssd pytorch ssd-pytorch[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * Group "**dataset**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_coco`** (default)
      - Environment variables:
        - *CM_ABTF_DATASET*: `coco`
        - *CM_ABTF_SSD_PYTORCH_BRANCH*: `main`
      - Workflow:
    * `_cognata`
      - Environment variables:
        - *CM_ABTF_DATASET*: `Cognata`
        - *CM_ABTF_SSD_PYTORCH_BRANCH*: `cognata`
        - *CM_ABTF_ML_MODEL_CONFIG*: `baseline_8MP`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_DEVICE*: `cpu`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_DEVICE*: `cuda`
      - Workflow:

    </details>


#### Default variations

`_coco,_cpu`

#### Input description

* --**input** input image (png)
* --**output** output image (png)
* --**export_model** ONNX model name to be exported from PyTorch

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "input":...}
```

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--export_model=value`  &rarr;  `CM_ABTF_EXPORT_MODEL_TO_ONNX=value`
* `--input=value`  &rarr;  `CM_INPUT_IMAGE=value`
* `--output=value`  &rarr;  `CM_OUTPUT_IMAGE=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "export_model":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-abtf-ssd-pytorch/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_numpy
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.Pillow
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnx
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torch
       * CM names: `--adr.['torch']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torchvision
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_opencv-python
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,ml-model,abtf-ssd-pytorch
       * CM names: `--adr.['ml-model']...`
       - CM script: [get-ml-model-abtf-ssd-pytorch](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-abtf-ssd-pytorch)
     * get,git,repo,_repo.https://github.com/mlcommons/abtf-ssd-pytorch
       * CM names: `--adr.['abtf-ssd-pytorch-git-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-abtf-ssd-pytorch/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-abtf-ssd-pytorch/_cm.yaml)
  1. ***Run native script if exists***
     * [run-coco.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-abtf-ssd-pytorch/run-coco.bat)
     * [run-coco.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-abtf-ssd-pytorch/run-coco.sh)
     * [run-cognata.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-abtf-ssd-pytorch/run-cognata.bat)
     * [run-cognata.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-abtf-ssd-pytorch/run-cognata.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-abtf-ssd-pytorch/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-abtf-ssd-pytorch/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-abtf-ssd-pytorch/_cm.yaml)
</details>

___
### Script output
`cmr "test abtf ssd pytorch ssd-pytorch[,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)