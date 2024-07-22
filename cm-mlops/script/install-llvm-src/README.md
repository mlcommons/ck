**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/install-llvm-src).**



Automatically generated README for this automation recipe: **install-llvm-src**

Category: **Compiler automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-llvm-src,2af16e9a6c5f4702) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,src,llvm,from.src,src-llvm*
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

````cmr "install src llvm from.src src-llvm" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,src,llvm,from.src,src-llvm`

`cm run script --tags=install,src,llvm,from.src,src-llvm[,variations] `

*or*

`cmr "install src llvm from.src src-llvm"`

`cmr "install src llvm from.src src-llvm [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,src,llvm,from.src,src-llvm'
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

```cmr "cm gui" --script="install,src,llvm,from.src,src-llvm"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,src,llvm,from.src,src-llvm) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install src llvm from.src src-llvm[variations]" `

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
    * `_for-intel-mlperf-inference-v3.1-bert`
      - Environment variables:
        - *CM_LLVM_CONDA_ENV*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,gcc
             - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
           * get,conda,_name.bert-pt
             * CM names: `--adr.['conda']...`
             - CM script: [get-conda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-conda)
           * get,conda-package,_package.ncurses,_source.conda-forge
             * CM names: `--adr.['conda-package', 'ncurses']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.ninja
             * CM names: `--adr.['conda-package', 'ninja']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.cmake
             * CM names: `--adr.['conda-package', 'cmake']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,conda-package,_package.llvm-openmp,_source.conda-forge
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,conda-package,_package.chardet
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.libstdcxx-ng,_source.conda-forge
             * CM names: `--adr.['conda-package', 'libstdcxx-ng']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
    * `_for-intel-mlperf-inference-v3.1-gptj`
      - Environment variables:
        - *CM_LLVM_CONDA_ENV*: `yes`
        - *CM_LLVM_16_INTEL_MLPERF_INFERENCE*: `yes`
        - *USE_CUDA*: `0`
        - *CUDA_VISIBLE_DEVICES*: ``
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-sys-util,_g++-12
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
           * get,gcc
             - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
           * get,conda,_name.gptj-pt
             * CM names: `--adr.['conda']...`
             - CM script: [get-conda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-conda)
           * get,generic,conda-package,_package.python
             * CM names: `--adr.['conda-package', 'python']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,conda-package,_package.ncurses,_source.conda-forge
             * CM names: `--adr.['conda-package', 'ncurses']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,conda-package,_package.chardet
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.libstdcxx-ng,_source.conda-forge
             * CM names: `--adr.['conda-package', 'libstdcxx-ng']...`
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
           * get,generic,conda-package,_package.gperftools,_source.conda-forge
             * CM names: `--adr.['conda-package', 'gperftools']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic,conda-package,_package.pybind11,_source.conda-forge
             * CM names: `--adr.['conda-package', 'pybind11']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
           * get,generic-python-lib,_custom-python,_package.torch,_url.git+https://github.com/pytorch/pytorch.git@927dc662386af052018212c7d01309a506fc94cd
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_custom-python,_package.setuptools
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_custom-python,_package.neural-compressor,_url.git+https://github.com/intel/neural-compressor.git@a2931eaa4052eec195be3c79a13f7bfa23e54473
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_full-history`
      - Workflow:
    * `_runtimes.#`
      - Environment variables:
        - *CM_LLVM_ENABLE_RUNTIMES*: `#`
      - Workflow:
    * `_sha.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT_SHA*: `#`
      - Workflow:
    * `_tag.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT_TAG*: `#`
      - Workflow:

    </details>


  * Group "**build-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_debug`
      - Environment variables:
        - *CM_LLVM_BUILD_TYPE*: `debug`
      - Workflow:
    * **`_release`** (default)
      - Environment variables:
        - *CM_LLVM_BUILD_TYPE*: `release`
      - Workflow:

    </details>


  * Group "**clang**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_clang`** (default)
      - Environment variables:
        - *CM_LLVM_ENABLE_PROJECTS*: `clang`
      - Workflow:

    </details>


  * Group "**repo**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_repo.#`
      - Environment variables:
        - *CM_GIT_URL*: `#`
      - Workflow:

    </details>


#### Default variations

`_clang,_release`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-src/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,cmake
       * `if (CM_LLVM_CONDA_ENV  != yes)`
       - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
     * get,generic-sys-util,_ninja-build
       * `if (CM_LLVM_CONDA_ENV  != yes)`
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,git,repo
       * CM names: `--adr.['llvm-src-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-src/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-src/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-src/_cm.json)***
     * get,llvm
       * `if (CM_REQUIRE_INSTALL  != yes)`
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)

___
### Script output
`cmr "install src llvm from.src src-llvm [,variations]"  -j`
#### New environment keys (filter)

* `+C_INCLUDE_PATH`
* `+PATH`
* `CM_GET_DEPENDENT_CACHED_PATH`
* `CM_LLVM_*`
#### New environment keys auto-detected from customize

* `CM_GET_DEPENDENT_CACHED_PATH`
* `CM_LLVM_CLANG_BIN_WITH_PATH`
* `CM_LLVM_CMAKE_CMD`
* `CM_LLVM_INSTALLED_PATH`