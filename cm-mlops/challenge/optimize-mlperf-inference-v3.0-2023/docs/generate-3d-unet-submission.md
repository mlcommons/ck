## Setup
Please follow the MLCommons CK [installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md) to install CM.
Download the ck repo to get the CM script for MLPerf submission

```
cm pull repo mlcommons@ck --checkout=681547519f4d9a8991d992d1300c90cfde06e9b9
```

## Run Commands

3d-unet has two variants - `3d-unet-99` and `3d-unet-99.9` where the `99` and `99.9` specifies the required accuracy constraint with respect to the reference floating point model. Both models can be submitter under edge as well as datacenter category.

Since 3d-unet is one of the slowest running model, we are only running it using nvidia-implementation where the model is quantized and run on TensorRT backend on Nvidia GPU.

For `3d-unet-99.9` runs, simply replace `3d-unet-99` with `3d-unet-99.9`.

### TensorRT backend

#### Do a test run to detect and record the system performance

```
cm run script --tags=generate-run-cmds,inference,_find-performance,_all-scenarios \
--model=3d-unet-99 --implementation=nvidia-original --device=cuda --backend=tensorrt \
--category=edge --division=open --quiet
```
* Use `--category=datacenter` to run datacenter scenarios
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)

#### Do a full accuracy and performance runs for all the scenarios

```
cm run script --tags=generate-run-cmds,inference,_all-modes,_all-scenarios \
--model=3d-unet-99 --device=cuda --implementation=nvidia-original --backend=tensorrt \
--execution-mode=valid --results_dir=$HOME/inference_3.0_results \
--category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps` and `--singlestream_target_latency` can be used to override the determined performance numbers

#### Populate the README files
```
cm run script --tags=generate-run-cmds,inference,_populate-readme,_all-scenarios \
--model=3d-unet-99 --device=cuda --implementation=nvidia-original --backend=tensorrt \
--execution-mode=valid --results_dir=$HOME/inference_3.0_results \
--category=edge --division=open --quiet
```

#### Generate actual submission tree

Here, we are copying the performance and accuracy log files (compliance logs also in the case of closed division) from the results directory to the submission tree following the [directory structure required by MLCommons Inference](https://github.com/mlcommons/policies/blob/master/submission_rules.adoc#inference-1). After the submission tree is generated, [accuracy truncate script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log) is called to truncate accuracy logs and then the [submission checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker) is called to validate the generated submission tree.

We should use the master branch of MLCommons inference repo for the submission checker. You can use `--hw_note_extra` option to add your name to the notes.
```
cm run script --tags=generate,inference,submission --results_dir=$HOME/inference_3.0_results/valid_results \
--device=cpu --submission_dir=$HOME/inference_submission_tree --clean --run-checker --submitter=cTuning 
--adr.inference-src.version=master --hw_notes_extra="Result taken by NAME" --quiet
```
