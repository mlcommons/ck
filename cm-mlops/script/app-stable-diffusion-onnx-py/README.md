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


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *Modular AI/ML application pipeline.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-stable-diffusion-onnx-py)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *modular,python,app,stable-diffusion,onnx*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=modular,python,app,stable-diffusion,onnx[,variations] [--input_flags]`

2. `cmr "modular python app stable-diffusion onnx[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'modular,python,app,stable-diffusion,onnx'
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

```cmr "cm gui" --script="modular,python,app,stable-diffusion,onnx"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=modular,python,app,stable-diffusion,onnx) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "modular python app stable-diffusion onnx[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * Group "**target**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *USE_CPU*: `True`
        - *CM_DEVICE*: `cpu`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *USE_CUDA*: `True`
        - *CM_DEVICE*: `cuda:0`
      - Workflow:

    </details>


#### Default variations

`_cpu`

#### Input description

* --**text** Text to generate image
* --**output** Output directory

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "text":...}
```

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--output=value`  &rarr;  `CM_APP_STABLE_DIFFUSION_ONNX_PY_OUTPUT=value`
* `--text=value`  &rarr;  `CM_APP_STABLE_DIFFUSION_ONNX_PY_TEXT=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "output":...}
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

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-stable-diffusion-onnx-py/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,cuda
       * `if (USE_CUDA  == True)`
       * CM names: `--adr.['cuda']...`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,cudnn
       * `if (USE_CUDA  == True)`
       * CM names: `--adr.['cudnn']...`
       - CM script: [get-cudnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cudnn)
     * get,generic-python-lib,_package.optimum[onnxruntime]
       * `if (USE_CUDA  != True)`
       * CM names: `--adr.['optimum']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.optimum[onnxruntime-gpu]
       * `if (USE_CUDA  == True)`
       * CM names: `--adr.['optimum']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.diffusers
       * CM names: `--adr.['diffusers']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,ml-model,huggingface,zoo,_model-stub.runwayml/stable-diffusion-v1-5
       - CM script: [get-ml-model-huggingface-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-huggingface-zoo)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-stable-diffusion-onnx-py/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-stable-diffusion-onnx-py/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-stable-diffusion-onnx-py/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-stable-diffusion-onnx-py/_cm.yaml)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-stable-diffusion-onnx-py/_cm.yaml)
</details>

___
### Script output
`cmr "modular python app stable-diffusion onnx[,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)