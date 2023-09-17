[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)


### Breaking news

*We are proud that our open-source MLCommons CM automation language and CK playground helped the community 
automate > 90% of all [MLPerf inference v3.1 results](https://www.hpcwire.com/2023/09/13/mlperf-releases-latest-inference-results-and-new-storage-benchmark) 
and cross 10000 submissions in one round for the first time (submitted via [cTuning foundation](https://cTuning.org))!
Here is the [list of the new CM/CK capabilities](docs/news-mlperf-v3.1.md) available to everyone 
to prepare and automate their future MLPerf submissions - don't hesitate to reach us 
via [Discord server](https://discord.gg/JjWNWXKxwT) for more info!*

### Documentation

* [Table of contents](docs/README.md)

### Upcoming events

* [CM automation language makes it easier to reproduce experiments from the accepted ACM/IEEE MICRO'23 papers](https://github.com/ctuning/cm-reproduce-research-projects/tree/main/script)
* [CK/CM authors will give a tutorial about CM automation language and CK playground at IISWC'23](https://iiswc.org/iiswc2023/#/program/)
* [CM automation language and CK playground will help students run MLPerf inference benchmark at the Student Cluster Competition at SuperComputing'23](https://sc23.supercomputing.org/students/student-cluster-competition)

*More events to come soon!*

### About

The [MLCommons Task Force on Automation and Reproducibility](docs/taskforce.md) has developed
a common, non-intrusive and technology-agnostic automation language (Collective Mind aka CM) 
to access, run and reuse any benchmark, research project, 
tool, ad-hoc script, data and model in a unified way on any hardware with any software.

The goal is to help the community make it easier to reproduce research projects, 
automate benchmarking and optimization of AI/ML systems,
and simplify transfer of research ideas to production across rapidly evolving software, hardware and data.

CM is being extended by the community and MLCommons via [public optimization and reproducibility challenges at the CK playground](https://access.cknowledge.org/playground/?action=challenges)
and used for [automated, collaborative and reproducible MLPerf benchmarking](docs/news-mlperf-v3.1.md) 
of diverse software/hardware stacks from different vendors at massive scale (thousands of submissions per round).

See the [ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339) and [MLPerf submitters orientation](https://doi.org/10.5281/zenodo.8144274)
for more details.

Join our [Discord server](https://discord.gg/JjWNWXKxwT) to ask questions, provide feedback and participate in collaborative developments.

### Docs

* [Table of contents](docs/README.md) 

### Some practical use cases

* [CM installation](docs/installation.md)
* [All CM tutorials](docs/tutorials)

#### Run Python Hello World app

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
* [MLPerf inference automation](docs/mlperf/inference)
* [Visualization of MLPerf results](https://access.cknowledge.org/playground/?action=experiments)

#### Participate in reproducible AI/ML Systems optimization challenges

We invite the community to participate in collaborative benchmarking and optimization of AI/ML systems:
* [Community challenges (reproducibility, extension, benchmarking, optimization)](https://access.cknowledge.org/playground/?action=challenges)
* [Shared benchmarking results for AI/ML Systems (performance, accuracy, power consumption, costs)](https://access.cknowledge.org/playground/?action=experiments) 
* [Leaderboard](https://access.cknowledge.org/playground/?action=contributors)

### Project coordinators

* [Grigori Fursin](https://cKnowledge.org/gfursin) ([cTuning foundation](https://cTuning.org) and [cKnowledge.org](https://cKnowledge.org))
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) ([cTuning foundation](https://cTuning.org) and [cKnowledge.org](https://cKnowledge.org))

### Acknowledgments

Collective Knowledge Technology v3 (including Collective Mind automation language and Collective Knowledge playground)
was developed from scratch by [Grigori Fursin](https://cKnowledge.org/gfursin) 
and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) in 2022-2023
within the [MLCommons Task Force on Automation and Reproducibility](docs/taskforce.md)
and with many great contributions from [the community](CONTRIBUTING.md).

This project is supported by [MLCommons](https://mlcommons.org), 
[cTuning foundation](https://cTuning.org),
[cKnowledge.org](https://cKnowledge.org),
and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.

