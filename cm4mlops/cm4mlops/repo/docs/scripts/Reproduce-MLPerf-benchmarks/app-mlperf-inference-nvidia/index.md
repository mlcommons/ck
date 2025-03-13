# app-mlperf-inference-nvidia
Automatically generated README for this automation recipe: **app-mlperf-inference-nvidia**

Category: **[Reproduce MLPerf benchmarks](..)**

License: **Apache 2.0**



---

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
    --docker_cm_repo=mlcommons@cm4mlops  \
    --results_dir=$HOME/results_dir \
    --submission_dir=$HOME/submission_dir \
    --adr.compiler.tags=gcc
    ```
      * Use `--docker_cache=no` to turn off docker caching
      * Use `--docker_run_cmd_prefix="cm pull repo mlcommons@cm4mlops --checkout=dev"` to update the CK repository when docker caching is used
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
      cmr "get cudnn" --tar_file=<PATH_TO_CUDNN_TAR_FILE>
    ```
3. Install TensorRT
    ```bash
      cmr "get tensorrt _dev" --tar_file=<PATH_TO_TENSORRT_TAR_FILE>
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


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-nvidia/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "reproduce mlcommons mlperf inference harness nvidia-harness nvidia" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,nvidia-harness,nvidia[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "reproduce mlcommons mlperf inference harness nvidia-harness nvidia [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,inference,harness,nvidia-harness,nvidia'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

    if r['return']>0:
        print (r['error'])

    ```


=== "Docker"
    ##### Run this script via Docker (beta)

    ```bash
    cm docker script "reproduce mlcommons mlperf inference harness nvidia-harness nvidia[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_run-harness`
        * `_v3.1`
               - ENV variables:
                   - CM_MLPERF_INFERENCE_VERSION: `v3.1`
                   - CM_MLPERF_GPTJ_MODEL_FP8_PATH_SUFFIX: `GPTJ-07142023.pth`

        </details>


      * Group "**backend**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_tensorrt`** (default)
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tensorrt`
                   - CM_MLPERF_BACKEND_NAME: `TensorRT`

        </details>


      * Group "**batch-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_batch_size.#`
               - ENV variables:
                   - CM_MODEL_BATCH_SIZE: `#`
                   - CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE: `#`

        </details>


      * Group "**build-engine-options**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_build_engine_options.#`
               - ENV variables:
                   - CM_MLPERF_NVIDIA_HARNESS_EXTRA_BUILD_ENGINE_OPTIONS: `#`

        </details>


      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_cpu`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `cpu`
        * **`_cuda`** (default)
               - ENV variables:
                   - CM_MLPERF_DEVICE: `gpu`
                   - CM_MLPERF_DEVICE_LIB_NAMESPEC: `cudart`

        </details>


      * Group "**device-memory**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_gpu_memory.16`
               - ENV variables:
                   - CM_NVIDIA_GPU_MEMORY: `16`
        * `_gpu_memory.24`
               - ENV variables:
                   - CM_NVIDIA_GPU_MEMORY: `24`
        * `_gpu_memory.32`
               - ENV variables:
                   - CM_NVIDIA_GPU_MEMORY: `32`
        * `_gpu_memory.40`
               - ENV variables:
                   - CM_NVIDIA_GPU_MEMORY: `40`
        * `_gpu_memory.48`
               - ENV variables:
                   - CM_NVIDIA_GPU_MEMORY: `48`
        * `_gpu_memory.8`
               - ENV variables:
                   - CM_NVIDIA_GPU_MEMORY: `8`
        * `_gpu_memory.80`
               - ENV variables:
                   - CM_NVIDIA_GPU_MEMORY: `80`

        </details>


      * Group "**dla-batch-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_dla_batch_size.#`
               - ENV variables:
                   - CM_MLPERF_NVIDIA_HARNESS_DLA_BATCH_SIZE: `#`
                   - CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX2: `dla_batch_size.#`

        </details>


      * Group "**gpu-connection**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_pcie`
        * `_sxm`

        </details>


      * Group "**gpu-name**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_a100`
               - ENV variables:
                   - CM_NVIDIA_CUSTOM_GPU: `yes`
        * `_a6000`
               - ENV variables:
                   - CM_NVIDIA_CUSTOM_GPU: `yes`
        * `_custom`
               - ENV variables:
                   - CM_NVIDIA_CUSTOM_GPU: `yes`
                   - CM_MODEL_BATCH_SIZE: ``
                   - CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE: `<<<CM_MODEL_BATCH_SIZE>>>`
        * `_l4`
               - ENV variables:
                   - CM_NVIDIA_CUSTOM_GPU: `yes`
        * `_orin`
               - ENV variables:
                   - CM_NVIDIA_CUSTOM_GPU: `yes`
                   - CM_MODEL_BATCH_SIZE: ``
                   - CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE: `<<<CM_MODEL_BATCH_SIZE>>>`
        * `_rtx_4090`
               - ENV variables:
                   - CM_NVIDIA_CUSTOM_GPU: `yes`
        * `_rtx_6000_ada`
               - ENV variables:
                   - CM_NVIDIA_CUSTOM_GPU: `yes`
        * `_t4`
               - ENV variables:
                   - CM_NVIDIA_CUSTOM_GPU: `yes`

        </details>


      * Group "**loadgen-scenario**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_multistream`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `MultiStream`
        * `_offline`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `Offline`
        * `_server`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `Server`
        * `_singlestream`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `SingleStream`
                   - CUDA_VISIBLE_DEVICES_NOT_USED: `0`

        </details>


      * Group "**model**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_3d-unet-99`
               - ENV variables:
                   - CM_MODEL: `3d-unet-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/5597155/files/3dunet_kits19_128x128x128.onnx`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, affine fusion`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
        * `_3d-unet-99.9`
               - ENV variables:
                   - CM_MODEL: `3d-unet-99.9`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/5597155/files/3dunet_kits19_128x128x128.onnx`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, affine fusion`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
        * `_bert-99`
               - ENV variables:
                   - CM_MODEL: `bert-99`
                   - CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, affine fusion`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int32`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
        * `_bert-99.9`
               - ENV variables:
                   - CM_MODEL: `bert-99.9`
                   - CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/3733910/files/model.onnx`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, affine fusion`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int32`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp16`
        * `_dlrm-v2-99`
               - ENV variables:
                   - CM_MODEL: `dlrm-v2-99`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `affine fusion`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp16`
        * `_dlrm-v2-99.9`
               - ENV variables:
                   - CM_MODEL: `dlrm-v2-99.9`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `affine fusion`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp16`
        * `_gptj-99`
               - ENV variables:
                   - CM_MODEL: `gptj-99`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, affine fusion`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int32`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp16`
        * `_gptj-99.9`
               - ENV variables:
                   - CM_MODEL: `gptj-99.9`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, affine fusion`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int32`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp16`
        * **`_resnet50`** (default)
               - ENV variables:
                   - CM_MODEL: `resnet50`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, affine fusion`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
        * `_retinanet`
               - ENV variables:
                   - CM_MODEL: `retinanet`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/6617981/files/resnext50_32x4d_fpn.pth`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, affine fusion`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
        * `_rnnt`
               - ENV variables:
                   - CM_MODEL: `rnnt`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/3662521/files/DistributedDataParallel_1576581068.9962234-epoch-100.pt`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, affine fusion`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp16`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp16`

        </details>


      * Group "**num-gpus**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_num-gpus.#`
               - ENV variables:
                   - CM_NVIDIA_NUM_GPUS: `#`
        * **`_num-gpus.1`** (default)
               - ENV variables:
                   - CM_NVIDIA_NUM_GPUS: `1`

        </details>


      * Group "**power-mode**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_maxn`
               - ENV variables:
                   - CM_MLPERF_NVIDIA_HARNESS_MAXN: `True`
        * `_maxq`
               - ENV variables:
                   - CM_MLPERF_NVIDIA_HARNESS_MAXQ: `True`

        </details>


      * Group "**run-mode**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_build`
               - ENV variables:
                   - MLPERF_NVIDIA_RUN_COMMAND: `build`
                   - CM_MLPERF_NVIDIA_HARNESS_RUN_MODE: `build`
        * `_build_engine`
              - Aliases: `_build-engine`
               - ENV variables:
                   - MLPERF_NVIDIA_RUN_COMMAND: `generate_engines`
                   - CM_MLPERF_NVIDIA_HARNESS_RUN_MODE: `generate_engines`
        * `_calibrate`
               - ENV variables:
                   - MLPERF_NVIDIA_RUN_COMMAND: `calibrate`
                   - CM_MLPERF_NVIDIA_HARNESS_RUN_MODE: `calibrate`
        * `_download_model`
               - ENV variables:
                   - MLPERF_NVIDIA_RUN_COMMAND: `download_model`
                   - CM_MLPERF_NVIDIA_HARNESS_RUN_MODE: `download_model`
        * `_prebuild`
               - ENV variables:
                   - MLPERF_NVIDIA_RUN_COMMAND: `prebuild`
                   - CM_MLPERF_NVIDIA_HARNESS_RUN_MODE: `prebuild`
        * `_preprocess_data`
               - ENV variables:
                   - MLPERF_NVIDIA_RUN_COMMAND: `preprocess_data`
                   - CM_MLPERF_NVIDIA_HARNESS_RUN_MODE: `preprocess_data`
        * **`_run_harness`** (default)
               - ENV variables:
                   - CM_MLPERF_NVIDIA_HARNESS_RUN_MODE: `run_harness`
                   - MLPERF_NVIDIA_RUN_COMMAND: `run_harness`
                   - CM_CALL_MLPERF_RUNNER: `yes`

        </details>


      * Group "**triton**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_use_triton`
               - ENV variables:
                   - CM_MLPERF_NVIDIA_HARNESS_USE_TRITON: `yes`
                   - CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX3: `using_triton`

        </details>


      * Group "**version**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_v4.0`** (default)
               - ENV variables:
                   - CM_MLPERF_INFERENCE_VERSION: `v4.0`
                   - CM_MLPERF_GPTJ_MODEL_FP8_PATH_SUFFIX: `GPTJ-FP8-quantized`

        </details>


    ##### Default variations

    `_cuda,_num-gpus.1,_resnet50,_run_harness,_tensorrt,_v4.0`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--audio_buffer_num_lines=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_AUDIO_BUFFER_NUM_LINES=value`
    * `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
    * `--deque_timeout_usec=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_DEQUE_TIMEOUT_USEC=value`
    * `--devices=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_DEVICES=value`
    * `--dla_batch_size=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_DLA_BATCH_SIZE=value`
    * `--dla_copy_streams=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_DLA_COPY_STREAMS=value`
    * `--dla_inference_streams=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_DLA_INFERENCE_STREAMS=value`
    * `--embedding_weights_on_gpu_part=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_EMBEDDING_WEIGHTS_ON_GPU_PART=value`
    * `--enable_sort=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_ENABLE_SORT=value`
    * `--end_on_device=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_END_ON_DEVICE=value`
    * `--extra_run_options=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_EXTRA_RUN_OPTIONS=value`
    * `--gpu_batch_size=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE=value`
    * `--gpu_copy_streams=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS=value`
    * `--gpu_inference_streams=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_GPU_INFERENCE_STREAMS=value`
    * `--graphs_max_seqlen=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_GRAPHS_MAX_SEQLEN=value`
    * `--input_format=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_INPUT_FORMAT=value`
    * `--log_dir=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_LOG_DIR=value`
    * `--make_cmd=value`  &rarr;  `MLPERF_NVIDIA_RUN_COMMAND=value`
    * `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
    * `--max_dlas=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_MAX_DLAS=value`
    * `--mlperf_conf=value`  &rarr;  `CM_MLPERF_CONF=value`
    * `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
    * `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
    * `--num_issue_query_threads=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_NUM_ISSUE_QUERY_THREADS=value`
    * `--num_sort_segments=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_NUM_SORT_SEGMENTS=value`
    * `--num_warmups=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_NUM_WARMUPS=value`
    * `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
    * `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`
    * `--performance_sample_count=value`  &rarr;  `CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT=value`
    * `--power_setting=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_POWER_SETTING=value`
    * `--rerun=value`  &rarr;  `CM_RERUN=value`
    * `--run_infer_on_copy_streams=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_RUN_INFER_ON_COPY_STREAMS=value`
    * `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
    * `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
    * `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
    * `--skip_postprocess=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_SKIP_POSTPROCESS=value`
    * `--skip_preprocess=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
    * `--skip_preprocessing=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
    * `--soft_drop=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_SOFT_DROP=value`
    * `--start_from_device=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_START_FROM_DEVICE=value`
    * `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
    * `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
    * `--use_cuda_thread_per_device=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_USE_CUDA_THREAD_PER_DEVICE=value`
    * `--use_deque_limit=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_USE_DEQUE_LIMIT=value`
    * `--use_fp8=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_USE_FP8=value`
    * `--use_graphs=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_USE_GRAPHS=value`
    * `--use_small_tile_gemm_plugin=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_USE_SMALL_TILE_GEMM_PLUGIN=value`
    * `--use_triton=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_USE_TRITON=value`
    * `--user_conf=value`  &rarr;  `CM_MLPERF_USER_CONF=value`
    * `--workspace_size=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_WORKSPACE_SIZE=value`



=== "Default environment"

    #### Default environment


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



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-nvidia/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "reproduce mlcommons mlperf inference harness nvidia-harness nvidia [variations]" [--input_flags] -j
```