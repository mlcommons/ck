This [portable CM script](https://access.cknowledge.org/playground/?action=scripts) 
provides a unified API and CLI to benchmark ONNX models 
using the [MLPerf loadgen](https://github.com/mlcommons/inference/tree/master/loadgen).
It measures performance without accuracy using randomly generated inputs. 
If you need accuracy too, please check [official CM automation for MLPerf inference](../run-mlperf-inference-app).

## Development status

* [20240214] ONNX runtime (CPU & GPU) is connected with LoadGen and tested on Ubuntu, Windows and MacOS.
  See [sources](src/ort.py).

## Prerequisites

### Install CM with automation recipes

Install [MLCommons CM](https://github.com/mlcommons/ck/blob/master/docs/installation.md) 
and pull CM repository with portable automation scripts to benchmark ML Systems:

```bash
pip install cmind
cm pull repo mlcommons@ck
```

### Clean CM cache

If you want a "clean" environment, you may want to clean your CM cache as follows:
```bash
cm rm cache -f
```

### Set up CM virtual environment

<details>
<summary><b>Click if you want to use Python virtual environment</b></summary>

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

</details>


### Install dependencies via CM (optional)

<details>
<summary><b>Click if you want to install specific versions of dependencies</b></summary>

You can skip this sub-section if you want CM to automatically detect already installed
ONNX runtime on your system. Otherwise, follow the next steps to install the latest or specific
version of ONNX runtime.


### Download LoadGen sources from MLPerf inference benchmark

```bash
cm run script "get mlperf inference src" --version=r3.1
```

### Install MLPerf LoadGen
We can now install loadgen via CM while forcing compiler dependency to GCC:

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
</details>

### Benchmark standard MLPerf model

You can use CM variations prefixed by `_` to benchmark an official MLPerf model 
(_resnet50 or _retinanet):

```
cm run script "python app loadgen-generic _onnxruntime _retinanet" --samples=5
cmr "python app loadgen-generic _onnxruntime _resnet50"
```

Normally, you should see the following performance report from the loadgen:




<details>
<summary><b>Click to open</b></summary>

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

  - Running postprocess ...
  - running time of script "app,loadgen,generic,loadgen-generic,python": 370.87 sec.

```

</details>


### Benchmark custom model

You can also specify any custom onnx model file as follows:

```bash
cm run script "python app loadgen-generic _onnxruntime" --modelpath=<CUSTOM_MODEL_FILE_PATH>
```

### Benchmark Hugging Face model

```bash
cmr "python app loadgen-generic _onnxruntime _custom _huggingface _model-stub.ctuning/mlperf-inference-bert-onnx-fp32-squad-v1.1" --adr.hf-downloader.model_filename=model.onnx
```

*See more examples to download Hugging Face models via CM [here](../get-ml-model-huggingface-zoo/README-extra.md).*

### Benchmark using ONNX CUDA

```bash
cm rm cache -f
cmr "python app loadgen-generic _onnxruntime _cuda _retinanet" --quiet
cmr "python app loadgen-generic _onnxruntime _cuda _custom _huggingface _model-stub.ctuning/mlperf-inference-bert-onnx-fp32-squad-v1.1" --adr.hf-downloader.model_filename=model.onnx
```

These cases worked on Windows and Linux but may require GPU with > 8GB memory:
```bash
cmr "python app loadgen-generic _onnxruntime _cuda _custom _huggingface _model-stub.steerapi/Llama-2-7b-chat-hf-onnx-awq-w8" --adr.hf-downloader.model_filename=onnx/decoder_model_merged_quantized.onnx,onnx/decoder_model_merged_quantized.onnx_data --samples=2
cmr "python app loadgen-generic _onnxruntime _cuda _custom _huggingface _model-stub.alpindale/Llama-2-13b-ONNX" --adr.hf-downloader.model_filename=FP32/LlamaV2_13B_float32.onnx --adr.hf-downloader.full_subfolder=FP32 --samples=2
cmr "python app loadgen-generic _onnxruntime _cuda _custom _huggingface _model-stub.Intel/gpt-j-6B-int8-static" --adr.hf-downloader.model_filename=model.onnx --adr.hf-downloader.full_subfolder=. --samples=2
```

TBD: some cases that are not yet fully supported (data types, input mismatch, etc):
```bash
cmr "python app loadgen-generic _onnxruntime _custom _huggingface _model-stub.runwayml/stable-diffusion-v1-5" --adr.hf-downloader.revision=onnx --adr.hf-downloader.model_filename=unet/model.onnx,unet/weights.pb --samples=2
cmr "python app loadgen-generic _onnxruntime _cuda _custom _huggingface _model-stub.microsoft/Mistral-7B-v0.1-onnx" --adr.hf-downloader.model_filename=Mistral-7B-v0.1.onnx,Mistral-7B-v0.1.onnx.data  --samples=2
cmr "python app loadgen-generic _onnxruntime _cuda _custom _huggingface _model-stub.alpindale/Llama-2-7b-ONNX" --adr.hf-downloader.model_filename=FP16/LlamaV2_7B_float16.onnx --adr.hf-downloader.full_subfolder=FP16 --samples=2
```

### Other variations and flags:

You can obtain help about flags and variations from CMD:

```bash
cm run script "python app loadgen-generic" --help

Available variations:

  _cpu
  _cuda
  _custom
  _custom,huggingface
  _huggingface
  _model-stub.#
  _onnxruntime
  _pytorch
  _resnet50
  _retinanet

Available flags mapped to environment variables:

  --concurrency  ->  --env.CM_MLPERF_CONCURRENCY
  --ep  ->  --env.CM_MLPERF_EXECUTION_PROVIDER
  --execmode  ->  --env.CM_MLPERF_EXEC_MODE
  --interop  ->  --env.CM_MLPERF_INTEROP
  --intraop  ->  --env.CM_MLPERF_INTRAOP
  --modelpath  ->  --env.CM_ML_MODEL_FILE_WITH_PATH
  --output_dir  ->  --env.CM_MLPERF_OUTPUT_DIR
  --runner  ->  --env.CM_MLPERF_RUNNER
  --samples  ->  --env.CM_MLPERF_LOADGEN_SAMPLES
  --scenario  ->  --env.CM_MLPERF_LOADGEN_SCENARIO

```

## Running this app via Docker

```bash
cm docker script "python app loadgen-generic _onnxruntime _custom _huggingface _model-stub.ctuning/mlperf-inference-bert-onnx-fp32-squad-v1.1" --adr.hf-downloader.model_filename=model.onnx  --samples=2 --output_dir=new_results --docker_cm_repo=ctuning@mlcommons-ck
```

## Tuning CPU performance via CM experiment

```bash
cm run experiment --tags=loadgen,python,llama2 -- cmr script "python app loadgen-generic _onnxruntime _cuda _custom _huggingface _model-stub.steerapi/Llama-2-7b-chat-hf-onnx-awq-w8" --adr.hf-downloader.model_filename=onnx/decoder_model_merged_quantized.onnx,onnx/decoder_model_merged_quantized.onnx_data --samples=2 --intraop={{CM_OPT_INTRAOP{[1,2,4]}}} --interop={{CM_OPT_INTEROP{[1,2,4]}}} --quiet
cm run experiment --tags=loadgen,python,llama2 -- cmr "python app loadgen-generic _onnxruntime" --modelpath={PATH TO ONNX MODEL} --samples=2 --intraop={{CM_OPT_INTRAOP{[1,2,4]}}} --interop={{CM_OPT_INTEROP{[1,2,4]}}} --quiet
```


## Developers

* [Gaz Iqbal](https://www.linkedin.com/in/gaziqbal)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)
* [Grigori Fursin](https://cKnowledge.org/gfursin)

## Get in touch

* [MLCommons Task Force on Automation and Reproducibility](../../../docs/taskforce.md)
* [Public Discord server](https://discord.gg/JjWNWXKxwT)
