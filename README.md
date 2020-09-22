# Collective Knowledge framework (CK)

[![Downloads](https://pepy.tech/badge/ck)](https://pepy.tech/project/ck)
[![PyPI version](https://badge.fury.io/py/ck.svg)](https://badge.fury.io/py/ck)
[![Python Version](https://img.shields.io/badge/python-2.7%20|%203.4+-blue.svg)](https://pypi.org/project/ck)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)

[![Documentation Status](https://readthedocs.org/projects/ck/badge/?version=latest)](https://ck.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

## Overview

Collective Knowledge framework (CK) helps to organize software projects
as a database of reusable components with common automation actions
and extensible meta descriptions based on [FAIR principles](https://www.nature.com/articles/sdata201618)
(findability, accessibility, interoperability, and reusability).

We want to help everyone share, reuse, and extend their knowledge
in the form of reusable artifacts and portable workflows with a common API, CLI,
and meta description. See how CK supports collaborative and reproducible AI, ML, and Systems R&D:
* [Real-world use-cases](https://cKnowledge.org/partners.html) from Arm, General Motors, IBM, MLPerf, the Raspberry Pi foundation, and ACM
* [Reddit discussion about reproducing 150 papers](https://www.reddit.com/r/MachineLearning/comments/ioq8do/n_reproducing_150_research_papers_the_problems)
* [Project overview (preprint; to appear soon in the journal)](https://doi.org/10.6084/m9.figshare.12988361)

## News

* **2020 August**: We have completed the prototyping phase and successfully validated CK 
  in [several projects](https://cKnowledge.org/partners)
  to automate the complex co-design process of [efficient ML/SW/HW stacks](https://cknowledge.io/c/result/crowd-benchmarking-mlperf-inference-classification-mobilenets-all),
  simplify [MLPerf benchmark](https://cKnowledge.io/c/docker) submissions,
  and quickly deploy emerging technologies (AI, ML, quantum) in production
  in the [most efficient way (speed, accuracy, energy, costs)]( https://cKnowledge.io/results ) 
  across diverse platforms from data centers to mobile phones and edge devices.
  See this [white paper](https://doi.org/10.6084/m9.figshare.12988361)
  and the [CK presentation](https://www.reddit.com/r/MachineLearning/comments/ioq8do/n_reproducing_150_research_papers_the_problems)
  for more details.
  *We are now raising funding to continue developing our [Collective Knowledge platform](https://cKnowledge.io) - 
  don't hesitate to get in touch with [Grigori Fursin]( https://cKnowledge.org/contacts.html ) to know more!*

## Documentation

* [News](https://github.com/ctuning/ck/wiki/News-archive)
* [Online CK documentation]( https://ck.readthedocs.io ) 
  * [Why CK?]( https://ck.readthedocs.io/en/latest/src/introduction.html ) 
  * [CK Basics](https://michel-steuwer.github.io/About-CK)
  * [Try CK]( https://ck.readthedocs.io/en/latest/src/first-steps.html )
* [Publications](https://github.com/ctuning/ck/wiki/Publications)

## CK-powered workflows, automation actions, and reusable artifacts

* [Real-world use-cases](https://cKnowledge.org/partners)
* Reproducibility initiatives: [[methodology](https://cTuning.org/ae)], [[events](https://cKnowledge.io/events)]
* Showroom (public projects powered by CK):
  * [MLPerf automation](https://github.com/ctuning/ck-mlperf)
  * Student Cluster Competition automation: [SCC18](https://github.com/ctuning/ck-scc18), [digital artifacts](https://github.com/ctuning/ck-scc)
  * ML-based autotuning project: [reproducible paper demo](https://cKnowledge.io/report/rpi3-crowd-tuning-2017-interactive),  [MILEPOST]( https://github.com/ctuning/reproduce-milepost-project )
  * Stable Docker containers with CK workflows: [MLPerf example](https://cknowledge.io/c/docker/mlperf-inference-vision-with-ck.intel.ubuntu-18.04/), [cKnowledge.io]( https://cKnowledge.io/c/docker ), [Docker Hub](https://hub.docker.com/u/ctuning)
  * [Quantum hackathons](https://cKnowledge.org/quantum)
  * [ACM SW/HW co-design tournaments for Pareto-efficient deep learning](https://cKnowledge.org/request)
  * Portable CK workflows and components for:
    * [TensorFlow](https://github.com/ctuning/ck-tensorflow)
    * [PyTorch](https://github.com/ctuning/ck-pytorch)
    * [TensorRT](https://github.com/ctuning/ck-tensorrt)
    * [OpenVino](https://github.com/ctuning/ck-openvino)
    * [individual NN operators](https://github.com/ctuning/ck-nntest)
    * [object detection](https://github.com/ctuning/ck-object-detection)
  * [GUI to automate  ML/SW/HW benchmarking with MLPerf example (under development)](https://cKnowledge.io/test)
  * [Reproduced papers]( https://cKnowledge.io/reproduced-papers )
  * [Live scoreboards for reproduced papers]( https://cKnowledge.io/reproduced-results )
* Examples of CK components (automations, API, meta descriptions):
    * *program : image-classification-tflite-loadgen* [[cKnowledge.io]( https://cKnowledge.io/c/program/image-classification-tflite-loadgen )] [[GitHub]( https://github.com/ctuning/ck-mlperf/tree/master/program/image-classification-tflite-loadgen )]
    * *program : image-classification-tflite* [[GitHub](https://github.com/ctuning/ck-tensorflow/tree/master/program/image-classification-tflite)]
    * *soft : lib.mlperf.loadgen.static* [[GitHub]( https://github.com/ctuning/ck-mlperf/tree/master/soft/lib.mlperf.loadgen.static )]
    * *package : lib-mlperf-loadgen-static* [[GitHub]( https://github.com/ctuning/ck-mlperf/tree/master/package/lib-mlperf-loadgen-static )]
    * *package : model-onnx-mlperf-mobilenet* [[GitHub]( https://github.com/ctuning/ck-mlperf/tree/master/package/model-onnx-mlperf-mobilenet/.cm )]
    * *package : lib-tflite* [[cKnowledge.io]( https://cKnowledge.io/c/package/lib-tflite )] [[GitHub]( https://github.com/ctuning/ck-tensorflow/tree/master/package/lib-tflite )]
    * *docker : object-detection-tf-py.tensorrt.ubuntu-18.04* [[cKnowledge.io]( https://cknowledge.io/c/docker/object-detection-tf-py.tensorrt.ubuntu-18.04 )]
    * *docker* [[GitHub]( https://github.com/ctuning/ck-mlperf/tree/master/docker )]
    * *docker : speech-recognition.rnnt* [[GitHub]( https://github.com/ctuning/ck-mlperf/tree/master/docker/speech-recognition.rnnt )]
    * *package : model-tf-** [[GitHub]( https://github.com/ctuning/ck-object-detection/tree/master/package )]
    * *script : mlperf-inference-v0.7.image-classification* [[cKnowledge.io]( https://cknowledge.io/c/script/mlperf-inference-v0.7.image-classification )]
    * *jnotebook : object-detection* [[GitHub](https://nbviewer.jupyter.org/urls/dl.dropbox.com/s/5yqb6fy1nbywi7x/medium-object-detection.20190923.ipynb)]


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

## Example

Here we show how to pull a GitHub repo in the CK format 
and use a unified CK interface to compile and run 
any program (image corner detection in our case)
with any compatible data set on any compatible platform:

```bash
pip install ck

ck pull repo --url=https://github.com/ctuning/ck-crowdtuning

ck ls program:*susan*

ck search dataset --tags=jpeg

ck compile program:cbench-automotive-susan --speed

ck run program:cbench-automotive-susan --cmd_key=corners --repeat=1 --env.MY_ENV=123 --env.TEST=xyz
```

You can check output of this program in the following directory:
```bash
cd `ck find program:cbench-automotive-susan`/tmp
ls -l

tmp-output.tmp - image with detected corners (rename to ppm to view it)
```

Check [CK docs](https://ck.readthedocs.io/en/latest/src/introduction.html) for further details.


## Open CK portal 

[cKnowledge.io](https://cKnowledge.io): organizing [ML and Systems knowledge]( https://doi.org/10.5281/zenodo.4005773 )
in the form of portable CK workflows, automation actions, and reusable components:

* [**All CK ML&systems components**](https://cknowledge.io/?q=mlsystems)
* [CK compatible repositories]( https://cknowledge.io/repos )
* [CK-based Docker images]( https://cKnowledge.io/c/module/docker )
* [CK modules]( https://cKnowledge.io/modules )
* [Automation actions]( https://cKnowledge.io/actions )
* [Portable program workflows]( https://cKnowledge.io/programs )
* [Meta packages]( https://cKnowledge.io/packages )
* [Software detection (code, data, models)]( https://cKnowledge.io/soft )
* [Platform detection]( https://cKnowledge.io/?q=module+AND+platform* )
* [Shared experiments]( https://cKnowledge.io/c/module/experiment )
* [Reproduced results from papers]( https://cKnowledge.io/reproduced-results )



## Author

* [Grigori Fursin](https://cKnowledge.io/@gfursin) ([cTuning foundation](https://cTuning.org) and [cKnowledge SAS](https://www.linkedin.com/company/cknowledge))

## Acknowledgments

We would like to thank all [contributors](https://github.com/ctuning/ck/blob/master/CONTRIBUTING.md) 
and [collaborators](https://cKnowledge.org/partners.html) for their support, fruitful discussions, 
and useful feedback!
