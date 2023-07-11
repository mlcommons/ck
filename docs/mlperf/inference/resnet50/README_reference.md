Please do the system setup as described [here](README.md)


## Run Commands


### Do a test run to detect and record the system performance

```
cm run script --tags=generate-run-cmds,inference,_find-performance,_all-scenarios \
--model=resnet50 --implementation=reference --device=cpu --backend=onnxruntime \
--category=edge --division=open --quiet
```
* Use `--device=cuda` to run the inference on Nvidia GPU
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--category=datacenter` to run datacenter scenarios
* Use `--backend=tf` or `--backend=tvm-onnx` to use tensorflow and tvm-onnx backends respectively

### Do full accuracy and performance runs for all the scenarios

```
cm run script --tags=generate-run-cmds,inference,_submission,_all-scenarios --model=resnet50 \
--device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/inference_3.1_results \
--category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, `--singlestream_target_latency` and `multistream_target_latency` can be used to override the determined performance numbers

### Populate the README files
```
cm run script --tags=generate-run-cmds,inference,_populate-readme,_all-scenarios \
--model=resnet50 --device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/inference_3.1_results \
--category=edge --division=open --quiet
```

### Generate actual submission tree

Here, we are copying the performance and accuracy log files (compliance logs also in the case of closed division) from the results directory to the submission tree following the [directory structure required by MLCommons Inference](https://github.com/mlcommons/policies/blob/master/submission_rules.adoc#inference-1). After the submission tree is generated, [accuracy truncate script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log) is called to truncate accuracy logs and then the [submission checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker) is called to validate the generated submission tree.

We should use the master branch of MLCommons inference repo for the submission checker. You can use `--hw_note_extra` option to add your name to the notes.
```
cm run script --tags=generate,inference,submission --results_dir=$HOME/inference_3.1_results/valid_results \
--submission_dir=$HOME/inference_submission_tree --clean  \
--run-checker --submitter=cTuning --adr.inference-src.version=master \
--hw_notes_extra="Result taken by NAME" --quiet
```
