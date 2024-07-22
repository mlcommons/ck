**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/install-python-src).**



Automatically generated README for this automation recipe: **install-python-src**

Category: **Python automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-python-src,12d3a608afe14a1e) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,src,python,python3,src-python3,src-python*
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

````cmr "install src python python3 src-python3 src-python" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,src,python,python3,src-python3,src-python`

`cm run script --tags=install,src,python,python3,src-python3,src-python[,variations] `

*or*

`cmr "install src python python3 src-python3 src-python"`

`cmr "install src python python3 src-python3 src-python [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,src,python,python3,src-python3,src-python'
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

```cmr "cm gui" --script="install,src,python,python3,src-python3,src-python"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,src,python,python3,src-python3,src-python) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install src python python3 src-python3 src-python[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_lto`
      - Environment variables:
        - *CM_PYTHON_LTO_FLAG*: ` --lto`
        - *CM_PYTHON_INSTALL_CACHE_TAGS*: `with-lto`
      - Workflow:
    * `_optimized`
      - Environment variables:
        - *CM_PYTHON_OPTIMIZATION_FLAG*: ` --enable-optimizations`
        - *CM_PYTHON_INSTALL_CACHE_TAGS*: `optimized`
      - Workflow:
    * `_shared`
      - Environment variables:
        - *CM_PYTHON_INSTALL_CACHE_TAGS*: `shared`
        - *CM_SHARED_BUILD*: `yes`
      - Workflow:
    * `_with-custom-ssl`
      - Environment variables:
        - *CM_CUSTOM_SSL*: `yes`
        - *CM_PYTHON_INSTALL_CACHE_TAGS*: `with-custom-ssl`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,openssl
             - CM script: [get-openssl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openssl)
    * `_with-ssl`
      - Environment variables:
        - *CM_ENABLE_SSL*: `yes`
        - *CM_PYTHON_INSTALL_CACHE_TAGS*: `with-ssl`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_ENABLE_SSL: `no`
* CM_CUSTOM_SSL: `no`
* CM_SHARED_BUILD: `no`
* CM_PYTHON_OPTIMIZATION_FLAG: ``
* CM_PYTHON_LTO_FLAG: ``
* CM_WGET_URL: `https://www.python.org/ftp/python/[PYTHON_VERSION]/Python-[PYTHON_VERSION].tgz`

</details>

#### Versions
Default version: `3.10.13`

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-src/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-src/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-src/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-src/_cm.json)***
     * get,python3
       * `if (CM_REQUIRE_INSTALL  != yes)`
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)

___
### Script output
`cmr "install src python python3 src-python3 src-python [,variations]"  -j`
#### New environment keys (filter)

* `+C_INCLUDE_PATH`
* `+LD_LIBRARY_PATH`
* `+PATH`
* `CM_PYTHON_BIN_WITH_PATH`
* `CM_PYTHON_INSTALL_PATH`
#### New environment keys auto-detected from customize

* `CM_PYTHON_BIN_WITH_PATH`