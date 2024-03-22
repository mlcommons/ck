Automatically generated README for this automation recipe: **test-onnxruntime-cpp**

Category: **Testing libraries and tools**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=test-onnxruntime-cpp,c7cb91ff52fc4798) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-onnxruntime-cpp)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *test,onnxruntime,cpp*
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

````cmr "test onnxruntime cpp" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=test,onnxruntime,cpp`

`cm run script --tags=test,onnxruntime,cpp[,variations] `

*or*

`cmr "test onnxruntime cpp"`

`cmr "test onnxruntime cpp [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'test,onnxruntime,cpp'
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

```cmr "cm gui" --script="test,onnxruntime,cpp"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=test,onnxruntime,cpp) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "test onnxruntime cpp[variations]" `

___
### Customization


#### Variations

  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_DEVICE*: `cpu`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_DEVICE*: `gpu`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_onnxruntime`** (default)
      - Environment variables:
        - *CM_BACKEND*: `onnxruntime`
      - Workflow:

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_resnet50`** (default)
      - Environment variables:
        - *CM_MODEL*: `resnet50`
      - Workflow:

    </details>


#### Default variations

`_cpu,_onnxruntime,_resnet50`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-onnxruntime-cpp/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,lib,onnxruntime,lang-cpp,_cpu
       * `if (CM_BACKEND  == onnxruntime AND CM_DEVICE  == cpu)`
       - CM script: [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)
     * get,lib,onnxruntime,lang-cpp,_cuda
       * `if (CM_BACKEND  == onnxruntime AND CM_DEVICE  == gpu)`
       - CM script: [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)
     * get,dataset,preprocessed,imagenet,_NCHW
       * `if (CM_MODEL  == resnet50)`
       * CM names: `--adr.['imagenet-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,ml-model,raw,resnet50,_onnx
       * `if (CM_MODEL  == resnet50)`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-onnxruntime-cpp/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-onnxruntime-cpp/_cm.yaml)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-onnxruntime-cpp/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-onnxruntime-cpp/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-onnxruntime-cpp/_cm.yaml)***
     * compile,cpp-program
       * `if (CM_SKIP_COMPILE  != True)`
       * CM names: `--adr.['compile-program']...`
       - CM script: [compile-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)
     * benchmark-program
       * `if (CM_SKIP_RUN  != True)`
       * CM names: `--adr.['benchmark-program']...`
       - CM script: [benchmark-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)

___
### Script output
`cmr "test onnxruntime cpp [,variations]"  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
