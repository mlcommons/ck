**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-aocl).**



Automatically generated README for this automation recipe: **get-aocl**

Category: **Compiler automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-aocl,a65d3088f57d413d) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aocl)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,lib,aocl,amd-optimized,amd*
* Output cached? *true*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "get lib aocl amd-optimized amd" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,lib,aocl,amd-optimized,amd`

`cm run script --tags=get,lib,aocl,amd-optimized,amd `

*or*

`cmr "get lib aocl amd-optimized amd"`

`cmr "get lib aocl amd-optimized amd " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,lib,aocl,amd-optimized,amd'
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

```cmr "cm gui" --script="get,lib,aocl,amd-optimized,amd"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,lib,aocl,amd-optimized,amd) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get lib aocl amd-optimized amd" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `4.0`

* `4.0`
* `master`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aocl/_cm.json)***
     * get,generic,sys-util,_libmpfr-dev
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic-python-lib,_scons
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,git,_repo.https://github.com/amd/aocl-libm-ose
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aocl/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aocl/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aocl/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aocl/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aocl/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aocl/_cm.json)

___
### Script output
`cmr "get lib aocl amd-optimized amd "  -j`
#### New environment keys (filter)

* `+LD_LIBRARY_PATH`
* `+LIBRARY_PATH`
* `CM_AOCL_BUILD_PATH`
* `CM_AOCL_LIB_PATH`
* `CM_AOCL_SRC_PATH`
#### New environment keys auto-detected from customize

* `CM_AOCL_BUILD_PATH`
* `CM_AOCL_LIB_PATH`
* `CM_AOCL_SRC_PATH`