[ [Back to index](README.md) ]

*Note: from Feb 2024, we suggest you to use [this GUI](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725)
 to configure MLPerf inference benchmark, generate CM commands to run it across different implementations, models, data sets, software
 and hardware, and prepare your submissions.*

# Tutorial: modularizing and automating MLPerf Inference Language Processing model bert



# Introduction

It should take less than an hour to complete this tutorial. In the end, you should obtain a tarball (`mlperf_submission.tar.gz`) with the MLPerf-compatible results.

*Note that both MLPerf and CM automation are evolving projects.
 If you encounter issues or have questions, please submit them [here](https://github.com/mlcommons/ck/issues)
 and feel free to join our [public discord channel](https://discord.gg/8jbEM4J6Ff).*

# System preparation

## Minimal system requirements

* CPU: 1 node (x86-64 or Arm64)
* OS: we have tested this automation on Ubuntu 20.04, Ubuntu 22.04, Debian 10, Red Hat 9 and MacOS 13
* Disk space: ~ 10GB
* Python: 3.8+
* All other dependencies (artifacts and tools) will be installed by the CM meta-framework

## System requirements to run MLPerf on Nvidia GPU
* GPU: any Nvidia GPU with 8GB+ or memory
* Disk space: ~ 30GB



# MLCommons CM automation meta-framework

The MLCommons is developing an open-source and technology-neutral 
[Collective Mind meta-framework (CM)](https://github.com/mlcommons/ck)
to modularize ML Systems and automate their benchmarking, optimization 
and design space exploration across continuously changing software, hardware and data.

CM is the second generation of the [MLCommons CK workflow automation framework](https://doi.org/10.1098/rsta.2020.0211) 
that was originally developed to make it easier to [reproduce research papers at ML and Systems conferences](https://learning.acm.org/techtalks/reproducibility).
The goal is to help researchers unify and automate all the steps to prepare and run MLPerf and other benchmarks
across diverse ML models, datasets, frameworks, compilers and hardware (see [HPCA'22 presentation](https://doi.org/10.5281/zenodo.6475385) about our motivation).



## CM installation

Follow [this guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md) to install the MLCommons CM automation language on your system.

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

*Our goal is to keep CM language and scripts backward compatible.*

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

```txt
mlcommons@ck,a4705959af8e447a = /home/ubuntu/CM/repos/mlcommons@ck
```


## Install system dependencies for your platform

First, you need to install various system dependencies required by the MLPerf inference benchmark.

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
you can run this script without `--quiet` flag and type "skip" in the script prompt.



## Use CM to detect or install Python 3.8+

Since we use Python reference implementation of the MLPerf inference benchmark (unoptimized),
we need to detect or install Python 3.8+ (MLPerf requirement). 

You need to detect it using the following [CM script](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md#get-python3):

```bash
cm run script "get python" --version_min=3.8
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

You can see the environment variables produced by this CM script in the following JSON file:
```bash
cat `cm find cache --tags=get,python`/cm-cached-state.json
```

If required Python is not detected, CM will automatically attempt to download and build it from sources 
using another [cross-platform CM script "install-python-src"](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md#install-python-src).
In the end, CM will also cache new binaries and related environment variables such as PATH, PYTHONPATH, etc:

```bash
cm show cache
```

You can find installed binaries and reuse them in your own project with or without CM as follows:
```bash
cm find cache --tags=install,python
```

Note that if you run the same script again, CM will automatically find and reuse the cached output:
```bash
cm run script "get python" --version_min=3.8 --out=json
```

## Setup a virtual environment for Python

```bash
cm run script "install python-venv" --name=mlperf
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```


## Pull MLPerf inference sources

You should now download and cache the MLPerf inference sources using the following command:

```bash
cm run script "get mlperf inference src"
```

## Compile MLPerf loadgen

You need to compile loadgen from the above inference sources:


```bash
cm run script "get mlperf loadgen"
```

# CM automation for the MLPerf benchmark

## MLPerf inference - Python - Bert FP32 - SQUAD v1.1 - ONNX - CPU - Offline

### Download the SQuAD dataset


```bash
cm run script "get dataset squad original"
```

After installing this dataset via CM, you can reuse it in your own projects or other CM scripts (including MLPerf benchmarks).
You can check the CM cache as follows (the unique ID of the CM cache entry will be different on your machine):
```bash
cm show cache --tags=get,dataset,squad,original
```

```txt

* Tags: dataset,get,language-processing,original,script-artifact-6651c119c3ae49b3,squad,validation,version-1.1
  Path: /home/arjun/CM/repos/local/cache/e5ac8a524ba64d09
  Version: 1.1
```



### Install ONNX runtime for CPU

Now detect or install ONNX Python runtime (targeting CPU) your system
using a [generic CM script](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md#get-generic-python-lib) to install python package:

```bash
cm run script "get generic-python-lib _onnxruntime"
```





### Download Bert-large model (FP32, ONNX format)

Download and cache this [reference model](https://paperswithcode.com/model/resnext?variant=resnext-50-32x4d) in the ONNX format (float32)
using the following [CM script](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md#get-ml-model-retinanet):

```bash
cm run script "get ml-model language-processing bert-large _onnx"
```

It takes around ~1GB of disk space. You can find it in the CM cache as follows:

```bash
cm show cache --tags=get,ml-model,bert-large,_onnx
```

```txt

*Tags: bert,bert-large,bert-squad,get,language,language-processing,ml-model,raw,script-artifact-5e865dbdc65949d2,_amazon-s3,_fp32,_onnx
  Path: /home/arjun/CM/repos/local/cache/8727a38b72aa4b3f
```

### Run reference MLPerf inference benchmark (offline, accuracy)

You are now ready to run the [reference (unoptimized) Python implementation](https://github.com/mlcommons/inference/tree/master/vision/classification_and_detection/python) 
of the MLPerf vision benchmark with [ONNX backend](https://github.com/mlcommons/inference/blob/master/vision/classification_and_detection/python/backend_onnxruntime.py).

Normally, you would need to go through this [README.md](https://github.com/mlcommons/inference/tree/master/vision/classification_and_detection)
and prepare all the dependencies and environment variables manually.

The [CM "app-mlperf-inference" script](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md#app-mlperf-inference)
allows you to run this benchmark as follows:

```bash
cm run script "app mlperf inference generic _python _bert-99 _onnxruntime _cpu" \
     --scenario=Offline \
     --mode=accuracy \
     --test_query_count=10 \
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

Congratulations, you can now play with this benchmark using the unified CM commands!

Note that even if did not install all the above dependencies manually, the below command
will automatically install all the necessary dependencies.

```bash

cm run script "app mlperf inference generic _python _bert-99 _onnxruntime _cpu" \
     --adr.python.version_min=3.8 \
     --adr.compiler.tags=gcc \
     --scenario=Offline \
     --mode=accuracy \
     --test_query_count=10 \
     --quiet \
     --rerun
```


### Run MLPerf inference benchmark (offline, performance)

Let's run the MLPerf object detection while measuring performance:

```bash
cm run script "app mlperf inference generic _python _bert-99 _onnxruntime _cpu" \
     --scenario=Offline \
     --mode=performance \
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



### Prepare MLPerf submission

You are now ready to generate the submission similar to the ones appearing
on the [official MLPerf inference dashboard](https://mlcommons.org/en/inference-edge-21).

We have developed another script that runs the MLPerf inference benchmark in both accuracy and performance mode,
runs the submission checker, unifies output for a dashboard and creates a valid MLPerf submission pack in `mlperf_submission.tar.gz` 
with all required MLPerf logs and stats.

You can run this script as follows:

```bash
cm run script --tags=run,mlperf,inference,run-mlperf,_submission,_short \
      --submitter="Community" \
      --hw_name=default \
      --implementation=reference \
      --model=bert-99 \
      --backend=onnxruntime \
      --device=cpu \
      --scenario=Offline \
      --test_query_count=10 \
      --clean
```      

It will take a few minutes to run and you should see the following output in the end:

```txt

[2023-09-26 19:20:42,245 submission_checker1.py:3308 INFO] Results open/Community/results/default-reference-cpu-onnxruntime-v1.15.1-default_config/bert-99/offline 3.72101
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
Organization                                                       Community
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
Location                   open/Community/results/default-reference-cpu-o...
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

You will also see the following 3 files in your current directory:
```
ls -l
mlperf_submission.tar.gz
summary.csv
summary.json
```

Note that by default, CM-MLPerf will store the raw results 
in `$HOME/mlperf_submission` (with truncated accuracy logs) and in `$HOME/mlperf_submission_logs` 
(with complete and very large accuracy logs).

You can change this directory using the flag `--submission_dir={directory to store raw MLPerf results}`
in the above script.

## Trying deepsparse backend

### int8
```
cm run script --tags=run,mlperf,inference,run-mlperf,_submission,_short  \
   --implementation=reference \
   --model=bert-99 \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --test_query_count=1024 \
   --adr.mlperf-inference-implementation.max_batchsize=128 \
   --env.CM_MLPERF_NEURALMAGIC_MODEL_ZOO_STUB=zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50_quant-none-vnni \
   --clean 
```
### fp32
```
cm run script --tags=run,mlperf,inference,run-mlperf,_submission,_short  \
   --adr.python.version_min=3.8 \
   --implementation=reference \
   --model=bert-99 \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --test_query_count=1024 \
   --adr.mlperf-inference-implementation.max_batchsize=128 \
   --env.CM_MLPERF_NEURALMAGIC_MODEL_ZOO_STUB=zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50_quant-none-vnni \
   --clean 
```

## Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
