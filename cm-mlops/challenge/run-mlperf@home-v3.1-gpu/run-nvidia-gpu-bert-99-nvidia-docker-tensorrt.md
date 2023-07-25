# Introduction

This guide will help you automatically run the Nvidia implementation of the MLPerf inference benchmark v3.1 
with BERT-99 model and TensorRT on any Linux-based system with Nvidia GPU (8..16GB min memory required)
and Docker.

This benchmark is automated by the MLCommons CM language and you should be able to submit official MLPerf v3.1 inference results
for all scenarios in closed division and edge category.

It will require ~30GB of disk space and can take ~2 hours to run on 1 system.


## Install CM automation language

Install the [MLCommons CM automation language](https://doi.org/10.5281/zenodo.8105339) as described in this [guide](../../../docs/installation.md). 
It is a small Python library with `cm` and `cmr` command line front-ends and minimal dependencies including Python 3+, Git and wget.

If you encounter problems, please report them at [GitHub](https://github.com/mlcommons/ck/issues).


## Install repository with CM automations

Install the MLCommons repository with [reusable and portable automation recipes (CM scripts)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) via CM.
These scripts are being developed and shared by the community and MLCommons under Apache 2.0 license 
to enable portable, modular, and technology-agnostic benchmarks and applications 
that can automatically run with any software, hardware, models and data sets.

```bash
cm pull repo mlcommons@ck
```

You can run it again at any time to pick up the latest updates.

Note that CM will store all such repositories and downloaded/installed data sets, models and tools
in your `$HOME/CM` directory. 

Since MLPerf benchmarks require lots of space (somethings hundreds of Gigabytes), 
you can change the above location to some large scratch disk using `CM_REPOS` 
environment variable as follows:

```bash
export CM_REPOS={new path to CM repositories and data}
echo "CM_REPOS=${CM_REPOS} >> $HOME/.bashrc"
cm pull repo mlcommons@ck
```



## Setup virtual environment

We suggest you to setup a Python virtual environment via CM to avoid contaminating your existing Python installation:

```bash
cm run script "install python-venv" --name=crowd-mlperf
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=crowd-mlperf"
```

CM will install a new Python virtual environment in CM cache and will install all Python dependencies there:
```bash
cm show cache
```

## Download the needed files

* Please ask privately in [this discord channel](https://discord.gg/y7hupJsUNb) if you would like to get access to an Amazon S3 bucket containing all the needed files for easiness. Otherwise, you can download them from the below links.
  
For x86 machines, please download the latest install tar files from the below sites
1. [cuDNN](https://developer.nvidia.com/cudnn) (for cuda 11)
2. [TensorRT](https://developer.nvidia.com/tensorrt)

<details>

<summary>
    
## Setup docker

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




