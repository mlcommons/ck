[ [Back to index](README.md) ]

## Run this benchmark via CM


### Do a test run to detect and record the system performance

```
cm run script --tags=run-mlperf,inference,_find-performance,_all-scenarios \
--model=bert-99 --implementation=reference --device=cpu --backend=onnxruntime \
--category=edge --division=open --quiet --rerun
```
* Use `--device=cuda` to run the inference on Nvidia GPU and `--device=rocm` to run on AMD GPUs
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--category=datacenter` to run datacenter scenarios
* Use `--backend=pytorch` and `--backend=tf` to use the pytorch and tensorflow backends respectively. `--backend=deepsparse` will run the sparse int8 model using deepsparse backend (not allowed to be submitted under closed division).
* Use `--model=bert-99.9` to run the high accuracy constraint bert-99 model. But since we are running the fp32 model, this is redundant and instead, we can reuse the results of bert-99 for bert-99.9


### Do full accuracy and performance runs for all the scenarios

```
cm run script --tags=run-mlperf,inference,_submission,_all-scenarios --model=bert-99 \
--device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, and `--singlestream_target_latency` can be used to override the determined performance numbers
* `--rerun` flag can be used to force a rerun even when a valid result exists in the results_dir

### Populate the README files describing your submission

```
cmr "run-mlperf inference _populate-readme _all-scenarios" \
--model=bert-99 --device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet
```
### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
