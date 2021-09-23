# Collective Knowledge framework (CK)

[![PyPI version](https://badge.fury.io/py/ck.svg)](https://badge.fury.io/py/ck)
[![Downloads](https://pepy.tech/badge/ck)](https://pepy.tech/project/ck)
[![Python Version](https://img.shields.io/badge/python-2.7%20|%203.4+-blue.svg)](https://pypi.org/project/ck)

[![Build Status](https://travis-ci.com/ctuning/ck.svg?branch=master)](https://travis-ci.com/ctuning/ck)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
[![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

[![Documentation Status](https://readthedocs.org/projects/ck/badge/?version=latest)](https://ck.readthedocs.io/en/latest/?badge=latest)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Fp6uxCqTazmCSSl8v-nY93VVmcOoLiXi?usp=sharing)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1a761nKgoHlJAy6gOXh-c9H4WkLV8nzRU?usp=sharing)


## Motivation

While Machine Learning is becoming more and more important in everyday life, designing efficient ML Systems and deploying them in the real world 
is becoming increasingly challenging, time consuming and costly.
Researchers and engineers must keep pace with rapidly evolving software stacks and a Cambrian explosion of hardware platforms from the cloud to the edge. 
Such platforms have their own specific libraries, frameworks, APIs and specifications and often require repetitive, tedious and ad-hoc optimization 
of the whole model/software/hardware stack to trade off accuracy, latency, throughout, power consumption, size and costs depending on user requirements and constraints.

### The CK framework

*The Collective Knowledge framework (CK)* is our attempt to develop a common infrastructure that can be used
by the community similar to Wikipedia to learn how to solve above challenges and make it easier to co-design, 
benchmark, optimize and deploy Machine Learning Systems in the real world across continuously evolving software, 
hardware and data sets (see our [ACM TechTalk](https://www.youtube.com/watch?v=7zpeIVwICa4) for more details):

* CK aims at providing a common playground for researchers and practitioners to share their knowledge
  in the form of reusable automation recipes with a unified Python API, CLI and meta description: 
  - [Stable CK automation recipes](https://github.com/mlcommons/ck/tree/master/ck/repo/module)
  - [MLPerf&trade; benchmark automation recipes](https://github.com/mlcommons/ck/tree/master/ck-mlops/repo/module)

* CK helps to organize software projects and Git repositories as a database of above automation recipes 
  and related artifacts based on [FAIR principles](https://www.nature.com/articles/sdata201618)
  as described in our [journal article](https://arxiv.org/pdf/2011.01149.pdf) ([shorter pre-print]( https://arxiv.org/abs/2006.07161 )).
  See examples of CK-compatible GitHub repositories: 
  - [MLPerf/MLOps automation](https://github.com/mlcommons/ck-mlops)
  - [ACM REQUEST tournament for collaborative and reproducible ML/SW/HW co-design](https://github.com/ctuning/ck-request)

### Community developments

We collaborated with the community to reproduce [150+ ML and Systems papers](https://cTuning.org/ae)
and implement the following reusable automation recipes in the CK format: 

* Portable meta package manager to automatically detect, install or rebuild various ML artifacts 
  (ML models, data sets, frameworks, libraries, etc) across different platform and operating systems including Linux, Windows, MacOS and Android:
  - [ML artifact detection plugins](https://github.com/mlcommons/ck-mlops/tree/main/soft)
  - [ML meta package installation plugins](https://github.com/mlcommons/ck-mlops/tree/main/package)
  - OS descriptions: [Linux/MacOS/Android](https://github.com/mlcommons/ck-mlops/tree/main/os) ; [Windows](https://github.com/ctuning/ck-win/tree/main/os) 

* Portable manager for Python virtual environments: [CK repo](https://github.com/mlcommons/ck-venv).

* Portable workflows to support collaborative, reproducible and cross-platform benchmarking:
  - [ML Systems benchmarking](https://github.com/mlcommons/ck-mlops/tree/main/program)
  - [Compiler benchmarking](https://github.com/ctuning/ctuning-programs/tree/master/program)

* Portable workflows to automate MLPerf&trade; benchmark:
  - [End-to-end submission suite used by multiple organizations to automate the submission of MLPerf inference benchmark](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/README.md)
    - MLperf inference v1.1 results: [MLCommons press-release](https://mlcommons.org/en/news/mlperf-inference-v11), 
      [Datacenter results](https://mlcommons.org/en/inference-datacenter-11), 
      [Edge results](https://mlcommons.org/en/inference-edge-11)
  - [Reproducibility studies for MLPerf inference benchmark v1.1 automated by CK](https://github.com/mlcommons/ck/tree/master/docs/mlperf-automation/reproduce#reproducibility-reports-mlperf-inference-benchmark-v11)
  - [Design space exploration of ML/SW/HW stacks and customizable visualization](https://cknowledge.io/result/crowd-benchmarking-mlperf-inference-classification-mobilenets-all)


Further community developments are supported by [MLCommons&trade;](https://mlcommons.org), [OctoML](https://octoml.ai) and the [cTuning foundation](https://cTuning.org)
within the *MLCommons' Design Space Exploration workgroup*. 
Please contact [Grigori Fursin](https://www.linkedin.com/in/grigorifursin) if you are interested to join this community effort!


## Releases

### Stable versions

The latest version of the CK automation suite supported by MLCommons&trade;:
* [CK framework v2.5.8 (Apache 2.0 license)](https://github.com/mlcommons/ck/releases/tag/V2.5.8)
* [CK automation suite for MLPerf&trade; and ML/SW/HW co-design](https://github.com/mlcommons/ck-mlops)

### Development versions

We plan to develop a new version of the CK framework (v3) 
within the MLCommons' Design Space Exploration workgroup -
please contact [Grigori Fursin](mailto:grigori@octoml.ai) to join this community effort!

### Deprecated versions

**Versions 1.x including v1.17.0 and 1.55.5 (BSD license)** are not supported anymore. 
Please get in touch and we will help you to upgrade your infrastructure to use the latest MLCommons technology!

## Current projects
* [Automating MLPerf(tm) inference benchmark and packing ML models, data sets and frameworks as CK components with a unified API and meta description](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/README.md)
* Developing customizable dashboards for MLPerf&trade; to help end-users select ML/SW/HW stacks on a Pareto frontier: [aggregated MLPerf&trade; results]( https://cknowledge.io/?q="mlperf-inference-all" )
* Providing a common format to share artifacts at ML, systems and other conferences: [video](https://youtu.be/DIkZxraTmGM), [Artifact Evaluation](https://cTuning.org/ae)
* Redesigning CK together with the community based on user feedback: [incubator](https://github.com/mlcommons/ck/tree/master/incubator)
* [Other real-world use cases](https://cKnowledge.org/partners.html) from MLPerf&trade;, Qualcomm, Arm, General Motors, IBM, the Raspberry Pi foundation, ACM and other great partners;

## Documentation

* [Online CK documentation]( https://ck.readthedocs.io ) 
  * [Why CK?]( https://ck.readthedocs.io/en/latest/src/introduction.html ) 
  * [CK Basics](https://michel-steuwer.github.io/About-CK)
  * [Try CK]( https://ck.readthedocs.io/en/latest/src/first-steps.html )
* [Publications](https://github.com/mlcommons/ck/wiki/Publications)

## Installation

Follow [this guide](https://ck.readthedocs.io/en/latest/src/installation.html) 
to install CK framework on your platform.

CK supports the following platforms:

|               | As a host platform | As a target platform |
|---------------|:------------------:|:--------------------:|
| Generic Linux | ✓ | ✓ |
| Linux (Arm)   | ✓ | ✓ |
| Raspberry Pi  | ✓ | ✓ |
| MacOS         | ✓ | ± |
| Windows       | ✓ | ✓ |
| Android       | ± | ✓ |
| iOS           | TBD | TBD |
| Bare-metal (edge devices)   | - | ± |

## Examples

### Portable CK workflow (native environment without Docker)

Here we show how to pull a GitHub repo in the CK format 
and use a unified CK interface to compile and run 
any program (image corner detection in our case)
with any compatible data set on any compatible platform:

```bash
python3 -m pip install ck

ck pull repo:mlcommons@ck-mlops

ck ls program:*susan*

ck search dataset --tags=jpeg

ck pull repo:ctuning-datasets-min

ck search dataset --tags=jpeg

ck detect soft:compiler.gcc
ck detect soft:compiler.llvm

ck show env --tags=compiler

ck compile program:image-corner-detection --speed

ck run program:image-corner-detection --repeat=1 --env.MY_ENV=123 --env.TEST=xyz
```

You can check output of this program in the following directory:
```bash
cd `ck find program:image-corner-detection`/tmp
ls

processed-image.pgm
```

You can now view this image with detected corners.


Check [CK docs](https://ck.readthedocs.io/en/latest/src/introduction.html) for further details.

### MLPerf&trade; benchmark workflows

* [Current coverage](https://github.com/mlcommons/ck/tree/master/docs/mlperf-automation#readme)
* [MLPerf inference v1.1 workflows](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/reproduce/README.md#reproducibility-reports-mlperf-inference-benchmark-v11)

### Portable CK workflows inside containers

We have prepared adaptive CK containers to demonstrate MLOps capabilities:
* https://github.com/mlcommons/ck-mlops/tree/main/docker

You can run them as follows:

```bash
ck pull repo:mlcommons@ck-mlops
ck build docker:ck-template-mlperf --tag=ubuntu-20.04
ck run docker:ck-template-mlperf --tag=ubuntu-20.04
```

### Portable workflow example with virtual CK environments

You can create multiple [virtual CK environments](https://github.com/mlcommons/ck-venv) with templates
to automatically install different CK packages and workflows, for example for MLPerf&trade; inference:

```
ck pull repo:mlcommons@ck-venv
ck create venv:test --template=mlperf-inference-main
ck ls venv
ck activate venv:test

ck pull repo:mlcommons@ck-mlops
ck install package --ask --tags=dataset,coco,val,2017,full
ck show env

```

### Integration with web services and CI platforms

All CK modules, automation actions and workflows are accessible as a micro-service with a unified JSON I/O API
to make it easier to integrate them with web services and CI platforms as described 
[here](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/tools/continuous-integration.md).




### Other use cases

* [List of various use cases]( https://ck.readthedocs.io/en/latest/src/introduction.html#ck-showroom )







## CK portal 

We have developed the [cKnowledge.io portal](https://cKnowledge.io) to help the community
organize and find all the CK workflows and components similar to PyPI:

* [Search CK components](https://cKnowledge.io)
* [Browse CK components](https://cKnowledge.io/browse)
* [Find reproduced results from papers]( https://cKnowledge.io/reproduced-results )
* [Test CK workflows to benchmark and optimize ML Systems]( https://cKnowledge.io/demo )



## Containers to test CK automation recipes and workflows

The community provides Docker containers to test CK and components using different ML/SW/HW stacks (DSE).

* A set of Docker containers to test the basic CK functionality
  using some MLPerf inference benchmark workflows: 
  https://github.com/mlcommons/ck-mlops/tree/main/docker/test-ck


## Contributions

Users can extend the CK functionality via [CK modules](https://github.com/mlcommons/ck/tree/master/ck/repo/module) 
or external [GitHub reposities](https://cKnowledge.io/repos) in the CK format
as described [here](https://ck.readthedocs.io/en/latest/src/typical-usage.html).

Please check [this documentation](https://ck.readthedocs.io/en/latest/src/how-to-contribute.html)
if you want to extend the CK core functionality and [modules](https://github.com/mlcommons/ck/tree/master/ck/repo/module). 

Note, that we plan to [redesign the CK core](https://github.com/mlcommons/ck/projects/1) 
to be more pythonic (we wrote the first prototype without OO to be able 
to port it to bare-metal devices in C but eventually we decided to drop this idea).

Please consider joining the *MLCommons' Design Space Exploration workgroup*
to join this community effort - contact [Grigori Fursin](mailto:grigori@octoml.ai) for more details.



## Author and coordinator

* [Grigori Fursin](https://fursin.net) (OctoML/MLCommons/cTuning foundation)

## Acknowledgments

We would like to thank all [contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) 
and [collaborators](https://cKnowledge.org/partners.html) for their support, fruitful discussions, 
and useful feedback! See more acknowledgments in the [CK journal article](https://arxiv.org/abs/2011.01149).
