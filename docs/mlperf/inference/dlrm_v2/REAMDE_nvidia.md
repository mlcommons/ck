[ [Back to the common setup](README.md) ]

## Build Nvidia Docker Container (from 3.1 Inference round)

```
cm docker script --tags=build,nvidia,inference,server
```
## Run this benchmark via CM


### Do a test run to detect and record the system performance

```
cmr "generate-run-cmds inference _find-performance _all-scenarios" \
--model=dlrm-v2-99 --implementation=nvidia-original --device=cuda --backend=tensorrt \
--category=datacenter --division=open --quiet
```
* Use `--division=closed` to run all scenarios for the closed division.

### Do full accuracy and performance runs for all the scenarios

```
cmr "generate-run-cmds inference _submission _all-scenarios" --model=dlrm-v2-99 \
--device=cuda --implementation=nvidia-original --backend=tensorrt \
--execution-mode=valid \
--category=datacenter --division=open --quiet --skip_submission_generation=yes
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division.
* `--offline_target_qps` and `--server_target_qps` can be used to override the determined performance numbers


### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.

### Run individual scenarios for testing and optimization

TBD

### Questions? Suggestions?

Don't hesitate to get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).

### Acknowledgments

* CM automation for Nvidia's MLPerf inference implementation was developed by Arjun Suresh and Grigori Fursin.
* Nvidia's MLPerf inference implementation was developed by Zhihan Jiang, Ethan Cheng, Yiheng Zhang and Jinho Suh.
