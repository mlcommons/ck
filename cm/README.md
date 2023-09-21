[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![Downloads](https://pepy.tech/badge/cmind/month)](https://pepy.tech/project/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### Breaking news

Breaking news: our open-source CM automation language and CK playground 
enabled the 1st mass-scale community submission of 10000+ MLPerf
inference benchmarking results (representing more than 90% of all v3.1 submissions)
across diverse models, data sets, software and hardware 
from different vendors via the cTuning foundation - see the [HPC Wire article](https://www.hpcwire.com/2023/09/13/mlperf-releases-latest-inference-results-and-new-storage-benchmark)
for more details and get in touch via our [public Discord server](https://discord.gg/JjWNWXKxwT) 
if you want to automate and optimize your future MLPerf submissions
using our open-source technology! 


### About

Collective Mind automation Language (CM) is a simple automation language that helps to implement modular, portable and technology-agnostic 
benchmarks and applications with a common API that can automatically plug in diverse and rapidly evolving models, data sets, software and hardware
from different vendors and users.
It is extended via [CM scripts](cm-mlops/scripts) - a database of portable, reusable and technology-agnostic automations 
to modularize benchmarks, software projects and AI/ML Systems.

CM is used by the community to provide a common interface to all shared knowledge, facilitate reproducible research and automate development, benchmarking, optimization, comparison and deployment of AI/ML Systems.
See [ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339) 
and [MLPerf submitters orientation](https://doi.org/10.5281/zenodo.8144274) 
to learn more about our open-source technology and long-term vision.

Join our [public Discord server](https://discord.gg/JjWNWXKxwT) to learn how to use CM, 
modularize your projects and benchmarks, run and extend MLPerf benchmarks, participate in future MLPerf submissions, 
automate reproducibility initiatives at ACM/IEEE/NeurIPS conferences and co-design efficient AI/ML Systems.

### Documentation

* [Table of contents](https://github.com/mlcommons/ck/blob/master/docs/README.md)

### Some practical use cases

* [CM installation](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [All CM tutorials](https://github.com/mlcommons/ck/blob/master/docs/tutorials)

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

### Copyright

2021-2023 [MLCommons](https://mlcommons.org)

### License

[Apache 2.0](LICENSE.md)

### Acknowledgments

Collective Mind automation language was developed from scratch by [Grigori Fursin](https://cKnowledge.org/gfursin) 
and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) in 2022-2023
within the [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
and with many great contributions from [the community](https://github.com/mlcommons/ck/blob/master/cm/CONTRIBUTING.md).

This project is supported by [MLCommons](https://mlcommons.org), 
[cTuning foundation](https://cTuning.org),
[cKnowledge.org](https://cKnowledge.org),
and [individual contributors](https://github.com/mlcommons/ck/blob/master/cm/CONTRIBUTING.md).
We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.

