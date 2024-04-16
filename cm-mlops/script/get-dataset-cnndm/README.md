**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-cnndm).**



Automatically generated README for this automation recipe: **get-dataset-cnndm**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-dataset-cnndm,aed298c156e24257) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cnndm)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,dataset,gpt-j,cnndm,cnn-dailymail,original*
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

````cmr "get dataset gpt-j cnndm cnn-dailymail original" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,dataset,gpt-j,cnndm,cnn-dailymail,original`

`cm run script --tags=get,dataset,gpt-j,cnndm,cnn-dailymail,original[,variations] `

*or*

`cmr "get dataset gpt-j cnndm cnn-dailymail original"`

`cmr "get dataset gpt-j cnndm cnn-dailymail original [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,gpt-j,cnndm,cnn-dailymail,original'
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

```cmr "cm gui" --script="get,dataset,gpt-j,cnndm,cnn-dailymail,original"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,gpt-j,cnndm,cnn-dailymail,original) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset gpt-j cnndm cnn-dailymail original[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_intel`
      - Workflow:
    * `_intel,validation`
      - Environment variables:
        - *CM_CNNDM_INTEL_VARIATION*: `yes`
      - Workflow:

    </details>


  * Group "**dataset-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calibration`
      - Environment variables:
        - *CM_DATASET_CALIBRATION*: `yes`
      - Workflow:
    * **`_validation`** (default)
      - Environment variables:
        - *CM_DATASET_CALIBRATION*: `no`
      - Workflow:

    </details>


#### Default variations

`_validation`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_DATASET_CALIBRATION: `no`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cnndm/_cm.json)***
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * mlperf,inference,source
       * `if (CM_CNNDM_INTEL_VARIATION  != yes)`
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,generic-python-lib,_package.simplejson
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_datasets
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.tokenizers
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_numpy
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cnndm/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cnndm/_cm.json)
  1. ***Run native script if exists***
     * [run-intel.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cnndm/run-intel.sh)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cnndm/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cnndm/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cnndm/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cnndm/_cm.json)

___
### Script output
`cmr "get dataset gpt-j cnndm cnn-dailymail original [,variations]"  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
