# Introduction

This guide will help you automatically run the Nvidia implementation of the MLPerf inference benchmark v3.1 
with BERT-99 model and TensorRT on any Linux-based system with Nvidia GPU (8..16GB min memory required)
in a native environment.

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
