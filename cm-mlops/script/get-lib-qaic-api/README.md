**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-lib-qaic-api).**



Automatically generated README for this automation recipe: **get-lib-qaic-api**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-lib-qaic-api,1e253ae184e44f23) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-qaic-api)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,api,lib-qaic-api,lib,qaic*
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

````cmr "get api lib-qaic-api lib qaic" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,api,lib-qaic-api,lib,qaic`

`cm run script --tags=get,api,lib-qaic-api,lib,qaic `

*or*

`cmr "get api lib-qaic-api lib qaic"`

`cmr "get api lib-qaic-api lib qaic " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,api,lib-qaic-api,lib,qaic'
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

```cmr "cm gui" --script="get,api,lib-qaic-api,lib,qaic"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,api,lib-qaic-api,lib,qaic) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get api lib-qaic-api lib qaic" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `master`

* `master`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-qaic-api/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-qaic-api/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-qaic-api/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-qaic-api/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-qaic-api/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-qaic-api/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-qaic-api/_cm.json)

___
### Script output
`cmr "get api lib-qaic-api lib qaic "  -j`
#### New environment keys (filter)

* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+LD_LIBRARY_PATH`
* `CM_LIB_QAIC_*`
* `CM_QAIC_API_*`
#### New environment keys auto-detected from customize

* `CM_QAIC_API_INC_FILE`
* `CM_QAIC_API_SRC_FILE`