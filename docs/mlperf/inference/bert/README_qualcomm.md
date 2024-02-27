[ [Back to index](README.md) ]


## Run this benchmark via CM

### Do a test run to detect and record the system performance

```
cmr "run-mlperf inference _find-performance _all-scenarios" \
--model=bert-99 --implementation=qualcomm --device=qaic --backend=glow \
--category=edge --division=open --quiet
```
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--category=datacenter` to run datacenter scenarios (only for bert-99.9)
* Use `--model=bert-99.9` to run the high-accuracy model (only for datacenter)
* Use `--rerun` to force a rerun even when result files (from a previous run) exist

### Do full accuracy and performance runs for all the scenarios

```
cmr "run-mlperf inference _submission _all-scenarios" --model=bert-99 \
--device=qaic --implementation=qualcomm --backend=qaic \
--execution-mode=valid --category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, and `--singlestream_target_latency` can be used to override the determined performance numbers

### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
