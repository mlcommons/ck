[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![arXiv](https://img.shields.io/badge/arXiv-2406.16791-b31b1b.svg)](https://arxiv.org/abs/2406.16791)
[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

## Collective Mind (CM)

Collective Mind (CM) is a very lightweight [Python-based framework](https://github.com/mlcommons/ck/tree/master/cm)
featuring a unified CLI, Python API, and minimal dependencies. It is available through [PYPI](https://pypi.org/project/cmind).

CM is designed for creating and managing portable and technology-agnostic automations for MLOps, DevOps and ResearchOps.
It aims to assist researchers and engineers in automating their repetitive, tedious and time-consuming tasks
to build, run, benchmark and optimize various applications 
across diverse and continuously changing models, data, software and hardware.

Collective Mind is a part of [Collective Knowledge (CK)](https://github.com/mlcommons/ck) - 
an educational community project to learn how to run AI, ML and other emerging workloads 
in the most efficient and cost-effective way across diverse 
and ever-evolving systems using the MLPerf benchmarking methodology.

## Collective Mind architecture

The diagram below illustrates the primary classes, functions, and internal automations within the Collective Mind framework:

![](https://github.com/mlcommons/ck/tree/master/docs/specs/cm-diagram-v3.5.1.png)

The CM API documentation is available [here](https://cknowledge.org/docs/cm/api/cmind.html).

## Collective Mind repositories

Collective Mind is continuously enhanced through public and private CM4* Git repositories, 
which serve as the unified interface for various collections of reusable automations and artifacts.

The most notable projects and repositories powered by CM are:

#### CM4MLOps

[CM4MLOPS repository powered by CM](https://github.com/mlcommons/cm4mlops) - 
a collection of portable, extensible and technology-agnostic automation recipes
with a common CLI and Python API (CM scripts) to unify and automate 
all the manual steps required to compose, run, benchmark and optimize complex ML/AI applications 
on diverse platforms with any software and hardware. 

The two key automations are *script" and *cache*:
see [online catalog at CK playground](https://access.cknowledge.org/playground/?action=scripts),
[online MLCommons catalog](https://docs.mlcommons.org/cm4mlops/scripts).

CM scripts extend the concept of `cmake` with simple Python automations, native scripts
and JSON/YAML meta descriptions. They require Python 3.7+ with minimal dependencies and are 
[continuously extended by the community and MLCommons members](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md)
to run natively on Ubuntu, MacOS, Windows, RHEL, Debian, Amazon Linux
and any other operating system, in a cloud or inside automatically generated containers
while keeping backward compatibility.

CM scripts were originally developed based on the following requirements from the
[MLCommons members](https://mlcommons.org) 
to help them automatically compose and optimize complex MLPerf benchmarks, applications and systems
across diverse and continuously changing models, data sets, software and hardware
from Nvidia, Intel, AMD, Google, Qualcomm, Amazon and other vendors:
* must work out of the box with the default options and without the need to edit some paths, environment variables and configuration files;
* must be non-intrusive, easy to debug and must reuse existing 
  user scripts and automation tools (such as cmake, make, ML workflows, 
  python poetry and containers) rather than substituting them; 
* must have a very simple and human-friendly command line with a Python API and minimal dependencies;
* must require minimal or zero learning curve by using plain Python, native scripts, environment variables 
  and simple JSON/YAML descriptions instead of inventing new workflow languages;
* must have the same interface to run all automations natively, in a cloud or inside containers.

See the [online documentation](https://docs.mlcommons.org/inference) 
at MLCommons to run MLPerf inference benchmarks across diverse systems using CM.

#### CM4ABTF

[CM4ABTF repository powered by CM](https://github.com/mlcommons/cm4abtf) - 
a collection of portable automations and CM scripts to run the upcoming 
automotive MLPerf benchmark across different models, data sets, software 
and hardware from different vendors.

#### CM4MLPerf-results

[CM4MLPerf-results powered by CM](https://github.com/mlcommons/cm4mlperf-results) - 
a simplified and unified representation of the past MLPerf results 
in the CM format for further visualization and analysis using [CK graphs](https://access.cknowledge.org/playground/?action=experiments).

#### CM4Research

[CM4Research repository powered by CM](https://github.com/ctuning/cm4research) - 
a unified interface designed to streamline the preparation, execution, and reproduction of experiments in research projects.


### Projects powered by Collective Mind

#### Collective Knowledge Playground

[Collective Knowledge Playground](https://access.cKnowledge.org) - 
a unified and open-source platform designed to [index all CM scripts](https://access.cknowledge.org/playground/?action=scripts) similar to PYPI,
assist users in preparing CM commands to:

* [run MLPerf benchmarks](https://access.cknowledge.org/playground/?action=howtorun)
* aggregate, process, visualize, and compare [benchmarking results](https://access.cknowledge.org/playground/?action=experiments) for AI and ML systems
* organize [open, reproducible optimization challenges and tournaments](https://access.cknowledge.org/playground/?action=challenges). 

These initiatives aim to help academia and industry
collaboratively enhance the efficiency and cost-effectiveness of AI systems.

#### Artifact Evaluation

[Artifact Evaluation automation](https://cTuning.org/ae) - a community-driven initiative 
leveraging the Collective Mind framework to automate artifact evaluation 
and support reproducibility efforts at ML and systems conferences.

CM scripts extend the concept of `cmake` with simple Python automations, native scripts
and JSON/YAML meta descriptions. They require Python 3.7+ with minimal dependencies and are 
[continuously extended by the community and MLCommons members](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md)
to run natively on Ubuntu, MacOS, Windows, RHEL, Debian, Amazon Linux
and any other operating system, in a cloud or inside automatically generated containers
while keeping backward compatibility.

CM scripts were originally developed based on the following requirements from the
[MLCommons members](https://mlcommons.org) 
to help them automatically compose and optimize complex MLPerf benchmarks, applications and systems
across diverse and continuously changing models, data sets, software and hardware
from Nvidia, Intel, AMD, Google, Qualcomm, Amazon and other vendors:
* must work out of the box with the default options and without the need to edit some paths, environment variables and configuration files;
* must be non-intrusive, easy to debug and must reuse existing 
  user scripts and automation tools (such as cmake, make, ML workflows, 
  python poetry and containers) rather than substituting them; 
* must have a very simple and human-friendly command line with a Python API and minimal dependencies;
* must require minimal or zero learning curve by using plain Python, native scripts, environment variables 
  and simple JSON/YAML descriptions instead of inventing new workflow languages;
* must have the same interface to run all automations natively, in a cloud or inside containers.

### Author and maintainer

* [Grigori Fursin](https://cKnowledge.org/gfursin) (FlexAI, cTuning)

### Repositories powered by CM

* [CM4MLOPS / CM4MLPerf](https://github.com/mlcommons/cm4mlops) - 
  a collection of portable, extensible and technology-agnostic automation recipes
  with a common CLI and Python API (CM scripts) to unify and automate 
  all the manual steps required to compose, run, benchmark and optimize complex ML/AI applications 
  on diverse platforms with any software and hardware: see [online catalog at CK playground](https://access.cknowledge.org/playground/?action=scripts),
  [online MLCommons catalog](https://docs.mlcommons.org/cm4mlops/scripts) 

* [CM interface to run MLPerf inference benchmarks](https://docs.mlcommons.org/inference)

* [CM4ABTF](https://github.com/mlcommons/cm4abtf) - a unified CM interface and automation recipes
  to run automotive benchmark across different models, data sets, software and hardware from different vendors.

* [CM4Research](https://github.com/ctuning/cm4research) - a unified CM interface an automation recipes
  to make it easier to reproduce results from published research papers.


### Resources

* CM v2.x (2022-cur) (stable): [installation on Linux, Windows, MacOS](https://access.cknowledge.org/playground/?action=install) ; 
  [docs](https://docs.mlcommons.org/ck) ; [popular commands](https://github.com/mlcommons/ck/tree/master/cm/docs/demos/some-cm-commands.md) ; 
  [getting started guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)
* CM v3.x aka CMX (2024-cur) (stable): [docs](https://github.com/orgs/mlcommons/projects/46)
* MLPerf inference benchmark automated via CM
  * [Run MLPerf for submissions](https://docs.mlcommons.org/inference)
  * [Run MLPerf at the Student Cluster Competition'24](https://docs.mlcommons.org/inference/benchmarks/text_to_image/reproducibility/scc24)
* Examples of modular containers and GitHub actions with CM commands:
  * [GitHub action with CM commands to test MLPerf inference benchmark](https://github.com/mlcommons/inference/blob/master/.github/workflows/test-bert.yml)
  * [Dockerfile to run MLPerf inference benchmark via CM](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference/dockerfiles/bert-99.9/ubuntu_22.04_python_onnxruntime_cpu.Dockerfile)

### License

[Apache 2.0](LICENSE.md)

### Citing Collective Mind

If you found CM automations, please cite this article: 
[ [ArXiv](https://arxiv.org/abs/2406.16791) ], [ [BibTex](https://github.com/mlcommons/ck/blob/master/citation.bib) ].

You can learn more about the motivation behind these projects from the following presentations:

* "Enabling more efficient and cost-effective AI/ML systems with Collective Mind, virtualized MLOps, MLPerf, Collective Knowledge Playground and reproducible optimization tournaments": [ [ArXiv](https://arxiv.org/abs/2406.16791) ]
* ACM REP'23 keynote about the MLCommons CM automation framework: [ [slides](https://doi.org/10.5281/zenodo.8105339) ] 
* ACM TechTalk'21 about Collective Knowledge project: [ [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4) ] [ [slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2021/grigorifursin_techtalk_slides.pdf) ]

### Acknowledgments

Collective Mind (CM) was originally developed by [Grigori Fursin](https://cKnowledge.org/gfursin), 
as a part of the [Collective Knowledge educational initiative](https://cKnowledge.org),
sponsored by [cTuning.org](https://cTuning.org) and [cKnowledge.org](https://cKnowledge.org), 
and contributed to MLCommons for the benefit of all. 

This open-source technology, including CM4MLOps/CM4MLPerf, CM4ABTF, CM4Research, and more, 
is a collaborative project supported by [MLCommons](https://mlcommons.org), 
[FlexAI](https://flex.ai), [cTuning](https://cTuning.org)
and our [amazing volunteers, collaborators, and contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md)! 
