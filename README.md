[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### Documentation

* [Table of contents](docs/README.md)

### Upcoming events

* [CM automation and CK playground for MLPerf inference v3.1 submissions](docs/news-mlperf-v3.1.md)
* [CK playground for MLPerf at AI hardware summit'23](https://aihwedgesummit.com/events/aihwedgesummit)
* [CM automation for ACM MICRO'23](https://ctuning.org/ae/micro2023.html)
* [Tutorial about CM automation and CK playground for MLPerf at IISCWC'23]( https://iiswc.org/iiswc2023/#/program/ )
* [CM automation and CK playground to run MLPerf at the Student Cluster Competition at SuperComputing'23](https://sc23.supercomputing.org/students/student-cluster-competition)

### About

We deeply believe in the power of open science and open source to solve the world's most challenging problems.

Following our [tedious experience reproducing 150 research papers and validating them in the real world](https://learning.acm.org/techtalks/reproducibility),
we started working with [the community](CONTRIBUTING.md) to develop the [Collective Knowledge Technology](https://arxiv.org/abs/2011.01149)
to access and reuse any shared knowledge (research projects, experiments, AI/ML models, code, data and automation scripts), 
implement portable automation workflows, facilitate reproducible research, and simplify transfer to production across rapidly evolving models, software, hardware and data.

The [cTuning foundation](https://cTuning.org) donated the original Collective Knowledge technology to MLCommons 
to continue developments as a community effort in an [open and transparent way](docs/taskforce.md) 
and deprecated v1 in 2021 and v2 in 2022.

The Collective Knowledge technology v3 consists of the following sub-projects:
* Non-intrusive and technology-agnostic [Collective Mind automation language (CM)](https://doi.org/10.5281/zenodo.8105339) 
  helps to convert any project, code or data into a collection of portable and reusable components with a unified CM interface. 
  CM language allows users to run various automation workflows and applications in the same way either inside automatically generated container snapshots
  or the latest software/hardware stacks (that may fail and then collaboratively improved by the community).
  CM is intended to be always backward compatible and continuously extended by the community via Python automation recipes and JSON/YAML meta descriptions:
  * [Common CM automations](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation) 
  * [Portable and reusable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
* [Collective Knowledge Platform (CK Playground)](https://access.cKnowledge.org) provides a user-friendly GUI 
  to help the community explore, reproduce, understand, optimize and reuse the state-of-the-art AI/ML Systems.
* [Modular Inference library (MIL)](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-cpp/README-extra.md)
  to help new MLPerf submitters add new hardware backends, optimize their MLPerf results using low-level knobs, 
  and reduce their submission costs with the help of the open-source automation for MLPerf benchmarks
  powered by MLCommons CM automation language and CK playground.

The first practical use case for CM language and CK platform is to let everyone participate in collaborative benchmarking,
optimization and validation of the state-of-the-art AI/ML applications across rapidly evolving models, data, software and hardware 
from different vendors - see our [reproducibility and optimization challenges](https://access.cknowledge.org/playground/?action=challenges), 
[shared benchmarking and optimization results for ML Systems (performance, accuracy, power consumption, costs)](https://access.cknowledge.org/playground/?action=experiments) 
and the [leaderboard](https://access.cknowledge.org/playground/?action=contributors).

Read [our documentation](docs/README.md) to learn about how our open-source technology can help you.

Join our [Discord server](https://discord.gg/JjWNWXKxwT) to ask questions, provide feedback and participate in collaborative developments.

### Copyright

2021-2023 [MLCommons](https://mlcommons.org)

### License

[Apache 2.0](LICENSE.md)

### Acknowledgments

This project is supported by [MLCommons](https://mlcommons.org), 
[cKnowledge.org](https://cKnowledge.org),
[cTuning.org](https://cTuning.org),
and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.

### Coordinators

The development of the Collective Knowledge technology is led by [Grigori Fursin](https://cKnowledge.org/gfursin) 
and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) 
