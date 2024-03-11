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
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

*Build pytorch from sources.*

#### Summary

* Category: *Compiler automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *install,get,src,from.src,pytorch,src-pytorch*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=install,get,src,from.src,pytorch,src-pytorch[,variations] `

2. `cmr "install get src from.src pytorch src-pytorch[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,get,src,from.src,pytorch,src-pytorch'
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

```cmr "cm gui" --script="install,get,src,from.src,pytorch,src-pytorch"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,get,src,from.src,pytorch,src-pytorch) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install get src from.src pytorch src-pytorch[ variations]" `

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
        - *CUDNN_LIBRARY_PATH*: `<<<CM_CUDA_PATH_LIB_CUDNN>>>`
        - *CUDNN_INCLUDE_PATH*: `<<<CM_CUDA_PATH_INCLUDE_CUDNN>>>`
        - *CUDA_NVCC_EXECUTABLE*: `<<<CM_NVCC_BIN_WITH_PATH>>>`
        - *USE_CUDA*: `1`
        - *USE_CUDNN*: `1`
        - *TORCH_CUDA_ARCH_LIST*: `Ampere Ada Hopper`
        - *TORCH_CXX_FLAGS*: `-D_GLIBCXX_USE_CXX11_ABI=1`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda,_cudnn
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
    * `_for-intel-mlperf-inference-v3.1-bert`
      - Environment variables:
        - *CM_CONDA_ENV*: `yes`
        - *CM_MLPERF_INFERENCE_INTEL*: `yes`
        - *USE_CUDA*: `0`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-sys-util,_libffi7
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
           * get,conda,_name.bert-pt
             * CM names: `--adr.['conda']...`
             - CM script: [get-conda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-conda)
           * get,generic,conda-package,_package.ncurses,_source.conda-forge
             * CM names: `--adr.['conda-package', 'ncurses']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.python
             * CM names: `--adr.['conda-package', 'python3']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * install,llvm,src,_tag.llvmorg-15.0.7,_runtimes.libcxx:libcxxabi:openmp,_clang,_release,_for-intel-mlperf-inference-v3.1-bert
             - CM script: [install-llvm-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-src)
           * get,generic,conda-package,_package.ninja
             * CM names: `--adr.['conda-package', 'ninja']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.cmake
             * CM names: `--adr.['conda-package', 'cmake']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.mkl,_source.intel
             * CM names: `--adr.['conda-package', 'mkl']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.mkl-include,_source.intel
             * CM names: `--adr.['conda-package', 'mkl-include']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.intel-openmp,_source.intel
             * CM names: `--adr.['conda-package', 'intel-openmp']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.llvm-openmp,_source.conda-forge
             * CM names: `--adr.['conda-package', 'llvm-openmp']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.jemalloc,_source.conda-forge
             * CM names: `--adr.['conda-package', 'jemalloc']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.wheel,_source.conda-forge
             * CM names: `--adr.['conda-package', 'wheel']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.setuptools,_source.conda-forge
             * CM names: `--adr.['conda-package', 'setuptools']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.future,_source.conda-forge
             * CM names: `--adr.['conda-package', 'future']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.libstdcxx-ng,_source.conda-forge
             * CM names: `--adr.['conda-package', 'libstdcxx-ng']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
    * `_for-nvidia-mlperf-inference-v3.1`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cmake
             - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
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
    * **`_repo.https://github.com/pytorch/pytorch`** (default)
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/pytorch/pytorch`
      - Workflow:

    </details>


#### Default variations

`_repo.https://github.com/pytorch/pytorch`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from-src/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python3
       * `if (CM_CONDA_ENV  != yes)`
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,git,repo
       * CM names: `--adr.['pytorch-src-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from-src/_cm.json)
  1. ***Run native script if exists***
     * [run-intel-mlperf-inference-v3_1.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from-src/run-intel-mlperf-inference-v3_1.sh)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from-src/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from-src/_cm.json)
</details>

___
### Script output
`cmr "install get src from.src pytorch src-pytorch[,variations]"  -j`
#### New environment keys (filter)

* `CM_PYTORCH_*`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)