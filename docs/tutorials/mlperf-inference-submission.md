[ [Back to index](../README.md) ]

# Tutorial: running the MLPerf inference benchmark and preparing the submission

<details>
<summary>Click here to see the table of contents.</summary>

* [Tutorial: running the MLPerf inference benchmark and preparing the submission](#tutorial-running-the-mlperf-inference-benchmark-and-preparing-the-submission)
* [Introduction](#introduction)
* [System preparation](#system-preparation)
  * [Minimal system requirements](#minimal-system-requirements)
  * [CM installation](#cm-installation)
  * [Pull CM repository with cross-platform MLOps and DevOps scripts](#pull-cm-repository-with-cross-platform-mlops-and-devops-scripts)
  * [Optional: update CM and repository to the latest version](#optional-update-cm-and-repository-to-the-latest-version)
  * [Install system dependencies for your platform](#install-system-dependencies-for-your-platform)
  * [Use CM to detect or install Python 3.8+](#use-cm-to-detect-or-install-python-38)
  * [Install Python virtual environment with above Python](#install-python-virtual-environment-with-above-python)
  * [Customize and run the MLPerf inference benchmark](#customize-and-run-the-mlperf-inference-benchmark)
  * [Debug the MLPerf benchmark](#debug-the-mlperf-benchmark)
  * [Customize MLPerf benchmark](#customize-mlperf-benchmark)
    * [Implementations](#implementations)
    * [Device](#device)
      * [CPU](#cpu)
      * [CUDA](#cuda)
    * [Backend (ML framework)](#backend-ml-framework)
      * [Deepsparse](#deepsparse)
      * [ONNX runtime CPU](#onnx-runtime-cpu)
      * [ONNX runtime CUDA](#onnx-runtime-cuda)
      * [PyTorch CPU](#pytorch-cpu)
      * [PyTorch CUDA](#pytorch-cuda)
      * [TensorFlow (Python)](#tensorflow-python)
      * [TensorFlow from source](#tensorflow-from-source)
      * [TensorFlow Lite](#tensorflow-lite)
      * [TensorRT](#tensorrt)
      * [TVM ONNX (Python)](#tvm-onnx-python)
    * [Datasets](#datasets)
    * [Power measurements](#power-measurements)
  * [Prepare submission](#prepare-submission)
* [The next steps](#the-next-steps)
* [Authors](#authors)
* [Acknowledgments](#acknowledgments)

</details>

# Introduction

This tutorial briefly explains how to run a modular version of the [MLPerf inference benchmark](https://arxiv.org/abs/1911.02549)
using the [cross-platform automation meta-framework (MLCommons CM aka CK2)](https://github.com/mlcommons/ck) 
with a simple [GUI](https://cKnowledge.org/mlperf-inference-gui)
and prepare your submission.

Please follow [this CM tutorial from the Student Cluster Competition](sc22-scc-mlperf.md) for more details.

If you have questions, encounter issues or have feature requests, please submit them [here](https://github.com/mlcommons/ck/issues)
and feel free to join our [open taskforce on automation and reproducibility](../taksforce.md)
and [Discord discussions](https://discord.gg/JjWNWXKxwT).*

# System preparation

## Minimal system requirements

* Device: CPU (x86-64 or Arm64) or GPU (Nvidia)
* OS: we have tested CM automations on Ubuntu 20.04, Ubuntu 22.04, Debian 10, Red Hat 9 and MacOS 13
* Disk space: 
  - test runs: minimal preprocessed datasets < ~5GB
  - otherwise depends on a task and a dataset. Sometimes require 0.3 .. 3TB
* Python: 3.8+
* All other dependencies (artifacts and tools) will be installed by the CM meta-framework


## CM installation

Follow [this guide](../installation.md) to install the MLCommons CM framework (CK2) on your system.

After the installation, you should be able to access the CM command line as follows:

```bash
$ cm

cm {action} {automation} {artifact(s)} {--flags} @input.yaml @input.json
```

## Pull CM repository with cross-platform MLOps and DevOps scripts

Pull stable MLCommons CM repository with [cross-platform CM scripts for modular ML Systems](../list_of_scripts.md):

```bash
cm pull repo mlcommons@ck
```

CM pulls all such repositories into the `$HOME/CM` directory to search for CM automations and artifacts.
You can find the location of a pulled repository as follows:

```bash
cm find repo mlcommons@ck
```

You can also pull a stable version of this CM repository using some checkout:

```bash
cm pull repo mlcommons@ck --checkout=...
```

You can now use the unified CM CLI/API of [reusable and cross-platform CM scripts](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md))
to detect or install all artifacts (tools, models, datasets, libraries, etc) 
required for a given software project (MLPerf inference benchmark in our case).

Conceptually, these scripts take some environment variables and files as an input, perform a cross-platform action (detect artifact, download files, install tools),
prepare new environment variables and cache output if needed.

Note that CM can automatically detect or install all dependencies for a given benchmark and run it on a given platform in just one command
using a simple [JSON or YAML description of dependencies on all required CM scripts](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference/_cm.yaml#L61).

However, since the goal of this tutorial is to explain you how we modularize MLPerf and any other benchmark, 
we will show you all individual CM commands to prepare and run the MLPerf inference benchmark. 
You can reuse these commands in your own projects thus providing a common interface for research projects.

In the end, we will also show you how to run MLPerf benchmark in one command from scratch.

## Optional: update CM and repository to the latest version

Note that if you already have CM and mlcommons@ck repository installed on your system,
you can update them to the latest version at any time and clean the CM cache as follows:

```bash
python3 -m pip install cmind -U
cm pull repo mlcommons@ck --checkout=master
cm rm cache -f
```

## Install system dependencies for your platform

We suggest you to install system dependencies required by the MLPerf inference benchmark using CM
(requires SUDO access).

For this purpose, we have created a cross-platform CM script that will automatically install 
such dependencies based on your OS (Ubuntu, Debian, Red Hat, MacOS ...). 

In this case, CM script serves simply as a wrapper with a unified and cross-platform interface
for native scripts that you can find and extend [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
if some dependencies are missing on your machine - this is a collaborative way to make 
CM scripts portable and interoperable.

You can run this CM scripts as follows (note that you may be asked for a SUDO password on your platform):

```bash
cm run script "get sys-utils-cm" --quiet
```

If you think that you have all system dependencies installed,
you can run this script with a `--skip` flag:
```bash
cm run script "get sys-utils-cm" --skip
```


## Use CM to detect or install Python 3.8+

Since we use Python reference implementation of the MLPerf inference benchmark (unoptimized),
we need to detect or install Python 3.8+ (MLPerf requirement). 

You need to detect it using the following [CM script](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md#get-python3):

```bash
cm run script "get python" --version_min=3.8
```

## Install Python virtual environment with above Python

```bash
cm run script "install python-venv" --name=mlperf --version_min=3.8
```

You can change the name of your virtual Python environment using `--name` flag.

## Customize and run the MLPerf inference benchmark

You can use this [online GUI](https://cKnowledge.org/mlperf-inference-gui) to generate CM commands
to customize and run the MLPerf inference benchmark. You can select different implementations, models, data sets,
frameworks and parameters and then copy/paste the final commands to your shell to run MLPerf.

Alternatively, you can use your own local GUI to run this benchmark as follows:
```bash
cm run script --tags=gui \
     --script="app generic mlperf inference" \
     --prefix="gnome-terminal --"
```

You may just need to substitute `gnome-terminal --` with a command line that opens a new shell on your OS.

CM will attempt to automatically detect or download and install the default versions of all required ML components.

## Debug the MLPerf benchmark

You can add flag `--debug` to CM command to let CM stop just before running a given MLPerf benchmark, open a shell
and let you run/customize benchmark manually from command line while reusing environment variables and tools prepared by CM.

## Customize MLPerf benchmark

### Implementations

The community provided a unified CM API for the following implementations of the MLPerf inference benchmark:
* [Python reference implementation (CPU and CUDA)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)
  * See the current coverage [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-reference/README-extra.md) 
    and please help us test different combinations of models, frameworks and platforms (i.e. collaborative design space exploration)!
* [Universal C++ implementation (CPU and CUDA)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp)
  * Check our [community projects](https://github.com/mlcommons/ck/issues/627) to extend this and other implementations.
* [TFLite C++ implementation (CPU)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp)
* [Nvidia's implementation (CPU and CUDA)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-nvidia)

We are also working on a [light-weight universal script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python) 
to benchmark performance of any ML model with MLPerf loadgen without accuracy.

If you want to add your own implementation or backend, the simplest solution is to create a fork of the 
[MLPerf inference GitHub repo](https://github.com/mlcommons/inference),
specify this repo in the above GUI in the fields `Git URL for MLPerf inference sources to build LoadGen` and `Git URL for MLPerf inference sources to run benchmarks`
and update the [CM meta description](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference/_cm.yaml) of our MLPerf wrapper.

Don't hesitate to get in touch with [this taksforce](../taksforce.md)
to get free help from the community to add your implementation and prepare the submission.


### Device

#### CPU

We have tested out-of-the-box CM automation for the MLPerf inference benchmark across diverse x86-64-based platforms (Intel and AMD)
as well as Arm64-based machines from RPi4 to AWS Graviton.

#### CUDA

As a minimum requirement, you should have CUDA installed. It can be detected using CM as follows:
```bash
cm run script "get cuda"
```

We suggest you to install cuDNN and TensorRT too.

If it's not installed, you can use CM scripts to install them as follows:

```bash
cm run script --tags=get,cudnn --tar_file=<PATH_TO_CUDNN_TAR_FILE>
```

```bash
cm run script --tags=get,tensorrt --tar_file=<PATH_TO_TENSORRT_TAR_FILE>
```

### Backend (ML framework)

You can install specific versions of various backends using CM as follows (optional):

#### Deepsparse

See [this PR](https://github.com/mlcommons/ck/pull/619) prepared by the [open taskforce](../taksforce.md) 
during the public hackathon to add Neural Magic's Deepsparse BERT backend for MLPerf to the CM automation.

*We currently support BERT large model int 8 targeting CPU only. CUDA may come soon...*


#### ONNX runtime CPU

```bash
cm run script "get generic-python-lib _onnxruntime" (--version=...)
```

#### ONNX runtime CUDA

```bash
cm run script "get generic-python-lib _onnxruntime_gpu" (--version=...)
```

#### PyTorch CPU

```bash
cm run script "get generic-python-lib _torch" (--version=...)
```

#### PyTorch CUDA

```bash
cm run script "get generic-python-lib _torch_cuda" (--version=...)
```

#### TensorFlow (Python)

```bash
cm run script "get generic-python-lib _tensorflow" (--version=...)
```

#### TensorFlow from source

```bash
cm run script "get tensorflow from-src" (--version=...)
```

#### TensorFlow Lite

```bash
cm run script "get tensorflow from-src _tflite" (--version=...)
```

#### TensorRT

```bash
cm run script --tags=get,tensorrt (--tar_file=<PATH_TO_DOWNLOADED_TENSORRT_PACKAGE_FILE>)
```

#### TVM ONNX (Python)

```bash
cm run script "get generic-python-lib _apache-tvm" (--version=...)
```


### Datasets

* [ImageNet](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md)
* [Open Images](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
* [Squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
* [Criteo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-criteo)
* [Kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-kits19)
* [Libris Speech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-librispeech)


### Power measurements

Please follow [this tutorial](mlperf-inference-power-measurement.md) to run MLPerf with power measurements using CM.


## Prepare submission

You can use this [online GUI](https://cKnowledge.org/mlperf-inference-submission-gui) to generate CM commands
to run the MLPerf inference benchmark, generate your submission and add your results to a temporal W&B dashboard. 

Alternatively, you can use your own local GUI to run this benchmark as follows:
```bash
cm run script --tags=gui \
     --script="run mlperf inference generate-run-cmds" \
     --prefix="gnome-terminal --"
```


# The next steps

You are welcome to join the [open MLCommons taskforce on automation and reproducibility](../taksforce.md)
to contribute to this project and continue optimizing this benchmark and prepare an official submission 
for MLPerf inference benchmarks with the free help of the community.

See the development roadmap [here](https://github.com/mlcommons/ck/issues/536).

# Authors

* [Grigori Fursin](https://cKnowledge.org/gfursin) (cTuning foundation and cKnowledge.org)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) (cTuning foundation and cKnowledge.org)

# Acknowledgments

We thank 
[Hai Ah Nam](https://www.nersc.gov/about/nersc-staff/advanced-technologies-group/hai-ah-nam),
[Steve Leak](https://www.linkedin.com/in/steve-leak),
[Vijay Janappa Reddi](https://scholar.harvard.edu/vijay-janapa-reddi/home),
[Tom Jablin](https://scholar.google.com/citations?user=L_1FmIMAAAAJ&hl=en),
[Ramesh N Chukka](https://www.linkedin.com/in/ramesh-chukka-74b5b21),
[Peter Mattson](https://www.linkedin.com/in/peter-mattson-33b8863/),
[David Kanter](https://www.linkedin.com/in/kanterd),
[Pablo Gonzalez Mesa](https://www.linkedin.com/in/pablo-gonzalez-mesa-952ab2207),
[Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189),
[Thomas Schmid](https://www.linkedin.com/in/tschmid)
and [Gaurav Verma](https://www.linkedin.com/in/grverma)
for their suggestions and contributions.
