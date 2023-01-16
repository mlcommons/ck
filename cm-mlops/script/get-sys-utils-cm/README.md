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
  * [ Default environment](#default-environment)
  * [ Variations](#variations)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys](#new-environment-keys)
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! Use `README-extra.md` to add more info.*

### Description

#### Information

* Category: *Detection or installation of tools and artifacts.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,sys-utils-cm*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=get,sys-utils-cm(,variations from below) (flags from below)`

*or*

`cm run script "get sys-utils-cm (variations from below)" (flags from below)`

*or*

`cm run script bc90993277e84b8e`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,sys-utils-cm'
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

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.


</details>


#### Variations

  * *No group (any variation can be selected)*
<details>
<summary>Click here to expand this section.</summary>

    * `_user`
      - Environment variables:
        - *CM_PYTHON_PIP_USER*: `--user`
      - Workflow:

</details>

___
### Script workflow, dependencies and native scripts

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm/_cm.json)
  1. ***Run native script if exists***
     * [run-arch.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm/run-arch.sh)
     * [run-debian.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm/run-debian.sh)
     * [run-macos.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm/run-macos.sh)
     * [run-rhel.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm/run-rhel.sh)
     * [run-ubuntu.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm/run-ubuntu.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm/_cm.json)
___
### Script output
#### New environment keys

* **+PATH**
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)