# Introduction

This guide will help you run the Nvidia implementation of the MLPerf inference benchmark v3.1 
with BERT-99 model and TensorRT on any Linux-based system with Nvidia GPU (8..16GB min memory required)
and Docker.

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



## Setup CUDA and Docker container

### Download CUDA 11.8

Nvidia recommends the following version of CUDA to be used with their MLPerf inference implementation:

```
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
```

However, you are very welcome to try another version!

### Download cuDNN, TensorRT

For x86 machines, please download the following TAR files:
1. [cuDNN](https://developer.nvidia.com/cudnn) - note that Nvidia recommends `cudnn-linux-x86_64-8.9.2.26_cuda11-archive.tar.xz`
   but you are welcome to try another version
2. [TensorRT](https://developer.nvidia.com/tensorrt) - note that Nvidia recommends `TensorRT-8.6.1.6.Linux.x86_64-gnu.cuda-11.8.tar.gz`
   but you can try another version

Please ask privately in [this Discord server](https://discord.gg/y7hupJsUNb) if you would like to get access 
to an Amazon S3 bucket containing all the needed files to automatically download them for the MLPerf submission. 


### Set up Nvidia Docker container with MLPerf benchmarks

1. [Install Docker](https://docs.docker.com/engine/install/) and [Nvidia container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
     
2. Give Docker permission to the current user
     ```
     sudo usermod -aG docker $USER
     ```
     Logout and login
     Restart docker if required and confirm that Nvidia container toolkit is working by
     ```
     nvidia-ctk --version
     ```

3. Check if Nvidia driver is working properly on the host. 
     ```
     nvidia-smi
     ```
     If the above command produces any error you'll need to install Nvidia drivers on the host. You can do this via CM if you have sudo access
     ```
     cmr "install cuda prebuilt _driver" --version=11.8.0
     ```


4. Build the docker container and mount the paths from the host machine.

    *You may need to change --cuda_run_file_path, --tensorrt_tar_file_path and --cudnn_tar_file_path if you downloaded other versions than recommended by Nvidia.*

    *You may want to change the `scratch_path` location as it can take 100s of GBs.*

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


### Do a test run to detect and record the system performance

```
cmr "generate-run-cmds inference _find-performance _all-scenarios" \
   --model=bert-99 \
   --implementation=nvidia-original \
   --device=cuda \
   --backend=tensorrt \
   --category=edge \
   --division=closed \
   --test_query_count=1000 \
   --quiet
```

### Do full accuracy and performance runs

```
cmr "generate-run-cmds inference _submission _allscenarios" \
   --model=bert-99 \
   --device=cuda \
   --implementation=nvidia-original \
   --backend=tensorrt \
   --execution-mode=valid \
   --results_dir=$HOME/results_dir \
   --category=edge \
   --division=closed \
   --quiet
```

* `--offline_target_qps` and `--singlestream_target_latency` can be used to override the determined performance numbers

### Populate the README files describing your submission

```
cmr "generate-run-cmds inference _populate-readme _all-scenarios" \
   --model=bert-99 \
   --device=cuda \
   --implementation=nvidia-original \
   --backend=tensorrt \
   --execution-mode=valid \
   --results_dir=$HOME/results_dir \
   --category=edge \
   --division=closed \
   --quiet
```

### Generate and upload MLPerf submission

Follow [this guide](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/Submission.md) to generate the submission tree and upload your results.


## Questions? Suggestions?

Don't hesitate to get in touch with the community and organizers 
via [public Discord server](https://discord.gg/JjWNWXKxwT).
