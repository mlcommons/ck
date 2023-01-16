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

* Category: *ML/AI datasets.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,aux,dataset-aux,image-classification,imagenet-aux*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=get,aux,dataset-aux,image-classification,imagenet-aux(,variations from below) (flags from below)`

*or*

`cm run script "get aux dataset-aux image-classification imagenet-aux (variations from below)" (flags from below)`

*or*

`cm run script bb2c6dd8c8c64217`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,aux,dataset-aux,image-classification,imagenet-aux'
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

    * `_2012`
      - Environment variables:
        - *CM_DATASET_AUX_VER*: `2012`
      - Workflow:
    * `_from.berkeleyvision`
      - Environment variables:
        - *CM_WGET_URL*: `http://dl.caffe.berkeleyvision.org/caffe_ilsvrc12.tar.gz`
      - Workflow:
    * **`_from.dropbox`** (default)
      - Environment variables:
        - *CM_WGET_URL*: `https://www.dropbox.com/s/92n2fyej3lzy3s3/caffe_ilsvrc12.tar.gz`
      - Workflow:

</details>

___
### Script workflow, dependencies and native scripts

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)
___
### Script output
#### New environment keys

* **CM_DATASET_AUX_***
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)