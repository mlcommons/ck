[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### About

Collective Knowledge (CK) in a community project to develop open-source tools and platforms
that can help researchers and engineers automate their repetitive, tedious and time-consuming tasks
to build, run, benchmark and optimize AI, ML and other applications and systems 
across diverse and continuously changing models, data, software and hardware.

CK consists of several ongoing sub-projects:

* [Collective Mind framework (CM)](cm) - a simple, Python-based, technology-agnostic, non-intrusive and decentralized workflow automation framework.

  * [CM automation recipes for MLOps and DevOps](https://github.com/mlcommons/cm4mlops) - a collection of portable, extensible and technology-agnostic automation recipes
    with a human-friendly interface (aka CM scripts) to unify and automate all the manual steps required to compose, run, benchmark and optimize complex ML/AI applications 
    on diverse platforms with any software and hardware: see [online catalog](https://access.cknowledge.org/playground/?action=scripts) 
    and [source code](https://github.com/mlcommons/cm4mlops/blob/master/script).

  * [CM automation recipes to reproduce research projects](https://github.com/ctuning/cm4research) - a unified CM interface to help researchers
    and engineers access, prepare and run diverse research projects and make it easier to validate them in the real world 
    across rapidly evolving models, data, software and hardware
    (see [our reproducibility initatives](https://cTuning.org/ae) 
    and [motivation](https://www.youtube.com/watch?v=7zpeIVwICa4) behind this project).

  * [Modular C++ harness for MLPerf loadgen](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-mlcommons-cpp)

  * [Modular Python harness for MLPerf loadgen](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-mlcommons-python)

* [Collective Knowledge Playground](https://access.cKnowledge.org) - an open-source platform to list CM scripts similar to PYPI,
  aggregate AI/ML Systems benchmarking results with CM workflows, and organize public optimization challenges to find performance 
  and cost-efficient AI systems.

### License

[Apache 2.0](LICENSE.md)

### Copyright

2022-2024 [MLCommons](https://mlcommons.org)

### Motivation behind CK and CM projects

* ACM REP'23 keynote about MLCommons CM: [ [slides](https://doi.org/10.5281/zenodo.8105339) ] 
* ACM TechTalk'21 about automating research projects: [ [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4) ] [ [slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2021/grigorifursin_techtalk_slides.pdf) ]

### Documentation

**We plan to rewrite and simplify the CM documentation and tutorials based on user feedback in Q2 2024 - please stay tuned for more details**.

* [News](docs/news.md)
* [Getting Started Guide and FAQ](docs/getting-started.md)
  * [Common CM interface to run MLPerf inference benchmarks](docs/mlperf/inference)
  * [Common CM interface to re-run experiments from ML and Systems papers including MICRO'23 and the Student Cluster Competition @ SuperComputing'23](docs/tutorials/common-interface-to-reproduce-research-projects.md)
  * [CM automation recipes for MLOps and DevOps](cm-mlops/script)
  * [Other CM tutorials](docs/tutorials)
* [Full documentation](docs/README.md)
* [CM and CK history](docs/history.md)


### Get in touch

Collective Mind workflow automation framework and Collective Knowledge Playground are being developed 
by the [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
as a community effort. Volunteers are very welcome to help with this community project!

### Acknowledgments

CK and CM are community projects based on the feedback from our users and MLCommons members.
We would like to thank all [collaborators and contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) 
for their support, fruitful discussions, and useful feedback! 
