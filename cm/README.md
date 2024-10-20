[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![arXiv](https://img.shields.io/badge/arXiv-2406.16791-b31b1b.svg)](https://arxiv.org/abs/2406.16791)
[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### About

Collective Mind (CM) is a small, modular, cross-platform and decentralized workflow automation framework 
with a human-friendly interface to make it easier to build, run, benchmark and optimize applications 
across diverse models, data sets, software and hardware.

CM is a part of [Collective Knowledge (CK)](https://github.com/mlcommons/ck) - 
an educational community project to learn how to run emerging workloads 
in the most efficient and cost-effective way across diverse 
and continuously changing systems.

CM includes a collection of portable, extensible and technology-agnostic automation recipes
with a common API and CLI (aka CM scripts) to unify and automate different steps 
required to compose, run, benchmark and optimize complex ML/AI applications 
on any platform with any software and hardware. 

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

### Resources

* CM v2.x (stable version 2022-cur): [installation on Linux, Windows, MacOS](https://access.cknowledge.org/playground/?action=install) ; 
  [docs](https://docs.mlcommons.org/ck) ; [popular commands](https://github.com/mlcommons/ck/tree/master/cm/docs/demos/some-cm-commands.md) ; 
  [getting started guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)
* CM v3.x (prototype 2024-cur): [docs](https://github.com/mlcommons/ck/tree/master/cm/docs/cmx)
* MLPerf inference benchmark automated via CM
  * [Run MLPerf for submissions](https://docs.mlcommons.org/inference)
  * [Run MLPerf at the Student Cluster Competition'24](https://docs.mlcommons.org/inference/benchmarks/text_to_image/reproducibility/scc24)
* Examples of modular containers and GitHub actions with CM commands:
  * [GitHub action with CM commands to test MLPerf inference benchmark](https://github.com/mlcommons/inference/blob/master/.github/workflows/test-bert.yml)
  * [Dockerfile to run MLPerf inference benchmark via CM](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference/dockerfiles/bert-99.9/ubuntu_22.04_python_onnxruntime_cpu.Dockerfile)

### License

[Apache 2.0](LICENSE.md)

### Citing CM and CM4MLOps

If you found CM useful, please cite this article: 
[ [ArXiv](https://arxiv.org/abs/2406.16791) ], [ [BibTex](https://github.com/mlcommons/ck/blob/master/citation.bib) ].

You can learn more about the motivation behind these projects from the following articles and presentations:

* "Enabling more efficient and cost-effective AI/ML systems with Collective Mind, virtualized MLOps, MLPerf, Collective Knowledge Playground and reproducible optimization tournaments": [ [ArXiv](https://arxiv.org/abs/2406.16791) ] 
* ACM REP'23 keynote about the MLCommons CM automation framework: [ [slides](https://doi.org/10.5281/zenodo.8105339) ] 
* ACM TechTalk'21 about Collective Knowledge project: [ [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4) ] [ [slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2021/grigorifursin_techtalk_slides.pdf) ]

### Acknowledgments

The Collective Mind framework (CM) was created by [Grigori Fursin](https://cKnowledge.org/gfursin),
sponsored by cKnowledge.org and cTuning.org, and donated to MLCommons to benefit everyone. 
Since then, this open-source technology (CM, CM4MLOps, CM4MLPerf, CM4ABTF, CM4Research, etc)
is being developed as a community effort thanks to all our
[volunteers, collaborators and contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md)! 
