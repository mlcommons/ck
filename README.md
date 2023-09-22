[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### Breaking news

Breaking news: our open-source CM automation language and CK playground 
enabled the 1st mass-scale community submission of 10000+ MLPerf
inference benchmarking results (representing more than 90% of all v3.1 submissions)
across diverse models, data sets, software and hardware 
from different vendors via the [cTuning foundation](https://cTuning.org) - 
see the [HPC Wire article](https://www.hpcwire.com/2023/09/13/mlperf-releases-latest-inference-results-and-new-storage-benchmark)
for more details and get in touch via our [public Discord server](https://discord.gg/JjWNWXKxwT) 
if you want to automate and optimize your future MLPerf submissions
using our open-source technology! 


### About

Collective Knowledge (CK) is an open-source, non-intrusive and technology-agnostic toolset
to facilitate reproducible research and automate development, benchmarking, optimization, comparison and 
deployment of Pareto-efficient AI/ML Systems across diverse and rapidly evolving models, data sets, 
software and hardware from different vendors and users.

Collective Knowledge v3 has been developed from scratch by the [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md), 
[cTuning foundation](https://cTuning.org), [cKnowledge.org](https://cKnowledge.org) and [the community](CONTRIBUTING.md) 
and includes the following sub-projects:

* [Collective Mind automation Language (CM)](cm) - a simple automation language
  that helps to implement modular, portable and technology-agnostic 
  benchmarks and applications with a common API that can automatically
  plug in diverse and rapidly evolving models, data sets, software and hardware
  from different vendors and users.
* [CM scripts](cm-mlops/scripts) - a database of portable, reusable and technology-agnostic automations to modularize benchmarks, software projects and AI/ML Systems.
* [Modular Inference Library (MIL)](https://cknowledge.org/mil) - a universal and modular C++ implementation of MLPerf inference benchmarks.
* [Collective Knowledge Playground](https://access.cKnowledge.org) - an open platform to benchmark and optimize AI and ML Systems via community challenges.

See related [ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339), 
[ACM Tech Talk](https://learning.acm.org/techtalks/reproducibility) 
and [MLPerf submitters orientation](https://doi.org/10.5281/zenodo.8144274) 
to learn more about our open-source technology and long-term vision.

Join our [public Discord server](https://discord.gg/JjWNWXKxwT) to learn how to run and extend MLPerf benchmarks, participate in future MLPerf submissions, 
automate reproducibility initiatives at ACM/IEEE/NeurIPS conferences and co-design efficient AI Systems.

### Documentation

* [Table of contents](docs/README.md)

### Upcoming events

* [CM automation language makes it easier to reproduce experiments from the accepted ACM/IEEE MICRO'23 papers](https://github.com/ctuning/cm-reproduce-research-projects/tree/main/script)
* [CK/CM authors will give a tutorial about CM automation language and CK playground at IISWC'23](https://iiswc.org/iiswc2023/#/program/)
* [CM automation language and CK playground will help students run MLPerf inference benchmark at the Student Cluster Competition at SuperComputing'23](https://sc23.supercomputing.org/students/student-cluster-competition)

*More events to come soon!*


### Some practical use cases

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

#### Run MLPerf benchmarks out-of-the-box

* [CM automation for the new MLPerf submitters](https://doi.org/10.5281/zenodo.8144274)
* [MLPerf inference automation](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference)
* [Visualization of MLPerf results](https://access.cknowledge.org/playground/?action=experiments)

#### Participate in reproducible AI/ML Systems optimization challenges

We invite the community to participate in collaborative benchmarking and optimization of AI/ML systems:
* [Community challenges (reproducibility, extension, benchmarking, optimization)](https://access.cknowledge.org/playground/?action=challenges)
* [Shared benchmarking results for AI/ML Systems (performance, accuracy, power consumption, costs)](https://access.cknowledge.org/playground/?action=experiments) 
* [Leaderboard](https://access.cknowledge.org/playground/?action=contributors)

#### Reproduce results from ACM/IEEE/NeurIPS papers

* [CM automation to reproduce results from ACM/IEEE MICRO'23 papers](https://github.com/ctuning/cm-reproduce-research-projects)
* [CM automation to support Student Cluster Competition at SuperComputing'23](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md)
* [CM automation to reproduce IPOL paper](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/reproduce-ipol-paper-2022-439/README-extra.md)



### Project coordinators

* [Grigori Fursin](https://cKnowledge.org/gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)

### Acknowledgments

Collective Knowledge Technology v3 (including Collective Mind automation language and Collective Knowledge Playground)
was developed from scratch by [Grigori Fursin](https://cKnowledge.org/gfursin) 
and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) in 2022-2023
within the [MLCommons Task Force on Automation and Reproducibility](docs/taskforce.md)
and with many great contributions from [the community](CONTRIBUTING.md).

This project is supported by [MLCommons](https://mlcommons.org), 
[cTuning foundation](https://cTuning.org),
[cKnowledge.org](https://cKnowledge.org),
and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.

