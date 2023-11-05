[ [Back to index](../README.md) ]

*An interactive version of this tutorial is also available 
 at this [Google Colab page](https://colab.research.google.com/drive/1fPFw86BKOQ79U1-lksTkAtJHn3_jhP9o?usp=sharing).*

# Trying CM: modular image classification

This example demonstrates our unified, technology-agnostic and human-readable CM automation language 
to prepare and run image classification on any platform while automatically detecting or installing 
all related artifacts and adapting them to your system and environment.

This language is being developed by the [open taskforce](../taksforce.md) 
to solve the dependency hell and make it easier for the community to run, customize and reuse 
research (software) projects in a unified way.

## Install CM automation language

Please follow this [guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
to install the MLCommons CM language on your platform.


## Prepare and run modular image classification via CM

Here is an example of a modular image classification assembled from 
([portable and reusable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script))
using a [human-readable YAML file](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L19).
CM scripts simply wrap native scripts, tools, and artifacts while making them findable, accessible, portabl, interoperable, and reusable
based on [FAIR principles](https://www.go-fair.org/fair-principles).

CM will read this YAML (or JSON) description, go through all dependencies to run other CM scripts, 
and attempt to automatically detect, download, install and build all related artifacts 
and tools to adapt this example to any software and hardware.

We have tested this tutorial on various Linux distributions, MacOS and Windows.

Let's go through these steps manually to better understand how CM scripts work.

First you need to install an [MLCommons CM-MLOps repository](https://github.com/mlcommons/ck/tree/master/cm-mlops) 
with portable and reusable scripts developed by the [MLCommons taskforce on automation and reproducibility](../taskforce.md)
to unify benchmarking and optimization of ML/AI systems:

```bash
cm pull repo mlcommons@ck
```

You can then run a CM script implementing modular image classification example as follows:

```bash
cm run script --tags=app,image-classification,onnx,python --quiet
```

or

```bash
cm run script "python app image-classification onnx" --quiet
```

or for CM v1.4.1+

```bash
cmr "python app image-classification onnx" --quiet
```


Note that you can also access this CM script using just one unified function `cmind.access` from CM Python API similar to micro services:

```python
import cmind
r=cmind.access({'action':'run', 
                'automation':'script'
                'tags':'app,image-classification,onnx,python',
                'out':'con',
                'quiet':True})
print (r)
```

It may take a few minutes to run this CM script for the first time and adapt it to your platform depending on your hardware and the Internet speed.

Note that all the subsequent runs will be much faster because CM automatically caches the output of all portable CM scripts 
to be quickly reused in this and other CM scripts.

## Detect or install individual tools and artifacts via CM interface

You can also force to install specific versions of ML artifacts and tools
(models, data sets, engines, libraries, run-times, etc) 
using individual CM scripts to automatically plug them into the above ML application:

```bash
cmr "detect os" --out=json
cmr "get sys-utils-cm" --quiet
cmr "get python" --version_min=3.9.1
cmr "install python-venv" --name=my-virtual-env
cmr "get ml-model resnet50 image-classification _onnx _fp32" --const.CM_PACKAGE_URL=https://huggingface.co/ctuning/mlperf-inference-resnet50-onnx-fp32-imagenet2012-v1.0/resolve/main/resnet50_v1.onnx
cmr "get original imagenet dataset _2012-500"
cmr "get generic-python-lib _onnxruntime" --version=1.12.0

cm show cache
cm show cache --tags=python
cm show cache --tags=ml-model

cmr "python app image-classification onnx"
cmr "python app image-classification onnx" --quiet --input=`cm find script app-image-classification-onnx-py,3d5e908e472b417e`/img/computer_mouse.jpg
```

CM scripts converts CLI flags into environment variables and generates some input files 
in the `preprocess function` of `customize.py` module.
They then run a Python function or some native script with these environment variables and input files, 
and outputs new environment variables and files to the unified CM output dictionary.
The output and files can be cached and reused by other CM scripts. 

Feel free to explore this [CM script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py) 
with `_cm.yaml`, `run.sh`, `run.bat`, `src/onnx_classify.py` and other files required to run modular inference.


## Run this script with CUDA

Here is another example to run the above image classification application with CUDA using the same CM interface:

First detect or install CUDA:

```bash
cm run script "get cuda"
cm run script "get cuda-devices"
```

Then run the same CM script with so-called variation `_cuda`:
```bash
cm run script "python app image-classification onnx _cuda"
```

Note that variations are different from script tags because they simply update environment variables and dependencies 
in a given CM script found using tags.

If you have some image, you can classify it using this CM script as follows:

```bash
cm run script "python app image-classification onnx _cuda" --input=my-image.jpg
```

The variation [*_cuda*](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L45) 
will set a specific environment variables such as `USE_CUDA="yes"`, 
that will simply [turn on and off](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L36) 
some dependencies on other CM scripts. 

For example, this environment variable will be used to automatically detect or install ONNX run-time with CUDA support instead of the CPU version.

