[ [Back to MLPerf benchmarks index](../README.md) ]


# Unified interface to run MLPerf inference benchmarks




Running the [MLPerf inference benchmarks](https://arxiv.org/abs/1911.02549) and preparing valid submissions 
[is not trivial](https://doi.org/10.5281/zenodo.10605079).

This guide explains how to automate all the steps required to prepare, 
customize, run and extend MLPerf inference benchmarks across 
diverse models, datasets, software and hardware using 
the [MLCommons Collective Mind automation framework (CM)](https://github.com/mlcommons/ck).

CM makes it possible to compose modular benchmarks from [portable and reusable automation recipes (CM scripts)](https://access.cknowledge.org/playground/?action=scripts) 
with a common interface and a [human-friendly GUI](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725).
Such benchmarks attempt to automatically adapt to any software and hardware natively or inside a container with any Operating System.

CM automation for MLPerf benchmarks is being developed by the [MLCommons Task Force on Automation and Reproducibility](../../taskforce.md) 
based on the feedback from MLCommons organizations while automating >90% of all performance and power submissions in the v3.1 round.

Don't hesitate to get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT) to get free help to run MLPerf benchmarks and submit valid results.


**Table of Contents:**

* [How to run existing MLPerf inference benchmarks?](#how-to-run-existing-mlperf-inference-benchmarks?)
* [How to measure power?](#how-to-measure-power?)
* [How to submit results?](#how-to-submit-results?)
* [How CM automation works?](#how-cm-automation-works?)
* [How to debug CM automation recipes?](#how-to-debug-cm-automation-recipes?)
* [How to add new implementations (models, frameworks, hardware)?](#how-to-add-new-implementations-models-frameworks-hardware?)
* [How to run MLPerf inference benchmarks with non-reference models?](#how-to-run-mlperf-inference-benchmarks-with-non-reference-models?)
* [How to run MLPerf inference benchmark via Docker?](#how-to-run-mlperf-inference-benchmark-via-docker?)
* [How to automate MLPerf experiments?](#how-to-automate-mlperf-experiments?)
* [How to visualize and compare MLPerf results?](#how-to-visualize-and-compare-mlperf-results?)
* [Current developments](#current-developments)
* [Acknowledgments](#acknowledgments)
* [Questions? Suggestions?](#questions?-suggestions?)






## How to run existing MLPerf inference benchmarks?

* Install [MLCommons CM framework](../../installation.md) with automation recipes for AI benchmarks.
* Use this [GUI](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725) 
  to generate CM commands to customize and run MLPerf inference benchmarks.
* Use some ready-to-use CM commands for the following models:
  * [ResNet50](resnet50)
  * [RetinaNet](retinanet)
  * [3D Unet](3d-unet)
  * [RNNT](rnnt)
  * [Bert](bert)
  * [GPT-J](gpt-j)
  * [LLAMA2 70B](llama2-70b)
  * [Stable Diffusion XL](stable-diffusion-xl)
* Check on-going [reproducibility studies](https://access.cknowledge.org/playground/?action=reproduce) for MLPerf benchmarks.
* Participate in [open submission and reproducibility challenges](https://access.cknowledge.org/playground/?action=challenges).


## How to measure power?

Power measurement is optional for MLPerf inference benchmark submissions and is known to be very difficult to set up and run.
However, if your system have a good power efficiency, it is great to showcase it and compare against other systems.
That's why we fully automated power measurements for MLPerf inference benchmark in CM.

You can follow [this tutorial](https://github.com/mlcommons/ck/blob/master/docs/tutorials/mlperf-inference-power-measurement.md) 
to set up your power analyzer and connect it with your host platform.

*Note that the [cTuning foundation](https://www.linkedin.com/company/ctuning-foundation)
 and [cKnowledge.org](https://cKnowledge.org) have several power analyzers and can help 
 you test your MLPerf benchmark implementations.*


## How to submit results?

We provided a [unified CM interface](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725) to run the following MLPerf inference benchmarks:
1. [Language processing](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/bert) using Bert-Large model and Squad v1.1 dataset
2. [Language processing](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/gpt-j) using GPT-J model and CNN Daily Mail dataset
3. [Image Classification](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/resnet50) using ResNet50 model and Imagenet-2012 dataset
4. [Image Classification](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/README-about.md) using variations of MobileNets and EfficientNets and Imagenet-2012 dataset
5. [Object Detection](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/retinanet) using Retinanet model and OpenImages dataset
6. [Speech Recognition](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/rnnt) using RNNT model and LibriSpeech dataset
7. [Medical Imaging](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/3d-unet)  using 3d-unet model and KiTS19 dataset
8. Recommendation using DLRMv2 model and Criteo multihot dataset

All seven benchmarks can participate in the datacenter category.
All seven benchmarks except Recommendation can participate in the edge category. 

Note that `language processing` and `medical imaging` benchmarks must achieve a higher accuracy of at least `99.9%` of the FP32 reference model
in comparison with `99%` default accuracy requirement for all other models.

The `recommendation` benchmark has a high-accuracy variant only. Currently, we are not supporting the `recommendation` benchmark in CM 
because we did not have a required high-end server for testing. 

After running MLPerf inference benchmarks and collecting results via CM, you can follow this [guide](Submission.md) to prepare your submission.




## How CM automation works?

Collective Mind was developed based on the feedback from MLCommons organizations
- it simply wraps numerous native scripts for all steps required to prepare, build and run applications and benchmarks
into [unified and reusable automation recipes](https://access.cknowledge.org/playground/?action=scripts) 
with human-friendly tags, a common API, YAML/JSON meta descriptions and simple Python code.
CM makes it easy to chain together different automation recipes into powerful workflows
that automatically prepare all environment variables and commands lines
on any software, hardware and operating system without the need for users 
to learn new tools and languages.


We suggest you to explore this [automation recipe](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
and check this [CM README](https://github.com/mlcommons/ck) 
and [CM Getting Started Guide](../../getting-started.md) for more details about CM.

Common CM interface and automation for MLPerf inference benchmark is implemented using
the ["run-mlperf-inference-app" CM script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app)
described by this [YAML meta-description](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/run-mlperf-inference-app/_cm.yaml)
and [customize.py](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/run-mlperf-inference-app/customize.py).

This script can be configured using this [GUI](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725)
and will run other CM scripts that set up different MLPerf inference implementations from different vendors:

* [CM script "app-mlperf-inference-reference" to run MLCommons reference implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)
* [CM script "app-mlperf-inference-nvidia" to run Nvidia implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-nvidia)
* [CM script "reproduce-mlperf-inference-intel" to run Intel implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-intel)
* [CM script "reproduce-mlperf-inference-qualcomm" to run Qualcomm implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-qualcomm)
* [CM script "app-mlperf-inference-cpp" to run MLCommons ONNX C++ implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp)
* [CM script "app-mlperf-inference-tflite-cpp" to run TFLite C++ implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp)

When running above scripts, CM will cache the output (MLPerf loadgen, downloaded models, preprocessed data sets, installed tools) 
that will be reused across different scripts. You can see the content of the cache at any time as follows:
```bash
cm show cache
```

You can clean the cache and start from scratch as follows:
```bash
cm rm cache -f
```


## How to debug CM automation recipes?

Since CM language uses native OS scripts with python wrappers, it is relatively straightforward to debug it using your existing tools.

You can add `--debug` flag to your CM command line when running MLPerf benchmarks
to open a shell with all MLPerf environment variables prepared to 
run and debug the final MLPerf loadgen tool manually.

You can also use GDB by adding environment variable `--env.CM_RUN_PREFIX="gdb --args "` to the CM command line.

Please check [this documentation](../../debugging.md) for more details.





## How to add new implementations (models, frameworks, hardware)?

If you do not yet have your own implementation, we suggest you to run already existing implementation 
via CM and then modify loadgen and inference sources in CM cache to develop your own implementation:
```bash
cm show cache --tags=mlperf,loadgen
cm show cache --tags=get,git,inference,repo
```

You can then push your changes to your own clone of the MLPerf inference repo;
copy any of above CM scripts for similar implementation; update tags in `_cm.yaml`;
and add your implementation tags to the meta description of the main CM interface 
for the MLPerf inference benchmark [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/run-mlperf-inference-app/_cm.yaml).

If you need help, don't hesitate to contact us via [public Discord server](https://discord.gg/JjWNWXKxwT).

It is in our plans to add a tutorial how to develop MLPerf inference benchmarks 
and add your implementations to CM.



## How to run MLPerf inference benchmarks with non-reference models?

If you want to benchmark some ML models using MLPerf loadgen without accuracy, 
you can use our [universal Python loadgen automation for ONNX models](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-loadgen-generic-python/README-extra.md).
You can benchmark Hugging Face ONNX models or your own local models.

If you want to benchmark ML models with the MLPerf inference benchmark and submit results to open division,
you need to make sure that they are trained on the same data sets as reference MLPerf models and
that their input/output is the same as MLPerf reference models. In such case, you can use the following CM flags 
to substitute reference model in MLPerf.

* `--env.CM_MLPERF_CUSTOM_MODEL_PATH = {full path to the local model}`
* `--env.CM_ML_MODEL_FULL_NAME = {some user-friendly model name for submission}`

Check these 2 examples for more details:
* [Run custom Bert-family ONNX models with MLPerf reference implementation](bert/run_custom_onnx_models.sh)
* [Run multiple DeepSparse Zoo BERT models via MLPerf](bert/run_sparse_models.sh)




## How to run MLPerf inference benchmark via Docker?

If a given vendor implementation uses Docker (Intel, Nvidia, Qualcomm), CM will build required container and run MLPerf inference benchmark automatically.

CM also has an option to run native MLPerf inference benchmark implementations inside automatically-generated container by substituting `cm run script`
command with `cm docker script` command. 

We plan to share snapshots of different MLPerf inference benchmarks via Docker Hub 
during our [reproducibility studies](https://access.cknowledge.org/playground/?action=reproduce)
to help the community benchmark their own systems using MLPerf inference benchmark containers.





## How to automate MLPerf experiments?

We have developed experiment automation in CM to run multiple experiments, automatically explore multiple parameters, 
record results and reproduce them by the workgroup.

Please check this [documentation](../../../cm-mlops/automation/experiment/README-extra.md) for more details.





## How to visualize and compare MLPerf results?

You can pull all past MLPerf results in the CM format, import your current experiments under preparation and visualize results 
with derived metrics on your system using the Collective Knowledge Playground as follows:

```bash
cm pull repo mlcommons@cm4mlperf-results
cmr "get git repo _repo.https://github.com/ctuning/mlperf_inference_submissions_v3.1" \
    --env.CM_GIT_CHECKOUT=main \
    --extra_cache_tags=mlperf-inference-results,community,version-3.1
cmr "gui _graph"
```

You can see example of this visualization GUI [online](https://access.cknowledge.org/playground/?action=experiments).



## Current developments

* [Current reproducibility studies](https://access.cknowledge.org/playground/?action=reproduce) for MLPerf benchmarks.
* [Current CM coverage to run and reproduce MLPerf inference benchmarks]( https://github.com/mlcommons/ck/issues/1052 ).
* [Development version of the modular MLPerf C++ inference implementation](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-cpp/README-extra.md).
* [Development version of the the reference network implementation with CM interface for BERT model](https://github.com/mlcommons/inference/tree/master/language/bert#loadgen-over-the-network).


## Acknowledgments

[Collective Mind](https://doi.org/10.5281/zenodo.8105339) is an open community project 
to modularize AI benchmarks and provide a common interface to run them across diverse models, data sets, software and hardware - 
we would like to thank all our [great contributors](../../../CONTRIBUTING.md) for their feedback, support and extensions!

## Questions? Suggestions?

Please check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
