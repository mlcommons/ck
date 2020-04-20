# Collective Knowledge framework (low-level CK SDK)

[![Downloads](https://pepy.tech/badge/ck)](https://pepy.tech/project/ck)
[![PyPI version](https://badge.fury.io/py/ck.svg)](https://badge.fury.io/py/ck)
[![Python Version](https://img.shields.io/badge/python-2.7%20|%203.4+-blue.svg)](https://pypi.org/project/ck)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2556147.svg)](https://doi.org/10.5281/zenodo.2556147)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
Coverage: [![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

[<img src="https://img.youtube.com/vi/DIkZxraTmGM/0.jpg" width="320">](https://www.youtube.com/watch?v=DIkZxraTmGM)
[<img src="https://img.youtube.com/vi/VpedDdia5yY/0.jpg" width="320">](https://www.youtube.com/watch?v=VpedDdia5yY)

## Introduction

We have developed the Collective Knowledge framework (CK) to help researchers 
share their projects and artifacts (code, data, models, scripts, experiments, papers)
in a common format as a human-readable database with a standardized API, CLI and JSON input/output/meta descriptions.

CK is a small, cross-platform, CLI-based and community-driven Python framework 
to add, share and reuse [automation actions](https://cKnowledge.io/actions) 
for repetitive, tedious, and time-consuming R&D tasks in a non-intrusive way
along with existing research projects.


CK also helps to convert all ad-hoc artfiacts into standardized and reusable CK components 
with a common API and JSON meta description.
For example, CK features 
[software detection plugins](https://cKnowledge.io/soft) (CK "soft" component), 
[meta packages](https://cKnowledge.io/packages) (CK "package" component) 
and [OS descriptions](https://cKnowledge.io/c/os)
to automate the detection and installation of all the dependencies 
required by a given research project to run on any target platform.

Such CK actions and components can be connected into platform-agnostic, 
portable, customizable, reusable and reproducible [workflows](https://cKnowledge.io/programs) 
(CK "program" component) that can be easily integrated with Continuous Integration tools, 
existing/legacy projects, and production systems.

The stable components are published at the [open Collective Knowledge platform](https://cKnowledge.io)
similar to PyPI along with auto-generated "live" papers and portable workflows 
to help the community participate in [collaborative validation of research results](https://cKnowledge.io/results) 
across diverse hardware, datasets and models similar to SETI@home.

Our long-term goal is to enable collaborative, reproducible, sustainable and production-ready research 
based on DevOps principles.

Learn more about our long-term vision in the following white papers and presentations: 
[MLOps@MLSys'20]( https://arxiv.org/abs/2001.07935 ),
[FOSDEM'19](https://doi.org/10.5281/zenodo.2556147),
[CNRS'17](https://www.slideshare.net/GrigoriFursin/enabling-open-and-reproducible-computer-systems-research-the-good-the-bad-and-the-ugly),
[DATE'16](https://www.researchgate.net/publication/304010295_Collective_Knowledge_Towards_RD_Sustainability),
[CTI'09](https://hal.inria.fr/inria-00436029v2).

## Important features

* CK actions can be shared and reused across research projects:
  see the [list of available actions and modules](https://cKnowledge.io/modules).

* Standardized CK APIs and meta-descriptions help  users 
  to easily connect actions into automated, portable and customizable workflows, 
  and quickly integrate them with practically all major tools, frameworks and Continuous Integration Services: 
  see the [list of shared repositories with CK workflows and actions](https://cKnowledge.io/repos).

* CK helps to automate [Artifact Evaluation](https://cTuning.org/ae), 
  perform [reproducible experiments](https://cKnowledge.io/results) 
  and generate papers with reusable research components:
  see [the list of articles with CK workflows](https://cKnowledge.io/?q=%22reproduced-papers%22) 
  and the [CK-based interactive report with the Raspberry Pi foundation](https://cKnowledge.io/report/rpi3-crowd-tuning-2017-interactive).

* CK is used in reproducible optimization competitions to co-design efficient software and hardware
  for emerging AI, ML and quantum computing workloads in terms of speed, accuracy, energy, and costs: 
  see the [live CK dashboard with results from different Hackathons, tournaments and crowd-tuning campaigns](https://cKnowledge.io/results).



## CK-based projects

* [CK portal to exchange CK components and participate in crowd-benchmarking](https://cKnowledge.io).
* Research projects in the CK format from [our partners](https://cKnowledge.org/partners.html).
* [MLOps platform and reproducible benchmarking](https://arxiv.org/abs/2001.07935)
* [Reproduced papers from ML and systems conferences](https://cKnowledge.io/?q=%22reproduced-papers%22%20AND%20%22portable-workflow-ck%22) shared with CK benchmarking pipelines
* [MLPerf benchmark automation demo](https://cKnowledge.io/demo).
* [GitHub repositories in the CK format](https://cKnowledge.io/repos).
* [R&D automation actions](https://cKnowledge.io/actions).
* [Software detection plugins](https://cKnowledge.io/soft).
* [Meta-packages](https://cKnowledge.io/packages).
* [Artifact abstractions (CK Python modules with a unified API and JSON IO)](https://cKnowledge.io/modules).




## Documentation

*We plan a major revision of the CK documentation in 2020 based on user-feedback*

* [CK wiki](https://github.com/ctuning/ck/wiki) - we plan to rewrite it in the Sphinx format 
* [CK basics](https://michel.steuwer.info/About-CK)
* [CK Getting Started Guide](https://github.com/ctuning/ck/wiki/First-steps)





## Installation

CK supports the following platforms:

|               | As a host platform | As a target platform |
|---------------|:------------------:|:--------------------:|
| Generic Linux | ✓ | ✓ |
| Linux (Arm)   | ✓ | ✓ |
| Raspberry Pi  | ✓ | ✓ |
| MacOS         | ✓ | ✓ |
| Windows       | ✓ | ✓ |
| Android       | partially | ✓ |
| iOS           | TBD | TBD |

Please follow [this guide](https://cKnowledge.io/docs/getting-started/ck-installation.html) 
to install CK SDK on your platform.





## Next steps

Based on user feedback we plan the following activities:

* Standardization of CK actions, APIs and meta descriptions
* Better documentation
* GUI to create, test and interconnect CK actions
* GUI to assemble portable workflows
* GUI to automate [MLPerf](https://mlperf.org) submissions


<img src="https://cTuning.org/_resources/ctuning-activities-resize.png" width="687">




## Get involved

Please follow this [guide](https://github.com/ctuning/ck/wiki) to add your workflows and components. Note that we plan to rewrite it and add tutorials as soon as we have more resources!

Provide your suggestions using our [public mailing list](https://groups.google.com/forum/#!forum/collective-knowledge) 
and the [Slack channel](https://cKnowledge.org/join-slack)!

Help the community to improve the existing CK components (actions, modules, packages, software plugins, workflows),
when they fail on new platforms or miss some functionality, share the new ones and fix buges - you can provide 
your feedback and report bugs in the respective [CK development repositories](https://cKnowledge.io/repos) 
or using [the Collective Knowledge platform](https://cKnowledge.io/browse)!

Consider sponsoring the [cTuning foundation](https://cTuning.org) to support our community activities.

Contact [Grigori Fursin](https://fursin.net) (the CK author) about our long-term vision and development plans.
