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
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from.src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *install,src,from.src,pytorch,src-pytorch*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=install,src,from.src,pytorch,src-pytorch[,variations] `

2. `cmr "install src from.src pytorch src-pytorch[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,src,from.src,pytorch,src-pytorch'
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

```cmr "cm gui" --script="install,src,from.src,pytorch,src-pytorch"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,src,from.src,pytorch,src-pytorch) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install src from.src pytorch src-pytorch[ variations]" `

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

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from.src/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * install,llvm,src,_tag.llvmorg-15.0.7,_runtimes.libcxx:libcxxabi:openmp,_clang,_release
       - CM script: [install-llvm-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-src)
     * get,git,repo
       * CM names: `--adr.['pytorch-src-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from.src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from.src/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from.src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from.src/_cm.json)
  1. Run "postrocess" function from customize.py
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from.src/_cm.json)***
     * get,llvm
       * `if (CM_REQUIRE_INSTALL  != yes)`
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
</details>

___
### Script output
`cmr "install src from.src pytorch src-pytorch[,variations]"  -j`
#### New environment keys (filter)

* `CM_GET_DEPENDENT_CACHED_PATH`
* `CM_PYTORCH_*`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)