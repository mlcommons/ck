[ [Back to index](README.md) ]

<details>
<summary>Click here to see the table of contents.</summary>

* [Run MLPerf inference benchmarks out-of-the-box](#run-mlperf-inference-benchmarks-out-of-the-box)
  * [Install CM automation language](#install-cm-automation-language)
  * [Install repository with CM automations](#install-repository-with-cm-automations)
  * [Prepare hardware](#prepare-hardware)
    * [CPU](#cpu)
    * [CUDA GPU](#cuda-gpu)
    * [TPU](#tpu)
    * [AWS inferentia](#aws-inferentia)
    * [Other backends](#other-backends)

</details>


# Run MLPerf inference benchmarks out-of-the-box

This documentation will help you run, reproduce and compare MLPerf inference benchmarks out-of-the-box 
across any software, hardware, models and data sets from any vendor
using the open-source and technology-agnostic [MLCommons Collective Mind automation language (CM)](https://doi.org/10.5281/zenodo.8105339)
and [MLCommons Collective Knowledge Playground (CK)](https://access.cknowledge.org/playground/?action=experiments).

This project is under heavy development led by [Grigori Fursin](https://cKnowledge.org/gfursin) and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)
and supported by the [MLCommons Task Force on Automation and Reproducibility](../taskforce.md),
[cTuning.org](https://cTuning.org) and [cKnowledge.org](https://cKnowledge.org).

Don't hesitate to get in touch with us using this [public Discord server](https://discord.gg/JjWNWXKxwT) 
to provide your feedback, ask questions, add new benchmark implementations, models, data sets and hardware backends,
prepare and optimize your MLPerf submissions and participate in our [reproducibility and optimization challenges](https://access.cknowledge.org/playground/?action=challenges).

You can learn more about our vision and plans from our [ACM REP keynote (June 2023)](https://doi.org/10.5281/zenodo.8105339).

## Install CM automation language

Install MLCommons CM automation language as described [here](../../installation.md). 
It is a very small Python library with `cm` and `cmr` command line front-ends and minimal dependencies including Python 3+, Git and wget.

If you encounter problems, please report them at [GitHub](https://github.com/mlcommons/ck/issues).


## Install repository with CM automations

Install the MLCommons repository with [reusable and portable automation recipes (CM scripts)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) via CM.
These scripts are being developed and shared by the community under Apache 2.0 license 
to enable portable, modular, and technology-agnostic benchmarks and applications 
that can automatically run with any software, hardware, models and data sets.

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

## Prepare hardware

Read this section if you want to run MLPerf benchmarks in a native environment, i.e. without containers.

### CPU

If you plan to run MLPerf benchmarks on x64 and/or Arm64 CPUs, no extra setup is necessary.

### CUDA GPU

If you plan to use CUDA in your native environment, please follow [this guide](../../installation-cuda.md) to set it up on your system.

### Other backends

We work with the community to add more hardware backends (TPU, Inferentia, etc) 
to MLPerf benchmarks via our [open challenges for AI//ML systems](https://access.cknowledge.org/playground/?action=challenges),
Please get in touch with us via [public Discord server](https://discord.gg/JjWNWXKxwT) 
if you are interested to participate, collaborate and contribute to this community project!


## Run benchmarks and prepare submissions

Please check our [MLPerf inference submitter orientation slides (July 2023)](https://doi.org/10.5281/zenodo.8144274)
explaining why we have developed the CM automation for MLPerf benchmarks and how it can help you run MLPerf benchmarks.

Note that only registered and paid MLCommons members can submit official results to MLPerf inference.
As an alternative, you can also participate in a community submission 
via the [cTuning foundation](https://cTuning.org) (a founding member of MLCommons).


For MLPerf inference 3.1 we have the following benchmark tasks
1. [Language processing](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/bert) using Bert-Large model and Squadv1.1 dataset
2. [Image Classification](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/resnet50) using ResNet50 model and Imagenet-2012 dataset
3. [Object Detection](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/retinanet) using Retinanet model and OpenImages dataset
4. [Speech Recognition](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/rnnt) using RNNT model and LibriSpeech dataset
5. [Medical Imaging](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/3d-unet)  using 3d-unet model and KiTS19 dataset
6. Recommendation using DLRMv2 model and Criteo multihot dataset
7. [Large Language Model](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/gpt-j) using GPT-J model and CNN Daily Mail dataset

All seven tasks are applicable to the datacenter category while all except Recommendation are applicable to the edge category. 

Further, language processing and medical imaging models have a high accuracy variant where the achieved accuracy 
must be within `99.9%` (`99%` is the default accuracy requirement) of the fp32 reference model. 

The recommendation task only has a high-accuracy variant. Currently, we are not supporting the Recommendation task as we are not having a high-end server which is a requirement.

### Measure power

Power measurement is optional for MLPerf inference benchmark submissions but is nice to have especially 
if your system is having good power efficiency. For any benchmark run via CM, power measurement is turned 
on by `--power=yes --adr.mlperf-power-client.power_server=<Power server IP> --adr.mlperf-power-client.port=<Power server port>`. 
On the hardware side, you can follow [this tutorial](https://github.com/mlcommons/ck/blob/master/docs/tutorials/mlperf-inference-power-measurement.md) to get the setup done. 

## Optimize benchmarks

## Visualize and compare results



## Customize benchmarks

### Add new implementation

### Add new backend

### Add new model

### Add new data set




## Participate in reproducibility and optimization challenges

Please help this community project by participating in our 
[reproducibility and optimization challenges for MLPerf](https://access.cknowledge.org/playground/?action=challenges)!
