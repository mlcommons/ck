[ [Back to index](../README.md) ]

<details>
<summary>Click here to see the table of contents.</summary>

* [Tutorial: reproducibility study for TinyMLPerf submission with MicroTVM and NUCLEO-L4R5ZI board from STMicroelecronics](#tutorial-reproducibility-study-for-tinymlperf-submission-with-microtvm-and-nucleo-l4r5zi-board-from-stmicroelecronics)
  * [Install software and setup hardware](#install-software-and-setup-hardware)
  * [Build all benchmarks from OctoML's v1.0 submission](#build-all-benchmarks-from-octoml's-v10-submission)
  * [Flash](#flash)
  * [Generate submission](#generate-submission)
  * [Run submission checker and prepare report](#run-submission-checker-and-prepare-report)
  * [Import results to the CK platform](#import-results-to-the-ck-platform)
  * [Visualize and compare TinyMLPerf](#visualize-and-compare-tinymlperf)
  * [The next steps](#the-next-steps)
  * [Contact MLCommons task force on automation and reproducibility](#contact-mlcommons-task-force-on-automation-and-reproducibility)

</details>

# Tutorial: reproducibility study for TinyMLPerf submission with MicroTVM and NUCLEO-L4R5ZI board from STMicroelecronics

The [MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md),
[cTuning foundation](https://www.linkedin.com/company/ctuning-foundation) and [cKnowledge Ltd](https://www.linkedin.com/company/cknowledge)
organize public challenges to let the community run, visualize and optimize MLPerf benchmarks 
out of the box across diverse software, hardware, models and data.

This tutorial demonstrates how to run and/or reproduce Tiny MLPerf benchmark (OctoML v1.0 submission)
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

## Install software and setup hardware

Please follow [this tutorial](automate-mlperf-tiny.md)
to install the MLCommons CM automation language, EEMBC Energy Runner and other software dependencies for your host platform,
and setup NUCLEO-L4R5ZI board from STMicroelecronics.

We reproduced/replicated OctoML's v1.0 submission using a host machine with Ubuntu 20.04 and Python 3.8.10.


## Build all benchmarks from OctoML's v1.0 submission

You can use CM script to automatically build all benchmarks in all variants to reproduce OctoML's v1.0 submission:

```bash
cm run script --tags=generate,tiny,mlperf,octoml,submission
```

The main CM scripts which automatically gets called from the above command are given below.

1. [Build Tiny Models](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)
2. [Flash Tiny Models](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary)
3. [Get Zephyr](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr)
4. [Get Zephyr SDK](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk)
5. [Get MictoTVM](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-microtvm)
6. [GET CMSIS_5](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmsis_5)

The above command should produce five elf binaries which can be located inside the respective cache entries given by the below command
```
cm show cache --tags=reproduce,tiny,octoml,mlperf
```

## Flash


To flash each benchmark, follow the command bellow. Make sure to replace `VARIANT` by either `cmsis_nn` or `native`. 
You need to specify the model by replacing `MODEL` with a value from (`ad`, `kws`, `ic`, `vww`). 
Finally, you need to choose `_NUCLEO` or `_NRF` to specify the target board to flash.

``` 
cm run script --tags=flash,tiny,_VARIANT,_MODEL,_BOARD
```

We have tested the following combinations:

```bash
cm run script --tags=flash,tiny,_cmsis_nn,_ic,_NUCLEO
cm run script --tags=flash,tiny,_native,_ic,_NUCLEO
cm run script --tags=flash,tiny,_cmsis_nn,_kws,_NUCLEO
cm run script --tags=flash,tiny,_native,_kws,_NUCLEO
```

After each flashing, follow the [EEMBC Runner guide](https://github.com/eembc/energyrunner#software-setup)
to run benchmark in performance and accuracy modes.

You can find the logs after each run in the following directory on your host machine:
`$HOME/eembc/runner/sessions`.



## Generate submission

[Under development](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission).

## Run submission checker and prepare report

Follow this [guide](https://github.com/ctuning/mlcommons-ck/blob/master/cm-mlops/script/generate-mlperf-tiny-report/README-extra.md).

## Import results to the CK platform

Follow this [guide](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/import-mlperf-tiny-to-experiment/README-extra.md)

## Visualize and compare TinyMLPerf 

You can visualize and compare TinyMLPerf results [here](https://access.cknowledge.org/playground/?action=experiments&tags=mlperf-tiny).
You can use this collaborative platform inside your organization to reproduce and optimize benchmarks and applications of your interest.


## The next steps

Please follow the rest of this [tutorial](automate-mlperf-tiny.md) 
to see how to visualize and compare your results, and learn more about our future automation plans.


## Contact MLCommons task force on automation and reproducibility

Please join the [MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
to get free help to automate and optimize MLPerf benchmarks for your software and hardware stack using the MLCommons CM automation language!
