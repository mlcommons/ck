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

CM automation for MLPerf benchmarks is being developed by the [MLCommons Task Force on Automation and Reproducibility](../../taskforce.md) -
don't hesitate to get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT) to get free help to run MLPerf benchmarks and submit valid results.


**Table of Contents:**

* [Unified interface to run MLPerf inference benchmarks](#unified-interface-to-run-mlperf-inference-benchmarks)
  * [How to run existing MLPerf inference benchmarks?](#how-to-run-existing-mlperf-inference-benchmarks?)
  * [How to measure power?](#how-to-measure-power?)
  * [How to submit results?](#how-to-submit-results?)
  * [How CM automation works?](#how-cm-automation-works?)
  * [How to add new implementations (models, frameworks, hardware)?](#how-to-add-new-implementations-models-frameworks-hardware?)
  * [How to run MLPerf inference benchamrks with non-reference models?](#how-to-run-mlperf-inference-benchamrks-with-non-reference-models?)
  * [How to automate MLPerf experiments?](#how-to-automate-mlperf-experiments?)
  * [How to visualize and compare results](#how-to-visualize-and-compare-results)
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
 has several power analyzer and can help you test your MLPerf benchmark implementations
 on our system.*


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

Since CM language uses native OS scripts with python wrappers, it is relatively straightforward to debug it using your existing tools.

The unified CM interface to run MLPerf inference benchmarks out of the box is implemented using these CM scripts:
* [run-mlperf-inference-app](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app)
  * [app-mlperf-inference-reference](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)
  * [app-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-nvidia)
  * [app-mlperf-inference-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp)
  * [app-mlperf-inference-tflite-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp)

You can add `--debug` flag to your CM command line when running MLPerf benchmarks
to open a shell with all MLPerf environment variables prepared to 
run and debug the final MLPerf loadgen tool manually.

You can also use GDB by adding environment variable `--env.CM_RUN_PREFIX="gdb --args "` to the CM command line.

Please check [this documentation](../../debugging.md) for more details.





## How to add new implementations (models, frameworks, hardware)?



## How to run MLPerf inference benchamrks with non-reference models?




## How to automate MLPerf experiments?

We have developed experiment automation in CM to run multiple experiments, automatically explore multiple parameters, 
record results and reproduce them by the workgroup.

Please check this [documentation](../../../cm-mlops/automation/experiment/README-extra.md) for more details.



## How to visualize and compare results

You can pull all past MLPerf results in the CM format, import your current experiments under preparation and visualize results 
with derived metrics on your system using the Collective Knowledge Playground as follows:

```bash
cm pull repo mlcommons@ck_mlperf_results
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

[Collective Mind](https://doi.org/10.5281/zenodo.8105339) is an open community project to modularize AI benchmarks 
and provide a common interface to run them across diverse models, data sets, software and hardware - 
we would like to thank all our [great contributors](../../../CONTRIBUTING.md) for their feedback, support and extensions!

## Questions? Suggestions?

Please check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
