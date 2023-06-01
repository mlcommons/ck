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

We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset and register in CM.

On edge category ResNet50 has Offline, SingleStream and MultiStream scenarios and in datacenter category it has Offline and Server scenarios. The below commands are assuming an edge category system. 

### Onnxruntime backend

#### Do a test run to detect and record the system performance

```
cm run script --tags=generate-run-cmds,inference,_find-performance,_all-scenarios \
--model=resnet50 --implementation=reference --device=cpu --backend=onnxruntime \
--category=edge --division=open --quiet
```
* Use `--device=cuda` to run the inference on Nvidia GPU
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--category=datacenter` to run datacenter scenarios

#### Do a full accuracy and performance runs for all the scenarios

```
cm run script --tags=generate-run-cmds,inference,_all-modes,_all-scenarios --model=resnet50 \
--device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/inference_3.1_results \
--category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, `--singlestream_target_latency` and `multistream_target_latency` can be used to override the determined performance numbers

#### Populate the README files
```
cm run script --tags=generate-run-cmds,inference,_populate-readme,_all-scenarios \
--model=resnet50 --device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/inference_3.1_results \
--category=edge --division=open --quiet
```

#### Generate actual submission tree

Here, we are copying the performance and accuracy log files (compliance logs also in the case of closed division) from the results directory to the submission tree following the [directory structure required by MLCommons Inference](https://github.com/mlcommons/policies/blob/master/submission_rules.adoc#inference-1). After the submission tree is generated, [accuracy truncate script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log) is called to truncate accuracy logs and then the [submission checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker) is called to validate the generated submission tree.

We should use the master branch of MLCommons inference repo for the submission checker. You can use `--hw_note_extra` option to add your name to the notes.
```
cm run script --tags=generate,inference,submission --results_dir=$HOME/inference_3.1_results/valid_results \
--submission_dir=$HOME/inference_submission_tree --clean  \
--run-checker --submitter=cTuning --adr.inference-src.version=master \
--hw_notes_extra="Result taken by NAME" --quiet
```


## Tensorflow backend

Same commands as for `onnxruntime` should work by replacing `backend=onnxruntime` with `--backend=tf`. For example,

```
cm run script --tags=generate-run-cmds,inference,_all-modes,_all-scenarios \
--model=resnet50 --device=cpu --implementation=reference --backend=tf \
--execution-mode=valid --results_dir=$HOME/inference_3.1_results \
--category=edge --division=open --quiet
```

## TVM backend

Same commands as for `onnxruntime` should work by replacing `backend=onnxruntime` with `--backend=tvm-onnx`. (Only `--device=cpu` is currently supported for TVM) For example,

```
cm run script --tags=generate-run-cmds,inference,_all-modes,_all-scenarios \
--model=resnet50 --device=cpu --implementation=reference --backend=tvm-onnx \
--execution-mode=valid --results_dir=$HOME/inference_3.1_results \
--category=edge --division=open --quiet
```
