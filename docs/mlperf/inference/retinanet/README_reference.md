[ [Back to index](README.md) ]


## Run this benchmark via CM


### Do a test run to detect and record the system performance

```
cmr "run-mlperf inference _find-performance _all-scenarios" \
--model=retinanet --implementation=reference --device=cpu --backend=onnxruntime \
--category=edge --division=open --quiet
```
* Use `--device=cuda` to run the inference on Nvidia GPU
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--category=datacenter` to run datacenter scenarios
* Use `--backend=pytorch` to use pytorch backend

### Do full accuracy and performance runs for all the scenarios

```
cmr "run-mlperf inference _submission _all-scenarios" --model=retinanet \
--device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, `--singlestream_target_latency` and `multistream_target_latency` can be used to override the determined performance numbers

### Populate the README files

```
cmr "run-mlperf inference _populate-readme _all-scenarios" \
--model=retinanet --device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet
```

### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
