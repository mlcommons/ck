## Setup

Please follow this [installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md) 
to install the MLCommons CM reproducibility and automation language in your native environment or Docker container.

Then install the repository with CM automation scripts to run MLPerf benchmarks out-of-the-box
across different software, hardware, models and data sets:


```
cm pull repo mlcommons@ck
```

Note that you can install Python virtual environment via CM to avoid contaminating 
your local Python installation as described [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/script/README-extra.md#using-python-virtual-environments).

## Run Commands

Bert has two variants - `bert-99` and `bert-99.9` where the `99` and `99.9` specifies the required accuracy constraint with respect to the reference floating point model. `bert-99.9` model is applicable only on a datacenter system.

On edge category `bert-99` has Offline and SingleStream scenarios and in datacenter category both `bert-99` and `bert-99.9` have Offline and Server scenarios. The below commands are assuming an edge category system. 

### Onnxruntime backend (Reference implementation)

#### Do a test run to detect and record the system performance

```
cm run script --tags=generate-run-cmds,inference,_find-performance,_all-scenarios \
--model=bert-99 --implementation=reference --device=cpu --backend=onnxruntime \
--category=edge --division=open --quiet
```
* Use `--device=cuda` to run the inference on Nvidia GPU
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* Use `--category=datacenter` to run datacenter scenarios

#### Do a full accuracy and performance runs for all the scenarios

```
cm run script --tags=generate-run-cmds,inference,_all-modes,_all-scenarios \
--model=bert-99 --device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/inference_3.1_results \
--category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs. This requires a power analyzer as described [here](https://github.com/ctuning/mlcommons-ck/blob/master/docs/tutorials/mlperf-inference-power-measurement.md)
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps` and `--singlestream_target_latency` can be used to override the determined performance numbers

#### Populate the README files
```
cm run script --tags=generate-run-cmds,inference,_populate-readme,_all-scenarios \
--model=bert-99 --device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/inference_3.1_results \
--category=edge --division=open --quiet
```

#### Generate actual submission tree

Here, we are copying the performance and accuracy log files (compliance logs also in the case of closed division) from the results directory to the submission tree following the [directory structure required by MLCommons Inference](https://github.com/mlcommons/policies/blob/master/submission_rules.adoc#inference-1). After the submission tree is generated, [accuracy truncate script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log) is called to truncate accuracy logs and then the [submission checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker) is called to validate the generated submission tree.

We should use the master branch of MLCommons inference repo for the submission checker. You can use `--hw_note_extra` option to add your name to the notes.
```
cm run script --tags=generate,inference,submission --results_dir=$HOME/inference_3.1_results/valid_results \
--device=cpu --submission_dir=$HOME/inference_submission_tree --clean --run-checker --submitter=cTuning 
--adr.inference-src.version=master --hw_notes_extra="Result taken by NAME" --quiet
```


## Tensorflow backend (Reference implementation)

Same commands as for `onnxruntime` should work by replacing `backend=onnxruntime` with `--backend=tf`. For example,

```
cm run script --tags=generate-run-cmds,inference,_accuracy-only,_all-scenarios \
--model=bert-99 --device=cpu --implementation=reference --backend=tf --execution-mode=valid \
--results_dir=$HOME/inference_3.1_results --quiet
```

## Pytorch backend (Reference implementation)

Same commands as for `onnxruntime` should work by replacing `backend=onnxruntime` with `--backend=pytorch`. For example,

```
cm run script --tags=generate-run-cmds,inference,_accuracy-only,_all-scenarios \
--model=bert-99 --device=cpu --implementation=reference --backend=pytorch \
--execution-mode=valid --results_dir=$HOME/inference_3.1_results --quiet
```

## TensorRT backend (Nvidia implementation)

For TensorRT backend we are using the [Nvidia implementation](https://github.com/ctuning/mlcommons-ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia) and not the [MLPerf inference reference implementation](https://github.com/ctuning/mlcommons-ck/tree/master/cm-mlops/script/app-mlperf-inference-reference) for the below reasons
* TensorRT backend is not supported by default in the reference implementation
* Reference implemnetation is mostly for fp32 models and quantization is not suppoted by default
* Nvidia has done some fantastic work in optimizing performance for TensorRT backend

To get setup please follow the instructions [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/README-about.md) to download and install TensorRT and cuDNN unless you already have them installed. This readme also details how to handle the configuration files which are automatically generated by the Nvidia implementation scripts. Once this is done, the following command will run all the modes and scenarios.

```
cm run script --tags=generate-run-cmds,inference,_all-modes,_all-scenarios \
--model=bert-99 --device=cuda --implementation=nvidia-original --backend=tensorrt \
--execution-mode=valid --results_dir=$HOME/inference_3.1_results --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs. This requires a power analyzer as described [here](https://github.com/ctuning/mlcommons-ck/blob/master/docs/tutorials/mlperf-inference-power-measurement.md)
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps` and `--singlestream_target_latency` can be used to override the default performance numbers
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* Use `--category=datacenter` to run datacenter scenarios


TensorRT backend has an engine generation stage which can be time consuming. For repeated runs `--adr.nvidia-harness.make_cmd=run_harness` option will avoid this engine regeneration and reuse the previously generated one.


