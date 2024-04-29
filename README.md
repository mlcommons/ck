[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### About

Collective Knowledge (CK) in a community project to develop open-source tools, platforms and automation recipes 
that can help researchers and engineers automate their repetitive, tedious and time-consuming tasks
to build, run, benchmark and optimize AI, ML and other applications and systems 
across diverse and continuously changing models, data, software and hardware.

CK consists of several ongoing sub-projects:

* [Collective Mind framework (CM)](cm) (*~1MB*) - a very light-weight Python-based framework with minimal dependencies
  to help users implement, share and reuse cross-platform automation recipes to 
  build, benchmark and optimize applications on any platform
  with any software and hardware. CM attempts to extends the `cmake` concept 
  with reusable automation recipes and workflows written in plain Python or native OS scripts,
  accessible via a human readable interface with simple tags,
  and shareable in public and private repositories in a decentralized way.
  Furthermore, in comparison with cmake, these automation recipes can not only detect missing code 
  but also download artifacts (models, data sets), preprocess them, build missing 
  dependencies, install them and run the final code on diverse platforms in a unified and automated way.
  You can read more about the CM concept in this [presentation](https://doi.org/10.5281/zenodo.8105339).


  * [CM automation recipes for MLOps and DevOps](cm-mlops) (*~6MB*) - a small collection of portable, extensible and technology-agnostic automation recipes
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
  aggregate AI/ML Systems benchmarking results with CM workflows, and organize 
  [public optimization challenges and reproducibility initiatives](https://access.cknowledge.org/playground/?action=challenges) 
  to find the most performance and cost-effective AI/ML Systems.

  * [CK GUI to run modular benchmarks](https://access.cknowledge.org/playground/?action=howtorun) - such benchmarks 
    are composed from [CM scripts](https://access.cknowledge.org/playground/?action=scripts)
    and can run via a unified CM interface.

### License

[Apache 2.0](LICENSE.md)

### Copyright

2022-2024 [MLCommons](https://mlcommons.org)

### Motivation behind CK and CM projects

* ACM REP'23 keynote about the MLCommons CM automation framework: [ [slides](https://doi.org/10.5281/zenodo.8105339) ] 
* ACM TechTalk'21 about automating research projects: [ [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4) ] [ [slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2021/grigorifursin_techtalk_slides.pdf) ]

### Documentation

**We plan to rewrite and simplify the CM documentation and tutorials based on user feedback in Q2 2024 - please stay tuned for more details**.

* [CM Getting Started Guide and FAQ](docs/getting-started.md)
  * [Common CM interface to run MLPerf inference benchmarks](docs/mlperf/inference)
  * [Common CM interface to re-run experiments from ML and Systems papers including MICRO'23 and the Student Cluster Competition @ SuperComputing'23](docs/tutorials/common-interface-to-reproduce-research-projects.md)
  * [CM automation recipes for MLOps and DevOps](cm-mlops/script)
  * [Other CM tutorials](docs/tutorials)
* [Full documentation](docs/README.md)
* [CM development tasks](docs/taskforce.md#current-tasks)
* [CM and CK history](docs/history.md)



### Acknowledgments

This open-source technology is being developed by the [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
as a community effort based on user feedback. 
We would like to thank all our [volunteers, collaborators and contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) 
for their support, fruitful discussions, and useful feedback! 
