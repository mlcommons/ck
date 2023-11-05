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

