[ [Back to index](../README.md) ]

# Tutorial: customizing the MLPerf inference benchmark (part 2)

<details>
<summary>Click here to see the table of contents.</summary>

  * [Update CM framework and automation repository](#update-cm-framework-and-automation-repository)
  * [MLPerf inference - Python - RetinaNet FP32 - Open Images - ONNX - GPU - Offline](#mlperf-inference---python---retinanet-fp32---open-images---onnx---gpu---offline)
    * [Prepare CUDA](#prepare-cuda)
    * [Prepare Python with virtual environment](#prepare-python-with-virtual-environment)
    * [Run MLPerf inference benchmark (offline, accuracy)](#run-mlperf-inference-benchmark-offline-accuracy)
    * [Run MLPerf inference benchmark (offline, performance)](#run-mlperf-inference-benchmark-offline-performance)
    * [Prepare MLPerf submission](#prepare-mlperf-submission)
  * [MLCommons taskforce on education and reproducibility](#mlcommons-taskforce-on-education-and-reproducibility)
  * [Authors](#authors)
  * [Acknowledgments](#acknowledgments)

</details>

We expect that you have completed the [1st part](sc22-scc-mlperf.md) of this tutorial 
and managed to run the MLPerf inference benchmark for object detection
with RetinaNet FP32, Open Images and ONNX runtime on a CPU target.

This tutorial shows you how to customize the MLPerf inference benchmark
and run it on a GPU target, with other MLPerf scenarios (single stream, multiple stream, server),
different implementations of this benchmark (C++, Nvidia, etc),
various ML engines (PyTorch, TF, TVM) and quantized/pruned/optimized models.

*Note that this tutorial is under preparation and is gradually extended
 by the [MLCommons taskforce on education and reproducibility](../mlperf-education-workgroup.md).*

## Update CM framework and automation repository

Note that the [CM automation meta-framework](https://github.com/mlcommons/ck) 
and the [repository with automation scripts ](https://github.com/mlcommons/ck/tree/master/cm-mlops)
are being continuously updated by the community to improve the portability and interoperability of 
all reusable components for MLOps and DevOps.

You can install the stable versions used for this tutorial as follows:
```bash
python3 -m pip install cmind==1.1.1
cm pull repo mlcommons@ck --checkout=2982b9a
```

You can also try to use the latest version of the CM framework and automation repository as follows
(though be careful since CM CLI and APIs may change):

```bash
python3 -m pip install cmind -U
cm pull repo mlcommons@ck --checkout=master
```

You can also clean your raw MLPerf logs in the default place to avoid incompatibilities with  previous MLPerf and CM versions as follows:
```bash
rm -rf $HOME/mlperf_submission
rm -rf $HOME/mlperf_submission_logs
```

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

cm run script "install python-venv" --version=3.10.7 --name=mlperf-cuda
```

### Run MLPerf inference benchmark (offline, accuracy)

You are now ready to run the MLPerf object detection benchmark on GPU with Python virtual environment as folllows:

```bash
cm run script "app mlperf inference generic _python _retinanet _onnxruntime _gpu" \
     --adr.python.name=mlperf-cuda \
     --scenario=Offline --mode=accuracy --test_query_count=10 --rerun
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

cm run script "app mlperf inference generic _python _retinanet _onnxruntime _gpu" \
     --adr.python.name=mlperf-cuda \
     --scenario=Offline --mode=performance --rerun
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

### Prepare MLPerf submission


You can now run MLPerf in the submission mode (accuracy and performance) on GPU using the following CM command with Python virtual env
(just substitute "OctoML" with your organization or any other identifier):

```bash
cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_short,_dashboard \
      --adr.python.extra_cache_tags=venv-mlperf \
      --adr.python.version_min=3.8 \
      --adr.compiler.tags=gcc \
      --adr.openimages-preprocessed.tags=_500 \
      --submitter="OctoML" \
      --hw_name=default \
      --lang=python \
      --model=retinanet \
      --backend=onnxruntime \
      --device=gpu \
      --scenario=Offline \
      --test_query_count=10 \
      --rerun
```

Note that CM will reuse the same MLPerf inference benchmark, Open Images dataset, model and tools
from the CM cache installed during the 1st part of this tutorial while installing extra `onnxruntime-gpu` package for Python.

If you want to reinstall all dependencies, you can clean the CM cache again and restart the above command:
```bash
cm rm cache -f
```

cm run script "app mlperf inference generic _python _retinanet _onnxruntime _cpu" \
     --adr.python.name=mlperf-cuda \
     --scenario=Offline --mode=performance --rerun







*To be continued ...*



## MLCommons taskforce on education and reproducibility

You are welcome to join the [open MLCommons taskforce on education and reproducibility](../mlperf-education-workgroup.md)
to contribute to this project and continue optimizing this benchmark and prepare an official submission 
for MLPerf inference v3.0 (Feb 2023) with the help of the community.


## Authors

* [Grigori Fursin](https://cKnowledge.io/@gfursin) (OctoML, MLCommons, cTuning foundation)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) (OctoML, MLCommons)


## Acknowledgments

We thank 
[Hai Ah Nam](https://www.nersc.gov/about/nersc-staff/advanced-technologies-group/hai-ah-nam),
[Steve Leak](https://www.linkedin.com/in/steve-leak),
[Vijay Janappa Reddi](https://scholar.harvard.edu/vijay-janapa-reddi/home),
[Tom Jablin](https://scholar.google.com/citations?user=L_1FmIMAAAAJ&hl=en),
[Ramesh N Chukka](https://www.linkedin.com/in/ramesh-chukka-74b5b21),
[Peter Mattson](https://www.linkedin.com/in/peter-mattson-33b8863/),
[David Kanter](https://www.linkedin.com/in/kanterd),
[Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189),
[Thomas Schmid](https://www.linkedin.com/in/tschmid)
and [Gaurav Verma](https://www.linkedin.com/in/grverma)
for their suggestions and contributions.
