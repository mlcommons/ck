# About

This portable CM script provides a unified API and CLI to benchmark ONNX models using the MLPerf loadgen.
It measures performance only. 
If you need accuracy for MLPerf inference submission, please check [this CM script](../run-mlperf-inference-app).

## Development status

Prototyping stage:
* ONNX runtime (CPU & GPU) is now supported and tested on Ubuntu

## Prerequisites

Install [MLCommons CM automation meta-framework (aka CK2)](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Pull CM repository with portable automation scripts to benchmark ML Systems:
```bash
cm pull repo mlcommons@ck
```

If you want a "clean" environment, you may want to clean your CM cache as follows:
```bash
cm rm cache -f
```

We suggest you to install a python virtual environment via CM though it's not strictly necessary 
(CM can automatically detect and reuse your Python installation and environments):
```bash
cm run script "install python-venv" --name=mlperf
```

You can install a specific version of Python on your system via:
```bash
cm run script "install python-venv" --name=mlperf --version=3.10.7
```

## Manual installation of dependencies

You can skip this sub-section if you want CM to automatically detect already installed
ONNX runtime on your system. Otherwise, follow the next steps to install the latest or specific
version of ONNX runtime.

### MLPerf loadgen

```bash
cm run script "get mlperf loadgen"
```

### ONNX, CPU

```bash
cm run script "get generic-python-lib _onnxruntime"
```

or

```bash
cm run script "get generic-python-lib _onnxruntime" --version=1.13.1
```

or 

```bash
cm run script "get generic-python-lib _onnxruntime" --version_min=1.10.0
```

### ONNX, CUDA

We suggest you not to mix ONNX runtime for CPU and CUDA in the same python environment.

```bash
cm run script "get cuda"
cm run script "get generic-python-lib _onnxruntime _cuda" --version=1.13.1
```


## Run command

You can use CM variations prefixed by `_` to benchmark an official MLPerf model 
(_resnet50 or _retinanet):

```
cm run script "app mlperf generic-harness _resnet50"
```

You can also specify any custom onnx model file as follows:
```
cm run script --tags=app,mlperf,generic-harness --modelpath=<CUSTOM_MODEL_FILE_PATH>
```

### Other Input Options:
* `output_dir`
* `scenario`
* `runner`
* `concurrency`
* `ep`
* `intraop`
* `interop`
* `execmode`
* `modelpath`


# Developers

* [Gaz Iqbal](https://www.linkedin.com/in/gaziqbal) (OctoML)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) (OctoML)
* [Grigori Fursin](https://cKnowledge.io/@gfursin) (OctoML)
