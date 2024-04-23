<br>
<br>
<br>

**Note that this directory is in the archive mode since the Collective Knowledge framework (v1 and v2)
  is now officially discontinued in favour of the new, light-weight, non-intrusive and technology-agnostic 
  [Collective Mind workflow workflow automation framework ](../cm). You can learn more about the motivation
  behind CK in this [ACM TechTalk](https://www.youtube.com/watch?v=7zpeIVwICa4) 
  and the [journal article](https://doi.org/10.1098/rsta.2020.0211).**

<br>
<br>
<br>

# Collective Knowledge framework (CK)

[![Downloads](https://pepy.tech/badge/ck)](https://pepy.tech/project/ck)
[![PyPI version](https://badge.fury.io/py/ck.svg)](https://badge.fury.io/py/ck)
[![Python Version](https://img.shields.io/badge/python-2.7%20|%203.4+-blue.svg)](https://pypi.org/project/ck)

[![Build Status](https://travis-ci.com/ctuning/ck.svg?branch=master)](https://travis-ci.com/ctuning/ck)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
[![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

[![Documentation Status](https://readthedocs.org/projects/ck/badge/?version=latest)](https://ck.readthedocs.io/en/latest/?badge=latest)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Fp6uxCqTazmCSSl8v-nY93VVmcOoLiXi?usp=sharing)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1a761nKgoHlJAy6gOXh-c9H4WkLV8nzRU?usp=sharing)


## News



* **2022 May:** [Grigori Fursin](https://cKnowledge.org/gfursin) 
  started prototyping the new [Collective Mind framework](https://doi.org/10.5281/zenodo.8105339)
  within the [MLCommons Task Force on Automation and Reproducibility](../../docs/taskforce.md)
  from scratch based on the feedback from the users and MLCommons members.

* **2022 April 3:** We presented the CK concept to bridge the growing gap between ML Systems research and production 
  at the HPCA'22 workshop on [benchmarking deep learning systems](https://sites.google.com/g.harvard.edu/mlperf-bench-hpca22/home).

* **2022 March:** We presented the [CK concept to enable collaborative and reproducible ML Systems R&D](https://meetings.siam.org/sess/dsp_programsess.cfm?SESSIONCODE=73126) 
  at the SIAM'22 workshop on "Research Challenges and Opportunities within Software Productivity, Sustainability, and Reproducibility"

* **2022 March:** we've released the first prototype of [the Collective Mind toolkit (CK2)](https://github.com/mlcommons/ck/tree/master/ck2)
  based on your feedback and our practical experience [reproducing 150+ ML and Systems papers and validating them in the real world](https://www.youtube.com/watch?v=7zpeIVwICa4).

## Motivation

While Machine Learning is becoming more and more important in everyday life, designing efficient ML Systems and deploying them in the real world 
is becoming increasingly challenging, time consuming and costly.
Researchers and engineers must keep pace with rapidly evolving software stacks and a Cambrian explosion of hardware platforms from the cloud to the edge. 
Such platforms have their own specific libraries, frameworks, APIs and specifications and often require repetitive, tedious and ad-hoc optimization 
of the whole model/software/hardware stack to trade off accuracy, latency, throughout, power consumption, size and costs depending on user requirements and constraints.

### The CK framework

*The Collective Knowledge framework (CK)* is our attempt to develop a common plug&play infrastructure that can be used
by the community similar to Wikipedia to learn how to solve above challenges and make it easier to co-design, 
benchmark, optimize and deploy Machine Learning Systems in the real world across continuously evolving software, 
hardware and data sets (see our [ACM TechTalk](https://www.youtube.com/watch?v=7zpeIVwICa4) for more details):

* CK aims at providing a simple playground with minimal software dependencies to help researchers and practitioners share their knowledge
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
    - MLPerf inference v1.1 results: [MLCommons press-release](https://mlcommons.org/en/news/mlperf-inference-v11), 
      [Datacenter results](https://mlcommons.org/en/inference-datacenter-11), 
      [Edge results](https://mlcommons.org/en/inference-edge-11)
  - [Reproducibility studies for MLPerf inference benchmark v1.1 automated by CK](https://github.com/mlcommons/ck/tree/master/docs/mlperf-automation/reproduce#reproducibility-reports-mlperf-inference-benchmark-v11)
  - [Design space exploration of ML/SW/HW stacks and customizable visualization](https://cknow.io/result/crowd-benchmarking-mlperf-inference-classification-mobilenets-all)


Please contact [Grigori Fursin](https://www.linkedin.com/in/grigorifursin) if you are interested to join this community effort!

### Tutorials

* [CK automations for unified benchmarking]( https://colab.research.google.com/drive/1a761nKgoHlJAy6gOXh-c9H4WkLV8nzRU?usp=sharing )
* [CK-based MLPerf inference benchmark automation example]( https://colab.research.google.com/drive/1Fp6uxCqTazmCSSl8v-nY93VVmcOoLiXi?usp=sharing )
  * [CK-based MLPerf inference vision benchmark v1.1 automation (TVM)]( https://colab.research.google.com/drive/1aywGlyD1ZRDtQTrQARVgL1882JcvmFK-?usp=sharing )
  * [CK-based MLPerf inference vision benchmark v1.1 automation (ONNX)]( https://colab.research.google.com/drive/1ij1rWoqje5-Sn6UsdFj1OzYakudI2RIS?usp=sharing )
* [CK basics]( https://colab.research.google.com/drive/15lQgxuTSkEPqi4plaat1_v2gJcfIrATF?usp=sharing )

## Releases

### Stable versions

The latest version of the CK automation suite supported by MLCommons&trade;:
* [CK framework v2.6.1 (Apache 2.0 license)](https://github.com/mlcommons/ck/releases/tag/V2.6.1)
* [CK automation suite for MLPerf&trade; and ML/SW/HW co-design](https://github.com/mlcommons/ck-mlops)


## Current projects
* [Automating MLPerf(tm) inference benchmark and packing ML models, data sets and frameworks as CK components with a unified API and meta description](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/README.md)
* Developing customizable dashboards for MLPerf&trade; to help end-users select ML/SW/HW stacks on a Pareto frontier: [aggregated MLPerf&trade; results]( https://cknow.io/?q="mlperf-inference-all" )
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

We use the [cKnowledge.io portal](https://cknow.io) to help the community
organize and find all the CK workflows and components similar to PyPI:

* [Search CK components](https://cknow.io)
* [Browse CK components](https://cknow.io/browse)
* [Find reproduced results from papers]( https://cknow.io/reproduced-results )
* [Test CK workflows to benchmark and optimize ML Systems]( https://cknow.io/demo )



## Containers to test CK automation recipes and workflows

The community provides Docker containers to test CK and components using different ML/SW/HW stacks (DSE).

* A set of Docker containers to test the basic CK functionality
  using some MLPerf inference benchmark workflows: 
  https://github.com/mlcommons/ck-mlops/tree/main/docker/test-ck



## Acknowledgments

We would like to thank all [collaborators and contributors](CONTRIBUTING.md) 
for their support, fruitful discussions, and useful feedback! 
See more acknowledgments in this [journal article](https://doi.org/10.1098/rsta.2020.0211)
and [ACM TechTalk'21](https://www.youtube.com/watch?v=7zpeIVwICa4).
