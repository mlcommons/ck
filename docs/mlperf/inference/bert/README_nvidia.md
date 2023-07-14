Please do the system setup as described [here](README.md)

Additionally, for using Nvidia MLPerf inference implementations we need to install TensorRT and set up the configuration files as detailed [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/README-about.md)

## Run Commands


### Do a test run to detect and record the system performance

```
cmr "generate-run-cmds inference _find-performance _all-scenarios" \
--model=bert-99 --implementation=nvidia-original --device=cuda --backend=tensorrt \
--category=edge --division=open --quiet
```
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--category=datacenter` to run datacenter scenarios (only for bert-99.9)
* Use `--model=bert-99.9` to run the high-accuracy model (only for datacenter)

### Do full accuracy and performance runs for all the scenarios

```
cmr "generate-run-cmds inference _submission _all-scenarios" --model=bert-99 \
--device=cuda --implementation=nvidia-original --backend=tensorrt \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, and `--singlestream_target_latency` can be used to override the determined performance numbers

### Populate the README files
```
cmr "generate-run-cmds inference _populate-readme _all-scenarios" \
--model=bert-99 --device=cuda --implementation=nvidia-original --backend=tensorrt \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet
```

### Generate and Upload the Submission
Follow [this README](../Submission.md) to generate the submission tree and upload your results. 

