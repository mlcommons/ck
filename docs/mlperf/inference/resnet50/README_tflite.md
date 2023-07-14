Please do the system setup as described [here](README.md)


## Run Commands

Please follow [this](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/README-about.md) readme for running mobilenet and efficientnet models using TFLite backend

### Do a test run to detect and record the system performance

```
cm run script --tags=generate-run-cmds,inference,_find-performance,_all-scenarios \
--model=resnet50 --implementation=tflite-cpp --device=cpu --backend=tflite \
--category=edge --division=open --quiet
```
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Since only singlestream is implemented for tflite-cpp, datacenter submission is not possible

### Do full accuracy and performance runs for all the scenarios

```
cm run script --tags=generate-run-cmds,inference,_all-modes,_all-scenarios --model=resnet50 \
--device=cpu --implementation=tflite-cpp --backend=tflite \
--execution-mode=valid --results_dir=$HOME/inference_3.1_results \
--category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, `--singlestream_target_latency` and `multistream_target_latency` can be used to override the determined performance numbers

Follow [this README](../Generate_Submission_tree.md) to generate the submission tree and upload your results. 
