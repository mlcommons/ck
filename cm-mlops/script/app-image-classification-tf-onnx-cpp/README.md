**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/app-image-classification-tf-onnx-cpp).**



Automatically generated README for this automation recipe: **app-image-classification-tf-onnx-cpp**

Category: **Modular AI/ML application pipeline**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=app-image-classification-tf-onnx-cpp,879ed32e47074033) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-tf-onnx-cpp)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *app,image-classification,cpp,tensorflow,onnx*
* Output cached? *False*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "app image-classification cpp tensorflow onnx" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=app,image-classification,cpp,tensorflow,onnx`

`cm run script --tags=app,image-classification,cpp,tensorflow,onnx `

*or*

`cmr "app image-classification cpp tensorflow onnx"`

`cmr "app image-classification cpp tensorflow onnx " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,image-classification,cpp,tensorflow,onnx'
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

```cmr "cm gui" --script="app,image-classification,cpp,tensorflow,onnx"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=app,image-classification,cpp,tensorflow,onnx) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "app image-classification cpp tensorflow onnx" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_BATCH_COUNT: `1`
* CM_BATCH_SIZE: `1`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-tf-onnx-cpp/_cm.json)***
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
     * get,ml-model,raw,image-classification,resnet50,_onnx,_opset-11
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * tensorflow,from-src
       - CM script: [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-tf-onnx-cpp/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-tf-onnx-cpp/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-tf-onnx-cpp/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-tf-onnx-cpp/_cm.json)

___
### Script output
`cmr "app image-classification cpp tensorflow onnx "  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
