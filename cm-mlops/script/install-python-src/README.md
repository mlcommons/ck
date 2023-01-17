<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Default environment](#default-environment)
* [Versions](#versions)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! Use `README-extra.md` to add more info.*

### Description

#### Information

* Category: *Python automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *install,src,python,python3,src-python3,src-python*
* Output cached?: *True*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=install,src,python,python3,src-python3,src-python(,variations from below) (flags from below)`

*or*

`cm run script "install src python python3 src-python3 src-python (variations from below)" (flags from below)`

*or*

`cm run script 12d3a608afe14a1e`

#### CM Python API

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

#### CM modular Docker container
*TBD*
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

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_ENABLE_SSL: **no**
* CM_CUSTOM_SSL: **no**
* CM_SHARED_BUILD: **no**
* CM_PYTHON_OPTIMIZATION_FLAG: ****
* CM_PYTHON_LTO_FLAG: ****
* CM_WGET_URL: **https://www.python.org/ftp/python/[PYTHON_VERSION]/Python-[PYTHON_VERSION].tgz**

</details>

#### Versions
Default version: *3.10.5*

___
### Script workflow, dependencies and native scripts

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src/_cm.json)***
     * get,python3
       * `if (CM_REQUIRE_INSTALL  != yes)`
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
___
### Script output
#### New environment keys (filter)

* **+C_INCLUDE_PATH**
* **+LD_LIBRARY_PATH**
* **+PATH**
* **CM_PYTHON_BIN_WITH_PATH**
* **CM_PYTHON_INSTALL_PATH**
#### New environment keys auto-detected from customize

* **CM_PYTHON_BIN_WITH_PATH**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)