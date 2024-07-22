**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-training-src).**



Automatically generated README for this automation recipe: **get-mlperf-training-src**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-mlperf-training-src,dc440bd88e794a28) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,src,source,training,training-src,training-source,mlperf,mlcommons*
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

````cmr "get src source training training-src training-source mlperf mlcommons" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,src,source,training,training-src,training-source,mlperf,mlcommons`

`cm run script --tags=get,src,source,training,training-src,training-source,mlperf,mlcommons[,variations] `

*or*

`cmr "get src source training training-src training-source mlperf mlcommons"`

`cmr "get src source training training-src training-source mlperf mlcommons [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,src,source,training,training-src,training-source,mlperf,mlcommons'
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

```cmr "cm gui" --script="get,src,source,training,training-src,training-source,mlperf,mlcommons"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,src,source,training,training-src,training-source,mlperf,mlcommons) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get src source training training-src training-source mlperf mlcommons[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_no-recurse-submodules`
      - Environment variables:
        - *CM_GIT_RECURSE_SUBMODULES*: ``
      - Workflow:
    * `_nvidia-retinanet`
      - Environment variables:
        - *CM_GIT_PATCH_FILENAMES*: `nvidia-retinanet.patch,cpu_load.patch`
      - Workflow:
    * `_patch`
      - Environment variables:
        - *CM_GIT_PATCH*: `yes`
      - Workflow:

    </details>


  * Group "**checkout**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_branch.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT*: `#`
      - Workflow:
    * `_sha.#`
      - Environment variables:
        - *CM_GIT_SHA*: `#`
      - Workflow:
    * `_tag.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT_TAG*: `#`
      - Workflow:

    </details>


  * Group "**git-history**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_full-history`
      - Environment variables:
        - *CM_GIT_DEPTH*: ``
      - Workflow:
    * **`_short-history`** (default)
      - Environment variables:
        - *CM_GIT_DEPTH*: `--depth 5`
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


  * Group "**src**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cknowledge`** (default)
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/cknowledge/training.git`
      - Workflow:
    * `_mlcommons`
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/mlcommons/training.git`
      - Workflow:

    </details>


#### Default variations

`_cknowledge,_short-history`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_CHECKOUT: `master`
* CM_GIT_DEPTH: `--depth 4`
* CM_GIT_PATCH: `no`
* CM_GIT_RECURSE_SUBMODULES: ` --recurse-submodules`
* CM_GIT_CHECKOUT_FOLDER: `training`

</details>

#### Versions
Default version: `master`

* `custom`
* `master`
___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-src/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-src/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-src/_cm.json)***
     * get,git,repo
       * CM names: `--adr.['mlperf-training-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-src/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-src/_cm.json)

___
### Script output
`cmr "get src source training training-src training-source mlperf mlcommons [,variations]"  -j`
#### New environment keys (filter)

* `+PYTHONPATH`
* `CM_MLPERF_TRAINING_*`
* `CM_MLPERF_TRAINING_LAST_RELEASE`
#### New environment keys auto-detected from customize
