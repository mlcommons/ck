# About

This portable CM script provides a unified API and CLI to benchmark ONNX models 
using the [MLPerf loadgen](https://github.com/mlcommons/inference/tree/master/loadgen).
It measures performance withou accuracy using randomly generated inputs. 
If you need accuracy too, please check [this portable CM script](../run-mlperf-inference-app).

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
cm run script "install python-venv" --name=loadgen
```

You can also install a specific version of Python on your system via:
```bash
cm run script "install python-venv" --name=loadgen --version=3.10.7
```

By default, CM will be asking users to select one from all detected and installed Python versions
including the above one, any time a script with python dependency is run. To avoid that, you 
can set up the following environment variable with the name of the current virtual environment:

```bash
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=loadgen"
```

The `--adr` flag stands for "Add to all Dependencies Recursively" and will find all sub-dependencies on other CM scripts 


## Manual installation of dependencies via CM

You can skip this sub-section if you want CM to automatically detect already installed
ONNX runtime on your system. Otherwise, follow the next steps to install the latest or specific
version of ONNX runtime.

### MLPerf loadgen

We can now install loadgen via CM while forcing compiler dependency to GCC:

```bash
cm run script "get mlperf loadgen" --adr.compiler.tags=gcc
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


## Run command

You can use CM variations prefixed by `_` to benchmark an official MLPerf model 
(_resnet50 or _retinanet):

```
cm run script "python app loadgen-generic _onnxruntime _resnet50"
```

Normally, you should see the following performance report from the loadgen:
```bash

2022-12-06 16:51:39,279 INFO MainThread - __main__ main: Model: /home/gfursin/CM/repos/local/cache/9c825a0a06fb48e2/resnet50_v1.onnx
2022-12-06 16:51:39,279 INFO MainThread - __main__ main: Runner: inline, Concurrency: 4
2022-12-06 16:51:39,279 INFO MainThread - __main__ main: Results: results/resnet50_v1.onnx/inline
2022-12-06 16:51:39,279 INFO MainThread - __main__ main: Test Started
2022-12-06 16:51:39,399 INFO MainThread - loadgen.harness load_query_samples: Loaded 100 samples
2022-12-06 16:51:55,723 INFO MainThread - loadgen.harness issue_query: Queries issued 550
2022-12-06 16:51:55,725 INFO MainThread - loadgen.harness flush_queries: Queries flushed
2022-12-06 16:51:55,731 INFO MainThread - loadgen.harness unload_query_samples: Unloaded samples
================================================
MLPerf Results Summary
================================================
SUT name : PySUT
Scenario : Offline
Mode     : PerformanceOnly
Samples per second: 33.6903
Result is : VALID
  Min duration satisfied : Yes
  Min queries satisfied : Yes
  Early stopping satisfied: Yes

================================================
Additional Stats
================================================
Min latency (ns)                : 16325180169
Max latency (ns)                : 16325180169
Mean latency (ns)               : 16325180169
50.00 percentile latency (ns)   : 16325180169
90.00 percentile latency (ns)   : 16325180169
95.00 percentile latency (ns)   : 16325180169
97.00 percentile latency (ns)   : 16325180169
99.00 percentile latency (ns)   : 16325180169
99.90 percentile latency (ns)   : 16325180169

================================================
Test Parameters Used
================================================
samples_per_query : 550
target_qps : 50
target_latency (ns): 0
max_async_queries : 1
min_duration (ms): 10000
max_duration (ms): 0
min_query_count : 1
max_query_count : 0
qsl_rng_seed : 0
sample_index_rng_seed : 0
schedule_rng_seed : 0
accuracy_log_rng_seed : 0
accuracy_log_probability : 0
accuracy_log_sampling_target : 0
print_timestamps : 0
performance_issue_unique : 0
performance_issue_same : 0
performance_issue_same_index : 0
performance_sample_count : 100

No warnings encountered during test.

No errors encountered during test.
2022-12-06 16:51:55,753 INFO MainThread - __main__ main: Observed QPS: 33.6903
2022-12-06 16:51:55,753 INFO MainThread - __main__ main: Result: VALID
2022-12-06 16:51:55,753 INFO MainThread - __main__ main: Test Completed
2022-12-06 16:51:55,753 INFO MainThread - loadgen.harness __exit__: <loadgen.runners.ModelRunnerInline object at 0x7f6c5c6a3580> : Exited
  - Running postprocess ...
  - running time of script "app,loadgen,generic,loadgen-generic,python": 370.87 sec.

```

You can also specify any custom onnx model file as follows:
```
cm run script --tags=python,app,loadgen-generic,_onnxruntime --modelpath=<CUSTOM_MODEL_FILE_PATH>
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


## Use modular Docker container with the CM API

Check sources [here](https://github.com/octoml/ck/tree/master/cm-mlops/script/app-loadgen-generic-python/modular-cm-containers).

### Build

```bash
cd `cm find script --tags=python,app,loadgen-generic`/modular-cm-containers
./build.sh
```

### Run
```bash
cd `cm find script --tags=python,app,loadgen-generic`/modular-cm-containers
./run.sh

cm run script --tags=python,app,loadgen-generic,_onnxruntime,_resnet50
```

If you want to use your own model, copy it to /tmp/cm-model.onnx and run docker as follows:
```bash
docker run -v /tmp:/tmp -it modularcm/loadgen-generic-python-cpu:ubuntu-22.04 -c \
  "cm run script --tags=python,app,loadgen-generic,_onnxruntime,_resnet50 --modelpath=/tmp/cm-model.onnx"

```




# Open discussions and developments

* [OctoML](https://octoml.ai)
* [MLCommons taskforce on education and reproducibility](https://cKnowledge.org/mlcommons-taskforce)

# Developers

* [Gaz Iqbal](https://www.linkedin.com/in/gaziqbal) (OctoML)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) (OctoML)
* [Grigori Fursin](https://cKnowledge.org/gfursin) (OctoML)
