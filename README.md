# Collective Knowledge framework (CK)

[![Downloads](https://pepy.tech/badge/ck)](https://pepy.tech/project/ck)
[![PyPI version](https://badge.fury.io/py/ck.svg)](https://badge.fury.io/py/ck)
[![Python Version](https://img.shields.io/badge/python-2.7%20|%203.4+-blue.svg)](https://pypi.org/project/ck)

Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)

[![DOI](https://zenodo.org/badge/26230485.svg)](https://zenodo.org/badge/latestdoi/26230485)
[![Documentation Status](https://readthedocs.org/projects/ck/badge/?version=latest)](https://ck.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

## License

* **V2+** : Apache 2.0
* **V1.x** : BSD 3-clause

## News

* [Project website](https://cKnowledge.org)
* [CK-powered MLPerf&trade; benchmark automation](https://github.com/ctuning/ck/blob/master/docs/mlperf-automation/README.md)
* [Community projects to improve and redesign CK](https://github.com/ctuning/ck/blob/master/incubator/README.md)

## Overview

Collective Knowledge framework (CK) helps to organize software projects
as a database of reusable components with common automation actions
and extensible meta descriptions based on [FAIR principles](https://www.nature.com/articles/sdata201618)
(findability, accessibility, interoperability and reusability)
as described in our [journal article](https://arxiv.org/pdf/2011.01149.pdf) ([shorter pre-print](https://arxiv.org/abs/2006.07161)).

Our goal is to help researchers and practitioners share, reuse and extend their knowledge
in the form of portable workflows, automation actions and reusable artifacts with a common API, CLI,
and meta description. See how CK helps to automate benchmarking, optimization and design space
exploration of [AI/ML/software/hardware stacks](https://cknowledge.io/result/crowd-benchmarking-mlperf-inference-classification-mobilenets-all/), 
simplifies [MLPerf&trade;](https://mlperf.org) submissions and supports collaborative, reproducible and reusable ML Systems research:

* [ACM TechTalk](https://www.youtube.com/watch?v=7zpeIVwICa4)
* [AI/ML/MLPerf&trade; automation workflows and components from the community](https://github.com/ctuning/ck-ml);
* [Real-world use cases](https://cKnowledge.org/partners.html) from MLPerf&trade;, Arm, General Motors, IBM, the Raspberry Pi foundation, ACM and other great partners;
* [Reddit discussion about reproducing 150 papers](https://www.reddit.com/r/MachineLearning/comments/ioq8do/n_reproducing_150_research_papers_the_problems);
* Our reproducibility initiatives: [methodology](https://cTuning.org/ae), [checklist](https://ctuning.org/ae/submission_extra.html), [events](https://cKnowledge.io/events).

## Documentation

* [Online CK documentation]( https://ck.readthedocs.io ) 
  * [Why CK?]( https://ck.readthedocs.io/en/latest/src/introduction.html ) 
  * [CK Basics](https://michel-steuwer.github.io/About-CK)
  * [Try CK]( https://ck.readthedocs.io/en/latest/src/first-steps.html )
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

## Examples

### Portable CK workflow (native environment without Docker)

Here we show how to pull a GitHub repo in the CK format 
and use a unified CK interface to compile and run 
any program (image corner detection in our case)
with any compatible data set on any compatible platform:

```bash
python3 -m pip install ck

ck pull repo:octoml@mlops

ck ls program:*susan*

ck search dataset --tags=jpeg

ck detect soft --tags=compiler,gcc
ck detect soft --tags=compiler,llvm

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

* [Image classification](https://github.com/ctuning/ck/blob/master/docs/mlperf-automation/tasks/task-image-classification.md)
* [Object detection](https://github.com/ctuning/ck/blob/master/docs/mlperf-automation/tasks/task-object-detection.md)

### Portable CK workflow (with Docker)

We have prepared m CK containers with ML Systems components:
* https://github.com/ctuning/ck-ml/tree/main/docker
* https://github.com/octoml/mlops/tree/main/docker

You can run them as follows:

```bash
ck pull repo:octoml@mlops
ck build docker:ck-template-mlperf-x8664-ubuntu-20.04
ck run docker:ck-template-mlperf-x8664-ubuntu-20.04
```

### Portable workflow example with virtual CK environments

You can create multiple [virtual CK environments](https://github.com/octoml/venv) with templates
to automatically install different CK packages and workflows, for example for MLPerf&trade; inference:

```
ck pull repo:octoml@venv
ck create venv:test --template=mlperf-inference-main
ck ls venv
ck activate venv:test

ck pull repo:octoml@mlops
ck install package --ask --tags=dataset,coco,val,2017,full
ck show env

```

### Integration with web services and CI platforms

All CK modules, automation actions and workflows are accessible as a micro-service with a unified JSON I/O API
to make it easier to integrate them with web services and CI platforms as described 
[here](https://github.com/ctuning/ck/blob/master/docs/mlperf-automation/tools/continuous-integration.md).




### More examples

* See [docs](https://ck.readthedocs.io/en/latest/src/introduction.html#ck-showroom)





## CK portal 

We have developed the [cKnowledge.io portal](https://cKnowledge.io) to help the community
organize and find all the CK workflows and components similar to PyPI:

* [Search CK components](https://cKnowledge.io)
* [Browse CK components](https://cKnowledge.io/browse)
* [Find reproduced results from papers]( https://cKnowledge.io/reproduced-results )
* [Test CK workflows to benchmark and optimize ML Systems]( https://cKnowledge.io/demo )





## Contributions

Users can extend the CK functionality via [CK modules](https://github.com/ctuning/ck/tree/master/ck/repo/module) 
or external [GitHub reposities](https://cKnowledge.io/repos) in the CK format
as described [here](https://ck.readthedocs.io/en/latest/src/typical-usage.html).

Please check [this documentation](https://ck.readthedocs.io/en/latest/src/how-to-contribute.html)
if you want to extend the CK core functionality and [modules](https://github.com/ctuning/ck/tree/master/ck/repo/module). 

Note, that we plan to [redesign the CK core](https://github.com/ctuning/ck/projects/1) 
to be more pythonic (we wrote the first prototype without OO to be able 
to port it to bare-metal devices in C but eventually we decided to drop this idea).


## Author

* [Grigori Fursin](https://cKnowledge.io/@gfursin)

## Sponsors

* [OctoML.ai](https://octoml.ai)
* [cTuning foundation](https://cTuning.org)

## Acknowledgments

We would like to thank all [contributors](https://github.com/ctuning/ck/blob/master/CONTRIBUTING.md) 
and [collaborators](https://cKnowledge.org/partners.html) for their support, fruitful discussions, 
and useful feedback! See more acknowledgments in the [CK journal article](https://arxiv.org/abs/2011.01149).
