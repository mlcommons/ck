# Collective Knowledge SDK

[![Downloads](https://pepy.tech/badge/ck)](https://pepy.tech/project/ck)
[![PyPI version](https://badge.fury.io/py/ck.svg)](https://badge.fury.io/py/ck)
[![Python Version](https://img.shields.io/badge/python-2.7%20|%203.4+-blue.svg)](https://pypi.org/project/ck)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2556147.svg)](https://doi.org/10.5281/zenodo.2556147)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
Coverage: [![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)



## Introduction

Developing complex computational systems for emerging workloads (ML, AI,
Quantum, IoT) and moving them to production is a very tedious, ad-hoc and
time consuming process due to continuously changing software, hardware,
models, data sets and research techniques.

After struggling with these problems for many years, we started the *Collective Knowledge project (CK)*
to decompose complex systems and research projects 
into [reusable, portable, customizable and non-virtualized CK components](https://cKnowledge.io/browse) 
with the unified [automation actions, Python APIs, CLI and JSON meta description](https://cKnowledge.io/actions).

Our idea is to gradually abstract all existing artifacts (software, hardware, models, data sets, results)
and use the DevOps methodology to connect such components together 
into [functional solutions](https://cKnowledge.io/demo)
that can automatically adapt to evolving models, data sets and bare-metal platforms
with the help of [customizable program workflows](https://cKnowledge.io/programs),
a list of [all dependencies](https://cknowledge.io/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows/#dependencies)
(models, data sets, frameworks), and a portable 
[meta package manager](https://cKnowledge.io/packages).

CK is basically our intermediate language to connect researchers and practitioners 
to collaboratively design, benchmark, optimize and validate innovative computational systems.
It then makes it possible to find the most efficient system configurations
on a [Pareto frontier](https://cKnowledge.org/request)
(trading off speed, accuracy, energy, size and different costs)
using an [open repository of knowledge](https://cKnowledge.io)
with [live SOTA scoreboards](https://cKnowledge.io/sota)
and [reproducible papers](https://cKnowledge.io/reproduced-papers).

We hope that such approach will make it possible 
to better understand [what is happening]( https://cknowledge.io/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows/#dependencies ) 
inside complex and "black box" computational systems,
integrate them with production and legacy systems,
use them inside Docker and Kubernetes,
share them along with [published papers](https://cKnowledge.io/events),
and apply the DevOps methodology in deep tech research and computational science.
We also use CK to complement related reproducibility initiatives
including [MLPerf](https://mlperf.org), 
[PapersWithCode](https://paperswithcode.com),
[ACM artifact review and badging](https://www.acm.org/publications/policies/artifact-review-badging)
and [artifact evaluation](https://cTuning.org/ae).

See the [real CK use cases from our partners](https://cKnowledge.org/partners.html)
and try our [MLPerf automation demo](https://cKnowledge.io/demo) on your platform.

You can learn more about our project in the [online documentation](https://cKnowledge.io/docs)
and the following presentations and white papers: 
[2019]( https://doi.org/10.5281/zenodo.2556147 ),
[2018]( https://cknowledge.io/c/report/rpi3-crowd-tuning-2017-interactive ),
[2017]( https://www.slideshare.net/GrigoriFursin/enabling-open-and-reproducible-computer-systems-research-the-good-the-bad-and-the-ugly ),
[2009]( https://hal.inria.fr/inria-00436029v2 ).

*Even though the CK technology is used [in production](https://cKnowledge.org/partners.html) for more than 5 years, it is still a proof-of-concept prototype requiring further improvements and standardization. Depending on the available resources, we plan to develop a new, backward-compatible and more user-friendly version - please [get in touch](https://cKnowledge.org/contacts.html) if you are interested to know more!*


## Open knowledge portal

* [cKnowledge.io](https://cKnowledge.io): the open portal with stable CK components, workflows, reproduced papers, and SOTA scoreboards for complex computational systems (AI,ML,quantum,IoT):
  * [Browse SOTA scoreboards powered by CK workflows](https://cKnowledge.io/reproduced-results)
  * [Browse all shared CK components](https://cKnowledge.io/browse)
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

We would like to thank all [CK users and partners](https://cKnowledge.org/partners.html) 
for fruitful discussions and feedback!


*Copyright 2015-2020 [Grigori Fursin](https://cKnowledge.io/@gfursin) and the [cTuning foundation](https://cTuning.org)*
