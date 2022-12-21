*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Modular ML/AI applications.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-cpp)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
app,image-classification,onnx,cpp

___
### Default environment

* CM_BATCH_COUNT: **1**
* CM_BATCH_SIZE: **1**
___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-cpp/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,gcc
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
     * get,dataset,image-classification,original
       - CM script: [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)
     * get,dataset-aux,image-classification
       - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
     * get,ml-model,image-classification,resnet50,_onnx-1.5-opset-11
       - *Warning: no scripts found*
     * get,mlcommons,loadgen
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
     * tensorflow,from-src
       - CM script: [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-cpp/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-cpp/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-cpp/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-cpp/_cm.json)
___
### New environment export

___
### New environment detected from customize

___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="app,image-classification,onnx,cpp"`

*or*

`cm run script "app image-classification onnx cpp"`

*or*

`cm run script 879ed32e47074033`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,image-classification,onnx,cpp'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)