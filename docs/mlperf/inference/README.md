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

This project is supported by the [MLCommons Task Force on Automation and Reproducibility](../taskforce.md),
[cTuning foundation](https://cTuning.org) and [cKnowledge Ltd](https://cKnowledge.org).

Don't hesitate to get in touch with us using this [public Discord server](https://discord.gg/JjWNWXKxwT) 
to provide your feedback, ask questions, add new benchmark implementations, models, data sets and hardware backends,
and prepare and optimize your MLPerf submissions.


## Install CM automation language

Install MLCommons CM automation language as described [here](../../installation.md). 
It is a very small Python library with `cm` and `cmr` command line front-ends and minimal dependencies including Python 3+, Git and wget.

If you encounter problems, please report them at [GitHub](https://github.com/mlcommons/ck/issues).


## Install repository with CM automations

Install the MLCommons repository with [reusable automation recipes (CM scripts)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
that are being developed and shared by the community under Apache 2.0 license 
to enable portable, modular, and technology-agnostic benchmarks and applications 
that can automatically run with any software, hardware, models and data sets.

```bash
cm pull repo mlcommons@ck
```

You can run it again at any time to pick up the latest updates.

Note that CM will store all such repositories and downloaded/installed data sets, models and tools
in your `$HOME/CM` directory. 

Since MLPerf benchmarks require lots of space (somethings hundreds of Gigabytes), 
you can change the above location to some large scratch disk using `CM_REPOS` 
environment variable as follows:

```bash
export CM_REPOS={new path to CM repositories and data}
```

## Prepare hardware

Read this section if you want to run MLPerf benchmarks in a native environment, i.e. without containers.

### CPU

If you plan to run MLPerf benchmarks on x64 and/or Arm64 CPUs, no extra setup is necessary.

### CUDA GPU

If you plan to use CUDA in your native environment, please follow [this guide](../../installation-cuda.md) to set it up on your system.

### TPU

*Under preparation*

### AWS inferentia

*Under preparation*

### Other backends

We work with the community to add more hardware backends to MLPerf benchmarks automated by CM.
Please get in touch with us via [public Discord server](https://discord.gg/JjWNWXKxwT) 
if you are interested to collaborate/help!


## Run benchmarks and prepare submissions

* [BERT](bert)
* [ResNet-50](resnet50)
* [RetinaNet](retinanet)
* [3D UNET](3d-unet)
* [RNNT](rnnt)
* GPT-J

### Measure power



## Optimize benchmarks

## Visualize and compare results



## Customize benchmarks

### Add new implementation

### Add new backend

### Add new model

### Add new data set




## Participate in reproducibility and optimization challenges
