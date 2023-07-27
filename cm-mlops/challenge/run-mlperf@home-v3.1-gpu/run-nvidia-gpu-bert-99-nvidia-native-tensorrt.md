# Introduction

This guide will help you run the Nvidia implementation of the MLPerf inference benchmark v3.1 
with BERT-99 model and TensorRT on any Linux-based system with Nvidia GPU (8..16GB min memory required)
in a native environment.

This benchmark is semi-automated by the [MLCommons CM language](https://doi.org/10.5281/zenodo.8105339) 
and you should be able to submit official MLPerf v3.1 inference results
for all scenarios in closed division and edge category
(**deadline to send us results for v3.1 submission: August 3, 2023**).


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
cm run script "install python-venv" --name=mlperf --version_min=3.8
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```

CM will install a new Python virtual environment in CM cache and will install all Python dependencies there:
```bash
cm show cache --tags=python-venv
```

Note that CM downloads and/or installs models, data sets, packages, libraries and tools in this cache.

You can clean it at any time and start from scratch using the following command:
```bash
cm rm cache -f
```

Alternatively, you can remove specific entries using tags:
```bash
cm show cache
cm rm cache --tags=tag1,tag2,...
```





## Setup CUDA and build MLPerf Nvidia inference benchmarks

1. We expect that CUDA driver 11+ is already installed on your system.
   However, even if it is not, any CM script with CUDA depedency should automatically
   download and install it using this [portable CM script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda).

   Note that Nvidia suggests to use CUDA toolkit 11.8 to run Nvidia implementations of MLPerf inference benchmarks.

2. Install cuDNN (x86 host)

   Download [cuDNN for CUDA 11](https://developer.nvidia.com/cudnn) and install it via CM (note that Nvidia recommends `cudnn-linux-x86_64-8.9.2.26_cuda11-archive.tar.xz`):
    
    ```bash
      cmr "get cudnn" --input=<PATH_TO_CUDNN_TAR_FILE>
    ```

3. Install TensorRT (x86 host)

    Download any [TensorRT](https://developer.nvidia.com/tensorrt) and install it via CM (note that Nvidia recommends `TensorRT-8.6.1.6.Linux.x86_64-gnu.cuda-11.8.tar.gz`):
    
    ```bash
      cmr "get tensorrt _dev" --input=<PATH_TO_TENSORRT_TAR_FILE>
    ```
    On non x86 systems such as Nvidia Orin, you can use a package manager install and then CM should automatically pick up this installation during any workflow run.

4. Build the Nvidia MLPerf benchmark with inference server 

    *You may need to change --cuda_run_file_path, --tensorrt_tar_file_path and --cudnn_tar_file_path if you downloaded other versions than recommended by Nvidia.*

    
    ```
      cmr "build nvidia inference server" \
         --adr.install-cuda-prebuilt.local_run_file_path=/data/cuda_11.8.0_520.61.05_linux.run \
         --adr.tensorrt.tar_file=/data/TensorRT-8.6.1.6.Linux.x86_64-gnu.cuda-11.8.tar.gz \
         --adr.cudnn.tar_file=/data/cudnn-linux-x86_64-8.9.2.26_cuda11-archive.tar.xz \
         --adr.compiler.tags=gcc
      ```

5. At the end of the build you'll get a prompt - please enter your system name such as "aws_nvidia_t4" 
   (note that space, `-` and other special characters are not allowed),
   and say `yes` to generating the configuration files.

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
    Now you'll be inside the CM Nvidia docker container and can access Nvidia implementations of MLPerf inference benchmarks.

6. Once the build is complete, you can run Nvidia implementations of MLPerf inference benchmarks
   using the unified CM interface.

   You can also save the container at this stage using [Docker commit](https://docs.docker.com/engine/reference/commandline/commit/) 
   so that it can be launched later without having to go through the previous steps.




## Questions? Suggestions?

Don't hesitate to get in touch with the community and organizers 
via [public Discord server](https://discord.gg/JjWNWXKxwT).
