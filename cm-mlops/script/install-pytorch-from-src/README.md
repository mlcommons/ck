**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/install-pytorch-from-src).**



Automatically generated README for this automation recipe: **install-pytorch-from-src**

Category: **Compiler automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-pytorch-from-src,64eaf3e81de94f41) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pytorch-from-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,get,src,from.src,pytorch,src-pytorch*
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

````cmr "install get src from.src pytorch src-pytorch" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,get,src,from.src,pytorch,src-pytorch`

`cm run script --tags=install,get,src,from.src,pytorch,src-pytorch[,variations] `

*or*

`cmr "install get src from.src pytorch src-pytorch"`

`cmr "install get src from.src pytorch src-pytorch [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

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

`cm docker script "install get src from.src pytorch src-pytorch[variations]" `

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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pytorch-from-src/_cm.json)***
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
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pytorch-from-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pytorch-from-src/_cm.json)
  1. ***Run native script if exists***
     * [run-intel-mlperf-inference-v3_1.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pytorch-from-src/run-intel-mlperf-inference-v3_1.sh)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pytorch-from-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pytorch-from-src/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pytorch-from-src/_cm.json)

___
### Script output
`cmr "install get src from.src pytorch src-pytorch [,variations]"  -j`
#### New environment keys (filter)

* `CM_PYTORCH_*`
#### New environment keys auto-detected from customize
