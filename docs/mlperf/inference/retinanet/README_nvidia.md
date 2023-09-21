[ [Back to the common setup](README.md) ]

## Prepare Nvidia software

You need to install TensorRT and set up the configuration files as detailed [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/README-about.md).


## Run this benchmark via CM


### Do a test run to detect and record the system performance

```
cmr "generate-run-cmds inference _find-performance _all-scenarios" \
--model=retinanet --implementation=nvidia-original --device=cuda --backend=tensorrt \
--category=edge --division=open --quiet
```
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--category=datacenter` to run datacenter scenarios

### Do full accuracy and performance runs for all the scenarios

```
cmr "generate-run-cmds inference _submission _all-scenarios" --model=retinanet \
--device=cuda --implementation=nvidia-original --backend=tensorrt \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, `--singlestream_target_latency` and `multistream_target_latency` can be used to override the determined performance numbers

### Populate the README files describing your submission

```
cmr "generate-run-cmds inference _populate-readme _all-scenarios" \
--model=retinanet --device=cuda --implementation=nvidia-original --backend=tensorrt \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet
```

### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.

### Run individual scenarios for testing and optimization

TBD

### Questions? Suggestions?

Don't hesitate to get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
