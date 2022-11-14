[ [Back to index](../README.md) ]

# Tutorial: customizing the MLPerf inference benchmark (part 2)

<details>
<summary>Click here to see the table of contents.</summary>

* [Tutorial: customizing the MLPerf inference benchmark (part 2)](#tutorial-customizing-the-mlperf-inference-benchmark-part-2)
  * [Update CM framework and automation repository](#update-cm-framework-and-automation-repository)
  * [MLPerf inference - Python - RetinaNet - Open Images - ONNX - GPU - Offline](#mlperf-inference---python---retinanet---open-images---onnx---gpu---offline)
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

We suggest you to update your installation from time to time:

```bash
python3 -m pip install cmind -U

cm pull repo mlcommons@ck
```

You can also clean your raw MLPerf logs in the default place to avoid incompatibilities with  previous MLPerf and CM versions as follows:
```bash
rm -rf $HOME/mlperf_submission
rm -rf $HOME/mlperf_submission_logs
```

## MLPerf inference - Python - RetinaNet - Open Images - ONNX - GPU - Offline

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

You can now run MLPerf on GPU using the following CM command with Python virtual env
(just substitute "OctoML" with your organization or any other identifier):

```bash
cm pull repo mlcommons@ck

cm run script "get sys-utils-cm" --quiet

cm run script "install python-venv" --version=3.10.7 --name=mlperf

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
[Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189)
and [Gaurav Verma](https://www.linkedin.com/in/grverma)
for their suggestions and contributions.
