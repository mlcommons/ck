# Collective Knowledge framework (CK)

[![Downloads](https://pepy.tech/badge/ck)](https://pepy.tech/project/ck)
[![PyPI version](https://badge.fury.io/py/ck.svg)](https://badge.fury.io/py/ck)
[![Python Version](https://img.shields.io/badge/python-2.7%20|%203.4+-blue.svg)](https://pypi.org/project/ck)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)

[![Documentation Status](https://readthedocs.org/projects/ck/badge/?version=latest)](https://ck.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

## News

* We are very excited to join forces with [OctoML.ai](https://OctoML.ai)! Contact [Grigori Fursin](https://cKnowledge.io/@gfursin) for more details!
* See our [ACM TechTalk](https://learning.acm.org/techtalks/reproducibility) about the CK technology, reproducible research, FAIR principles and MLPerf (February 2021).
* The overview of the CK technology has appeared in the Philosophical Transactions A, the world's longest-running journal where Newton published: <a href="https://doi.org/10.1098/rsta.2020.0211">DOI</a>, <a href="https://arxiv.org/pdf/2011.01149.pdf">ArXiv</a>.
* We are preparing a major redesign of the CK framework to make it more Pythonic and easier to use (CK2) - feel free to contact [Grigori Fursin]( https://cKnowledge.io/@gfursin ) for more details 
  and [subscribe](https://cKnowledge.io/register) for our newsletter!
* We have finished prototyping the [CK concept](https://arxiv.org/pdf/2011.01149.pdf)
  and successfully used it to automate  [MLPerf inference benchmark submissions for edge devices](https://cKnowledge.io/solutions)
  and the design space exploration of [efficient ML/SW/HW stacks](https://cknowledge.io/c/result/crowd-benchmarking-mlperf-inference-classification-mobilenets-all)
  in terms of speed, accuracy, energy and costs.

## Overview

Collective Knowledge framework (CK) helps to organize software projects
as a database of reusable components with common automation actions
and extensible meta descriptions based on [FAIR principles](https://www.nature.com/articles/sdata201618)
(findability, accessibility, interoperability and reusability)
as described in [this article](https://arxiv.org/pdf/2011.01149.pdf).

Our goal is to help researchers and practitioners share, reuse and extend their knowledge
in the form of portable workflows, automation actions and reusable artifacts with a common API, CLI,
and meta description. See how CK supports collaborative and reproducible research:
* [MLPerf automation workflows](https://cKnowledge.io/solutions) ([GitHub](https://github.com/ctuning/ai));
* [Real-world use cases](https://cKnowledge.org/partners.html) from MLPerf, Arm, General Motors, IBM, the Raspberry Pi foundation, ACM, dividiti and other great partners;
* [Reddit discussion about reproducing 150 papers](https://www.reddit.com/r/MachineLearning/comments/ioq8do/n_reproducing_150_research_papers_the_problems);
* Our reproducibility initiatives: [methodology](https://cTuning.org/ae), [checklist](https://ctuning.org/ae/submission_extra.html), [events](https://cKnowledge.io/events).

## Documentation

* [Online CK documentation]( https://ck.readthedocs.io ) 
  * [Why CK?]( https://ck.readthedocs.io/en/latest/src/introduction.html ) 
  * [CK Basics](https://michel-steuwer.github.io/About-CK)
  * [Try CK]( https://ck.readthedocs.io/en/latest/src/first-steps.html )
* [Publications](https://github.com/ctuning/ck/wiki/Publications)
* [All news](https://github.com/ctuning/ck/wiki/News-archive)

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

## Example (without Docker)

Here we show how to pull a GitHub repo in the CK format 
and use a unified CK interface to compile and run 
any program (image corner detection in our case)
with any compatible data set on any compatible platform:

```bash
python3 -m pip install ck

ck pull repo --url=https://github.com/ctuning/ck-crowdtuning

ck ls program:*susan*

ck search dataset --tags=jpeg

ck detect soft --tags=compiler,gcc
ck detect soft --tags=compiler,llvm

ck show env --tags=compiler

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

## Example (with Docker)

We have prepared a CK container with [AI and ML components](https://github.com/ctuning/ai): 
[[Docker](https://hub.docker.com/r/ctuning/ck-ai)], [[CK meta](https://github.com/ctuning/ai/tree/main/docker/ck-ai)]

You can start it as follows:

```bash
docker run --rm -it ctuning/ck-ai:ubuntu-20.04
```

You can then prepare and run [portable AI/ML workflows](https://cKnowledge.io/solutions) 
and [program pipelines](https://cKnowledge.io/programs).


## More examples of CK workflows, automation actions and reusable artifacts for

* Showroom (public projects powered by CK):
  * [MLPerf automation](https://cKnowledge.io/solution)
  * Student Cluster Competition automation: [SCC18](https://github.com/ctuning/ck-scc18), [digital artifacts](https://github.com/ctuning/ck-scc)
  * Jupyter notebooks: [ML/SW/HW DSE for edge devices](https://nbviewer.jupyter.org/urls/dl.dropbox.com/s/f28u9epifr0nn09/ck-dse-demo-object-detection.ipynb)
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
  * [GUI to automate ML/SW/HW benchmarking with MLPerf example (under development)](https://cKnowledge.io/test)
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



## CK portal 

[cKnowledge.io](https://cKnowledge.io): organizing [ML and Systems knowledge]( https://doi.org/10.5281/zenodo.4005773 )
in the form of portable CK workflows, automation actions and reusable components:

* [**All CK ML&systems components**](https://cknowledge.io/?q=mlsystems)
* [CK compatible repositories]( https://cknowledge.io/repos )
* [CK portable solutions (including MLPerf inference on edge)]( https://cKnowledge.io/solution )
* [CK-based adaptive containers]( https://cKnowledge.io/c/module/docker )
* [CK modules]( https://cKnowledge.io/modules )
* [Automation actions]( https://cKnowledge.io/actions )
* [Portable program workflows]( https://cKnowledge.io/programs )
* [Meta packages]( https://cKnowledge.io/packages )
* [Software detection (code, data, models)]( https://cKnowledge.io/soft )
* [Platform detection]( https://cKnowledge.io/?q=module+AND+platform* )
* [Shared experiments]( https://cKnowledge.io/c/module/experiment )
* [Reproduced results from papers]( https://cKnowledge.io/reproduced-results )



## Contributions

Users can extend the CK functionality via [CK modules](https://github.com/ctuning/ck/tree/master/ck/repo/module) 
or external [GitHub reposities](https://cKnowledge.io/repos) in the CK format
as described [here](https://ck.readthedocs.io/en/latest/src/typical-usage.html).

Please check [this documentation](https://ck.readthedocs.io/en/latest/src/how-to-contribute.html)
if you want to extend the CK core functionality and [modules](https://github.com/ctuning/ck/tree/master/ck/repo/module). 

Note, that we plan to [redesign the CK core](https://github.com/ctuning/ck/projects/1) 
to be more pythonic (we wrote the first prototype without OO to be able 
to port to bare-metal devices in C but we decided not to do it at the end).
We also plan to relicense the framework to Apache 2.0.


## Author

* [Grigori Fursin](https://cKnowledge.io/@gfursin) ([cTuning foundation](https://cTuning.org) and [cKnowledge SAS](https://www.linkedin.com/company/cknowledge))



## Acknowledgments

We would like to thank all [contributors](https://github.com/ctuning/ck/blob/master/CONTRIBUTING.md) 
and [collaborators](https://cKnowledge.org/partners.html) for their support, fruitful discussions, 
and useful feedback! See more acknowledgments in the [CK journal article](https://arxiv.org/abs/2011.01149).
