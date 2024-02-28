[ [Back to index](README.md) ]


## Run this benchmark via CM


### Do a test run to detect and record the system performance

```
cm run script --tags=run-mlperf,inference,_find-performance,_all-scenarios \
--model=llama2-70b-99 --implementation=reference --device=cuda --backend=pytorch \
--category=datacenter --division=open --precision=bfloat16--quiet 
```
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--precision=float16` or `--precision=float32` to change the model precision
* Use `--model=llama2-70b-99.9` to run the high accuracy constraint llama2-70b-99.9 model.



### Do full accuracy and performance runs for all the scenarios

```
cm run script --tags=run-mlperf,inference,_submission,_all-scenarios --model=llama2-70b-99 \
--device=cuda --implementation=reference --backend=pytorch --precision=bfloat16 \
--execution-mode=valid --category=datacenter --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps` and `--server_target_qps` can be used to override the determined performance numbers

### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.


### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
