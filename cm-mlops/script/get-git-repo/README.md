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
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *DevOps automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,git,repo,repository,clone*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,git,repo,repository,clone[,variations] [--input_flags]`

2. `cmr "get git repo repository clone[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,git,repo,repository,clone'
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

```cmr "cm gui" --script="get,git,repo,repository,clone"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,git,repo,repository,clone) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get git repo repository clone[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_lfs`
      - Environment variables:
        - *CM_GIT_REPO_NEEDS_LFS*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic,sys-util,_git-lfs
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
    * `_no-recurse-submodules`
      - Environment variables:
        - *CM_GIT_RECURSE_SUBMODULES*: ``
      - Workflow:
    * `_patch`
      - Environment variables:
        - *CM_GIT_PATCH*: `yes`
      - Workflow:
    * `_submodules.#`
      - Environment variables:
        - *CM_GIT_SUBMODULES*: `#`
      - Workflow:

    </details>


  * Group "**checkout**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_branch.#`
      - Environment variables:
        - *CM_GIT_BRANCH*: `#`
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


#### Default variations

`_short-history`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--branch=value`  &rarr;  `CM_GIT_CHECKOUT=value`
* `--depth=value`  &rarr;  `CM_GIT_DEPTH=value`
* `--env_key=value`  &rarr;  `CM_GIT_ENV_KEY=value`
* `--folder=value`  &rarr;  `CM_GIT_CHECKOUT_FOLDER=value`
* `--patch=value`  &rarr;  `CM_GIT_PATCH=value`
* `--submodules=value`  &rarr;  `CM_GIT_RECURSE_SUBMODULES=value`
* `--update=value`  &rarr;  `CM_GIT_REPO_PULL=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "branch":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_DEPTH: `--depth 4`
* CM_GIT_CHECKOUT_FOLDER: `repo`
* CM_GIT_PATCH: `no`
* CM_GIT_RECURSE_SUBMODULES: ` --recurse-submodules`
* CM_GIT_URL: `https://github.com/mlcommons/ck.git`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo/_cm.json)***
     * pull,git,repo
       * `if (CM_GIT_REPO_PULL in ['yes', 'True'])`
       * CM names: `--adr.['pull-git-repo']...`
       - CM script: [pull-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/pull-git-repo)
</details>

___
### Script output
`cmr "get git repo repository clone[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `<<<CM_GIT_CHECKOUT_PATH_ENV_NAME>>>`
* `CM_GIT_CHECKOUT_PATH`
* `CM_GIT_REPO_*`
#### New environment keys auto-detected from customize

* `CM_GIT_CHECKOUT_PATH`
* `CM_GIT_REPO_CURRENT_HASH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)