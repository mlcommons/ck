[ [Back to index](README.md) ]


## Run this benchmark via CM


### Do a test run to detect and record the system performance

```
cm run script --tags=run-mlperf,inference,_find-performance,_all-scenarios \
--model=gpt-j-99 --implementation=reference --device=cuda --backend=pytorch \
--category=edge --division=open --quiet --precision=bfloat16 --env.GPTJ_BEAM_SIZE=4
```
* GPU needs a minimum of 80 GB memory for fp32 model. For GPUs with shorter memory try `--env.GPTJ_BEAM_SIZE=2` and `--precision=float16` 
* Use `--device=cpu` to run the inference on CPU (can be extremely slow)
* `--precision=float16` can be tried on CPU and `--precision=fp32` on a 80 GB GPU 
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--category=datacenter` to run datacenter scenarios
* Use `--model=gptj-99.9` to run the high accuracy constraint gptj-99.9 model.


### Do full accuracy and performance runs for all the scenarios

```
cm run script --tags=run-mlperf,inference,_submission,_all-scenarios --model=gpt-j-99 \
--device=cuda --implementation=reference --backend=pytorch \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet --precision=bfloat16 --env.GPTJ_BEAM_SIZE=4
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, `--server_target_qps`, and `--singlestream_target_latency` can be used to override the determined performance numbers

### Populate the README files describing your submission

```
cmr "run-mlperf inference _populate-readme _all-scenarios" \
--model=gpt-j-99 --device=cpu --implementation=reference --backend=pytorch \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet --precision=bfloat16 --env.GPTJ_BEAM_SIZE=4
```

### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.


### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
