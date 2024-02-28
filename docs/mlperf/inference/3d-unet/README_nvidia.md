[ [Back to index](README.md) ]

## Build Nvidia Docker Container (from 3.1 Inference round)

```
cm docker script --tags=build,nvidia,inference,server
```
## Run this benchmark via CM

*Note: from Feb 2024, we suggest you to use [this GUI](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725)
 to configure MLPerf inference benchmark, generate CM commands to run it across different implementations, models, data sets, software
 and hardware, and prepare your submissions.*


### Do a test run to detect and record the system performance

```
cmr "run-mlperf inference _find-performance _all-scenarios" \
--model=3d-unet-99 --implementation=nvidia-original --device=cuda --backend=tensorrt \
--category=edge --division=open --quiet
```
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--category=datacenter` to run datacenter scenarios
* Use `--model=3d-unet-99.9` to run the high accuracy model

### Do full accuracy and performance runs for all the scenarios

```
cmr "run-mlperf inference _submission _all-scenarios" --model=3d-unet-99 \
--device=cuda --implementation=nvidia-original --backend=tensorrt \
--execution-mode=valid --category=edge --division=open --quiet
```

* Use `--power=yes` for measuring power. It is ignored for accuracy and compliance runs
* Use `--division=closed` to run all scenarios for the closed division including the compliance tests
* `--offline_target_qps`, and `--singlestream_target_latency` can be used to override the determined performance numbers


### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).

### Acknowledgments

* CM automation for Nvidia's MLPerf inference implementation was developed by Arjun Suresh and Grigori Fursin.
* Nvidia's MLPerf inference implementation was developed by Zhihan Jiang, Ethan Cheng, Yiheng Zhang and Jinho Suh.

