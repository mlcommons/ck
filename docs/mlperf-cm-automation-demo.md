# CM demo: modularizing MLPerf benchmarks and automating submissions

## Motivation

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
to bootstrap any given workflow (such as MLPerf benchmark) without even interfering with the system setup!

Here is a typical minimal CM setup on Ubuntu:

```bash
sudo apt-get install python3 python3-pip git wget
```

```bash
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

<details>
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
</details>

## Run MLPerf vision benchmark - ResNet-50 - ImageNet 100 images - ONNX - offline - accuracy

You can now run the MLPerf vision benchmark r2.1 with default parameters 
(reduced ImageNet with 100 original images, ResNet-50 model in ONNX format, 
ONNX runtime, offline MLPerf scenario and accuracy mode)
using the following CM command:

```bash
cm run script --tags=app,mlperf,inference,ref,python,_resnet50,_onnxruntime,_cpu,_r2.1_default --quiet
```

<details>
CM will automatically search for a portable CM script with a combination of above tags 
(without *_* prefix that will be explained later) in all CM repositories installed on your system -
this allows organizations to easily combine public and private automation scripts and artifacts!

CM will simply read all [*_cm.json*](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json) files
in CM repositories and compare the above combination of tags with a "tags" key.

CM will then run the [found script](https://github.com/octoml/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference) 
according to its human readable meta description provided in either *_cm.json*
or *_cm.yaml* file as shown [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json).

Tags with "_" prefix are called variations and help users customize the workflow 
by forcing some environment variables, flags and dependencies
for specific releases and purposes (see the key "variations" in *_cm.json* 
for all available variations for the above MLPerf
workflow [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json#L193).

For example, variation *resnet50* forces this MLPerf workflow to download and use ResNet-50 model,
variation *onnxruntime* forces this workflow to detect or install ONNX runtime
and variation *r2.1_default* forces this workflow to skip installing system utils,
sets query count to 100, forces the use of LLVM compiler,
forces the download and installation of loadgen for official MLPerf submission v2.1,
and forces overwriting of benchmarking results in consecutive runs.

The flag *quiet* tells CM to select default scripts when more than one script is found in dependencies
and to skip all questions. 

</details>

It will take 3..10 minutes to automatically detect, download and/or install all necessary ML components
required for this CM MLPerf workflow (which is also a portable CM script with 
simple [dependencies on other CM scripts](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json#L5))
depending on the speed of your Internet connection.

At the end of the execution, you should see accuracy reported by MLPerf infrastructure and postprocessed by the CM script:
```
accuracy=80.000%, good=80, total=100
```

## Use CM cache (automatic)

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

You can also clean the CM cache for specific CM components such as datasets as follows:
```bash
cm rm cache -f --tags=dataset
```

This will force CM to download and/or reinstall required components during the subsequent run of a given workflow.


## Use different engine version

You can also install a different version of ONNX runtime (or any other component) 
using the corresponding CM script as follows:
```bash
cm run script --tags=get,onnxruntime --version=1.10.0
```
The next time, you run the MLPerf benchmark via CM without *--quiet* flag, 
it will detect several cached versions of TVM and will ask you which one to plug into the workflow
before running the benchmark.

Such plug&play CM approach allows to automtically test the accuracy of MLPerf benchmark and detect errors 
in new or different versions of engines, libraries, models and tools.


## Customize MLPerf vision benchmark

You can customize the execution of CM scripts using variations (tags with *_* prefix), 
environment variables (flag *--env.VAR=VALUE*), 
dependencies (flag --add_deps_recursive.DEPENDENCY_NAME.tags=EXTRA TAGS),
and other flags that are converted to CM_flag environment variables:

```bash
cm run script --tags=app,mlperf,inference,ref,python,_resnet50,_onnxruntime,_cpu \
   --output_dir=$HOME/results \
   --add_deps_recursive.imagenet.tags=_2012-500 \
   --add_deps_recursive.compiler.tags=llvm \
   --add_deps_recursive.inference-src.tags=_octoml \
   --add_deps_recursive.loadgen.version=r2.1 \
   --env.CM_SKIP_SYS_UTILS=yes \
   --env.CM_RERUN=yes \
   --env.CM_TEST_QUERY_COUNT=100 \
   --env.CM_LOADGEN_MODE=accuracy \
   --env.CM_LOADGEN_SCENARIO=Offline \
   --env.CM_SUT_NAME=gcp-n2-standard-80-onnxruntime
```

## Run MLPerf vision benchmark - ResNet-50 - ImageNet 100 images - ONNX - offline - performance

For exampe, you can run the same MLPerf workflow to measure performance in offline mode using the following command:
```bash
cm run script --tags=app,mlperf,inference,ref,python,_resnet50,_onnxruntime,_cpu,_r2.1_default \
              --env.CM_LOADGEN_MODE=performance --quiet
```

CM will reuse all cached MLPerf components, files and environment variables and will quickly start measuring performance on the ResNet-50 model.
You should see the MLPerf benchmarking report after a successful run:

```
================================================
MLPerf Results Summary
================================================
SUT name : PySUT
Scenario : Offline
Mode     : PerformanceOnly
Samples per second: 410.191
Result is : INVALID
  Min duration satisfied : NO
  Min queries satisfied : Yes
  Early stopping satisfied: Yes
Recommendations:
 * Increase expected QPS so the loadgen pre-generates a larger (coalesced) query.

================================================
Additional Stats
================================================
Min latency (ns)                : 652722667
Max latency (ns)                : 1609007888
Mean latency (ns)               : 1236473032
50.00 percentile latency (ns)   : 1377611126
90.00 percentile latency (ns)   : 1604137492
95.00 percentile latency (ns)   : 1604775709
97.00 percentile latency (ns)   : 1609007888
99.00 percentile latency (ns)   : 1609007888
99.90 percentile latency (ns)   : 1609007888

================================================
Test Parameters Used
================================================
samples_per_query : 660
target_qps : 1
target_latency (ns): 0
max_async_queries : 1
min_duration (ms): 600000
max_duration (ms): 0
min_query_count : 1
max_query_count : 100
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

```

Note that MLPerf reports this run as INVALID because we force MLPerf to run just a few seconds for a demo instead of 10 minutes.


## Run MLPerf vision benchmark - ResNet-50 - ImageNet 100 images - ONNX - server - performance

We can now run the same workflow in the server mode as follows:

```bash
cm run script --tags=app,mlperf,inference,ref,python,_resnet50,_onnxruntime,_cpu,_r2.1_default  \
  --env.CM_LOADGEN_MODE=performance \
  --env.CM_LOADGEN_SCENARIO=Server \
  --quiet
```

CM will print the MLPerf results summary in case of the successful run:

```
================================================
MLPerf Results Summary
================================================
SUT name : PySUT
Scenario : Server
Mode     : PerformanceOnly
Scheduled samples per second : 100.67
Result is : INVALID
  Performance constraints satisfied : NO
  Min duration satisfied : NO
  Min queries satisfied : Yes
  Early stopping satisfied: NO
Recommendations:
 * Reduce target QPS to improve latency.
 * Increase the target QPS so the loadgen pre-generates more queries.
Early Stopping Result:
 * Run unsuccessful.
 * Processed 100 queries.
 * Would need to run at least 12471 more queries,
 with the run being successful if every additional
 query were under latency.

================================================
Additional Stats
================================================
Completed samples per second    : 30.23

Min latency (ns)                : 121384491
Max latency (ns)                : 2398618166
Mean latency (ns)               : 1340836884
50.00 percentile latency (ns)   : 1368839459
90.00 percentile latency (ns)   : 2271155990
95.00 percentile latency (ns)   : 2343500573
97.00 percentile latency (ns)   : 2366839679
99.00 percentile latency (ns)   : 2398618166
99.90 percentile latency (ns)   : 2398618166

================================================
Test Parameters Used
================================================
samples_per_query : 1
target_qps : 100
target_latency (ns): 15000000
max_async_queries : 0
min_duration (ms): 600000
max_duration (ms): 0
min_query_count : 100
max_query_count : 100
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

1 ERROR encountered. See detailed log.
```

Note that MLPerf reports this run as INVALID because we force MLPerf to run just a few seconds for a demo instead of 10 minutes. 
The one reported ERROR is because the early stopping requirement failed due to runtime being less than 10 minutes.

## Run MLPerf vision benchmark - RetinaNet - Open Images - ONNX - offline - accuracy

Instead of running MLPerf image classification, we can run object detection with RetinaNet 
model and Open Images dataset using the same CM automation workflow as follows:

```bash
cm run script --tags=app,mlperf,inference,ref,python,_retinanet,_onnxruntime,_cpu,_r2.1_default \
  --env.CM_LOADGEN_MODE=accuracy \
  --env.CM_LOADGEN_SCENARIO=Offline \
  --quiet
```

CM will print mAP after the successful run:

```
loading annotations into memory...
Done (t=2.47s)
creating index...
index created!
Loading and preparing results...
DONE (t=0.35s)
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=4.45s).
Accumulating evaluation results...
DONE (t=3.21s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.543
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.751
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.574
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.209
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.259
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.598
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.497
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.633
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.642
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.249
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.391
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.683
mAP=54.314%

```

Note that this CM workflow will automatically download RetinaNet model using this 
[portable CM script](https://github.com/octoml/ck/tree/master/cm-mlops/script/get-ml-model-resnext50) 
and Open Images using another [portable CM script](https://github.com/octoml/ck/tree/master/cm-mlops/script/get-openimages-original)
while reusing all other cached dependencies.

You can check that CM successfully cached this model and dataset as follows:

```bash
cm show cache --tags=ml-model
cm show cache --tags=dataset
```
You can even find them and reuse them in other projects as follows:

```bash
cm find cache --tags=dataset,openimages

ls `cm find cache --tags=dataset,openimages`/install
ls `cm find cache --tags=ml-model,retinanet`/install
```

## Run MLPerf vision benchmark - ResNet-50 - ImageNet 100 images - TVM - offline - accuracy

CM workflows allow to plug other ML engines to MLPerf such as TVM (or PyTorch, TF, TFLite, etc) 
in the same workflow. For example, we can run the same MLPerf vision benchmark with already
cached components and TVM backend (that OctoML recently added to MLPerf):

```bash
cm run script --tags=app,mlperf,inference,ref,python,_resnet50,_tvm-onnx,_cpu,_r2.1_default \
  --env.CM_LOADGEN_MODE=accuracy \
  --env.CM_LOADGEN_SCENARIO=Offline \
  --add_deps.inference-src.tags=_tvm \
  --quiet
```

The CM workflow will automatically download and build TVM together with other dependencies
including cmake, llvm, and then run MLPerf with the new engine. 
Normally, you should see the same accuracy as with ONNX runtime
at the end of the workflow execution:

```
accuracy=80.000%, good=80, total=100
```

## Automate MLPerf submission

Finally, we created another portable CM script as a wrapper to above MLPerf workflow 
to automatically generate and validate MLPerf submissions:

```bash
cm run script --tags=generate-run-cmds,_submission \
  --add_deps_recursive.inference-src.tags=_octoml \
  --add_deps_recursive.compiler.tags=llvm \
  --add_deps_recursive.loadgen.version=r2.1 \
  --env.CM_MODEL=resnet50 \
  --env.CM_DEVICE=cpu \
  --env.CM_BACKEND=onnxruntime \
  --env.CM_HW_NAME=gcp-n2-standard-80 \
  --env.CM_MLC_SUBMITTER=OctoML
```

You can find submittable results in the $HOME/results directory.

We continue improving this script with the community in the [open workgroup](mlperf-education-workgroup.md)
to make it easier for organizations to run MLPerf benchmark and submit valid results.


## The next steps

We suggest you to check the following [CM tutorial](../cm/docs/tutorial-scripts.md)
to understand the concept of portable CM scripts and workflows.

Feel free to follow the [MLCommons CM project](https://github.com/mlcommons/ck),
and join our [open education workgroup](mlperf-education-workgroup.md) 
to participate in this community project.

Don't hesitate to open a [ticket](https://github.com/mlcommons/ck/issues) 
if you have questions about CM, automation scripts and MLPerf workflows.
