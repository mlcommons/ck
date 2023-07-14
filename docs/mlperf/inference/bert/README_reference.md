Please do the system setup as described [here](README.md)


## Run Commands


### Do a test run to detect and record the system performance

```
cm run script --tags=generate-run-cmds,inference,_find-performance,_all-scenarios \
--model=bert-99 --implementation=reference --device=cpu --backend=onnxruntime \
--category=edge --division=open --quiet
```
* Use `--device=cuda` to run the inference on Nvidia GPU
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--category=datacenter` to run datacenter scenarios
* Use `--backend=pytorch` and `--backend=tf` to use the pytorch and tensorflow backends respectively
* Use `--model=bert-99.9` to run the high accuracy constraint bert-99 model. But since we are running the fp32 model, this is redundant and instead, we can reuse the results of bert-99 for bert-99.9


### Do full accuracy and performance runs for all the scenarios

```
cm run script --tags=generate-run-cmds,inference,_submission,_all-scenarios --model=bert-99 \
--device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, and `--singlestream_target_latency` can be used to override the determined performance numbers

### Populate the README files
```
cmr "generate-run-cmds inference _populate-readme _all-scenarios" \
--model=bert-99 --device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet
```

### Generate and Upload the Submission
Follow [this README](../Generate_Submission_tree.md) to generate the submission tree and upload your results. 
