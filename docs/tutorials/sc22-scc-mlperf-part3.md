[ [Back to index](../README.md) ]

# Tutorial: modularizing and automating MLPerf (part 3)

<details>
<summary>Click here to see the table of contents.</summary>

* [Introduction](#introduction)
* [System preparation](#system-preparation)
  * [Update CM framework and automation repository](#update-cm-framework-and-automation-repository)
  * [Install virtual environment](#install-virtual-environment)
* [CM automation for the MLPerf benchmark](#cm-automation-for-the-mlperf-benchmark)
  * [MLPerf inference - Python - ResNet50 FP32 - ImageNet - ONNX - CPU - Offline](#mlperf-inference---python---resnet50-fp32---imagenet---onnx---cpu---offline)
    * [Accuracy mode](#accuracy-mode)
    * [Performance mode](#performance-mode)
    * [Submission mode](#submission-mode)
    * [Summary](#summary)
  * [MLPerf inference - Python - ResNet50 FP32 - ImageNet - TVM - CPU - Offline](#mlperf-inference---python---resnet50-fp32---imagenet---tvm---cpu---offline)
    * [Accuracy](#accuracy)
    * [Submission mode](#submission-mode)
    * [Summary](#summary)
* [The next steps](#the-next-steps)
* [Authors](#authors)
* [Acknowledgments](#acknowledgments)

</details>

# Introduction

We expect that you have completed the [1st part](sc22-scc-mlperf.md) of this tutorial 
and managed to run the MLPerf inference benchmark for object detection
with RetinaNet FP32, Open Images and ONNX runtime on a CPU target.

This tutorial shows you how to customize the MLPerf inference benchmark
and run it with the reference Python implementation of image classification, 
ImageNet, ONNX runtime and TVM on CPU.

*Note that this tutorial is under preparation and is gradually extended
 by the [MLCommons taskforce on automation and reproducibility](../taksforce.md).*


# System preparation

## Update CM framework and automation repository

Note that the [CM automation meta-framework](https://github.com/mlcommons/ck) 
and the [repository with automation scripts ](https://github.com/mlcommons/ck/tree/master/cm-mlops)
are being continuously updated by the community to improve the portability and interoperability of 
all reusable components for MLOps and DevOps.

You can get the latest version of the CM framework and automation repository as follows
(though be careful since CM CLI and APIs may change):

```bash
python3 -m pip install cmind -U
cm pull repo mlcommons@ck --checkout=master

cm run script "get sys-utils-cm" --quiet

```

## Install virtual environment

We suggest you to use Python virtual environment to avoid mixing up your native installation with MLPerf dependencies.
You can use your own one or install Python virtual environment using CM automation as follows:`

```bash
cm run script "install python-venv" --version=3.10.8 --name=mlperf
```

# CM automation for the MLPerf benchmark

## MLPerf inference - Python - ResNet50 FP32 - ImageNet - ONNX - CPU - Offline

### Accuracy mode

You can run MLPerf image classification by customizing the CLI 
of our [universal CM wrapper](../list_of_scripts.md##run-mlperf-inference-app) 
for MLPerf inference.

You just need to update flag `--model=resnet50`:

```bash
cm run script --tags=run,mlperf,inference,generate-run-cmds \
         --adr.python.name=mlperf \
         --adr.python.version_min=3.8 \
         --submitter="Community" \
         --implementation=python \
         --hw_name=default \
         --model=resnet50 \
         --backend=onnxruntime \
         --device=cpu \
         --scenario=Offline \
         --mode=accuracy \
         --test_query_count=5 \
         --quiet \
         --clean
```

In case of a successful run, you should see the following output:
```txt
...

accuracy=80.000%, good=4, total=5

...


```

This CM script will install a small version of the ImageNet dataset (500 images) for testing
and will automatically preprocess it with NCHW shape:

```bash
cm show cache --tags=get,dataset,imagenet
```

```txt
* cache::242d289d79f54978
    Tags: ['ILSVRC', 'dataset', 'get', 'image-classification', 'imagenet', 'original', 'script-artifact-7afd58d287fe4f11', '_2012-500']
    Path: /home/fursin/CM/repos/local/cache/242d289d79f54978

* cache::9e1013fd58724e2f
    Tags: ['ILSVRC', 'dataset', 'get', 'image-classification', 'imagenet', 'preprocessed', 'script-artifact-f259d490bbaf45f5', '_NCHW']
    Path: /home/fursin/CM/repos/local/cache/9e1013fd58724e2f
```

Check this [CM script](../list_of_scripts.md#get-dataset-imagenet-val) if you want to detect a full ImageNet validation dataset for submission.

CM will also install a ResNet-50 model (FP32, ONNX) using this [CM script](../list_of_scripts.md#get-ml-model-resnet50):


```bash
cm show cache --tags=get,ml-model,resnet50
```

```txt

* cache::eccee9fed2194558
    Tags: ['get', 'image-classification', 'ml-model', 'ml-model-resnet50', 'resnet50', 'script-artifact-56203e4e998b4bc0', '_fp32', '_onnx', '_onnx-1.5-opset-11', '_onnx_']
    Path: /home/fursin/CM/repos/local/cache/eccee9fed2194558

```

### Performance mode

You can run MLPerf with ResNet50 in performance mode as follows:

```bash
cm run script --tags=run,mlperf,inference,generate-run-cmds \
         --adr.python.name=mlperf \
         --adr.python.version_min=3.8 \
         --submitter="Community" \
         --implementation=python \
         --hw_name=default \
         --model=resnet50 \
         --backend=onnxruntime \
         --device=cpu \
         --scenario=Offline \
         --mode=performance \
         --test_query_count=5 \
         --quiet \
         --clean
```

In case of a successful run, you should see the following output:
```txt
...

INFO:main:starting TestScenario.Offline
TestScenario.Offline qps=4.98, mean=0.1756, time=0.201, queries=1, tiles=50.0:0.1756,80.0:0.1756,90.0:0.1756,95.0:0.1756,99.0:0.1756,99.9:0.1756


================================================
MLPerf Results Summary
================================================
SUT name : PySUT
Scenario : Offline
Mode     : PerformanceOnly
Samples per second: 28.3498
Result is : VALID
  Min duration satisfied : Yes
  Min queries satisfied : Yes
  Early stopping satisfied: Yes

================================================
Additional Stats
================================================
Min latency (ns)                : 176368211
Max latency (ns)                : 176368211
Mean latency (ns)               : 176368211
50.00 percentile latency (ns)   : 176368211
90.00 percentile latency (ns)   : 176368211
95.00 percentile latency (ns)   : 176368211
97.00 percentile latency (ns)   : 176368211
99.00 percentile latency (ns)   : 176368211
99.90 percentile latency (ns)   : 176368211

================================================
Test Parameters Used
================================================
samples_per_query : 5
target_qps : 1
target_latency (ns): 0
max_async_queries : 1
min_duration (ms): 0
max_duration (ms): 0
min_query_count : 1
max_query_count : 5
qsl_rng_seed : 14284205019438841327
sample_index_rng_seed : 4163916728725999944
schedule_rng_seed : 299063814864929621
accuracy_log_rng_seed : 0
accuracy_log_probability : 0
accuracy_log_sampling_target : 0
print_timestamps : 0
performance_issue_unique : 0
performance_issue_same : 0
performance_issue_same_index : 0
performance_sample_count : 1024

No warnings encountered during test.

No errors encountered during test.

...


```


### Submission mode

You can now run MLPerf with ResNet50 in a submission mode:

```bash
cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_dashboard \
         --adr.python.name=mlperf \
         --adr.python.version_min=3.8 \
         --submitter="Community" \
         --implementation=python \
         --hw_name=default \
         --model=resnet50 \
         --backend=onnxruntime \
         --device=cpu \
         --scenario=Offline \
         --test_query_count=500 \
         --quiet \
         --clean
```

In case of a successfull run, you should see your crowd-testing results at this 
[live W&B dashboard](https://wandb.ai/cmind/cm-mlperf-dse-testing/table?workspace=user-gfursin).


### Summary

```bash
python3 -m pip install cmind -U
cm pull repo mlcommons@ck --checkout=master

cm run script "get sys-utils-cm" --quiet

cm run script "install python-venv" --version=3.10.8 --name=mlperf

cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_dashboard \
         --adr.python.name=mlperf \
         --adr.python.version_min=3.8 \
         --submitter="Community" \
         --implementation=python \
         --hw_name=default \
         --model=resnet50 \
         --backend=onnxruntime \
         --device=cpu \
         --scenario=Offline \
         --test_query_count=500 \
         --quiet \
         --clean
```





## MLPerf inference - Python - ResNet50 FP32 - ImageNet - TVM - CPU - Offline

### Accuracy

You can now run MLPerf inference with the [Apache TVM](https://tvm.apache.org/) backend
that [OctoML](https://octoml.ai) has recently added to the 
[MLPerf inference vision benchmark](https://github.com/mlcommons/inference/blob/master/vision/classification_and_detection/python/backend_tvm.py):

```bash
cm run script --tags=run,mlperf,inference,generate-run-cmds \
         --adr.python.name=mlperf \
         --adr.python.version_min=3.8 \
         --submitter="Community" \
         --implementation=python \
         --hw_name=default \
         --model=resnet50 \
         --backend=tvm-onnx \
         --device=cpu \
         --scenario=Offline \
         --mode=accuracy \
         --test_query_count=5 \
         --quiet \
         --clean
```

This workflow will use other CM scripts to install [CMake](../list_of_scripts.md#get-cmake),
[LLVM 14+](../list_of_scripts.md#get-llvm), 
[ONNX](../list_of_scripts.md#get-generic-python-lib) to load ONNX models to TVM 
and will build [Apache TVM](../list_of_scripts.md#get-tvm).

In case of a successful run, you should see the following output:
```txt
...

accuracy=80.000%, good=4, total=5

...


```

If you want to use TVM via PIP install, you can use `--adr.tvm.tags=_pip-install`:


```bash
cm run script --tags=run,mlperf,inference,generate-run-cmds \
         --adr.python.name=mlperf \
         --adr.python.version_min=3.8 \
         --adr.tvm.tags=_pip-install \
         --submitter="Community" \
         --implementation=python \
         --hw_name=default \
         --model=resnet50 \
         --backend=tvm-onnx \
         --device=cpu \
         --scenario=Offline \
         --mode=accuracy \
         --test_query_count=5 \
         --quiet \
         --clean
```

Note that sometimes this benchmark may hang with TVM. You need to stop it and restart it and then it should work fine.
We expect the TVM community to fix this problem at some point.

In case of a successful run, you should see the following output:
```txt
...

accuracy=80.000%, good=4, total=5

...


```

### Submission mode


```bash
cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_dashboard \
         --adr.python.name=mlperf \
         --adr.python.version_min=3.8 \
         --submitter="Community" \
         --implementation=python \
         --hw_name=default \
         --model=resnet50 \
         --backend=tvm-onnx \
         --device=cpu \
         --scenario=Offline \
         --test_query_count=500 \
         --quiet \
         --clean
```


In case of a successfull run, you should see your crowd-testing results at this 
[live W&B dashboard](https://wandb.ai/cmind/cm-mlperf-dse-testing/table?workspace=user-gfursin).


### Summary

```bash
python3 -m pip install cmind -U
cm pull repo mlcommons@ck --checkout=master

cm run script "get sys-utils-cm" --quiet

cm run script "install python-venv" --version=3.10.8 --name=mlperf

cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_dashboard \
         --adr.python.name=mlperf \
         --adr.python.version_min=3.8 \
         --submitter="Community" \
         --implementation=python \
         --hw_name=default \
         --model=resnet50 \
         --backend=tvm-onnx \
         --device=cpu \
         --scenario=Offline \
         --test_query_count=500 \
         --quiet \
         --clean
```


# The next steps

Please check other parts of this tutorial to learn how to 
customize and optimize MLPerf inference benchmark using MLCommons CM
(under preparation):

* [1st part](sc22-scc-mlperf.md): customize MLPerf inference (Python ref implementation, Open images, ONNX, CPU)
* [2nd part](sc22-scc-mlperf-part2.md): customize MLPerf inference (C++ implementation, CUDA, PyTorch)
* *To be continued*

You are welcome to join the [open MLCommons taskforce on automation and reproducibility](../taksforce.md)
to contribute to this project and continue optimizing this benchmark and prepare an official submission 
for MLPerf inference v3.0 (March 2023) with the help of the community.

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
