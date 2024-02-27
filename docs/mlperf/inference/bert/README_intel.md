[ [Back to index](README.md) ]

## Run this benchmark via CM

We use `cm docker` to run the Intel implementation to avoid compilation problems with any host OS dependencies. 

### Do a test run to detect and record the system performance

```
cm docker script --tags=run-mlperf,inference,_find-performance \
--scenario=Offline --model=bert-99 --implementation=intel-original --backend=pytorch \
--category=datacenter --division=open --quiet
```
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)


### Do full accuracy and performance runs for all the scenarios

```
cm docker script --tags=run-mlperf,inference,_submission,_all-scenarios \
--model=bert-99 --implementation=intel-original --backend=pytorch \
--category=datacenter --division=open --quiet
```


### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
