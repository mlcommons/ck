[ [Back to index](../README.md) ]

# Tutorial to run and optimize MLPerf BERT inference benchmark at SCC'23

<details>
<summary>Click here to see the table of contents.</summary>

* [Tutorial to run and optimize MLPerf BERT inference benchmark at SCC'23](#tutorial-to-run-and-optimize-mlperf-bert-inference-benchmark-at-scc'23)
  * [Introduction](#introduction)
  * [Scoring](#scoring)
  * [System preparation](#system-preparation)
    * [Minimal system requirements to run unoptimized MLPerf BERT inference benchmark](#minimal-system-requirements-to-run-unoptimized-mlperf-bert-inference-benchmark)
    * [Extra system requirements for Nvidia GPU](#extra-system-requirements-for-nvidia-gpu)
  * [MLCommons CM automation language](#mlcommons-cm-automation-language)
    * [CM installation](#cm-installation)
    * [Pull CM repository with cross-platform MLOps and DevOps scripts](#pull-cm-repository-with-cross-platform-mlops-and-devops-scripts)
    * [Test MLPerf BERT inference benchmark out-of-the-box](#test-mlperf-bert-inference-benchmark-out-of-the-box)
  * [Prepare to run MLPerf step-by-step via CM](#prepare-to-run-mlperf-step-by-step-via-cm)
    * [Install system dependencies for your platform](#install-system-dependencies-for-your-platform)
    * [Use CM to detect or install Python 3.8+](#use-cm-to-detect-or-install-python-38)
    * [Setup a virtual environment for Python](#setup-a-virtual-environment-for-python)
    * [Compile MLPerf loadgen](#compile-mlperf-loadgen)
    * [Download the SQuAD validation dataset](#download-the-squad-validation-dataset)
    * [Detect or install ONNX runtime for CPU](#detect-or-install-onnx-runtime-for-cpu)
    * [Download Bert-large model (FP32, ONNX format)](#download-bert-large-model-fp32-onnx-format)
    * [Pull MLPerf inference sources with reference implementations](#pull-mlperf-inference-sources-with-reference-implementations)
    * [Run short reference MLPerf inference benchmark (offline, accuracy)](#run-short-reference-mlperf-inference-benchmark-offline-accuracy)
    * [Run MLPerf inference benchmark (offline, performance)](#run-mlperf-inference-benchmark-offline-performance)
  * [Prepare minimal MLPerf submission to the SCC committee](#prepare-minimal-mlperf-submission-to-the-scc-committee)
  * [Run optimized implementation of the MLPerf inference benchmark](#run-optimized-implementation-of-the-mlperf-inference-benchmark)
    * [Trying Nvidia implementation](#trying-nvidia-implementation)
    * [Trying deepsparse backend](#trying-deepsparse-backend)
      * [int8](#int8)
      * [fp32](#fp32)
  * [Optimize benchmark yourself](#optimize-benchmark-yourself)
  * [Acknowledgments](#acknowledgments)
    * [Nvidia MLPerf inference backend](#nvidia-mlperf-inference-backend)
    * [DeepSparse MLPerf inference backend](#deepsparse-mlperf-inference-backend)

</details>

*This document is still being updated and will be finalized soon!*


## Introduction

This tutorial was prepared for the [Student Cluster Competition'23](https://studentclustercompetition.us/2023/index.html) 
to explain how to run and optimize the [MLPerf inference benchmark](https://arxiv.org/abs/1911.02549)
with [BERT Large model variations](https://github.com/mlcommons/inference/tree/master/language/bert#supported-models)
across different software and hardware. You will need to obtain the best throughput for your system
(samples per second) without degrading accuracy.

You will use [MLCommons CM automation language](https://doi.org/10.5281/zenodo.8105339)
that helps to modularize and automate (MLPerf) benchmarks 
using portable, technology-agnostic and reusable [CM scripts](../list_of_scripts.md)
being developed by the [MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md),
the [cTuning foundation](https://cTuning.org) and [the community](https://discord.gg/JjWNWXKxwT).

During this tutorial you will learn how to:
- Install, understand and use the MLCommons CM automation language on your system.
- Prepare the MLPerf BERT inference benchmark and make the first test run on a CPU using CM.
- Obtain official results (accuracy and throughput) for MLPerf BERT question answering model in offline mode on a CPU or GPU of your choice.
- Learn how to optimize this benchmark and submit your results to the SCC committee.

It should take less than an hour to complete this tutorial including 30 minutes to run the optimized version of this benchmark to completion. 
In the end, you should obtain a tarball (`mlperf_submission.tar.gz`) with the MLPerf-compatible results
that you will submit to the SCC organizers to get points.

## Scoring

During SCC, you will first attempt to run a reference (unoptimized) Python implementation of the MLPerf inference benchmark
with [BERT fp32 model](https://huggingface.co/ctuning/mlperf-inference-bert-onnx-fp32-squad-v1.1), 
[SQuAd v1.1 dataset](https://datarepository.wolframcloud.com/resources/SQuAD-v1.1), 
ONNX runtime (`MLPerf framework` or `backend`) with CPU target (`MLPerf device`) 
and [MLPerf loadgen library](https://github.com/mlcommons/inference/tree/master/loadgen) 
to get a minimal set of points.

After a successful run, you will be able to run optimized version of this benchmark on a GPU (Nvidia, AMD) or CPU (x64, Arm64),
change ML frameworks, try different batch sizes, etc to get better performance than the reference implementation that will be converted in extra points.

Note that since not all vendor implementations of MLPerf inference benchmark are still equal and they mostly support 1-node 
benchmarking at this stage, teams will compete to get better throughput only between the same architecture type (CPU, Nvidia GPU, AMD GPU, etc) 
to get more points.

Furthermore, if you improve existing implementation and/or provide support for new hardware (such as AMD GPU) 
add support for multi-node execution or improve MLPerf BERT models without dropping accuracy, 
and make all your improvements publicly available under Apache 2.0 license when submitting results to the SCC committee,
you will get substantial bonus points for supporting the MLPerf community.

After SCC, you are welcome to prepare an official submission to the next inference v4.0 round in February 2024 
to get your results and the team name to the official MLCommons release similar to [v3.1](https://mlcommons.org/en/inference-datacenter-31). 
(see the announcement of [community MLPerf submissions from the cTuning foundation at HPC Wire](https://www.hpcwire.com/2023/09/13/mlperf-releases-latest-inference-results-and-new-storage-benchmark)).


*Note that both MLPerf and CM automation are evolving projects.
 If you encounter issues or have questions, please submit them [here](https://github.com/mlcommons/ck/issues)
 and feel free to get in touch with the CM-MLPerf community via our [public Discord server](https://discord.gg/JjWNWXKxwT).*


## System preparation

### Minimal system requirements to run unoptimized MLPerf BERT inference benchmark

* CPU: 1 node (x86-64 or Arm64)
* OS: we have tested this automation on Ubuntu 20.04, Ubuntu 22.04, Debian 10, Red Hat 9 and MacOS 13
* Disk space: ~10GB
* Python: 3.8+
* All other dependencies (model, data set, benchmark, libraries and tools) should be detected or installed by CM

### Extra system requirements for Nvidia GPU

* GPU: Nvidia GPU with 8GB+ memory (official optimized backend) or AMD GPU via experimental backend from one of the teams
* Disk space: ~ 30GB




## MLCommons CM automation language

The MLCommons and cTuning foundation has developed an open-source and technology-agnostic
[Collective Mind automation language (MLCommons CM)](https://github.com/mlcommons/ck/tree/master/cm)
to modularize AI/ML Systems and automate their benchmarking, optimization 
and design space exploration across continuously changing software, hardware and data.

CM is a small Python library with minimal dependencies and a unified CLI, Python API and human readable YAML/JSON inputs and meta descriptions.
It is extended by the community via [portable CM scripts] that should run on any platform with any OS. 
Our goal is to provide a common, human-friendly and technology-agnostic interface to unify and automate all the steps 
to prepare, run and reproduce benchmarks and research projects across diverse ML models, datasets, frameworks, compilers and hardware.

We suggest you to check this [simple tutorial to run modular image classification using CM](modular-image-classification.md)
to understand how CM works and see [ACM TechTalk'21](https://learning.acm.org/techtalks/reproducibility) 
and [ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339) to learn about our motivation and long-term vision.



### CM installation

Follow [this guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md) to install the MLCommons CM framework on your system.

After the installation, you should be able to access the CM command line as follows:

```bash
cm
```

```txt
cm {action} {automation} {artifact(s)} {--flags} @input.yaml @input.json
```

```bash
cm --version
```

```txt
1.5.3
```



### Pull CM repository with cross-platform MLOps and DevOps scripts

Pull the stable version of the [MLCommons repository](https://github.com/mlcommons/ck/tree/master/cm-mlops) 
with [cross-platform CM scripts for modular benchmarking and optimization of AI/ML Systems](../list_of_scripts.md):

```bash
cm pull repo mlcommons@ck --checkout=scc23
```
or using equivalent form with a full URL:
```bash
cm pull repo --url=https://github.com/mlcommons/ck --checkout=scc23
```

CM pulls all such repositories into the `$HOME/CM` directory to search for CM automations and portable scripts
that can run on any OS (Linux, Windows, MacOS). You can find the location of a pulled repository as follows:

```bash
cm find repo mlcommons@ck
```

```txt
mlcommons@ck,a4705959af8e447a = /home/ubuntu/CM/repos/mlcommons@ck
```

Note that you can use the latest master version instead of the stable SCC'23 branch by removing
`--checkout` flag - it should be safe since our goal is to keep the CM interface always unified and backward compatible 
while continuously improving the underlying CM scripts based on the feedback from the community when running them across 
diverse software and hardware.

You can update this repository at any time with the same command:
```
cm pull repo mlcommons@ck
```

Note that if something goes wrong, you can always start from scratch
by simply removing `$HOME/CM` directory with all repositories completely:

```bash
rm -rf $HOME/CM
```


### Test MLPerf BERT inference benchmark out-of-the-box

*We suggest you to read this section but not run the CM script - 
 in such case, you will be able to learn how to prepare the MLPerf BERT benchmark 
 step-by-step using reusable CM automations in the next section.*

You are now ready to run the [reference (unoptimized) Python implementation](https://github.com/mlcommons/inference/tree/master/language/bert) 
of the MLPerf language benchmark with BERT model and [ONNX backend](https://github.com/mlcommons/inference/blob/master/language/bert/onnxruntime_SUT.py).

Normally, you would need to go through this [README.md](https://github.com/mlcommons/inference/blob/master/language/bert)
and use Docker containers or prepare all the dependencies and environment variables manually.


Note that at this stage, you should normally be able to run the MLPerf BERT inference benchmark out-of-the-box 
using just one CM command that will automatically detect all the required dependencies
and download and install the missing ones including benchmark sources, models, data sets, 
ML frameworks, libraries and tools. However, we suggest you run this command only
at the end of this tutorial to get more details about how it works:

```bash
cm run script "app mlperf inference generic _python _bert-99 _onnxruntime _cpu" \
     --scenario=Offline \
     --mode=accuracy \
     --device=cpu \
     --execution-mode=test \
     --test_query_count=10 \
     --rerun \
     --adr.mlperf-implementation.tags=_repo.https://github.com/ctuning/inference,_branch.scc23 \
     --adr.mlperf-implementation.version=custom \
     --adr.compiler.tags=gcc \
     --quiet
```

*Note that you can use `cmr` alias instead of `cm run script`:*

```bash
cmr "app mlperf inference generic _python _bert-99 _onnxruntime _cpu" \
     --scenario=Offline \
     --mode=accuracy \
     --device=cpu \
     --execution-mode=test \
     --test_query_count=10 \
     --rerun \
     --adr.mlperf-implementation.tags=_repo.https://github.com/ctuning/inference,_branch.scc23 \
     --adr.mlperf-implementation.version=custom \
     --adr.compiler.tags=gcc \
     --quiet
```


You will see a long output that should contain the following line with accuracy:
```bash
{"exact_match": 70.0, "f1": 70.0}
```

* `--device=cuda` and `--device=rocm` can be used to run the inference on Nvidia GPU and AMD GPUs respectively. 
  The current reference implementation supports only one GPU instance for inference but this can be changed.

* `--adr.mlperf-implementation.tags=_repo.URL` allows you to use your own fork 
  of the [MLPerf inference repo](https://github.com/mlcommons/inference)
  if you want to improve it. We use the [cTuning fork](https://github.com/ctuning/inference) 
  to keep a stable version of the official MLPerf inference repository.


If you remove flag `--adr.compiler.tags=gcc`, CM will attempt to download nad install LLVM as a default dependency for MLPerf loadgen.

You can add `-v` flag to debug any CM script.





## Prepare to run MLPerf step-by-step via CM



### Install system dependencies for your platform

First, you need to install various system dependencies required by the MLPerf inference benchmark.

For this purpose, we have created a cross-platform CM script that will automatically install 
such dependencies based on your OS (Ubuntu, Debian, Red Hat, MacOS ...). 

In this case, CM script serves simply as a wrapper with a unified and cross-platform interface
for native scripts that you can find and extend [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
if some dependencies are missing on your machine - this is a collaborative way to make 
CM scripts portable and interoperable.

You can run this CM scripts as follows (note that you may be asked for a SUDO password on your platform):

```bash
cmr "get sys-utils-cm" --quiet
```

If you think that you have all system dependencies installed,
you can run this script without `--quiet` flag and type "skip" in the script prompt.



### Use CM to detect or install Python 3.8+

Since we use Python reference implementation of the MLPerf inference benchmark (unoptimized),
we need to detect or install Python 3.8+ (MLPerf requirement). 

You need to detect it using the following [CM script](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md#get-python3):

```bash
cmr "get python" --version_min=3.8
```

You may see the output similar to
```bash

* cm run script "get python"
  - Searching for versions:  >= 3.8

    * /usr/bin/python3
      Detected version: 3.10.12

      Found artifact in /usr/bin/python3
      Detected version: 3.10.12

```

Note, that all artifacts (including the above scripts) in MLCommons CM are organized as a database of interconnected components.
They can be found either by their user friendly tags (such as `get,python`) or aliases (`get-python3`) and unique identifiers
(`5b4e0237da074764`).
You can find this information in a [CM meta description of this script](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-python3/_cm.json).

If required Python is installed on your system, CM will detect it and cache related environment variables such as PATH, PYTHONPATH, etc.
to be reused by other CM scripts. You can find an associated CM cache entry for your python as follows:

```bash
cm show cache --tags=get,python
```

or

```bash
cm show cache "get python"
```

You should see the output similar to
```bash

* Tags: get,get-python,get-python3,non-virtual,python,python3,script-artifact-d0b5dd74373f4a62,version-3.10.12
  Path: /home/ubuntu/CM/repos/local/cache/d7d9e170f0ac498f
  Version: 3.10.12

```

CM will automatically generate a unique CM ID (16 hexadecimal lowercase characters) on your system and cache produced artifacts and meta descriptions there.

For example, you can see all the environment variables produced by this CM script (that can be reused in your projects or other CM scripts) in the following JSON file:
```bash
cat `cm find cache "get python"`/cm-cached-state.json
```

If required Python is not detected, CM will automatically attempt to download and build it from sources 
using another [cross-platform CM script "install-python-src"](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md#install-python-src).
In the end, CM will also cache new binaries and related environment variables such as PATH, PYTHONPATH.

You can see the state of CM cache with all reusable artifacts and meta-descriptions as follows:

```bash
cm show cache
```

You can find the PATH to cached artifacts and reuse them in your own projects as follows:
```bash
cm find cache "get python"
```

Note that if you run the same script again, CM will automatically find and reuse the cached output:
```bash
cmr "get python" --version_min=3.8 --out=json
```

You can also clean CM cache and start from scratch as follows:
```bash
cm rm cache -f
```


### Setup a virtual environment for Python

We also automated the very commonly used command to install virtual environment.
You can create multiple virtual environments that will be automatically used by CM scripts as follows:

```bash
cmr "install python-venv" --name=mlperf
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```

Now flag `--adr.python.name=mlperf` will be added to all CM scripts automatically forcing them to use this virtual environment.
You can also delete a given virtual environment and start from scratch as follows:
```bash
cm rm cache "python name-mlperf" -f
```

You can test the virtual environment using CM script to print "Hello World" via detected python
```bash
cmr "python hello-world"
```

You should normally see that python is used from the CM cache:
```bash
* cm run script "python hello-world"
  * cm run script "detect os"
  * cm run script "get sys-utils-cm"
  * cm run script "get python3"
  * cm run script "print python-version"
    * cm run script "get python3"

CM_PYTHON_BIN = python3
CM_PYTHON_BIN_WITH_PATH = /home/ubuntu/CM/repos/local/cache/b9dafcf15d4045af/mlperf/bin/python3

Python 3.10.12
/home/ubuntu/CM/repos/local/cache/b9dafcf15d4045af/mlperf/bin/python3
Python 3.10.12

HELLO WORLD from Python
```



### Compile MLPerf loadgen

You need to compile the [MLPerf C++ loadgen library with Python bindings](https://github.com/mlcommons/inference/tree/master/loadgen) 
while forcing compiler dependency to GCC using the 
[CM "get-mlperf-inference-loadgen" script](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-mlperf-inference-loadgen/README-extra.md):


```bash
cmr "get mlperf loadgen" --adr.compiler.tags=gcc --quiet
```

The `--adr` flag stands for "Add to all Dependencies Recursively" and will find all sub-dependencies on other CM scripts 
in the CM loadgen script with the "compiler" name and will append "gcc" tag 
to enforce detection and usage of GCC to build loadgen.




### Download the SQuAD validation dataset

You can download the SQuAD v1.1 validation dataset using the [CM "get-dataset-squad" script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad) as follows:

```bash
cmr "get dataset squad original"
```

After installing this dataset via CM, you can reuse it in your own projects or other CM scripts (including MLPerf benchmarks).
You can check the CM cache as follows (the unique ID of the CM cache entry will be different on your machine):
```bash
cm show cache "get dataset squad original"
```

```txt

* Tags: dataset,get,language-processing,original,script-artifact-6651c119c3ae49b3,squad,validation,version-1.1
  Path: /home/arjun/CM/repos/local/cache/e5ac8a524ba64d09
  Version: 1.1
```



### Detect or install ONNX runtime for CPU

You can now detect or install the ONNX Python run-time on your system while targeting CPU
using this [generic CM script](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md#get-generic-python-lib)
to install any Python package to the default or virtual Python installation using so-called CM script variations prefixed by `_`:

```bash
cmr "get generic-python-lib _onnxruntime"
```

If needed, you can install a specific version of ONNX runtime using flag `--version`:
```bash
cmr "get generic-python-lib _onnxruntime" --version=1.16.1
```



### Download Bert-large model (FP32, ONNX format)

Download and cache this [reference model](https://huggingface.co/ctuning/mlperf-inference-bert-onnx-fp32-squad-v1.1) in the ONNX format (float32)
using the following [CM script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad):

```bash
cmr "get ml-model language-processing bert-large _onnx"
```

It takes around ~1GB of disk space. You can find it in the CM cache as follows:

```bash
cm show cache --tags=get,ml-model,bert-large,_onnx
```

```txt

*Tags: bert,bert-large,bert-squad,get,language,language-processing,ml-model,raw,script-artifact-5e865dbdc65949d2,_amazon-s3,_fp32,_onnx
  Path: /home/arjun/CM/repos/local/cache/8727a38b72aa4b3f
```

*Note that you will have a different CM UID consisting of 16 hexadecimal lowercase characters.*



### Pull MLPerf inference sources with reference implementations

You should now download and cache the MLPerf inference sources using the following command:

```bash
cmr "get mlperf inference src _repo.https://github.com/ctuning/inference _branch.scc23" \
     --version=custom
```

We use the [cTuning fork](https://github.com/ctuning/inference) of the [MLPerf inference repo](https://github.com/mlcommons/inference)
to make sure that there are no last-minute changes during SCC.

You can use your own fork if you want to improve/optimize benchmark implementations.


### Run short reference MLPerf inference benchmark to measure accuracy (offline scenario)

You are now ready to run the [reference (unoptimized) Python implementation](https://github.com/mlcommons/inference/tree/master/language/bert) 
of the MLPerf language benchmark with BERT model, [ONNX backend](https://github.com/mlcommons/inference/blob/master/language/bert/onnxruntime_SUT.py)
and Offline scenario while measuring accuracy. 

Normally, you would need to go through this [README.md](https://github.com/mlcommons/inference/blob/master/language/bert)
and use Docker containers or prepare all the dependencies and environment variables manually.

The [CM "app-mlperf-inference" script](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md#app-mlperf-inference)
allows you to run this benchmark in a native environment as follows (short test run with 10 samples):

```bash
cmr "app mlperf inference generic _python _bert-99 _onnxruntime _cpu" \
     --scenario=Offline \
     --mode=accuracy \
     --device=cpu \
     --execution-mode=test \
     --test_query_count=10 \
     --adr.mlperf-implementation.tags=_repo.https://github.com/ctuning/inference,_branch.scc23 \
     --adr.mlperf-implementation.version=custom \
     --adr.compiler.tags=gcc \
     --quiet \
     --rerun
```

This CM script will automatically find or install all dependencies
described in its [CM meta description](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference/_cm.yaml),
aggregate all environment variables, preprocess all files and assemble the MLPerf benchmark CMD. After running the benchmark, it calls the MLPerf accuracy script to evaluate the accuracy of the results. 

It will take a few minutes to run it and you should see the following accuracy:

```txt
{"exact_match": 70.0, "f1": 70.0}
Reading examples...
No cached features at 'eval_features.pickle'... converting from examples...
Creating tokenizer...
Converting examples to features...
Caching features at 'eval_features.pickle'...
Loading LoadGen logs...
Post-processing predictions..

```

Congratulations, you can now play with this benchmark using the unified CM interface!

Note that even if did not install all the above dependencies manually, the below command
will automatically install all the necessary dependencies.





### Run short MLPerf inference benchmark to measure performance (offline scenario)

Let's run the MLPerf language processing benchmark while measuring performance in offline scenario
(samples per second):

```bash
cmr "app mlperf inference generic _python _bert-99 _onnxruntime _cpu" \
     --scenario=Offline \
     --mode=performance \
     --execution-mode=test \
     --test_query_count=10 \
     --adr.mlperf-implementation.tags=_repo.https://github.com/ctuning/inference,_branch.scc23 \
     --adr.mlperf-implementation.version=custom \
     --adr.compiler.tags=gcc \
     --quiet \
     --rerun
```

It will run for a few seconds and you should see an output similar to the following one at the end
(the QPS is the performance result of this benchmark that depends on the speed of your system):

```txt

================================================
MLPerf Results Summary
================================================
SUT name : PySUT
Scenario : Offline
Mode     : PerformanceOnly
Samples per second: 3.71597
Result is : VALID
  Min duration satisfied : Yes
  Min queries satisfied : Yes
  Early stopping satisfied: Yes

================================================
Additional Stats
================================================
Min latency (ns)                : 267223684
Max latency (ns)                : 2691085775
Mean latency (ns)               : 1478150052
50.00 percentile latency (ns)   : 1612665856
90.00 percentile latency (ns)   : 2691085775
95.00 percentile latency (ns)   : 2691085775
97.00 percentile latency (ns)   : 2691085775
99.00 percentile latency (ns)   : 2691085775
99.90 percentile latency (ns)   : 2691085775

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
qsl_rng_seed : 148687905518835231
sample_index_rng_seed : 520418551913322573
schedule_rng_seed : 811580660758947900
accuracy_log_rng_seed : 0
accuracy_log_probability : 0
accuracy_log_sampling_target : 0
print_timestamps : 0
performance_issue_unique : 0
performance_issue_same : 0
performance_issue_same_index : 0
performance_sample_count : 10833

No warnings encountered during test.

No errors encountered during test.


```

Note that QPS is very low because we use an unoptimized reference implementation of this benchmark on CPU.



## Prepare minimal MLPerf submission to the SCC committee

You are now ready to generate the submission similar to the ones appearing
on the [official MLPerf inference dashboard](https://mlcommons.org/en/inference-edge-31).

We have developed another script that runs the MLPerf inference benchmark in both accuracy and performance mode,
runs the submission checker, unifies output for a dashboard and creates a valid MLPerf submission pack in `mlperf_submission_short.tar.gz` 
with all required MLPerf logs and stats.

You can run this script as follows:

```bash
cmr --tags=run,mlperf,inference,generate-run-cmds,_submission,_short \
      --submitter="SCC23" \
      --hw_name=default \
      --implementation=reference \
      --model=bert-99 \
      --backend=onnxruntime \
      --device=cpu \
      --scenario=Offline \
      --execution-mode=test \
      --test_query_count=10 \
      --adr.mlperf-implementation.tags=_repo.https://github.com/ctuning/inference,_branch.scc23 \
      --adr.mlperf-implementation.version=custom \
      --quiet \
      --output_tar=mlperf_submission_short.tar.gz \
      --output_summary=mlperf_submission_short_summary \
      --clean
```
* `--execution-mode=valid` can be used to do a full valid run and in this mode `--test_query_count` is ignored and the loadgen generates the number of queries for a 10-minute run based on `--target_qps` value from a previous run. We can also override this value by giving `--offline_target_qps=<>` in case the estimated value from a test run turns out to be inaccurate.
* We can also use custom (public/private) fork of the inference repository to enable custom changes to the harness code. For this you can change "ctuning" in the `https://github.com/ctuning/inference,_branch.scc23` to your username and can even change the branch name.


It will take a few minutes to run and you should see the following output in the end:

```txt

[2023-09-26 19:20:42,245 submission_checker1.py:3308 INFO] Results open/SCC23/results/default-reference-cpu-onnxruntime-v1.15.1-default_config/bert-99/offline 3.72101
[2023-09-26 19:20:42,245 submission_checker1.py:3310 INFO] ---
[2023-09-26 19:20:42,245 submission_checker1.py:3395 INFO] ---
[2023-09-26 19:20:42,245 submission_checker1.py:3396 INFO] Results=1, NoResults=0, Power Results=0
[2023-09-26 19:20:42,245 submission_checker1.py:3403 INFO] ---
[2023-09-26 19:20:42,245 submission_checker1.py:3404 INFO] Closed Results=0, Closed Power Results=0

[2023-09-26 19:20:42,245 submission_checker1.py:3409 INFO] Open Results=1, Open Power Results=0

[2023-09-26 19:20:42,245 submission_checker1.py:3414 INFO] Network Results=0, Network Power Results=0

[2023-09-26 19:20:42,245 submission_checker1.py:3419 INFO] ---
[2023-09-26 19:20:42,245 submission_checker1.py:3421 INFO] Systems=1, Power Systems=0
[2023-09-26 19:20:42,245 submission_checker1.py:3422 INFO] Closed Systems=0, Closed Power Systems=0
[2023-09-26 19:20:42,245 submission_checker1.py:3427 INFO] Open Systems=1, Open Power Systems=0
[2023-09-26 19:20:42,245 submission_checker1.py:3432 INFO] Network Systems=0, Network Power Systems=0
[2023-09-26 19:20:42,245 submission_checker1.py:3437 INFO] ---
[2023-09-26 19:20:42,245 submission_checker1.py:3442 INFO] SUMMARY: submission looks OK
/usr/bin/python3 /home/arjun/CM/repos/local/cache/0cfdde8a3bd64fb6/inference/tools/submission/generate_final_report.py --input summary.csv
=========================================================
Searching for summary.csv ...
Converting to json ...

                                                                           0
Organization                                                           SCC23
Availability                                                       available
Division                                                                open
SystemType                                                              edge
SystemName                                                           default
Platform                   default-reference-cpu-onnxruntime-v1.15.1-defa...
Model                                                                bert-99
MlperfModel                                                          bert-99
Scenario                                                             Offline
Result                                                               3.72101
Accuracy                                                                70.0
number_of_nodes                                                            1
host_processor_model_name                AMD Ryzen 9 7950X 16-Core Processor
host_processors_per_node                                                   1
host_processor_core_count                                                 16
accelerator_model_name                                                   NaN
accelerators_per_node                                                      0
Location                       open/SCC23/results/default-reference-cpu-o...
framework                                                onnxruntime v1.15.1
operating_system             Ubuntu 22.04 (linux-6.2.0-32-generic-glibc2.35)
notes                      Powered by MLCommons Collective Mind framework...
compliance                                                                 1
errors                                                                     0
version                                                                 v3.1
inferred                                                                   0
has_power                                                              False
Units                                                              Samples/s
```

Note that `--clean` flag cleans all previous runs of MLPerf benchmark to make sure that the MLPerf submission script picks up the latest results.

You will also see the following 4 files in your current directory:
```
ls -l

mlperf_submission_short.tar.gz
mlperf_submission_short_summary.csv
mlperf_submission_short_summary.json
mlperf_submission_short_summary.xlsx
```

Please submit `mlperf_submission_short.tar.gz`
and `mlperf_submission_short_summary.json`  
to the SCC'23 committee to get the first (minimum) set of points 
for managing to run MLPerf on your system.

Note that by default, CM-MLPerf will store the raw results 
in `$HOME/mlperf_submission` (with truncated accuracy logs) and in `$HOME/mlperf_submission_logs` 
(with complete and very large accuracy logs).

You can change this directory using the flag `--submission_dir={directory to store raw MLPerf results}`
in the above script.





## Run optimized implementation of the MLPerf inference benchmark



### Trying Nvidia implementation

Please follow [this README](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/bert/README_nvidia.md)


### Trying deepsparse backend

For deepsparse backend the implementation is coming from [this repo](https://github.com/neuralmagic/inference/tree/deepsparse)

#### int8
```
cmr --tags=run,mlperf,inference,generate-run-cmds,_submission,_short  \
   --implementation=reference \
   --model=bert-99 \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --execution-mode=test \
   --test_query_count=1024 \
   --adr.mlperf-inference-implementation.max_batchsize=128 \
   --env.CM_MLPERF_NEURALMAGIC_MODEL_ZOO_STUB=zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50_quant-none-vnni \
   --clean 
```

#### fp32
```
cmr --tags=run,mlperf,inference,generate-run-cmds,_submission,_short  \
   --adr.python.version_min=3.8 \
   --implementation=reference \
   --model=bert-99 \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --execution-mode=test \
   --test_query_count=1024 \
   --adr.mlperf-inference-implementation.max_batchsize=128 \
   --env.CM_MLPERF_NEURALMAGIC_MODEL_ZOO_STUB=zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50_quant-none-vnni \
   --clean 
```



## Optimize benchmark yourself




## Acknowledgments

This tutorial, MLCommons CM automation language and CM scripts and workflows for MLPerf
were developed by [Grigori Fursin](https://cKnowledge.org/gfursin) 
and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) ([cTuning foundation](https://cTuning.org) 
and [cKnowledge.org](https://cKnowledge.org)).

We thank Peter Mattson, David Kanter, Miro Hodak, Mitchelle Rasquinha, Vijay Janappa Reddi 
and [the community](../../CONTRIBUTING.md)
for their feedback, suggestions and contributions!

### Nvidia MLPerf inference backend

Nvidia's MLPerf inference implementation was developed by Zhihan Jiang, Ethan Cheng, Yiheng Zhang and Jinho Suh.

### DeepSparse MLPerf inference backend

We thank Michael Goin from Neural Magic for fruitful collaboration to add DeepSparse backend for x86-64 and Arm64 CPU targets
to MLPerf inference benchmarks and submit many competitive BERT results across diverse hardware 
to [MLPerf inference v3.1](https://neuralmagic.com/blog/latest-mlperf-inference-v3-1-results-show-50x-faster-ai-inference-for-x86-and-arm-from-neural-magic).
