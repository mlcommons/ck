**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-qaic-software-kit).**



Automatically generated README for this automation recipe: **get-qaic-software-kit**

Category: **AI/ML frameworks**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-qaic-software-kit,3344655922694bbb) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-software-kit)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,qaic,software,kit,qaic-software-kit*
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

````cmr "get qaic software kit qaic-software-kit" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,qaic,software,kit,qaic-software-kit`

`cm run script --tags=get,qaic,software,kit,qaic-software-kit[,variations] `

*or*

`cmr "get qaic software kit qaic-software-kit"`

`cmr "get qaic software kit qaic-software-kit [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,qaic,software,kit,qaic-software-kit'
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

```cmr "cm gui" --script="get,qaic,software,kit,qaic-software-kit"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,qaic,software,kit,qaic-software-kit) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get qaic software kit qaic-software-kit[variations]" `

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


  * Group "**repo-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_repo.#`
      - Environment variables:
        - *CM_GIT_URL*: `#`
      - Workflow:
    * **`_repo.quic`** (default)
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/quic/software-kit-for-qualcomm-cloud-ai-100`
      - Workflow:

    </details>


#### Default variations

`_repo.quic`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-software-kit/_cm.json)***
     * get,git,repo
       * CM names: `--adr.['qaic-software-git-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
     * get,generic,sys-util,_libudev-dev
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic,sys-util,_libpci-dev
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,google,test
       - CM script: [get-google-test](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-google-test)
     * get,cmake
       * CM names: `--adr.['cmake']...`
       - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
     * get,compiler
       * CM names: `--adr.['compiler']...`
       - CM script: [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-software-kit/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-software-kit/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-software-kit/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-software-kit/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-software-kit/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-software-kit/_cm.json)

___
### Script output
`cmr "get qaic software kit qaic-software-kit [,variations]"  -j`
#### New environment keys (filter)

* `+PATH`
* `CM_QAIC_RUNNER_PATH`
* `CM_QAIC_SOFTWARE_KIT_PATH`
#### New environment keys auto-detected from customize

* `CM_QAIC_RUNNER_PATH`
* `CM_QAIC_SOFTWARE_KIT_PATH`