[ [Back to the common setup](README.md) ]

## Run this benchmark via CM

### Do a test run to detect and record the system performance

```
cmr "generate-run-cmds inference _find-performance _all-scenarios" \
--model=bert-99 --implementation=intel-original --device=cuda --backend=pytorch \
--category=datacenter --division=open --quiet
```
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)


### Do full accuracy and performance runs for all the scenarios

```
cmr "generate-run-cmds inference _submission" --model=bert-99 \
--device=cuda --implementation=intel-original --backend=pytorch \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet --scenario=Offline
```


### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.

### Run individual scenarios for testing and optimization

TBD

### Questions? Suggestions?

Don't hesitate to get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
