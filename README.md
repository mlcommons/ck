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

Collective Knowledge framework (CK) helps to organize any software project
as a database of reusable components with common automation actions
and extensible meta descriptions based on [FAIR principles](https://www.nature.com/articles/sdata201618)
(findability, accessibility, interoperability, and reusability).

The ultimate goal is to help everyone share, reuse, and extend their knowledge
in the form of reusable artifacts and portable workflows with a common API, CLI,
and JSON meta description. 

See how CK helps to support collaborative and reproducible AI, ML, and systems R&D
in some real-world use cases from Arm, General Motors, IBM, MLPerf, the Raspberry Pi foundation, 
and ACM at [cKnowledge.org/partners](https://cKnowledge.org/partners.html).

## News

* **2020 August**: We are very excited to announce that we have completed 
  the prototyping phase of the Collective Knowledge framework (CK)
  and successfully validated it in several [industrial and academic projects](https://cKnowledge.org/partners)
  as briefly described in this [white paper](https://arxiv.org/abs/2006.07161)
  and the [CK presentation](https://cKnowledge.io/presentation/ck).
  We have helped our partners and the community to use CK as a playground to implement reusable 
  [components]( https://cknowledge.io/?q=%22digital-component%22 ) with [automation actions]( https://cKnowledge.io/actions ) 
  for AI, ML, and systems R&D while agreeing on common APIs and JSON meta descriptions. 
  We then used such components to assemble [portable workflows](https://cknowledge.io/programs)
  from [reproduced research papers](https://cknowledge.io/reproduced-papers) during 
  the so-called [artifact evaluation](https://cTuning.org/ae).
  We also  demonstrated that it was possible to use such portable workflows 
  to automate the complex co-design process of efficient software, hardware and models, 
  simplify [MLPerf benchmark](https://mlperf.org) submissions,
  and [quickly deploy]( https://cKnowledge.io/solution )  emerging AI, ML, and IoT technology in production
  in the [most efficient way (speed, accuracy, energy, costs)]( https://cKnowledge.io/results ) 
  across diverse platforms from supercomputers and data centers to mobile phones and edge devices.

  *We are now raising funding for the second phase of this project to standardize CK APIs and meta descriptions, 
  make CK more pythonic and user-friendly, and enhance our [open CK platform](https://cKnowledge.io). 
  Our mission is to organize all AI, ML, and systems knowledge in the form of portable workflows
  with reusable automation actions and artifacts
  to accelerate the development and adoption of innovative technology -
  get in touch with [Grigori Fursin](https://cKnowledge.io/@gfursin) (CK author and project leader) to know more!*

## Documentation

* [News](https://github.com/ctuning/ck/wiki/News-archive)
* [Online CK documentation]( https://ck.readthedocs.io ) 
  * [Why CK?]( https://ck.readthedocs.io/en/latest/src/introduction.html ) 
  * [CK Basics](https://michel-steuwer.github.io/About-CK)
  * [Try CK](https://github.com/ctuning/ck/wiki/First-steps)
  * [CK Wiki]( https://github.com/ctuning/ck/wiki )
* [Open CK portal with all CK components, workflows, and live dashboards](https://cKnowledge.io) 
  * Automation actions and components for [ML&systems R&D]( https://doi.org/10.5281/zenodo.4005773 ):
    * [platform detection]( https://cnowledge.io/?q=module+AND+platform* )
    * [software detection (code, data, models)]( https://cKnowledge.io/soft )
    * [package installation]( https://cKnowledge.io/packages )
    * [portable program workflow]( https://cKnowledge.io/programs )
    * [experiment replay]( https://cKnowledge.io/c/module/experiment )
    * [live scoreboards]( https://cKnowledge.io/reproduced-results )
* [Real-world use-cases](https://cKnowledge.org/partners)
  * [MLPerf CK solution (GUI)](https://cKnowledge.io/test)
  * [MLPerf CK workflows and components (development version)](https://github.com/ctuning/ck-mlperf)
    * [ck-mlperf:soft:lib.mlperf.loadgen.static](https://github.com/ctuning/ck-mlperf/tree/master/soft/lib.mlperf.loadgen.static)
    * [ck-mlperf:package:lib-mlperf-loadgen-static](https://github.com/ctuning/ck-mlperf/tree/master/package/lib-mlperf-loadgen-static)
    * [ck-mlperf:package:model-onnx-mlperf-mobilenet](https://github.com/ctuning/ck-mlperf/tree/master/package/model-onnx-mlperf-mobilenet/.cm)
    * [ck-tensorflow:package:lib-tflite](https://github.com/ctuning/ck-tensorflow/tree/master/package/lib-tflite)
    * [ck-mlperf:program:image-classification-tflite-loadgen](https://github.com/ctuning/ck-mlperf/tree/master/program/image-classification-tflite-loadgen)
    * [ck-tensorflow:program:image-classification-tflite](https://github.com/ctuning/ck-tensorflow/tree/master/program/image-classification-tflite)
    * [ck-mlperf:docker:*](https://github.com/ctuning/ck-mlperf/tree/master/docker)
    * [ck-mlperf:docker:speech-recognition.rnnt](https://github.com/ctuning/ck-mlperf/tree/master/docker/speech-recognition.rnnt)
    * [ck-object-detection:docker:object-detection-tf-py.tensorrt.ubuntu-18.04](https://github.com/ctuning/ck-object-detection/blob/master/docker/object-detection-tf-py.tensorrt.ubuntu-18.04)
    * [ck-object-detection:package:model-tf-*](https://github.com/ctuning/ck-object-detection/tree/master/package)
    * [ck-mlperf:script:mlperf-inference-v0.7.image-classification](https://github.com/ctuning/ck-mlperf/tree/master/script/mlperf-inference-v0.7.image-classification)
    * [ck-object-detection:jnotebook:object-detection](https://nbviewer.jupyter.org/urls/dl.dropbox.com/s/5yqb6fy1nbywi7x/medium-object-detection.20190923.ipynb)
  * [MLPerf stable crowd-benchmarking demo with the live scoreboard](https://cKnowledge.io/test)
  * [CK-based live research paper (collaboration with the Raspberry Pi foundation)](https://cKnowledge.io/report/rpi3-crowd-tuning-2017-interactive).
* [Publications](https://github.com/ctuning/ck/wiki/Publications)

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

## Author

* [Grigori Fursin](https://cKnowledge.io/@gfursin) ([cTuning foundation](https://cTuning.org) and [cKnowledge SAS](https://www.linkedin.com/company/cknowledge))

## Acknowledgments

We would like to thank all [contributors](https://github.com/ctuning/ck/blob/master/CONTRIBUTING.md) 
and [collaborators](https://cKnowledge.org/partners.html) for their support, fruitful discussions, 
and useful feedback!
