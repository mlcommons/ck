# CM demo: modularizing MLPerf benchmarks and automating submissions

This tutorial demonstrates how to use the [MLCommons Collective Mind toolkit (CM)](https://github.com/mlcommons/ck) 
being developed by the [open education workgroup](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
to make it easier to run [MLPerf inference benchmark](https://github.com/mlcommons/inference)
and automate submissions across diverse ML models, data sets, engines and platforms.

Our goal is to develop a simple workflow management meta-framework that can be convenient for both researchers and engineers 
to design, benchmark, optimize and deploy complex AI and ML systems across rapidly evolving 
software and hardware from the cloud to the edge (see [CM motivation](../cm/docs/motivation.md) for more details).

CM is the next generation of the MLCommons Collective Knowledge framework donated to MLCommons 
by the [cTuning foundation](https://cTuning.org) and [OctoML](https://octoml.ai) 
after being successfully used to automate MLPerf inference benchmark submissions 
from different organizations including Qualcomm, Krai, HPE, Lenovo, Dell and Alibaba.

CM helps to decompose complex software projects into a database of [portable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
that can automatically detect, download and install all required artifacts, packages and tools 
on any platform in a unified way.

All CM scripts have a human-friendly CLI, unified Python API and extensible JSON/YAML meta descriptions 
that turn ad-hoc and platform-specific scripts and artifacts into reusable components 
adaptable to any platform.

CM scripts can be automatically chained together into portable automation workflows, applications
and web-services using simple [JSON/YAML description](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.json) 
or traditional [Python scripting](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-ml-model-resnet50-onnx/customize.py#L22).

This combination of the human-friendly CLI and JSON/YAML descriptions combined with low-level Python scripting 
is intended to make CM easier to use and extend by both researchers and engineers.

## Install CM toolkit

The CM toolkit requires minimal dependencies: Python 3+, Python PIP and a Git client. 

CM will then automatically install all other dependencies and artifacts into a local CM repository
to bootstrap any given workflow (such as MLPerf benchmark) without even intefering with the system setup!

Here is a typical minimal CM setup on Ubuntu:

```bash
sudo apt-get install python3 python3-pip git wget
python3 -m pip install cmind
```

Note that sometimes you may need to log out from your shell and then log back 
to update the PATH to the "cm" front-end:
```bash
grigori@mlperf:~$ cm version
v0.7.24
```
Please check the [CM installation guide](https://github.com/mlcommons/ck/blob/master/cm/docs/installation.md) 
to install CM on other platforms including Windows and MacOS.

## Install CM repository with MLPerf automations

You can now pull a [GitHub repository with reusable CM components for MLPerf](https://github.com/mlcommons/ck/tree/master/cm-mlops) 
as follows:

```bash
cm pull repo mlcommons@ck
```

You can list all portable and reusable CM scripts to modularize and automate MLPerf as follows:
```bash
cm list script | sort
```

```
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/app-image-classification-onnx-cpp
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/app-image-classification-onnx-py
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/app-image-classification-torch-py
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/app-image-classification-tvm-onnx-py
...
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/build-docker-image
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/detect-os
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/generate-mlc-inference-submission
...
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-bazel
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-cmake
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-imagenet-val
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-ml-model-resnet50-onnx
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-ml-model-resnet50-pytorch
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-ml-model-resnet50-tf
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-ml-model-resnext50
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-mlc-inference-src
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-onnxruntime
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-openimages-original
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-python3
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-pytorch
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-sut
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-sut-mlc-configs
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-sys-utils-cm
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-tensorflow
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-transformers
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/get-tvm
...
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/install-llvm-prebuilt
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/install-pytorch
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/install-tensorflow
...
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/run-accuracy-imagenet
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/run-docker-container
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/run-mlc-accuracy-truncation
/home/grigori/CM/repos/mlcommons@ck/cm-mlops/script/run-mlc-submission-checker

```

## Run MLPerf inference

### Vision benchmark - ResNet-50 - ImageNet 100 images - ONNX - offline - accuracy

You can now run the MLPerf vision benchmark r2.1 with default parameters 
(reduced ImageNet with 100 original images, ResNet-50 model in ONNX format, 
ONNX runtime, offline MLPerf scenario and accuracy mode)
using the following CM command:

```bash
cm run script --tags=app,mlperf,inference,reference,python,_resnet50,_onnxruntime,_cpu,_r2.1_default --quiet
```

CM will automatically search for a portable CM script using above tags in all CM repositories 
installed on your system (this allows one to easily combine public and private automation scripts and artifacts)
and will run it according to its human readable meta description provided in either *_cm.json*
or *_cm.yaml* file as shown [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json).

It may take a few minutes to automatically detect, download and/or install all necessary ML components
required for this CM workflow (which is also a portable CM script with 
[dependencies on other CM scripts](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json#L5))
depending on the speed of your Internet connection.

Note that CM will automatically cache CM scripts during the first run!
This means that when you run the MLPerf benchmark again using CM,
it will automatically reuse cached components instead of downloading and installing them!

You can see all cached CM components using the following command:
```bash
cm show cache
```

You can also see some specific cached CM components such as ML models as follows:
```bash
cm show cache --tags=ml-model
```

## Clean CM cache (optional)

In case you need to perform a "clean" run without cached components, you can clean the whole cache as follows:
```bash
cm rm cache -f
```

Or you can clean the cache for specific CM components such as datasets as follows:
```bash
cm rm cache -f --tags=dataset
```

This will force CM to download and/or reinstall required components during the subsequent run of a given workflow.

## Customize MLPerf workflow

TBD

--add_deps_recursive.compiler.tags=gcc

## Run MLPerf inference with different tasks, models and engines

### Vision benchmark - ResNet-50 - ImageNet 100 images - ONNX - offline - performance

### Vision benchmark - RetinaNet - Open Images - ONNX - offline - accuracy

### Vision benchmark - ResNet-50 - ImageNet 100 images - TVM - offline - accuracy


## Automate MLPerf submission


## The next steps

Please feel free to follow the [MLCommons CM project](https://github.com/mlcommons/ck),
check the [CM tutorial about portable CM scripts](../cm/docs/tutorial-scripts.md) 
and join our [open education workgroup](mlperf-education-workgroup.md) 
to participate in this community project.

