[ [Back to index](README.md) ]

## Running a mobilenet model using TFLite backend

Please follow [this guide](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/README-about.md) 
to run the entire set of MobileNet and EfficientNet models trained using ImageNet dataset (total 81 models) using TFLite backend.

If you want to try an individual model run, you can proceed as follows:


### Run Command
```
cm run script --tags=run,mlperf,inference,run-mlperf,_submission,_short  \
   --adr.python.version_min=3.8 \
   --implementation=tflite-cpp \
   --model=efficientnet \
   --backend=tflite \
   --device=cpu \
   --scenario=SingleStream \
   --test_query_count=100 \
   --adr.tflite-model.tags=_lite0 \
   --adr.mlperf-inference-implementation.tags=_armnn,_use-neon \
   --clean
```


## Run ResNet50 TFLite via CM


### Do a test run to detect and record the system performance

```
cm run script --tags=run-mlperf,inference,_find-performance,_all-scenarios \
--model=resnet50 --implementation=tflite-cpp --device=cpu --backend=tflite \
--category=edge --division=open --quiet
```
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Since only singlestream is implemented for tflite-cpp, datacenter submission is not possible
* Use `--adr.mlperf-inference-implementation.tags=_armnn,_use-neon` to use ARMNN backend


### Do full accuracy and performance runs for all the scenarios

```
cm run script --tags=run-mlperf,inference,_submission,_all-scenarios --model=resnet50 \
--device=cpu --implementation=tflite-cpp --backend=tflite \
--execution-mode=valid --category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, `--singlestream_target_latency` and `multistream_target_latency` can be used to override the determined performance numbers
* Use `--adr.mlperf-inference-implementation.tags=_armnn,_use-neon` to use ARMNN backend



### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.


### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
