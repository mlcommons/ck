**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/install-tensorflow-from-src).**



Automatically generated README for this automation recipe: **install-tensorflow-from-src**

Category: **AI/ML frameworks**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-tensorflow-from-src,a974533c4c854597) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tensorflow-from-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,install,tensorflow,lib,source,from-source,from-src,src,from.src*
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

````cmr "get install tensorflow lib source from-source from-src src from.src" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,install,tensorflow,lib,source,from-source,from-src,src,from.src`

`cm run script --tags=get,install,tensorflow,lib,source,from-source,from-src,src,from.src[,variations] `

*or*

`cmr "get install tensorflow lib source from-source from-src src from.src"`

`cmr "get install tensorflow lib source from-source from-src src from.src [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,install,tensorflow,lib,source,from-source,from-src,src,from.src'
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

```cmr "cm gui" --script="get,install,tensorflow,lib,source,from-source,from-src,src,from.src"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,install,tensorflow,lib,source,from-source,from-src,src,from.src) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get install tensorflow lib source from-source from-src src from.src[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_tflite`
      - Environment variables:
        - *CM_TFLITE*: `on`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_URL: `https://github.com/tensorflow/tensorflow`
* CM_GIT_DEPTH: `1`
* CM_TFLITE: `off`

</details>

#### Versions
Default version: `master`

* `master`
* `v1.15.0`
* `v2.0.0`
* `v2.1.0`
* `v2.2.0`
* `v2.3.0`
* `v2.4.0`
* `v2.5.0`
* `v2.6.0`
* `v2.7.0`
* `v2.8.0`
* `v2.9.0`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tensorflow-from-src/_cm.json)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,generic-sys-util,_zlib
       * `if (CM_HOST_OS_FLAVOR  == ubuntu AND CM_HOST_OS_VERSION  == 18.04)`
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic-python-lib,_package.numpy
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tensorflow-from-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tensorflow-from-src/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tensorflow-from-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tensorflow-from-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tensorflow-from-src/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tensorflow-from-src/_cm.json)

___
### Script output
`cmr "get install tensorflow lib source from-source from-src src from.src [,variations]"  -j`
#### New environment keys (filter)

* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+DYLD_FALLBACK_LIBRARY_PATH`
* `+LD_LIBRARY_PATH`
#### New environment keys auto-detected from customize
