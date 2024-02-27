[ [Back to index](README.md) ]

## Run this benchmark via CM


### Do a test run to detect and record the system performance

```
cm run script --tags=run-mlperf,inference,_find-performance,_all-scenarios \
--model=resnet50 --implementation=reference --device=cpu --backend=onnxruntime \
--category=edge --division=open --quiet
```
* Use `--device=cuda` to run the inference on Nvidia GPU
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--category=datacenter` to run datacenter scenarios
* Use `--backend=tf`, `--backend=ncnn` or `--backend=tvm-onnx` to use tensorflow, ncnn and tvm-onnx backends respectively
* Remove `_all-scenarios` and use `--scenario=Offline` to run the `Offline` scenario and similarly for `Server`, `SingleStream` and `MultiStream` scenarios.


### Do full accuracy and performance runs for all the scenarios

```
cm run script --tags=run-mlperf,inference,_submission,_all-scenarios --model=resnet50 \
--device=cpu --implementation=reference --backend=onnxruntime --execution-mode=valid \
--category=edge --division=open --quiet
```

* Use `--power=yes --adr.mlperf-power-client.power_server=192.168.0.15 --adr.mlperf-power-client.port=4950` for measuring power. Please adjust the server IP (where MLPerf power server is installed) and Port (default is 4950). `power=yes` is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, `--singlestream_target_latency` and `multistream_target_latency` can be used to override the determined performance numbers


### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
