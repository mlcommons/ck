[ [Back to index](README.md) ]

## Run this benchmark via CM

*Note: from Feb 2024, we suggest you to use [this GUI](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725)
 to configure MLPerf inference benchmark, generate CM commands to run it across different implementations, models, data sets, software
 and hardware, and prepare your submissions.*


### Do a test run to detect and record the system performance

```
cmr "run-mlperf inference _find-performance _all-scenarios" \
--model=3d-unet-99.9 --implementation=reference --device=cpu --backend=onnxruntime \
--category=edge --division=open --quiet
```
* Use `--device=cuda` to run the inference on Nvidia GPU
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Use `--category=datacenter` to run datacenter scenarios
* Use `--backend=pytorch` and `backend=tf` to use pytorch and tensorflow backends respectively
* Use `--model=3d-unet-99` to run the low accuracy constraint 3d-unet-99 model. But since we are running the fp32 model, this is redundant and instead, we can reuse the results of 3d-unet-99.9 for 3d-unet-99

### Do full accuracy and performance runs for all the scenarios

```
cmr "run-mlperf inference _submission _all-scenarios" --model=3d-unet-99.9 \
--device=cpu --implementation=reference --backend=onnxruntime \
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
