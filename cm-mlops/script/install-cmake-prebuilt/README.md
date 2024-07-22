**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/install-cmake-prebuilt).**



Automatically generated README for this automation recipe: **install-cmake-prebuilt**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-cmake-prebuilt,5a39ef05992b4103) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cmake-prebuilt)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,prebuilt,cmake,prebuilt-cmake,install-prebuilt-cmake*
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

````cmr "install prebuilt cmake prebuilt-cmake install-prebuilt-cmake" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,prebuilt,cmake,prebuilt-cmake,install-prebuilt-cmake`

`cm run script --tags=install,prebuilt,cmake,prebuilt-cmake,install-prebuilt-cmake `

*or*

`cmr "install prebuilt cmake prebuilt-cmake install-prebuilt-cmake"`

`cmr "install prebuilt cmake prebuilt-cmake install-prebuilt-cmake " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,prebuilt,cmake,prebuilt-cmake,install-prebuilt-cmake'
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

```cmr "cm gui" --script="install,prebuilt,cmake,prebuilt-cmake,install-prebuilt-cmake"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,prebuilt,cmake,prebuilt-cmake,install-prebuilt-cmake) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install prebuilt cmake prebuilt-cmake install-prebuilt-cmake" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `3.28.3`

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cmake-prebuilt/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cmake-prebuilt/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cmake-prebuilt/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cmake-prebuilt/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cmake-prebuilt/_cm.json)
  1. Run "postrocess" function from customize.py
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cmake-prebuilt/_cm.json)***
     * get,cmake
       * `if (CM_REQUIRE_INSTALL  != yes)`
       - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)

___
### Script output
`cmr "install prebuilt cmake prebuilt-cmake install-prebuilt-cmake "  -j`
#### New environment keys (filter)

* `+C_INCLUDE_PATH`
* `+LD_LIBRARY_PATH`
* `+PATH`
* `CM_CMAKE_*`
* `CM_GET_DEPENDENT_CACHED_PATH`
#### New environment keys auto-detected from customize

* `CM_CMAKE_BIN_WITH_PATH`
* `CM_CMAKE_INSTALLED_PATH`
* `CM_CMAKE_PACKAGE`
* `CM_GET_DEPENDENT_CACHED_PATH`