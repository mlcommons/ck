[ [Back to index](../README.md) ]

# Tutorial: modularizing and automating MLPerf (part 2)

<details>
<summary>Click here to see the table of contents.</summary>

* [Introduction](#introduction)
* [Update CM framework and automation repository](#update-cm-framework-and-automation-repository)
* [CM automation for the MLPerf benchmark](#cm-automation-for-the-mlperf-benchmark)
  * [MLPerf inference - C++ - RetinaNet FP32 - Open Images - ONNX - CPU - Offline](#mlperf-inference---c---retinanet-fp32---open-images---onnx---cpu---offline)
    * [Summary](#summary)
  * [MLPerf inference - Python - RetinaNet FP32 - Open Images - ONNX - GPU - Offline](#mlperf-inference---python---retinanet-fp32---open-images---onnx---gpu---offline)
    * [Prepare CUDA](#prepare-cuda)
    * [Prepare Python with virtual environment](#prepare-python-with-virtual-environment)
    * [Run MLPerf inference benchmark (offline, accuracy)](#run-mlperf-inference-benchmark-offline-accuracy)
    * [Run MLPerf inference benchmark (offline, performance)](#run-mlperf-inference-benchmark-offline-performance)
    * [Summary](#summary)
  * [MLPerf inference - C++ - RetinaNet FP32 - Open Images - ONNX - GPU - Offline](#mlperf-inference---c---retinanet-fp32---open-images---onnx---gpu---offline)
    * [Summary](#summary)
  * [MLPerf inference - Python - RetinaNet FP32 - Open Images - PyTorch - CPU - Offline](#mlperf-inference---python---retinanet-fp32---open-images---pytorch---cpu---offline)
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
and run it with a C++ implementation, CUDA and PyTorch.

# Update CM framework and automation repository

Note that the [CM automation meta-framework](https://github.com/mlcommons/ck) 
and the [repository with automation scripts ](https://github.com/mlcommons/ck/tree/master/cm-mlops)
are being continuously updated by the community to improve the portability and interoperability of 
all reusable components for MLOps and DevOps.

You can get the latest version of the CM framework and automation repository as follows
(though be careful since CM CLI and APIs may change):

```bash
python3 -m pip install cmind -U
cm pull repo mlcommons@ck --checkout=master
```
# CM automation for the MLPerf benchmark

## MLPerf inference - C++ - RetinaNet FP32 - Open Images - ONNX - CPU - Offline

Let's now run a [universal and modular C++ implementation of the MLPerf inference benchmark](../list_of_scripts.md#app-mlperf-inference-cpp) 
(developed by [Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189) during his internship at [OctoML](https://octoml.ai)).

Note that CM will reuse already installed and preprocessed Open Images dataset, model and tools
from the CM cache installed during the 1st part of this tutorial while installing the ONNX runtime library with C++ bindings for your system.

If you want to reinstall all dependencies, you can clean the CM cache again and restart the above command:
```bash
cm rm cache -f
```

You can run C++ implementation by simply changing `_python` variation to `_cpp` variation in our high-level CM MLPerf script
that will then set up the correct dependencies and will run the C++ implementation of this script

```bash

cm run script "app mlperf inference generic _cpp _retinanet _onnxruntime _cpu" \
     --adr.python.version_min=3.8 \
     --adr.compiler.tags=gcc \
     --adr.openimages-preprocessed.tags=_500 \
     --scenario=Offline \
     --mode=accuracy \
     --test_query_count=10 \
     --rerun

```

CM will download the ONNX binaries for your system, compile our C++ implementation with the ONNX backend
and will run the MLPerf inference benchmark. You should normally see the following output:
```txt
...

loading annotations into memory...
Done (t=0.02s)
creating index...
index created!
Loading and preparing results...
DONE (t=0.01s)
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.10s).
Accumulating evaluation results...
DONE (t=0.12s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.548
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.787
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.714
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.304
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.631
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.433
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.648
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.663
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.343
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.731
mAP=54.814%

    - running time of script "run,mlperf,mlcommons,accuracy,mlc,process-accuracy": 1.18 sec.
  - running time of script "app,vision,language,mlcommons,mlperf,inference,reference,generic,ref": 53.81 sec.
```

You can then obtain performance using the C++ implemnentation of the MLPerf inference benchmark as follows:
```bash

cm run script "app mlperf inference generic _cpp _retinanet _onnxruntime _cpu" \
     --adr.python.version_min=3.8 \
     --adr.compiler.tags=gcc \
     --adr.openimages-preprocessed.tags=_500 \
     --scenario=Offline \
     --mode=performance \
     --test_query_count=10 \
     --rerun

```

You should get the following output (QPS will depend on the speed of your machine):
```txt
================================================
MLPerf Results Summary
================================================
SUT name : QueueSUT
Scenario : Offline
Mode     : PerformanceOnly
Samples per second: 0.631832
Result is : VALID
  Min duration satisfied : Yes
  Min queries satisfied : Yes
  Early stopping satisfied: Yes

================================================
Additional Stats
================================================
Min latency (ns)                : 14547257820
Max latency (ns)                : 15826999233
Mean latency (ns)               : 15129106642
50.00 percentile latency (ns)   : 15045448544
90.00 percentile latency (ns)   : 15826999233
95.00 percentile latency (ns)   : 15826999233
97.00 percentile latency (ns)   : 15826999233
99.00 percentile latency (ns)   : 15826999233
99.90 percentile latency (ns)   : 15826999233

================================================
Test Parameters Used
================================================
samples_per_query : 10
target_qps : 1
target_latency (ns): 0
max_async_queries : 1
min_duration (ms): 0
max_duration (ms): 0
min_query_count : 1
max_query_count : 10
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
performance_sample_count : 64

No warnings encountered during test.

No errors encountered during test.

  - running time of script "app,vision,language,mlcommons,mlperf,inference,reference,generic,ref": 50.24 sec.
rsa-key-fgg-universal@mlperf-tests-e2-x86-16-64-ubuntu

```

We plan to continue optimizing this implementation of the MLPerf inference benchmark 
together with the community across different ML engines, models, data sets and systems.

### Summary

You can now test the end-to-end benchmarking and submission with the C++ implementation and ONNX on CPU
using Python virtual environment as follows (just substitute "Community" with your name or organization or anything else): 

```bash

cm pull repo mlcommons@ck

cm run script "get sys-utils-cm" --quiet

cm run script "install python-venv" --version=3.10.8 --name=mlperf

cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_short,_dashboard \
      --adr.python.name=mlperf \
      --adr.python.version_min=3.8 \
      --adr.compiler.tags=gcc \
      --adr.openimages-preprocessed.tags=_500 \
      --submitter="Community" \
      --implementation=cpp \
      --hw_name=default \
      --model=retinanet \
      --backend=onnxruntime \
      --device=cpu \
      --scenario=Offline \
      --test_query_count=10 \
      --clean

```

In case of a successfull run, you should see your crowd-testing results at this [live W&B dashboard](https://wandb.ai/cmind/cm-mlperf-dse-testing/table?workspace=user-gfursin).

            

## MLPerf inference - Python - RetinaNet FP32 - Open Images - ONNX - GPU - Offline

### Prepare CUDA

If your system has an Nvidia GPU, you can run the MLPerf inference benchmark on this GPU
using the CM automation.

First you need to detect CUDA and cuDNN installation using CM as follows:

```bash
cm run script "get cuda" --out=json
```

You should see the output similar to the following one (for CUDA 11.3):
```json
{
  "deps": [],
  "env": {
    "+CPLUS_INCLUDE_PATH": [
      "/usr/local/cuda-11.3/include"
    ],
    "+C_INCLUDE_PATH": [
      "/usr/local/cuda-11.3/include"
    ],
    "+DYLD_FALLBACK_LIBRARY_PATH": [],
    "+LD_LIBRARY_PATH": [],
    "+PATH": [
      "/usr/local/cuda-11.3/bin"
    ],
    "CM_CUDA_CACHE_TAGS": "version-11.3",
    "CM_CUDA_INSTALLED_PATH": "/usr/local/cuda-11.3",
    "CM_CUDA_PATH_BIN": "/usr/local/cuda-11.3/bin",
    "CM_CUDA_PATH_INCLUDE": "/usr/local/cuda-11.3/include",
    "CM_CUDA_PATH_LIB": "/usr/local/cuda-11.3/lib64",
    "CM_CUDA_PATH_LIB_CUDNN": "/usr/local/cuda-11.3/lib64/libcudnn.so",
    "CM_CUDA_PATH_LIB_CUDNN_EXISTS": "yes",
    "CM_CUDA_VERSION": "11.3",
    "CM_NVCC_BIN": "nvcc",
    "CM_NVCC_BIN_WITH_PATH": "/usr/local/cuda-11.3/bin/nvcc"
  },
  "new_env": {
    "+CPLUS_INCLUDE_PATH": [
      "/usr/local/cuda-11.3/include"
    ],
    "+C_INCLUDE_PATH": [
      "/usr/local/cuda-11.3/include"
    ],
    "+DYLD_FALLBACK_LIBRARY_PATH": [],
    "+LD_LIBRARY_PATH": [],
    "+PATH": [
      "/usr/local/cuda-11.3/bin"
    ],
    "CM_CUDA_CACHE_TAGS": "version-11.3",
    "CM_CUDA_INSTALLED_PATH": "/usr/local/cuda-11.3",
    "CM_CUDA_PATH_BIN": "/usr/local/cuda-11.3/bin",
    "CM_CUDA_PATH_INCLUDE": "/usr/local/cuda-11.3/include",
    "CM_CUDA_PATH_LIB": "/usr/local/cuda-11.3/lib64",
    "CM_CUDA_PATH_LIB_CUDNN": "/usr/local/cuda-11.3/lib64/libcudnn.so",
    "CM_CUDA_PATH_LIB_CUDNN_EXISTS": "yes",
    "CM_CUDA_VERSION": "11.3",
    "CM_NVCC_BIN": "nvcc",
    "CM_NVCC_BIN_WITH_PATH": "/usr/local/cuda-11.3/bin/nvcc"
  },
  "new_state": {},
  "return": 0,
  "state": {}
}

```

You can obtain the information about your GPU using CM as follows:
```bash
cm run script "get cuda-devices"
```

### Prepare Python with virtual environment

We suggest you to install Python virtual environment to avoid mixing up your local Python:
```bash
cm run script "get sys-utils-cm" --quiet

cm run script "install python-venv" --version=3.10.8 --name=mlperf-cuda
```

### Run MLPerf inference benchmark (offline, accuracy)

You are now ready to run the MLPerf object detection benchmark on GPU with Python virtual environment as folllows:

```bash
cm run script "app mlperf inference generic _python _retinanet _onnxruntime _cuda" \
     --adr.python.name=mlperf-cuda \
     --scenario=Offline \
     --mode=accuracy \
     --test_query_count=10 \
     --clean
```

This CM script will automatically find or install all dependencies
described in its [CM meta description](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference/_cm.yaml#L61),
aggregate all environment variables, preprocess all files and assemble the MLPerf benchmark CMD.

It will take a few minutes to run it and you should see the following accuracy:

```txt
loading annotations into memory...
Done (t=0.02s)
creating index...
index created!
Loading and preparing results...
DONE (t=0.02s)
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.09s).
Accumulating evaluation results...
DONE (t=0.11s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.548
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.787
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.714
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.304
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.631
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.433
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.648
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.663
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.343
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.731

mAP=54.814%
```

### Run MLPerf inference benchmark (offline, performance)

Let's run the MLPerf object detection on GPU while measuring performance:

```bash

cm run script "app mlperf inference generic _python _retinanet _onnxruntime _cuda" \
     --adr.python.name=mlperf-cuda \
     --scenario=Offline \
     --mode=performance \
     --clean
```

It will run for 2-5 minutes and you should see the output similar to the following one in the end
(the QPS is the performance result of this benchmark that depends on the speed of your system):

```txt

TestScenario.Offline qps=8.44, mean=4.7238, time=78.230, queries=660, tiles=50.0:4.8531,80.0:5.0225,90.0:5.1124,95.0:5.1658,99.0:5.2730,99.9:5.3445


================================================
MLPerf Results Summary
================================================
...

No warnings encountered during test.

No errors encountered during test.

  - running time of script "app,vision,language,mlcommons,mlperf,inference,reference,generic,ref": 86.90 sec.

```

### Summary


You can now run MLPerf in the submission mode (accuracy and performance) on GPU using the following CM command with Python virtual env
(just substitute "Community" with your organization or any other identifier):

```bash
cm pull repo mlcommons@ck

cm run script "get sys-utils-cm" --quiet

cm run script "install python-venv" --version=3.10.8 --name=mlperf-cuda

cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_short,_dashboard \
      --adr.python.name=mlperf-cuda \
      --adr.python.version_min=3.8 \
      --adr.compiler.tags=gcc \
      --adr.openimages-preprocessed.tags=_500 \
      --submitter="Community" \
      --implementation=python \
      --hw_name=default \
      --model=retinanet \
      --backend=onnxruntime \
      --device=gpu \
      --scenario=Offline \
      --test_query_count=10 \
      --clean
```

In case of a successfull run, you should see your crowd-testing results at this [live W&B dashboard](https://wandb.ai/cmind/cm-mlperf-dse-testing/table?workspace=user-gfursin).





## MLPerf inference - C++ - RetinaNet FP32 - Open Images - ONNX - GPU - Offline

### Summary

After installing and detecting CUDA using CM in the previous section, you can also 
run the C++ implementation of the MLPerf vision benchmark with CUDA as follows
(just substitute "Community" with your organization or any other identifier):


```bash

cm pull repo mlcommons@ck

cm run script "get sys-utils-cm" --quiet

cm run script "install python-venv" --version=3.10.8 --name=mlperf-cuda

cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_short,_dashboard \
      --adr.python.name=mlperf-cuda \
      --adr.python.version_min=3.8 \
      --adr.compiler.tags=gcc \
      --adr.openimages-preprocessed.tags=_500 \
      --submitter="Community" \
      --implementation=cpp \
      --hw_name=default \
      --model=retinanet \
      --backend=onnxruntime \
      --device=gpu \
      --scenario=Offline \
      --test_query_count=10 \
      --clean

```

In case of a successfull run, you should see your crowd-testing results at this [live W&B dashboard](https://wandb.ai/cmind/cm-mlperf-dse-testing/table?workspace=user-gfursin).



## MLPerf inference - Python - RetinaNet FP32 - Open Images - PyTorch - CPU - Offline

### Summary

You can now try to use PyTorch instead of ONNX as follows:


```bash

cm pull repo mlcommons@ck

cm run script "get sys-utils-cm" --quiet

cm run script "install python-venv" --version=3.10.8 --name=mlperf

cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_short,_dashboard \
      --adr.python.name=mlperf \
      --adr.python.version_min=3.8 \
      --adr.compiler.tags=gcc \
      --adr.ml-engine-torchvision.version_max=0.12.1 \
      --adr.openimages-preprocessed.tags=_500 \
      --submitter="Community" \
      --implementation=python \
      --hw_name=default \
      --model=retinanet \
      --backend=onnxruntime \
      --device=cpu \
      --scenario=Offline \
      --test_query_count=10 \
      --num_threads=1 \
      --clean

```

CM will install PyTorch and PyTorch Vision <= 0.12.1 (we need that because current MLPerf inference implementation 
fails with other PyTorch Vision version - this will be fixed by the MLCommons inference WG)
and will run this benchmark with 1 thread (this is needed because the current PyTorch implementation 
sometimes fail with a high number of threads - this will be fixed by the MLCommons inference WG)

In case of a successfull run, you should see your crowd-testing results at this [live W&B dashboard](https://wandb.ai/cmind/cm-mlperf-dse-testing/table?workspace=user-gfursin).

# The next steps

Please check other parts of this tutorial to learn how to 
customize and optimize MLPerf inference benchmark using MLCommons CM
(under preparation):

* [1st part](sc22-scc-mlperf.md): customize MLPerf inference (Python ref implementation, Open images, ONNX, CPU)
* [3rd part](sc22-scc-mlperf-part3.md): customize MLPerf inference (ResNet50 Int8, ImageNet, TVM)
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
