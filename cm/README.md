[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![Downloads](https://pepy.tech/badge/cmind/month)](https://pepy.tech/project/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### About

The [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md), 
[cTuning foundation](https://cTuning.org) and [cKnowledge.org](https://cKnowledge.org) have developed
a non-intrusive, technology-agnostic and plugin-based [Collective Mind automation language (CM)](https://doi.org/10.5281/zenodo.8105339)
to enable collaborative, reproducible, automated and unified benchmarking, optimization and comparison of computer systems
access diverse and rapidly evolving models, data sets, software and hardware from different vendors.

The CM automation language was successfully validated by the community and [cTuning foundation](https://cTuning.org)
via [public optimization and reproducibility challenges at the CK playground](https://access.cknowledge.org/playground/?action=challenges)
to automate > 90% of all [MLPerf inference v3.1 results](https://mlcommons.org/en/news/mlperf-inference-storage-q323/) 
and cross 10000 submissions in one round for the first time - please read this [HPC Wire article](https://www.hpcwire.com/2023/09/13/mlperf-releases-latest-inference-results-and-new-storage-benchmark)
about the cTuning's community submission and check the [list of the new CM/CK capabilities](https://github.com/mlcommons/ck/blob/master/docs/news-mlperf-v3.1.md) 
available to everyone to prepare and automate their future MLPerf submissions.

See related [ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339), 
[ACM Tech Talk](https://learning.acm.org/techtalks/reproducibility) 
and [MLPerf submitters orientation](https://doi.org/10.5281/zenodo.8144274) 
to learn more about our open-source developments and long-term vision.

Join our [Discord server](https://discord.gg/JjWNWXKxwT) to ask questions, provide feedback and participate in collaborative developments.

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

