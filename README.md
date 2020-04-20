# Collective Knowledge framework (low-level CK SDK)

[![Downloads](https://pepy.tech/badge/ck)](https://pepy.tech/project/ck)
[![PyPI version](https://badge.fury.io/py/ck.svg)](https://badge.fury.io/py/ck)
[![Python Version](https://img.shields.io/badge/python-2.7%20|%203.4+-blue.svg)](https://pypi.org/project/ck)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2556147.svg)](https://doi.org/10.5281/zenodo.2556147)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
Coverage: [![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)



## Introduction

Designing deep tech systems (ML, AI, Quantum, IoT) and moving them to production
is a very tedious process due to continuously changing models, data sets, software and hardware.

The Collective Knowledge project (CK) is our attempt to develop a common SDK
and an [open repository of knowledge]( https://cKnowledge.io ) 
to share [deep tech components]( https://cKnowledge.io/browse ) 
and [R&D automation actions]( https://cKnowledge.io/actions ) 
in a human-readable format 
with a unified CLI, JSON API, and JSON meta descriptions.

Our idea is to abstract and connect different evolving software and hardware
into [portable and non-virtualized (bare-metal) benchmarking "solutions"]( https://cKnowledge.io/solutions )
with [public SOTA scoreboards]( https://cKnowledge.io/results )
to collaboratively benchmark and optimize deep tech systems across diverse hardware,
models and data sets in terms of speed, accuracy, energy and other costs.

We hope that the unified APIs and meta descriptions of such functional CK solutions 
will make it possible to understand [what is happening]( https://cknowledge.io/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows/#dependencies ) 
inside "black box" deep tech systems,
integrate them with production and legacy systems,
use them inside Docker and Kubernetes,
share them along with [published and reproduced papers](https://cKnowledge.io/reproduced-papers)
and bring DevOps principles to deep tech R&D.


We are only at the beginning of this long-term project. Please check our [MLPerf automation demo](https://cKnowledge.io/demo)
and feel free to [get in touch](https://cKnowledge.org/contacts.html) if you have any feedback and suggestions!
Learn more about our project in the [CK documentation](https://cKnowledge.io/docs) 
and the following presentations and white papers: 
[2019]( https://doi.org/10.5281/zenodo.2556147 ),
[2018]( https://cknowledge.io/c/report/rpi3-crowd-tuning-2017-interactive ),
[2017]( https://www.slideshare.net/GrigoriFursin/enabling-open-and-reproducible-computer-systems-research-the-good-the-bad-and-the-ugly ),
[2009]( https://hal.inria.fr/inria-00436029v2 ).


*Note that the CK framework is a low-level and no so user-friendly SDK. That is why we are also developing a more user-friendly wrapper around CK ([cBrain](https://github.com/cknowledge/cbrain)) and a [CK GUI](https://cKnowledge.io/demo).*


## Open knowledge portal

* [cKnowledge.io](https://cKnowledge.io): the open portal with stable CK components, workflows, reproduced papers, and SOTA scoreboards for deep tech systems (AI,ML,quantum,IoT):
  * [Browse SOTA scoreboards powered by CK workflows](https://cKnowledge.io/reproduced-results)
  * [Browse all deep tech CK components](https://cKnowledge.io/browse)
  * [Search for reusable CK components](https://cKnowledge.io)
* [Our reproducibility initiatives for systems and ML conferences](https://cTuning.org/ae)




## CK use cases

* [Real world use cases from our industrial and academic partners](https://cKnowledge.org/partners.html)
* [MLPerf benchmark automation demo with a CK SOTA scoreboard](https://cKnowledge.io/demo)
* [Demo of a CK-based live research paper (collaboration with the Raspberry Pi foundation)](https://cKnowledge.io/report/rpi3-crowd-tuning-2017-interactive).

[<img src="https://img.youtube.com/vi/DIkZxraTmGM/0.jpg" width="320">](https://www.youtube.com/watch?v=DIkZxraTmGM)
[<img src="https://img.youtube.com/vi/VpedDdia5yY/0.jpg" width="320">](https://www.youtube.com/watch?v=VpedDdia5yY)







## Documentation

* [Online CK documentation](https://cKnowledge.io/docs) 

Older wiki-based documentation (we gradually move it to Sphinx-based docs above):

* [CK wiki](https://github.com/ctuning/ck/wiki)
* [CK basics](https://michel.steuwer.info/About-CK)
* [CK Getting Started Guide](https://github.com/ctuning/ck/wiki/First-steps)
* [Contributing to CK](https://github.com/ctuning/ck/wiki/Adding-new-workflows)



## Installation

Follow [this guide](https://cKnowledge.io/docs/getting-started/ck-installation.html) 
to install the CK SDK on your platform.

Check [CK-based demo](https://cKnowledge.io/demo) to participate in reproducible MLPerf benchmarking
with a [public SOTA scoreboard](https://cknowledge.io/c/result/sota-mlperf-object-detection-v0.5-crowd-benchmarking).

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




## Get involved

* This is an ongoing community project and there is a lot to be improved - 
  don't hesitate to [get in touch](https://cKnowledge.org/contacts.html)
  using our slack, mailing list, twitter and email
  if you have any feedback or would like to collaborate.

* Check this [outdated guide](https://github.com/ctuning/ck/wiki) to add your workflows and components. 
  We are gradually rewriting [this guide](https://cKnowledge.io/docs) with our limited resources
  and developing a [CK wrapper (cBrain)](https://github.com/cknowledge/cbrain) to simplify
  the user experience and provide a CK GUI at the [open cKnowledge.io platform](https://cKnowledge.io).



## Acknowledgments

We would like to thank all [CK users](https://cKnowledge.org/partners.html) 
for fruitful discussions and feedback!


*Copyright 2015-2020 [Grigori Fursin](https://cKnowledge.io/@gfursin) and the [cTuning foundation](https://cTuning.org)*
