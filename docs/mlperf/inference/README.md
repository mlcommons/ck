[ [Back to MLPerf benchmarks index](../README.md) ]

<details>
<summary>Click here to see the table of contents.</summary>

  * [Development](#development)
  * [CM interface for MLPerf](#cm-interface-for-mlperf)
    * [Install CM](#install-cm)
    * [Install repository with CM automation recipes for MLPerf](#install-repository-with-cm-automation-recipes-for-mlperf)
    * [Setup virtual environment](#setup-virtual-environment)
    * [Test Docker](#test-docker)
    * [Prepare cloud instances](#prepare-cloud-instances)
    * [Prepare hardware](#prepare-hardware)
      * [CPUs](#cpus)
      * [CUDA GPUs](#cuda-gpus)
      * [Nvidia Jetson AGX Orin](#nvidia-jetson-agx-orin)
      * [Other backends](#other-backends)
    * [Run benchmarks and submit results](#run-benchmarks-and-submit-results)
    * [Measure power](#measure-power)
    * [Debug benchmarks](#debug-benchmarks)
    * [Extend CM interface and workflows](#extend-cm-interface-and-workflows)
    * [Optimize benchmarks](#optimize-benchmarks)
    * [Visualize and compare results](#visualize-and-compare-results)
  * [Questions? Suggestions?](#questions?-suggestions?)

</details>


This document described how to run [MLPerf inference benchmarks](https://arxiv.org/abs/1911.02549) 
on any platforms in a unified way via [MLCommons CM interface](https://github.com/mlcommons/ck).
This interface is being developed and maintained by the [MLCommons Task Force on Automation and Reproducibility](../../taskforce.md)
with [great contributions](CONTRIBUTING.md) from the community and important feedback from Google, AMD, Neural Magic, Nvidia, Qualcomm, Dell, HPE, 
Red Hat, Intel, TTA, One Stop Systems, ACM and other organizations.
Don't hesitate to get in touch with us using this [public Discord server](https://discord.gg/JjWNWXKxwT) 
to get free help with your MLPerf submissions and/or participate in the CM developments.

## Development

[![MLPerf inference resnet50](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-resnet50.yml/badge.svg?branch=master&event=pull_request)](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-resnet50.yml)
[![MLPerf inference retinanet](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-retinanet.yml/badge.svg?branch=master&event=pull_request)](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-retinanet.yml)
[![MLPerf inference bert](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-bert.yml/badge.svg?event=pull_request)](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-bert.yml)
[![MLPerf inference rnnt](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-rnnt.yml/badge.svg?event=pull_request)](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-rnnt.yml)

* [Current development status](../../taskforce.md#status).
* [Current CM coverage to run and reproduce MLPerf inference benchmarks](https://github.com/mlcommons/ck/issues/1052).
* [Development version of the modular MLPerf C++ inference implementation](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-cpp/README-extra.md).
* [Development version of the the reference network implementation with CM interface for BERT model](https://github.com/mlcommons/inference/tree/master/language/bert#loadgen-over-the-network).

## CM interface for MLPerf

### Install CM 

Follow [this guide](../../installation.md) to install CM on Linux, Windows or MacOS.
It is a small Python library with minimal dependencies (Python 3+, Git and wget) and `cm` and `cmr` command line.

If you encounter problems, please report them at [GitHub](https://github.com/mlcommons/ck/issues).


### Install repository with CM automation recipes for MLPerf

Install the MLCommons repository with [portable and reusable automation recipes for MLOps and DevOps (CM scripts)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script).
These scripts are being developed and shared by the community and MLCommons under Apache 2.0 license 
to decompose complex software projects into small, simple, reusable, portable and technology-agnostic 
components that can automatically run on any software, hardware, models and data sets.

```bash
cm pull repo mlcommons@ck
```

You can run it again at any time to pick up the latest updates.

If you want to extend existing automations, contribute the new ones or register in our 
[reproducibility and optimization challenges for AI//ML systems](https://access.cknowledge.org/playground/?action=challenges),
we suggest you to create a fork of this repository and use it instead of the main one. Just do not forget to delete the original repository from the CM:
```bash
cm rm repo mlcommons@ck --all
cm pull repo --url={URL of the mlcommons@ck fork}
```

Note that CM will store all such repositories and downloaded/installed data sets, models and tools
in your `$HOME/CM` directory. 

Since MLPerf benchmarks require lots of space (somethings hundreds of Gigabytes), 
you can change the above location to some large scratch disk using `CM_REPOS` 
environment variable as follows:

```bash
export CM_REPOS={new path to CM repositories and data}
echo "CM_REPOS=${CM_REPOS} >> $HOME/.bashrc"
```

You will need to pull above repository with CM automations again to place it in the new directory.



### Setup virtual environment

If you plan to use your native environment to run MLPerf benchmarks, we suggest you to set up
a Python virtual environment via CM to avoid contaminating your existing Python installation:

```bash
cm run script "install python-venv" --name=mlperf
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```

CM will install a new Python virtual environment in CM cache and will install all Python dependencies there:
```bash
cm show cache
```

Note that you can install multiple virtual environments with different names and python versions (Linux):
```bash
cm run script "install python-venv" --version=3.10.8 --name=mlperf2
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf2"
```



### Test Docker

If you have Docker installed on your system, you can test it and run some CM scripts as follows:
```bash
cm docker script --tags=detect,os -j
```


### Prepare cloud instances

If you want to run MLPerf in multiple cloud instances, please follow these guides to set them up:

* [AWS](../setup/setup-aws-instance.md)
* [GCP](../setup/setup-gcp-instance.md)


### Prepare hardware

Read this section if you want to run MLPerf benchmarks in a native environment, i.e. without containers.

#### CPUs

If you plan to run MLPerf benchmarks on x64 and/or Arm64 CPUs, no extra setup is necessary.

#### CUDA GPUs

If you plan to use CUDA in your native environment, please follow [this guide](../../installation-cuda.md) to set it up on your system.

#### Nvidia Jetson AGX Orin

Follow [this guide](../setup/setup-nvidia-jetson-orin.md).

#### Other backends

We work with the community to add more hardware backends (Google TPU, Amazon Inferentia, Qualcomm AI100, etc) 
to MLPerf benchmarks via our [open challenges for AI//ML systems](https://access.cknowledge.org/playground/?action=challenges),
Please get in touch with us via [public Discord server](https://discord.gg/JjWNWXKxwT) 
if you are interested to participate, collaborate and contribute to this community project!





### Run benchmarks and submit results

Please check our [MLPerf inference submitter orientation slides (July 2023)](https://doi.org/10.5281/zenodo.8144274)
explaining why we have developed a common CM interface to run all MLPerf benchmarks.

Note that only official (registered) MLCommons members can submit results to MLPerf inference.
As an alternative, you can also participate in our community submissions to MLPerf
via the [cTuning foundation](https://www.linkedin.com/company/ctuning-foundation) (a founding member of MLCommons).


We provided a unified CM interface to run the following MLPerf inference benchmarks:
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




### Measure power

Power measurement is optional for MLPerf inference benchmark submissions and is known to be very difficult to set up and run.
However, if your system have a good power efficiency, it is great to showcase it and compare against other systems.
That's why we fully automated power measurements for MLPerf inference benchmark in CM.

For any above MLPerf inference benchmark, you can turn on power measurements by adding the following flags to the CM command:
```
--power=yes \
--adr.mlperf-power-client.power_server=<Power server IP> \
--adr.mlperf-power-client.port=<Power server port>
```

On the hardware side, you can follow [this tutorial](https://github.com/mlcommons/ck/blob/master/docs/tutorials/mlperf-inference-power-measurement.md) 
to set up your power analyzer and connect it with your host platform.

Note that the [cTuning foundation](https://www.linkedin.com/company/ctuning-foundation)
has several power analyzer and can help you test your MLPerf benchmark implementations
on our system.



### Debug benchmarks


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



### Extend CM interface and workflows

The CM concept is to be always keep backward compatibility
of the human readable interface while improving and extending low-level CM scripts.

You should be able to update CM language and scripts at any time as follows:
```bash
python3 -m pip install cmind -U
cm pull repo mlcommons@ck
```

However, some local installations and downloads may become outdated in CM cache.
In such case, you can either start from scratch by cleaning all CM cache entries as follows
```bash
cm rm cache -f
```

or by cleaning only entries related to updated components such as MLPerf inference sources and harnesses:
```bash
cm show cache
cm rm cache --tags=inference,src -f
cm rm cache --tags=harness -f
```



### Optimize benchmarks

We are developing `CM experiment automation` to run multiple experiments, automatically explore multiple parameters, 
record results and reproduce them by the workgroup.

Please check this [documentation](../../../cm-mlops/automation/experiment/README-extra.md) for more details.

*This is ongoing development.*


### Visualize and compare results

You can pull all past MLPerf results in the CM format, import your current experiments under preparation and visualize results 
with derived metrics on your system using the Collective Knowledge Playground as follows:

```bash
cm pull repo mlcommons@ck_mlperf_results
cmr "get git repo _repo.https://github.com/ctuning/mlperf_inference_submissions_v3.1" \
    --env.CM_GIT_CHECKOUT=main \
    --extra_cache_tags=mlperf-inference-results,community,version-3.1
cmr "gui _graph"
```

*This is ongoing development.*




## Questions? Suggestions?

Get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).

