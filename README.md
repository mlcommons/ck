[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)

### About

MLCommons' [Collective Knowledge (CK)](https://www.youtube.com/watch?v=7zpeIVwICa4) is an open-source community project 
intended to make AI accessible to everyone by harnessing the growing complexity and cost of development, benchmarking, optimization, deployment, and maintenance of
AI/ML applications and systems across diverse and rapidly evolving models, datasets, software and hardware from the cloud to the edge.

This project is being developed, supported and maintained by the [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md), 
[cTuning foundation](https://cTuning.org), [cKnowledge.org](https://cKnowledge.org) and [individual contributors](CONTRIBUTING.md).
It includes the following sub-projects:

* [Collective Mind scripting language (CM)](cm) - a light-weight and non-intrusive workflow automation meta-framework 
  that helps users decompose complex software projects into simple, portable, reusable and extensible automation recipes (CM scripts). 
  These scripts are connected into portable and technology-agnostic workflows that can run a given application 
  on any platform with any software and hardware in an automated and unified way using a common and human-readable interface.
  The goal is to help researchers and developers focus on innovation while automating all their tedious, repetitive and manual tasks 
  when preparing, bechmarking, reproducing, optimizing and porting AI, ML and other complex projects to continuously evolving models, datasets, software and hardware.
  *CM is complementary to existing automation tools including Docker, Kubeflow, MLFlow, cmake, spack, etc.*
* [CM scripts](cm-mlops/scripts) - a collection of portable, reusable, customizable and  technology-agnostic automations
  that wrap existing MLOps, DevOps, ResearchOps and LLMOps with a human-readable command line, simple Python API and extensible JSON/YAML meta descriptions 
  to make them run in a more unified and deterministic way on any Operating System (Windows, Ubuntu, MacOS, RedHat ...) with any software and hardware.
  CM scripts should work in the same way in a native environment or inside containers.

* [CM automation for Artifact Evaluation and reproducibility initiatives at ML and Systems conferences](https://github.com/ctuning/cm-reproduce-research-projects) - 
  a common CM interface to help the community prepare, run and reproduce experiments 
  from research projects and reuse their automations and artifacts in a simple and unified way.
* [Modular Inference Library (MIL)](https://cknowledge.org/mil) - a universal, modular and extensible C++ implementation of MLPerf inference benchmarks.
* [Collective Knowledge Playground](https://access.cKnowledge.org) - an open platform to benchmark, optimize and compare AI and ML Systems using CM.

Join our [public Discord server](https://discord.gg/JjWNWXKxwT) to learn how this technology can help you how to run and extend MLPerf benchmarks, participate in future MLPerf submissions, 
automate reproducibility initiatives at ACM/IEEE/NeurIPS conferences and co-design efficient AI Systems.



### Documentation

* [Table of Contents](docs/README.md)

### Motivation

* [CK vision (ACM Tech Talk at YouTube)](https://www.youtube.com/watch?v=7zpeIVwICa4) 
* [CK concepts (Philosophical Transactions of the Royal Society)](https://arxiv.org/abs/2011.01149) 
* [CM workflow automation introduction (slides from ACM REP'23 keynote)](https://doi.org/10.5281/zenodo.8105339)
* [MLPerf inference submitter orientation (slides)](https://doi.org/10.5281/zenodo.8144274) 

### Tests

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)
[![Dockerfile update for CM scripts](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml)

[![MLPerf inference resnet50](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-resnet50.yml/badge.svg?branch=master&event=pull_request)](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-resnet50.yml)
[![MLPerf inference retinanet](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-retinanet.yml/badge.svg?branch=master&event=pull_request)](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-retinanet.yml)
[![MLPerf inference bert](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-bert.yml/badge.svg?event=pull_request)](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-bert.yml)
[![MLPerf inference rnnt](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-rnnt.yml/badge.svg?event=pull_request)](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-rnnt.yml)



### Getting Started

* [CM installation](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [All CM tutorials](https://github.com/mlcommons/ck/blob/master/docs/tutorials)

#### Run Python Hello World app on Linux, Windows and MacOS

```bash
python3 -m pip install cmind
# restart bash to add cm and cmr binaries to PATH

cm pull repo mlcommons@ck
cm run script --tags=print,python,hello-world
cmr "print python hello-world"
```

This CM script is a simple wrapper to native scripts and tools
described by a simple declarative YAML configuration file
specifying inputs, environment variables and dependencies on other portable
and shared [CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script):

```yaml
alias: print-hello-world-py
uid: d83274c7eb754d90

automation_alias: script
automation_uid: 5b4e0237da074764

deps:
- tags: detect,os
- tags: get,sys-utils-cm
- names:
  - python
  tags: get,python3

tags:
- print
- hello-world
- python

```

Our goal is to let the community start using CM within minutes!

### Projects supported by CM

#### Running MLPerf benchmarks out-of-the-box

* [CM interface to run MLPerf inference benchmarks](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference)
* [CK playground to aggregate, visualize and compare MLPerf results](https://access.cknowledge.org/playground/?action=experiments)

#### Supporting reproducible AI/ML Systems optimization challenges

We invite the community to participate in collaborative benchmarking and optimization of AI/ML systems:
* [Community challenges (reproducibility, extension, benchmarking, optimization)](https://access.cknowledge.org/playground/?action=challenges)
* [Shared benchmarking results for AI/ML Systems (performance, accuracy, power consumption, costs)](https://access.cknowledge.org/playground/?action=experiments) 
* [Leaderboard](https://access.cknowledge.org/playground/?action=contributors)

#### Making it easier to reproducing research results from ACM/IEEE/NeurIPS papers

* [CM automation to reproduce results from ACM/IEEE MICRO'23 papers](https://github.com/ctuning/cm-reproduce-research-projects)
* [CM automation to support Student Cluster Competition at SuperComputing'23](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md)
* [CM automation to reproduce IPOL paper](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/reproduce-ipol-paper-2022-439/README-extra.md)



### Authors and project coordinators

* [Grigori Fursin](https://cKnowledge.org/gfursin) (MLCommons.org, cTuning.org, cKnowledge.org)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) (MLCommons.org, cTuning.org, cKnowledge.org)




### Acknowledgments

The Collective Knowledge Technology v1 and v2 [was originally developed](https://arxiv.org/abs/2011.01149) 
by [Grigori Fursin](https://cKnowledge.org/gfursin) and the [cTuning foundation](https://cTuning.org)
with generous sponsorship from [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai)
and donated to MLCommons in 2022. 

The Collective Knowledge Technology v3 including the new [Collective Mind workflow automation language (MLCommons CM)](https://doi.org/10.5281/zenodo.8105339)
and [Collective Knowledge Playground](https://access.cKnowledge.org)
was developed by the [MLCommons Task Force on Automation and Reproducibility](docs/taskforce.md)
led by [Grigori Fursin](https://cKnowledge.org/gfursin) and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) 
with many great contributions from [the community](CONTRIBUTING.md).

This community project is now officially supported and maintained by [MLCommons.org](https://mlcommons.org), 
[cTuning.org](https://cTuning.org) and [cKnowledge.org](https://cKnowledge.org).
