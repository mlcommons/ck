<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM GUI](#cm-gui)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! Use `README-extra.md` to add more info.*

### Description

#### Information

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-resnet)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *prepare,mlperf,training,data,input,resnet*
* Output cached?: *True*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=prepare,mlperf,training,data,input,resnet[,variations] [--input_flags]`

2. `cm run script "prepare mlperf training data input resnet[,variations]" [--input_flags]`

3. `cm run script d42a8a8ca2704f9f [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

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


#### CM GUI

```cm run script --tags=gui --script="prepare,mlperf,training,data,input,resnet"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=prepare,mlperf,training,data,input,resnet) to generate CM CMD.

#### CM modular Docker container

*TBD*

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
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-resnet/_cm.json)***
     * get,dataset,imagenet,train
       * CM names: `--adr.['imagenet-train']...`
       - CM script: [get-dataset-imagenet-train](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-train)
     * get,dataset,imagenet,val,original,_full
       * CM names: `--adr.['imagenet-val']...`
       - CM script: [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)
     * get,generic-sys-util,_rsync
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-resnet/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-resnet/_cm.json)***
     * download,file,_wget,_url.https://raw.githubusercontent.com/tensorflow/models/master/research/slim/datasets/imagenet_2012_validation_synset_labels.txt
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
     * download,file,_wget,_url.https://raw.githubusercontent.com/tensorflow/tpu/master/tools/datasets/imagenet_to_gcs.py
       * `if (CM_TMP_VARIATION  == reference)`
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. ***Run native script if exists***
     * [run-nvidia.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-resnet/run-nvidia.sh)
     * [run-reference.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-resnet/run-reference.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-resnet/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-resnet/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-resnet/_cm.json)
</details>

___
### Script output
#### New environment keys (filter)

* `CM_MLPERF_TRAINING_NVIDIA_RESNET_PREPROCESSED_PATH`
* `CM_MLPERF_TRAINING_RESNET_*`
#### New environment keys auto-detected from customize

* `CM_MLPERF_TRAINING_NVIDIA_RESNET_PREPROCESSED_PATH`
* `CM_MLPERF_TRAINING_RESNET_DATA_PATH`
* `CM_MLPERF_TRAINING_RESNET_TFRECORDS_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)