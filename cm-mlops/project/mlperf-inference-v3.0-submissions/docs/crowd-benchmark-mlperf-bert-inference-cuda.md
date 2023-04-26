# Crowd-benchmarking MLPerf BERT inference

<details>
<summary>Click here to see the table of contents.</summary>

* [Crowd-benchmarking MLPerf BERT inference](#crowd-benchmarking-mlperf-bert-inference)
* [System preparation](#system-preparation)
  * [Minimal system requirements](#minimal-system-requirements)
  * [Install CM (CK2) automation meta-framework](#install-cm-ck2-automation-meta-framework)
  * [Pull CM repository with portable automation recipes](#pull-cm-repository-with-portable-automation-recipes)
  * [Detect or install CUDA](#detect-or-install-cuda)
    * [Test CUDA installation](#test-cuda-installation)
  * [Install Python virtual environment](#install-python-virtual-environment)
  * [Detect or install cuDNN](#detect-or-install-cudnn)
  * [Detect or install TensorRT](#detect-or-install-tensorrt)
  * [Run MLPerf inference benchmark with BERT](#run-mlperf-inference-benchmark-with-bert)
    * [Try ONNX runtime backend](#try-onnx-runtime-backend)
      * [Do a test run to detect and record the system performance](#do-a-test-run-to-detect-and-record-the-system-performance)
      * [Do a full accuracy run for all the scenarios](#do-a-full-accuracy-run-for-all-the-scenarios)
      * [Do a full performance run for all the scenarios](#do-a-full-performance-run-for-all-the-scenarios)
      * [Populate the README files](#populate-the-readme-files)
      * [Generate MLPerf submission tree](#generate-mlperf-submission-tree)
      * [Push the results to GitHub repo](#push-the-results-to-github-repo)
    * [Try PyTorch backend](#try-pytorch-backend)
  * [Test composable ML benchmark with other models, data sets, frameworks and platforms](#test-composable-ml-benchmark-with-other-models-data-sets-frameworks-and-platforms)
* [The next steps](#the-next-steps)

</details>


This is a pilot community project to collaboratively run MLPerf BERT inference benchmark
across diverse platforms provided by volunteers similar to [SETI@home](https://setiathome.berkeley.edu/).
However, instead of searching for extraterrestrial intelligence, we are 
searching for optimal software/hardware combination to run various AI and ML workloads
in terms of performance, accuracy, power and costs ...

This benchmark is composed from [portable and reusable automation recipes](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md)
developed by [MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md) 
to modularize complex AI and ML Systems and automate their benchmarking, design space exploration, optimization and deployment
across continuously evolving software, hardware, models and data.

*If you submit your results before 1pm PST on Friday 3rd, 2023, 
 they will be accepted for the official MLPerf inference v3.0 submission round
 and your name acknowledged in the notes!*


# System preparation

## Minimal system requirements

* CPU: any x86-64 or Arm64 based machine
* GPU: any relatively modern Nvidia GPU with 8GB+ memory and CUDA 11.4+
* OS: we have tested this automation on Ubuntu 20.04, Ubuntu 22.04 and Debian 10
* Disk space: ~10GB
* Python: 3.8+
* All other dependencies (artifacts and tools) will be installed by the CM meta-framework aka (CK2)

## Install CM (CK2) automation meta-framework

Follow [this guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md) to install the [MLCommons CM framework](https://github.com/mlcommons/ck)
(the 2nd generation on the Collective Mind framework) on your system.

## Pull CM repository with portable automation recipes

Pull MLCommons CM repository with [cross-platform CM scripts](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md)
supporting portable MLOps and DevOps:

```bash
cm pull repo mlcommons@ck
```

CM pulls all such repositories into the `$HOME/CM` directory to search for portable CM automation recipes and artifacts.

We use the unified CM CLI & Python API of [portable and reusable CM scripts](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md)
to compose portable automation pipelines (also implemented as CM scripts) that can automatically detect or install all necessary artifacts (tools, models, datasets, libraries, etc) 
required to run a given software project such as the MLPerf inference benchmark.

These CM scripts simply wrap existing native scripts and tools as simple micro-services
with a human-readable CLI and simple Python API to be able to easily connect them together 
and run on any platform in a unified way.

## Detect or install CUDA 

Run the following CM script:
```bash
cm run script "get cuda" --out=json
```

If CUDA is automatically detected, it will be registered in the CM cache:
```bash
cm show cache --tags=get,cuda
```

Otherwise, this script will attempt to download and install the latest CUDA 
from Nvidia website.

Please report any issue with CM scripts [here](https://github.com/mlcommons/ck/issues).
Also join our [Discord server](https://discord.gg/JjWNWXKxwT) if you have any questions or suggestions.

### Test CUDA installation

You can test if CUDA toolkit and driver was detected or installed successfully using the following command:
```bash
cm run script "get cuda-devices"
```

You should see similar output:
```txt
Checking compiler version ...

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Wed_Sep_21_10:33:58_PDT_2022
Cuda compilation tools, release 11.8, V11.8.89
Build cuda_11.8.r11.8/compiler.31833905_0

Compiling program ...

Running program ...

  - Running postprocess ...
GPU Device ID: 0
GPU Name: Tesla K80
GPU compute capability: 3.7
CUDA driver version: 11.4
CUDA runtime version: 11.8
Global memory: 11997020160
Max clock rate: 823.500000 MHz
Total amount of shared memory per block: 49152
Total number of registers available per block: 65536
Warp size: 32
Maximum number of threads per multiprocessor:  2048
Maximum number of threads per block: 1024
Max dimension size of a thread block X: 1024
Max dimension size of a thread block Y: 1024
Max dimension size of a thread block Z: 64
Max dimension size of a grid size X: 2147483647
Max dimension size of a grid size Y: 65535
Max dimension size of a grid size Z: 65535

  - running time of script "get,cuda-devices": 4.16 sec.

```

## Install Python virtual environment

```bash
cm run script "get sys-utils-cm" --quiet

cm run script "install python-venv" --name=mlperf-cuda
```

If you want to install specific version of Python use the following command:
```bash
cm run script "install python-venv" --version=3.10.8  --name=mlperf-cuda
```

## Detect or install cuDNN

```bash
cm run script "get cudnn"
```

If cuDNN is not detected on your system, you can download a TAR file
from [Nvidia website](https://developer.nvidia.com/cudnn) and then use the same CM script
to install it as follows:
```bash
cm run script "get cudnn" --tar_file=<FULL PATH TO DOWNLOADED TAR FILE WITH CUDNN>
```

We have tested this project with the following tar file `cudnn-linux-x86_64-8.7.0.84_cuda11-archive.tar.xz`.

## Detect or install TensorRT

```bash
cm run script "get tensorrt"
```
If TensorRT is not detected on your system, you can download a TAR file
from [Nvidia website](https://developer.nvidia.com/tensorrt) and then use the same CM script
to install it as follows:
```bash
cm run script "get tensorrt" --tar_file=<FULL PATH TO DOWNLOADED TAR FILE WITH TENSORRT>
```

We have tested this project with the following tar file `TensorRT-8.5.1.7.Linux.x86_64-gnu.cuda-11.8.cudnn8.6.tar.gz`.


## Run MLPerf inference benchmark with BERT

### Try ONNX runtime backend

#### Do a test run to detect and record the system performance

```bash
cm run script --tags=generate-run-cmds,inference,_find-performance,_all-scenarios \
    --adr.python.name=mlperf-cuda --model=bert-99 --implementation=reference \
    --device=cuda --backend=onnxruntime --quiet
```

#### Do a full accuracy run for all the scenarios

```bash
cm run script --tags=generate-run-cmds,inference,_accuracy-only,_all-scenarios \
    --adr.python.name=mlperf-cuda --model=bert-99 --device=cuda \
    --implementation=reference --backend=onnxruntime --quiet \
    --execution-mode=valid --results_dir=$HOME/inference_3.0_results
```

#### Do a full performance run for all the scenarios

```bash
cm run script --tags=generate-run-cmds,inference,_performance-only,_all-scenarios \
    --adr.python.name=mlperf-cuda --model=bert-99 --device=cuda \
    --implementation=reference --backend=onnxruntime --quiet \
    --execution-mode=valid --results_dir=$HOME/inference_3.0_results
```

#### Populate the README files

```bash
cm run script --tags=generate-run-cmds,inference,_populate-readme,_all-scenarios \
    --adr.python.name=mlperf-cuda --model=bert-99 --device=cuda \
    --implementation=reference --backend=onnxruntime --quiet \
    --execution-mode=valid --results_dir=$HOME/inference_3.0_results
```

#### Generate MLPerf submission tree

We should use the master branch of MLCommons inference repo for the submission checker. 
You can use `--hw_note_extra` option to add your name to the notes.

```bash
cm run script --tags=generate,inference,submission \
    --results_dir=$HOME/inference_3.0_results/valid_results \
    --adr.python.name=mlperf-cuda \
    --device=cuda --submission_dir=$HOME/inference_submission_tree --clean  \
    --run-checker --submitter=cTuning --adr.inference-src.version=master 
    --hw_notes_extra="Result taken by <YOUR NAME>" --quiet
```

#### Push the results to GitHub repo

First create a fork of [this GitHub repo with aggregated results](https://github.com/ctuning/mlperf_inference_submissions_v3.0). 
Then run the following command after replacing `--repo_url` with your fork URL.

```bash
cm run script --tags=push,github,mlperf,inference,submission \
    --submission_dir=$HOME/inference_submission_tree \
    --adr.python.name=mlperf-cuda \
    --repo_url=https://github.com/ctuning/mlperf_inference_submissions_v3.0 \
    --commit_message="Bert crowd-results added"
```

Create a PR to the [GitHub repo with aggregated results](https://github.com/ctuning/mlperf_inference_submissions_v3.0/)



### Try PyTorch backend

You can run the same commands with PyTorch by rerunning all above commands and replacing `--backend=onnxruntime` with `--backend=pytorch`. 

For example,

```bash
cm run script --tags=generate-run-cmds,inference,_accuracy-only,_all-scenarios \
    --adr.python.name=mlperf-cuda --model=bert-99 --device=cuda \
    --implementation=reference --backend=pytorch --execution-mode=valid \
    --results_dir=$HOME/inference_3.0_results --quiet
```


## Test composable ML benchmark with other models, data sets, frameworks and platforms

* [GUI to prepare CM command line and run benchmark](https://cknowledge.org/mlperf-inference-gui)
* [GUI to compare performance, accuracy, power and costs of ML/SW/HW combinations](https://cKnowledge.org/cm-gui-graph)
 

# The next steps

Feel free to join our [open taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
and the public [Discord server](https://discord.gg/JjWNWXKxwT) to learn about our roadmap and related community projects.

Our ultimate goal is to help anyone automatically find or generate the optimal software/hardware stack from the cloud to the edge
for their AI/ML tasks based on their requrements and constraints (accuracy, performance, power consumption, costs, etc).

*Prepared by [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) and [Grigori Fursin](https://cKnowledge.org/gfursin) (OctoML, MLCommons, cTuning foundation)*
