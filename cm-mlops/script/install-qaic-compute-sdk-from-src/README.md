**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/install-qaic-compute-sdk-from-src).**



Automatically generated README for this automation recipe: **install-qaic-compute-sdk-from-src**

Category: **AI/ML frameworks**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-qaic-compute-sdk-from-src,9701bdda97fa4045) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-qaic-compute-sdk-from-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,qaic,from.src,software,compute,compute-sdk,qaic-compute-sdk,sdk*
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

````cmr "get qaic from.src software compute compute-sdk qaic-compute-sdk sdk" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,qaic,from.src,software,compute,compute-sdk,qaic-compute-sdk,sdk`

`cm run script --tags=get,qaic,from.src,software,compute,compute-sdk,qaic-compute-sdk,sdk[,variations] `

*or*

`cmr "get qaic from.src software compute compute-sdk qaic-compute-sdk sdk"`

`cmr "get qaic from.src software compute compute-sdk qaic-compute-sdk sdk [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,qaic,from.src,software,compute,compute-sdk,qaic-compute-sdk,sdk'
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

```cmr "cm gui" --script="get,qaic,from.src,software,compute,compute-sdk,qaic-compute-sdk,sdk"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,qaic,from.src,software,compute,compute-sdk,qaic-compute-sdk,sdk) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get qaic from.src software compute compute-sdk qaic-compute-sdk sdk[variations]" `

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

    </details>


  * Group "**installation-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_debug`
      - Environment variables:
        - *CM_QAIC_COMPUTE_SDK_INSTALL_MODE*: `debug`
      - Workflow:
    * **`_release`** (default)
      - Environment variables:
        - *CM_QAIC_COMPUTE_SDK_INSTALL_MODE*: `release`
      - Workflow:
    * `_release-assert`
      - Environment variables:
        - *CM_QAIC_COMPUTE_SDK_INSTALL_MODE*: `release-assert`
      - Workflow:

    </details>


  * Group "**repo-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_repo.#`
      - Environment variables:
        - *CM_GIT_URL*: `#`
      - Workflow:
    * **`_repo.quic`** (default)
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/quic/software-kit-for-qualcomm-cloud-ai-100-cc`
      - Workflow:

    </details>


#### Default variations

`_release,_repo.quic`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-qaic-compute-sdk-from-src/_cm.json)***
     * get,git,repo,_repo.https://github.com/quic/software-kit-for-qualcomm-cloud-ai-100-cc
       * CM names: `--adr.['qaic-software-git-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
     * get,cmake
       * CM names: `--adr.['cmake']...`
       - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
     * get,llvm,_from-src
       * CM names: `--adr.['llvm']...`
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
     * get,generic,sys-util,_libudev-dev
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic,sys-util,_libpci-dev
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,google,test
       - CM script: [get-google-test](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-google-test)
     * get,generic-sys-util,_ninja-build
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic-sys-util,_rsync
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * download-and-extract,_extract,_url.https://codelinaro.jfrog.io/artifactory/codelinaro-toolchain-for-hexagon/v15.0.5/clang+llvm-15.0.5-cross-hexagon-unknown-linux-musl.tar.xz
       * CM names: `--adr.['dae']...`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-qaic-compute-sdk-from-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-qaic-compute-sdk-from-src/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-qaic-compute-sdk-from-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-qaic-compute-sdk-from-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-qaic-compute-sdk-from-src/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-qaic-compute-sdk-from-src/_cm.json)

___
### Script output
`cmr "get qaic from.src software compute compute-sdk qaic-compute-sdk sdk [,variations]"  -j`
#### New environment keys (filter)

* `+PATH`
* `CM_QAIC_COMPUTE_SDK_PATH`
#### New environment keys auto-detected from customize

* `CM_QAIC_COMPUTE_SDK_PATH`