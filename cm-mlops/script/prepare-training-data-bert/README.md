**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/prepare-training-data-bert).**



Automatically generated README for this automation recipe: **prepare-training-data-bert**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=prepare-training-data-bert,1e06a7abe23545eb) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-bert)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *prepare,mlperf,training,data,input,bert*
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

````cmr "prepare mlperf training data input bert" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=prepare,mlperf,training,data,input,bert`

`cm run script --tags=prepare,mlperf,training,data,input,bert[,variations] [--input_flags]`

*or*

`cmr "prepare mlperf training data input bert"`

`cmr "prepare mlperf training data input bert [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'prepare,mlperf,training,data,input,bert'
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

```cmr "cm gui" --script="prepare,mlperf,training,data,input,bert"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=prepare,mlperf,training,data,input,bert) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "prepare mlperf training data input bert[variations]" [--input_flags]`

___
### Customization


#### Variations

  * Group "**implementation**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_nvidia`** (default)
      - Environment variables:
        - *CM_TMP_VARIATION*: `nvidia`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,git,repo,_repo.https://github.com/wchen61/training_results_v2.1,_branch.fix_bert_prepare_data
             - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
    * `_reference`
      - Environment variables:
        - *CM_TMP_VARIATION*: `reference`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,mlperf,training,src
             * CM names: `--adr.['mlperf-training-src']...`
             - CM script: [get-mlperf-training-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src)
           * get,python3
             * CM names: `--adr.['python3']...`
             - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
           * get,generic-python-lib,_tensorflow
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_protobuf
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


#### Default variations

`_nvidia`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--clean=value`  &rarr;  `CM_MLPERF_TRAINING_CLEAN_TFRECORDS=value`
* `--data_dir=value`  &rarr;  `CM_DATA_DIR=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "clean":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-bert/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-bert/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-bert/_cm.json)***
     * download,file,_gdown,_url.https://drive.google.com/uc?id=1fbGClQMi2CoMv7fwrwTC5YYPooQBdcFW
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
     * download,file,_gdown,_url.https://drive.google.com/uc?id=1USK108J6hMM_d27xCHi738qBL8_BT1u1
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
     * download,file,_gdown,_url.https://drive.google.com/uc?id=1tmMgLwoBvbEJEHXh77sqrXYw5RpqT8R_
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
     * download-and-extract,file,_gdown,_extract,_url.https://drive.google.com/uc?id=14xV2OUGSQDG_yDBrmbSdcDC-QGeqpfs_
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
     * download,file,_gdown,_url.https://drive.google.com/uc?id=1chiTBljF0Eh1U5pKs6ureVHgSbtU8OG_
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
     * download,file,_gdown,_url.https://drive.google.com/uc?id=1Q47V3K3jFRkbJ2zGCrKkKk-n0fvMZsa0
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
     * download,file,_gdown,_url.https://drive.google.com/uc?id=1vAcVmXSLsLeQ1q7gvHnQUSth5W_f_pwv
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. ***Run native script if exists***
     * [run-nvidia.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-bert/run-nvidia.sh)
     * [run-reference.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-bert/run-reference.sh)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-bert/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-bert/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-bert/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-bert/_cm.json)

___
### Script output
`cmr "prepare mlperf training data input bert [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_MLPERF_TRAINING_BERT_*`
#### New environment keys auto-detected from customize

* `CM_MLPERF_TRAINING_BERT_CONFIG_PATH`
* `CM_MLPERF_TRAINING_BERT_DATA_PATH`
* `CM_MLPERF_TRAINING_BERT_TFRECORDS_PATH`
* `CM_MLPERF_TRAINING_BERT_VOCAB_PATH`