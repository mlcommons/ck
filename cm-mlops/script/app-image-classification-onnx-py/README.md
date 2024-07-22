**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/app-image-classification-onnx-py).**



Automatically generated README for this automation recipe: **app-image-classification-onnx-py**

Category: **Modular AI/ML application pipeline**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=app-image-classification-onnx-py,3d5e908e472b417e) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-onnx-py)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *modular,python,app,image-classification,onnx*
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

````cmr "modular python app image-classification onnx" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=modular,python,app,image-classification,onnx`

`cm run script --tags=modular,python,app,image-classification,onnx[,variations] [--input_flags]`

*or*

`cmr "modular python app image-classification onnx"`

`cmr "modular python app image-classification onnx [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*


#### Input Flags

* --**input**=Path to JPEG image to classify
* --**output**=Output directory (optional)
* --**j**=Print JSON output

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "input":...}
```
#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'modular,python,app,image-classification,onnx'
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

```cmr "cm gui" --script="modular,python,app,image-classification,onnx"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=modular,python,app,image-classification,onnx) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "modular python app image-classification onnx[variations]" [--input_flags]`

___
### Customization


#### Variations

  * Group "**target**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *USE_CPU*: `True`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *USE_CUDA*: `True`
      - Workflow:

    </details>


#### Default variations

`_cpu`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--input=value`  &rarr;  `CM_IMAGE=value`
* `--output=value`  &rarr;  `CM_APP_IMAGE_CLASSIFICATION_ONNX_PY_OUTPUT=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "input":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_BATCH_COUNT: `1`
* CM_BATCH_SIZE: `1`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml)***
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
     * get,dataset,imagenet,image-classification,original
       - CM script: [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)
     * get,dataset-aux,imagenet-aux,image-classification
       - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
     * get,ml-model,resnet50,_onnx,image-classification
       * CM names: `--adr.['ml-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,generic-python-lib,_package.Pillow
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.numpy
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.opencv-python
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnxruntime
       * `if (USE_CUDA  != True)`
       * CM names: `--adr.['onnxruntime']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnxruntime_gpu
       * `if (USE_CUDA  == True)`
       * CM names: `--adr.['onnxruntime']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-onnx-py/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-onnx-py/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-onnx-py/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-onnx-py/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml)

___
### Script output
`cmr "modular python app image-classification onnx [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_APP_IMAGE_CLASSIFICATION_ONNX_PY*`
#### New environment keys auto-detected from customize
