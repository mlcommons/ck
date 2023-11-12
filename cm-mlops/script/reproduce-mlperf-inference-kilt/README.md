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

This script is a CM wrapper to the official [Nvidia submission code](https://github.com/mlcommons/inference_results_v3.0/tree/master/closed/NVIDIA) used for MLPerf inference submissions. 



## Download the needed files

* Please ask privately in [this discord channel](https://discord.gg/y7hupJsUNb) if you would like to get access to an Amazon S3 bucket containing all the needed files for easiness. Otherwise, you can download them from the below links.
  
For x86 machines, please download the latest install tar files from the below sites
1. [cuDNN](https://developer.nvidia.com/cudnn) (for cuda 11)
2. [TensorRT](https://developer.nvidia.com/tensorrt)
3. Imagenet validation set (unfortunately not available via public URL) following the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md)

<details>

<summary>
    
## Using Docker (Recommended on x86 systems)

</summary>
Assuming all the downloaded files are to the user home directory please do the following steps:

1. Download CUDA 11.8
    ```
    wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
    ```
2. [Install docker](https://docs.docker.com/engine/install/) and [Nvidia container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
     
3. Give docker permission to the current user
     ```
     sudo usermod -aG docker $USER
     ```
     Logout and login
     Restart docker if required and confirm that Nvidia container toolkit is working by
     ```
     nvidia-ctk --version
     ```
4. Check if Nvidia driver is working properly on the host. 
     ```
     nvidia-smi
     ```
     If the above command produces any error you'll need to install Nvidia drivers on the host. You can do this via CM if you have sudo access
     ```
     cmr "install cuda prebuilt _driver" --version=11.8.0
     ```
5. Build the docker container and mount the paths from the host machine.
    ** You may want to change the `scratch_path` location as it can take 100s of GBs.**
    ```bash
    cm docker script --tags=build,nvidia,inference,server \
    --cuda_run_file_path=$HOME/cuda_11.8.0_520.61.05_linux.run \
    --tensorrt_tar_file_path=$HOME/TensorRT-8.6.1.6.Linux.x86_64-gnu.cuda-11.8.tar.gz \
    --cudnn_tar_file_path=$HOME/cudnn-linux-x86_64-8.9.2.26_cuda11-archive.tar.xz \
    --imagenet_path=$HOME/imagenet-2012-val \
    --scratch_path=$HOME/mlperf_scratch \
    --docker_cm_repo=mlcommons@ck  \
    --results_dir=$HOME/results_dir \
    --submission_dir=$HOME/submission_dir \
    --adr.compiler.tags=gcc
    ```
      * Use `--docker_cache=no` to turn off docker caching
      * Use `--docker_run_cmd_prefix="cm pull repo mlcommons@ck"` to update the CK repository when docker caching is used
      * Use `--custom_system=no` if you are using a similar system to the [Nvidia submission systems for MLPerf inference 3.0](https://github.com/mlcommons/inference_results_v3.0/tree/main/closed/NVIDIA/systems).

6. At the end of the build you'll get the following prompt unless you have chosen `--custom_system=no`. Please give a system name and say yes to generating the configuration files
    ### Example output
    ```
    ============================================
    => A system ID is a string containing only letters, numbers, and underscores
    => that is used as the human-readable name of the system. It is also used as
    => the system name when creating the measurements/ and results/ entries.
    => This string should also start with a letter to be a valid Python enum member name.
    => Specify the system ID to use for the current system: phoenix
      => Reloaded system list. MATCHED_SYSTEM: KnownSystem.phoenix
    => This script will generate Benchmark Configuration stubs for the detected system.
    Continue? [y/n]: y
    ```
    Now you'll be inside the CM Nvidia docker container and can run further scripts. 

7. Once the build is complete, you can proceed with any further CM scripts like for MLPerf inference. You can also save the container at this stage using [docker commit](https://docs.docker.com/engine/reference/commandline/commit/) so that it can be launched later without having to go through the previous steps.

</details>

<details>

<summary>

## Without Docker
</summary>

1. Install CUDA
    If CUDA is not detected, CM should download and install it automatically when you run the workflow. 
    ** Nvidia drivers are expected to be installed on the system **

2. Install cuDNN
    ```bash
      cmr "get cudnn" --input=<PATH_TO_CUDNN_TAR_FILE>
    ```
3. Install TensorRT
    ```bash
      cmr "get tensorrt _dev" --input=<PATH_TO_TENSORRT_TAR_FILE>
    ```
    On non x86 systems like Nvidia Orin, you can do a package manager install and then CM should pick up the installation automatically during the workflow run.

4. Build the Nvidia inference server 
    ```
      cmr "build nvidia inference server" \
      --adr.install-cuda-prebuilt.local_run_file_path=/data/cuda_11.8.0_520.61.05_linux.run \
      --adr.tensorrt.tar_file=/data/TensorRT-8.6.1.6.Linux.x86_64-gnu.cuda-11.8.tar.gz \
      --adr.cudnn.tar_file=/data/cudnn-linux-x86_64-8.9.2.26_cuda11-archive.tar.xz \
      --adr.compiler.tags=gcc \
      [--custom_system=no]
      ```
    Use `--custom_system=no` if you are using a similar system to the [Nvidia submission systems for MLPerf inference 3.0](https://github.com/mlcommons/inference_results_v3.0/tree/main/closed/NVIDIA/systems).

5. At the end of the build you'll get the following prompt unless you have chosen `--custom_system=no`. Please give a system name and say yes to generating the configuration files

    ### Example output
    ```
    ============================================
    => A system ID is a string containing only letters, numbers, and underscores
    => that is used as the human-readable name of the system. It is also used as
    => the system name when creating the measurements/ and results/ entries.
    => This string should also start with a letter to be a valid Python enum member name.
    => Specify the system ID to use for the current system: phoenix
      => Reloaded system list. MATCHED_SYSTEM: KnownSystem.phoenix
    => This script will generate Benchmark Configuration stubs for the detected system.
    Continue? [y/n]: y
    ```
</details>


## Acknowledgments

* A common CM interface and automation for MLPerf inference benchmarks was developed by Arjun Suresh and Grigori Fursin 
  sponsored by the [cTuning foundation](https://cTuning.org) and [cKnowledge.org](https://cKnowledge.org).
* Nvidia's MLPerf inference implementation was developed by Zhihan Jiang, Ethan Cheng, Yiheng Zhang and Jinho Suh.


#### Information

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *reproduce,mlcommons,mlperf,inference,harness,kilt-harness,kilt*
* Output cached?: *False*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,kilt-harness,kilt[,variations] [--input_flags]`

2. `cm run script "reproduce mlcommons mlperf inference harness kilt-harness kilt[,variations]" [--input_flags]`

3. `cm run script eef1aca5d7c0470e [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,inference,harness,kilt-harness,kilt'
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

```cm run script --tags=gui --script="reproduce,mlcommons,mlperf,inference,harness,kilt-harness,kilt"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=reproduce,mlcommons,mlperf,inference,harness,kilt-harness,kilt) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert_`
      - Environment variables:
        - *CM_BENCHMARK*: `STANDALONE_BERT`
        - *kilt_model_name*: `bert`
        - *kilt_model_seq_length*: `384`
        - *kilt_model_batch_size*: `384`
        - *kilt_model_bert_variant*: `BERT_PACKED`
        - *kilt_input_format*: `INT64,1,384:INT64,1,8:INT64,1,384:INT64,1,384`
        - *kilt_output_format*: `FLOAT32,1,384:FLOAT32,1,384`
        - *dataset_squad_tokenized_max_seq_length*: `384`
        - *loadgen_buffer_size*: `10833`
        - *loadgen_dataset_size*: `10833`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_transformers
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_safetensors
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_onnx
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert_,network-client`
      - Environment variables:
        - *CM_BENCHMARK*: `NETWORK_BERT_CLIENT`
      - Workflow:
    * `_bert_,network-server`
      - Environment variables:
        - *CM_BENCHMARK*: `NETWORK_BERT_SERVER`
      - Workflow:
    * `_bert_,singlestream`
      - Environment variables:
        - *kilt_model_batch_size*: `1`
      - Workflow:

    </details>


  * Group "**batch-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_batch_size.#`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `#`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `#`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
        - *kilt_backend_type*: `cpu`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `gpu`
        - *CM_MLPERF_DEVICE_LIB_NAMESPEC*: `cudart`
        - *kilt_backend_type*: `gpu`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_onnxruntime`** (default)
      - Environment variables:
        - *device*: `onnxrt`
        - *CM_MLPERF_BACKEND*: `onnxruntime`
        - *CM_MLPERF_BACKEND_LIB_NAMESPEC*: `onnxruntime`
      - Workflow:
    * `_tensorrt`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tensorrt`
        - *device*: `tensorrt`
        - *CM_MLPERF_BACKEND_NAME*: `TensorRT`
      - Workflow:

    </details>


  * Group "**loadgen-scenario**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_multistream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `MultiStream`
      - Workflow:
    * `_offline`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `Offline`
      - Workflow:
    * `_server`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `Server`
      - Workflow:
    * `_singlestream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `SingleStream`
        - *kilt_model_batch_size*: `1`
      - Workflow:

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert-99`
      - Environment variables:
        - *CM_MODEL*: `bert-99`
        - *CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx`
      - Workflow:
    * `_bert-99.9`
      - Environment variables:
        - *CM_MODEL*: `bert-99.9`
        - *CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/3733910/files/model.onnx`
      - Workflow:
    * **`_resnet50`** (default)
      - Environment variables:
        - *CM_MODEL*: `resnet50`
        - *kilt_model_name*: `resnet50`
        - *kilt_input_count*: `1`
        - *kilt_output_count*: `1`
        - *kilt_input_format*: `FLOAT32,-1,224,224,3`
        - *kilt_output_format*: `INT64,-1`
        - *kilt_model_batch_size*: `32`
        - *dataset_imagenet_preprocessed_input_square_side*: `224`
        - *ml_model_has_background_class*: `YES`
        - *ml_model_image_height*: `224`
        - *loadgen_buffer_size*: `1024`
        - *loadgen_dataset_size*: `50000`
        - *CM_BENCHMARK*: `STANDALONE_CLASSIFICATION`
      - Workflow:
    * `_retinanet`
      - Environment variables:
        - *CM_MODEL*: `retinanet`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/6617981/files/resnext50_32x4d_fpn.pth`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_Pillow
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torch
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torchvision
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_opencv-python
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_pycocotools
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * Group "**power-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_maxn`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_MAXN*: `True`
      - Workflow:
    * `_maxq`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_MAXQ*: `True`
      - Workflow:

    </details>


  * Group "**run-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calibrate`
      - Environment variables:
        - *MLPERF_NVIDIA_RUN_COMMAND*: `calibrate`
        - *CM_MLPERF_NVIDIA_HARNESS_RUN_MODE*: `calibrate`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * reproduce,mlperf,inference,nvidia,harness,_download_model
             * `if (CM_MODEL not in ['retinanet_old', 'resnet50', 'bert-99', 'bert-99.9', 'dlrm-v2-99', 'dlrm-v2-99.9'])`
             - CM script: [reproduce-mlperf-inference-kilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt)
    * `_download_model`
      - Environment variables:
        - *MLPERF_NVIDIA_RUN_COMMAND*: `download_model`
        - *CM_MLPERF_NVIDIA_HARNESS_RUN_MODE*: `download_model`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torch_cuda
             * `if (CM_MODEL  == retinanet)`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_network-client`
      - Environment variables:
        - *CM_RUN_MODE*: `network-client`
      - Workflow:
    * `_network-server`
      - Environment variables:
        - *CM_RUN_MODE*: `network-server`
      - Workflow:
    * `_preprocess_data`
      - Environment variables:
        - *MLPERF_NVIDIA_RUN_COMMAND*: `preprocess_data`
        - *CM_MLPERF_NVIDIA_HARNESS_RUN_MODE*: `preprocess_data`
      - Workflow:
    * **`_standalone`** (default)
      - Environment variables:
        - *CM_RUN_MODE*: `standalone`
      - Workflow:

    </details>


#### Default variations

`_cpu,_onnxruntime,_resnet50,_standalone`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
* `--devices=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_DEVICES=value`
* `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
* `--mlperf_conf=value`  &rarr;  `CM_MLPERF_CONF=value`
* `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
* `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
* `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
* `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`
* `--performance_sample_count=value`  &rarr;  `CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
* `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
* `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
* `--skip_preprocess=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
* `--skip_preprocessing=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
* `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
* `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
* `--user_conf=value`  &rarr;  `CM_MLPERF_USER_CONF=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "count":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_BATCH_COUNT: `1`
* CM_BATCH_SIZE: `1`
* CM_FAST_COMPILATION: `yes`
* CM_MLPERF_LOADGEN_SCENARIO: `Offline`
* CM_MLPERF_LOADGEN_MODE: `performance`
* CM_SKIP_PREPROCESS_DATASET: `no`
* CM_SKIP_MODEL_DOWNLOAD: `no`
* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `nvidia_original`
* CM_MLPERF_SKIP_RUN: `no`
* CM_KILT_REPO_URL: `https://github.com/krai/kilt-mlperf`
* kilt_device_ids: `0`
* kilt_max_wait_abs: `10000`
* verbosity: `1`
* loadgen_trigger_cold_run: `0`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,cuda,_cudnn
       * CM names: `--adr.['cuda']...`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,git,repo
       * CM names: `--adr.['kilt-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
     * get,generic-python-lib,_mlperf_logging
       * CM names: `--adr.['mlperf-logging']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,dataset,imagenet,preprocessed,_NHWC,_full
       * `if (CM_MODEL  == resnet50)`
       * CM names: `--adr.['imagenet-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,ml-model,resnet50,_fp32,_onnx,_no-argmax
       * `if (CM_MODEL  == resnet50)`
       * CM names: `--adr.['resnet50-model', 'ml-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,ml-model,bert-large,_packed,_pytorch
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       * CM names: `--adr.['bert-model']...`
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
     * get,squad-vocab
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       * CM names: `--adr.['bert-vocab']...`
       - CM script: [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)
     * get,dataset,tokenized,squad
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       * CM names: `--adr.['squad-itokenized']...`
       - CM script: [get-preprocessed-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad)
     * get,dataset,original,openimages,_validation,_full,_custom-annotations
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['openimages-original']...`
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
     * get,dataset,original,openimages,_calibration
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['openimages-calibration']...`
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,mlcommons,inference,loadgen
       * CM names: `--adr.['inference-loadgen']...`
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
     * generate,user-conf,mlperf,inference
       * CM names: `--adr.['user-conf-generator']...`
       - CM script: [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)
     * get,lib,onnxruntime,lang-cpp,_cpu
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MLPERF_DEVICE  == cpu)`
       - CM script: [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)
     * get,lib,onnxruntime,lang-cpp,_cuda
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MLPERF_DEVICE  == gpu)`
       - CM script: [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/_cm.yaml)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-kilt/_cm.yaml)***
     * compile,cpp-program
       * `if (CM_MLPERF_SKIP_RUN  != True)`
       * CM names: `--adr.['compile-program']...`
       - CM script: [compile-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)
     * benchmark-mlperf
       * `if (CM_MLPERF_SKIP_RUN not in ['yes', True])`
       * CM names: `--adr.['runner', 'mlperf-runner']...`
       - CM script: [benchmark-program-mlperf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program-mlperf)
</details>

___
### Script output
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)