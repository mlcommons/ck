[![PyPI version](https://badge.fury.io/py/cbench.svg)](https://badge.fury.io/py/cbench)
[![Python Version](https://img.shields.io/badge/python-2.7%20|%203.4+-blue.svg)](https://pypi.org/project/cbench)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/cbench.svg?branch=master)](https://travis-ci.org/ctuning/cbench)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/yjq5myrrrkx3rydc?svg=true)](https://ci.appveyor.com/project/gfursin/cbench)


## News

We have successfully completed the prototyping phase of the Collective Knowledge technology
to make it easier to reproduce AI&ML and deploy it in production with the help of portable CK workflows, reusable artifacts and MLOps
as described in this [white paper](https://arxiv.org/abs/2006.07161)
and the [CK presentation](https://cKnowledge.io/presentation/ck).
We are now preparing the second phase of this project to make CK simpler to use, more stable and more user friendly - 
don't hesitate to get in touch with the [CK author](https://cKnowledge.io/@gfursin) to know more!



## Introduction

cBench is a small and cross-platform framework 
connected with the [open Collective Knowledge portal](https://cKnowledge.io)
to help researchers and practitioners 
[reproduce ML&systems research](https://cKnowledge.io/reproduced-papers)
on their own bare-metal platforms, participate in collaborative
benchmarking and optimization, 
and share results on [live scoreobards](https://cKnowledge.io/reproduced-results).

You can try to reproduce MLPerf inference benchmark on your machine using [this solution](https://cKnowledge.io/test)
and see public results from the community on this [scoreboard](https://cknowledge.io/c/result/sota-mlperf-object-detection-v0.5-crowd-benchmarking).

cBench is a part of the [Collective Knowledge project (CK)](https://cKnowledge.org)
and uses [portable CK solutions](https://cknowledge.io/docs/intro/introduction.html#portable-ck-solution)
to describe how to download, build, benchmark and optimize applications
across different hardware, software, models and data sets.

## Platform support:

|               | As a host platform | As a target platform |
|---------------|:------------------:|:--------------------:|
| Generic Linux | ✓ | ✓ |
| Linux (Arm)   | ✓ | ✓ |
| Raspberry Pi  | ✓ | ✓ |
| MacOS         | ✓ | ± |
| Windows       | ✓ | ✓ |
| Android       | ± | ✓ |
| iOS           | TBD | TBD |


## Object detection crowd-benchmarking demo on Ubuntu

Install prerequisites:

```
sudo apt update
sudo apt install git wget libz-dev curl cmake
sudo apt install gcc g++ autoconf autogen libtool
sudo apt install libfreetype6-dev
sudo apt install python3.7-dev
sudo apt install -y libsm6 libxext6 libxrender-dev
```

Install cbench:

```
python3 -m pip install cbench
```

Initialize the [CK solution for MLPerf](https://cknowledge.io/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows):

```
cb init demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows
```

Participate in crowd-benchmarking:

```
cb benchmark demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows
```

See your results on a public [SOTA dashboard](https://cknowledge.io/c/result/sota-mlperf-object-detection-v0.5-crowd-benchmarking).

You can also use the stable Docker image to participate in crowd-benchmarking:

```
sudo docker run ctuning/cbench-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows /bin/bash -c "cb benchmark demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows"
```

You can also check [all dependencies for this solution](https://cknowledge.io/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows/#dependencies).



## Documentation

* [Online docs for the Collective Knowledge technology](https://cKnowledge.io/docs)

## Feedback

* This is an ongoing project - don't hesitate to [contact us](https://cKnowledge.org/contacts.html) 
  if you have any feedback and suggestions!

## Acknowledgments

We would like to thank all [CK partners](https://cKnowledge.org/partners.html) 
for fruitful discussions and feedback!


*Copyright 2020 [cTuning foundation](https://cTuning.org)*
