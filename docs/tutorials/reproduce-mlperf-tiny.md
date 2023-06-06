[ [Back to index](../README.md) ]

<details>
<summary>Click here to see the table of contents.</summary>

* [Tutorial: automate, visualize and reproduce Tiny MLPerf submissions](#tutorial-automate-visualize-and-reproduce-tiny-mlperf-submissions)
  * [Install CM](#install-cm)

</details>

# Tutorial: reproducibility study for TinyMLPerf submission with MicroTVM and NUCLEO-L4R5ZI board from STMicroelecronics

The [MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
is developing an [open-source Collective Knowledge platform](https://access.cknowledge.org/playground/?action=experiments&tags=mlperf-tiny)
to make it easier for the community to run, visualize and optimize MLPerf benchmarks 
out of the box across diverse software, hardware, models and data.

This tutorial demonstrates how to run and/or reproduce Tiny MLPerf benchmark and prepare your own submission
with the help of the [MLCommons CM automation language](https://github.com/mlcommons/ck/blob/master/docs/README.md).

You will build, flash and run image classification and keyword spotting applications
using [microTVM compiler](https://tvm.apache.org/docs/topic/microtvm/index.html)
on the [NUCLEO-L4R5ZI board](https://estore.st.com/en/nucleo-l4r5zi-cpn.html)
from STMicroelectronics.

You will need ~12GB of disk space and it will take ~20..30 minutes to download all dependencies 
and build TinyMLPerf benchmarks depending on your Internet and host platform speed.

Benchmark compilation and device flashing can be done on any Linux-based platform
while running benchmark using EEMBC GUI can be done on Linux and Windows.

If you have any questions about this tutorial, please get in touch via our public [Discord server](https://discord.gg/JjWNWXKxwT)
or open a GitHub issue [here](https://github.com/mlcommons/ck/issues).

## Install CM automation language

Follow [this guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md) 
to install the MLCommons CM automation language on your platform. 

We have tested this tutorial with Ubuntu 20.04 and Windows 10.

## Install MLCommons CK repository with CM automations

```bash
cm pull repo mlcommons@ck
```

If you have been using CM and would like to have a clean installation,
you can clean CM cache as follows:
```bash
cm rm cache -f
```

## Install all dependencies and build benchmarks





## Setup NUCLEO-L4R5ZI board

Before connecting your board to your platform via UBS port, please check that you have this 


## Flash 







To be continued ...
