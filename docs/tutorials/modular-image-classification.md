[ [Back to index](../README.md) ]

# Trying CM: modular image classification

This example demonstrates our unified and human-readable CM interface to run 
image classification on any platform while automatically detecting or installing 
all related artifacts and adapting them to your environment.

This interface is being developed by the [open taskforce](../taksforce.md) 
to solve the dependency hell and make it easier for the community to run, customize and reuse 
any software projects in native environments or containers in a unified way.

## Install CM

Please follow this [guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
to install the CM tool on your platform.

## Run modular image classification via CM interface

Here is an example of a modular image classification assembled from 
([reusable and portable CM scripts (that simply wrap native scripts and tools)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)).
using a [human-readable YAML file](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L19).

CM will read this YAML (or JSON) description, go through all dependencies on other CM scripts, and attempt to automatically detect, download, install and build all related artifacts 
and tools to adapt this example to a user platform with Linux, Windows or MacOS.

First you need to install a CM repository with these portable and reusable scripts as follows:

```bash
cm pull repo mlcommons@ck
```

You can then run a CM script implementing modular image classification as follows:

```bash
cm run script --tags=app,image-classification,onnx,python --quiet
```

Note that you can also access CM from Python using just one unified function `cmind.access` similar to micro-services:

```python
import cmind
r=cmind.access({'action':'run', 'automation':'script'
                'tags':'app,image-classification,onnx,python',
                'out':'con',
                'quiet':True})
print (r)
```

It may take a few minutes to run this CM script for the first time and adapt it to your platform depending on your Internet speed.

Note that all the subsequent runs will be much faster because CM automatically caches the output of all portable CM scripts 
to be quickly reused in this and other CM scripts.

## Detect or install individual tools and artifacts via CM interface

You can also force to install specific versions of ML artifacts and tools
(models, data sets, engines, libraries, run-times, etc) 
using individual CM scripts to automatically plug them into the above ML task:

```bash
cm run script --tags=detect,os --out=json
cm run script --tags=get,python --version_min=3.9.1
cm run script --tags=install,python-venv --name=my-virtual-env
cm run script --tags=get,ml-model-onnx,resnet50
cm run script --tags=get,dataset,imagenet,original,_2012-500
cm run script --tags=get,onnxruntime,python-lib --version=1.12.0

cm show cache

cm run script --tags=app,image-classification,onnx,python (--input=my-image.jpg)
```

Each CM script CLI converts flags into environment variables, optionally updates them and generates tmp files using `customize.py`, 
runs some native script with these environment variables and files, and outputs new environment variables and files that can be cached
and reused by other CM scripts. Feel free to explore this [CM entry](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py) 
that wraps `_cm.yaml`, `run.sh`, `run.bat`, `src/onnx_classify.py` and other files required to run modular inference.

## Run this script with CUDA

Here is another example to run image classification on CUDA using the same CM interface:

First detect or install CUDA:

```bash
cm run script "get cuda"
cm run script "get cuda-devices"
```

Then run the same CM script with so-called variation `_cuda`:
```bash
cm run script "python app image-classification onnx _cuda"
```

If you have some image, you can now classify it using this script as follows:

```bash
cm run script "python app image-classification onnx _cuda" --input=my-image.jpg
```

This [variation](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L45) 
will set a specific environment variables such as `USE_CUDA="yes"`, 
that will simply [turn on and off](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L36) 
some dependencies on other CM scripts. 

For example, this environment variable will be used to automatically detect or install ONNX run-time with CUDA support instead of the CPU version.

