[ [Back to index](README.md) ]

## Run this benchmark via CM

You can use `cm docker` instead of `cm run` to run the Intel implementation inside a docker container. But for `gptj` we have found an issue of the code getting hanged when run on a 24 core machine but only when inside a docker container. 

### Do a test run to detect and record the system performance

```
cm run script --tags=generate-run-cmds,inference,_find-performance \
--scenario=Offline --model=gptj-99 --implementation=intel-original --backend=pytorch \
--category=datacenter --division=open --quiet
```
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Intel implementation currently supports only datacenter scenarios


### Do full accuracy and performance runs for all the scenarios

```
cm docker script --tags=generate-run-cmds,inference,_submission,_all-scenarios \
--model=gptj-99 --implementation=intel-original --backend=pytorch \
--category=datacenter --division=open --quiet
```


### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
