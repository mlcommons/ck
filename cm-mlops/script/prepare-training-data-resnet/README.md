**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/prepare-training-data-resnet).**



Automatically generated README for this automation recipe: **prepare-training-data-resnet**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=prepare-training-data-resnet,d42a8a8ca2704f9f) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-resnet)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *prepare,mlperf,training,data,input,resnet*
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

````cmr "prepare mlperf training data input resnet" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=prepare,mlperf,training,data,input,resnet`

`cm run script --tags=prepare,mlperf,training,data,input,resnet[,variations] [--input_flags]`

*or*

`cmr "prepare mlperf training data input resnet"`

`cmr "prepare mlperf training data input resnet [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'prepare,mlperf,training,data,input,resnet'
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

```cmr "cm gui" --script="prepare,mlperf,training,data,input,resnet"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=prepare,mlperf,training,data,input,resnet) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "prepare mlperf training data input resnet[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_mxnet.#`
      - Environment variables:
        - *CM_MXNET_VERSION*: `#`
      - Workflow:

    </details>


  * Group "**implementation**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_nvidia`** (default)
      - Environment variables:
        - *CM_TMP_VARIATION*: `nvidia`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,mlperf,training,nvidia,code
             * CM names: `--adr.['nvidia-training-code']...`
             - CM script: [get-mlperf-training-nvidia-code](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-nvidia-code)
           * get,git,repo,_repo.https://github.com/NVIDIA/DeepLearningExamples,_sha.81ee705868a11d6fe18c12d237abe4a08aab5fd6
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

* `--data_dir=value`  &rarr;  `CM_DATA_DIR=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "data_dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-resnet/_cm.json)***
     * get,dataset,imagenet,train
       * CM names: `--adr.['imagenet-train']...`
       - CM script: [get-dataset-imagenet-train](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-train)
     * get,dataset,imagenet,val,original,_full
       * CM names: `--adr.['imagenet-val']...`
       - CM script: [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)
     * get,generic-sys-util,_rsync
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-resnet/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-resnet/_cm.json)***
     * download,file,_wget,_url.https://raw.githubusercontent.com/tensorflow/models/master/research/slim/datasets/imagenet_2012_validation_synset_labels.txt
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
     * download,file,_wget,_url.https://raw.githubusercontent.com/tensorflow/tpu/master/tools/datasets/imagenet_to_gcs.py
       * `if (CM_TMP_VARIATION  == reference)`
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. ***Run native script if exists***
     * [run-nvidia.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-resnet/run-nvidia.sh)
     * [run-reference.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-resnet/run-reference.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-resnet/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-resnet/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-resnet/_cm.json)

___
### Script output
`cmr "prepare mlperf training data input resnet [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_MLPERF_TRAINING_NVIDIA_RESNET_PREPROCESSED_PATH`
* `CM_MLPERF_TRAINING_RESNET_*`
#### New environment keys auto-detected from customize

* `CM_MLPERF_TRAINING_NVIDIA_RESNET_PREPROCESSED_PATH`
* `CM_MLPERF_TRAINING_RESNET_DATA_PATH`
* `CM_MLPERF_TRAINING_RESNET_TFRECORDS_PATH`