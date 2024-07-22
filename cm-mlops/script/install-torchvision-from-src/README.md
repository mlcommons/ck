**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/install-torchvision-from-src).**



Automatically generated README for this automation recipe: **install-torchvision-from-src**

Category: **Compiler automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-torchvision-from-src,68b855780d474546) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-torchvision-from-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,get,src,from.src,pytorchvision,torchvision,src-pytorchvision*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "install get src from.src pytorchvision torchvision src-pytorchvision" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,get,src,from.src,pytorchvision,torchvision,src-pytorchvision`

`cm run script --tags=install,get,src,from.src,pytorchvision,torchvision,src-pytorchvision[,variations] `

*or*

`cmr "install get src from.src pytorchvision torchvision src-pytorchvision"`

`cmr "install get src from.src pytorchvision torchvision src-pytorchvision [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,get,src,from.src,pytorchvision,torchvision,src-pytorchvision'
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

```cmr "cm gui" --script="install,get,src,from.src,pytorchvision,torchvision,src-pytorchvision"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,get,src,from.src,pytorchvision,torchvision,src-pytorchvision) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install get src from.src pytorchvision torchvision src-pytorchvision[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_branch.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT*: `#`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CUDA_HOME*: `<<<CM_CUDA_INSTALLED_PATH>>>`
        - *CUDA_NVCC_EXECUTABLE*: `<<<CM_NVCC_BIN_WITH_PATH>>>`
        - *CUDNN_INCLUDE_PATH*: `<<<CM_CUDA_PATH_INCLUDE_CUDNN>>>`
        - *CUDNN_LIBRARY_PATH*: `<<<CM_CUDA_PATH_LIB_CUDNN>>>`
        - *USE_CUDA*: `1`
        - *USE_CUDNN*: `1`
        - *TORCH_CUDA_ARCH_LIST*: `Ampere Ada Hopper`
        - *TORCH_CXX_FLAGS*: `-D_GLIBCXX_USE_CXX11_ABI=1`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda,_cudnn
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
    * `_for-nvidia-mlperf-inference-v3.1`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * install,pytorch,from.src,_for-nvidia-mlperf-inference-v3.1
             - CM script: [install-pytorch-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from-src)
    * `_sha.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT_SHA*: `#`
      - Workflow:
    * `_tag.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT_TAG*: `#`
      - Workflow:

    </details>


  * Group "**repo**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_repo.#`
      - Environment variables:
        - *CM_GIT_URL*: `#`
      - Workflow:
    * **`_repo.https://github.com/pytorch/vision`** (default)
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/pytorch/vision`
      - Workflow:

    </details>


#### Default variations

`_repo.https://github.com/pytorch/vision`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-torchvision-from-src/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python3
       * `if (CM_CONDA_ENV  != yes)`
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,git,repo
       * CM names: `--adr.['pytorchision-src-repo', 'torchision-src-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-torchvision-from-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-torchvision-from-src/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-torchvision-from-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-torchvision-from-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-torchvision-from-src/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-torchvision-from-src/_cm.json)

___
### Script output
`cmr "install get src from.src pytorchvision torchvision src-pytorchvision [,variations]"  -j`
#### New environment keys (filter)

* `CM_PYTORCHVISION_*`
#### New environment keys auto-detected from customize
