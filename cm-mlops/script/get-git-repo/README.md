**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-git-repo).**



Automatically generated README for this automation recipe: **get-git-repo**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-git-repo,ed603e7292974f10) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-git-repo)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,git,repo,repository,clone*
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

````cmr "get git repo repository clone" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,git,repo,repository,clone`

`cm run script --tags=get,git,repo,repository,clone[,variations] [--input_flags]`

*or*

`cmr "get git repo repository clone"`

`cmr "get git repo repository clone [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

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

`cm docker script "get git repo repository clone[variations]" [--input_flags]`

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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-git-repo/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-git-repo/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-git-repo/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-git-repo/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-git-repo/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-git-repo/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-git-repo/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-git-repo/_cm.json)***
     * pull,git,repo
       * `if (CM_GIT_REPO_PULL in ['yes', 'True'])`
       * CM names: `--adr.['pull-git-repo']...`
       - CM script: [pull-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/pull-git-repo)

___
### Script output
`cmr "get git repo repository clone [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `<<<CM_GIT_CHECKOUT_PATH_ENV_NAME>>>`
* `CM_GIT_CHECKOUT_PATH`
* `CM_GIT_REPO_*`
#### New environment keys auto-detected from customize

* `CM_GIT_CHECKOUT_PATH`
* `CM_GIT_REPO_CURRENT_HASH`