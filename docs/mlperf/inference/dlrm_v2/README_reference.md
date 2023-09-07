[ [Back to the common setup](README.md) ]


## Run this benchmark via CM


## Detect the preprocessed criteo dataset

```
cm run script --tags=get,preprocessed,dataset,criteo --dir=<path_to_multihot_preprocessed_dataset>
```

### Do a test run to detect and record the system performance

```
cm run script --tags=generate-run-cmds,inference,_find-performance,_all-scenarios \
--model=dlrm-99 --implementation=reference --device=cuda --backend=pytorch \
--category=datacenter --division=open --quiet 
```
* GPU needs a minimum of 92 GB memory for fp32 model. 
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--model=dlrm_v2-99.9` to run the high accuracy constraint gptj-99.9 model.


### Do full accuracy and performance runs for all the scenarios

```
cm run script --tags=generate-run-cmds,inference,_submission,_all-scenarios --model=dlrm-99 \
--device=cuda --implementation=reference --backend=pytorch \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=datacenter --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, and `--singlestream_target_latency` can be used to override the determined performance numbers

### Populate the README files describing your submission

```
cmr "generate-run-cmds inference _populate-readme _all-scenarios" \
--model=dlrm-99 --device=cpu --implementation=reference --backend=pytorch \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=datacenter --division=open --quiet
```

### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.


### Run individual scenarios for testing and optimization

TBD

### Questions? Suggestions?

Don't hesitate to get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
