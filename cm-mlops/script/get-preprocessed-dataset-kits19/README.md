**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-kits19).**



Automatically generated README for this automation recipe: **get-preprocessed-dataset-kits19**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-preprocessed-dataset-kits19,2094d9b9ab6c4c9e) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-kits19)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,dataset,medical-imaging,kits19,preprocessed*
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

````cmr "get dataset medical-imaging kits19 preprocessed" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,dataset,medical-imaging,kits19,preprocessed`

`cm run script --tags=get,dataset,medical-imaging,kits19,preprocessed[,variations] [--input_flags]`

*or*

`cmr "get dataset medical-imaging kits19 preprocessed"`

`cmr "get dataset medical-imaging kits19 preprocessed [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,medical-imaging,kits19,preprocessed'
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

```cmr "cm gui" --script="get,dataset,medical-imaging,kits19,preprocessed"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,medical-imaging,kits19,preprocessed) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset medical-imaging kits19 preprocessed[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_nvidia`
      - Environment variables:
        - *CM_PREPROCESSING_BY_NVIDIA*: `yes`
      - Workflow:

    </details>


  * Group "**dataset-count**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_1`
      - Environment variables:
        - *CM_DATASET_SIZE*: `1`
      - Workflow:
    * `_5`
      - Environment variables:
        - *CM_DATASET_SIZE*: `5`
      - Workflow:
    * `_50`
      - Environment variables:
        - *CM_DATASET_SIZE*: `50`
      - Workflow:
    * `_500`
      - Environment variables:
        - *CM_DATASET_SIZE*: `500`
      - Workflow:
    * `_full`
      - Environment variables:
        - *CM_DATASET_SIZE*: ``
      - Workflow:

    </details>


  * Group "**dataset-precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_DATASET_DTYPE*: `fp32`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_DATASET_DTYPE*: `int8`
      - Workflow:

    </details>


  * Group "**dataset-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calibration`
      - Environment variables:
        - *CM_DATASET_PATH*: `<<<CM_CALIBRATION_DATASET_PATH>>>`
      - Workflow:
    * **`_validation`** (default)
      - Workflow:

    </details>


#### Default variations

`_fp32,_validation`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_PATH=value`
* `--threads=value`  &rarr;  `CM_NUM_PREPROCESS_THREADS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_DATASET: `kits19`
* CM_DATASET_DTYPE: `fp32`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-kits19/_cm.json)***
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,dataset,medical-imaging,kits19,original
       * CM names: `--adr.['original-dataset']...`
       - CM script: [get-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-kits19)
     * mlperf,mlcommons,inference,source,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,generic-python-lib,_scipy
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_nibabel
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_numpy
       * CM names: `--adr.['numpy']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-kits19/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-kits19/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-kits19/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-kits19/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-kits19/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-kits19/_cm.json)

___
### Script output
`cmr "get dataset medical-imaging kits19 preprocessed [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_DATASET_*`
#### New environment keys auto-detected from customize

* `CM_DATASET_PREPROCESSED_PATH`