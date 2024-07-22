[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![arXiv](https://img.shields.io/badge/arXiv-2406.16791-b31b1b.svg)](https://arxiv.org/abs/2406.16791)
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
  You can learn more about the CM concept from this [white paper](https://arxiv.org/abs/2406.16791) 
  and the [ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339).


  * [CM4MLOPS: CM automation recipes for MLOps, MLPerf and DevOps](https://github.com/mlcommons/cm4mlops) (*~6MB*) - 
    a collection of portable, extensible and technology-agnostic automation recipes
    with a human-friendly interface (aka CM scripts) to unify and automate all the manual steps required to compose, run, benchmark and optimize complex ML/AI applications 
    on diverse platforms with any software and hardware: see [online cKnowledge catalog](https://access.cknowledge.org/playground/?action=scripts),
    [online MLCommons catalog](https://docs.mlcommons.org/cm4mlops/scripts) 
    and [source code](https://github.com/mlcommons/cm4mlops/blob/master/script).

  * [CM automation recipes to reproduce research projects](https://github.com/ctuning/cm4research) (*~1MB*) - a unified CM interface to help researchers
    and engineers access, prepare and run diverse research projects and make it easier to validate them in the real world 
    across rapidly evolving models, data, software and hardware
    (see [our reproducibility initatives](https://cTuning.org/ae) 
    and [motivation](https://www.youtube.com/watch?v=7zpeIVwICa4) behind this project).

  * [CM automation recipes for ABTF](https://github.com/mlcommons/cm4abtf) (*~1MB*) - a unified CM interface and automation recipes
    to run automotive benchmark across different models, data sets, software and hardware from different vendors.

  * [Modular C++ harness for MLPerf loadgen](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-mlcommons-cpp)

  * [Modular Python harness for MLPerf loadgen](https://github.com/mlcommons/cm4mlops/tree/main/script/app-loadgen-generic-python)

* [Collective Knowledge Playground](https://access.cKnowledge.org) - an external platform being developed by [cKnowledge](https://cKnowledge.org)
  to list CM scripts similar to PYPI, aggregate AI/ML Systems benchmarking results in a reproducible format with CM workflows, 
  and organize [public optimization challenges and reproducibility initiatives](https://access.cknowledge.org/playground/?action=challenges) 
  to find the most performance and cost-effective AI/ML Systems.

  * [GUI to run modular benchmarks](https://access.cknowledge.org/playground/?action=howtorun) - such benchmarks 
    are composed from [CM scripts](https://access.cknowledge.org/playground/?action=scripts)
    and can run via a unified CM interface.

  * [MLCommons docs to run MLPerf inference benchmarks from command line via CM](https://docs.mlcommons.org/inference)

### Incubator

We are preparing new projects based on user feedback:
* [The next generation of CM](_incubator/cm-next-gen) *(prototyping stage)*
* [The crowd-testing infrastructure for CM4MLOps and CM4MLPerf](_incubator/cm4mlops-testing) *(brainstorming stage)*


### License

[Apache 2.0](LICENSE.md)

### Documentation

**MLCommons is updating the CM documentation based on user feedback - please check stay tuned for more details**.

* [CM Getting Started Guide and FAQ](docs/getting-started.md)
  * [Common CM interface to run MLPerf inference benchmarks](docs/mlperf/inference)
  * [Common CM interface to re-run experiments from ML and Systems papers including MICRO'23 and the Student Cluster Competition @ SuperComputing'23](docs/tutorials/common-interface-to-reproduce-research-projects.md)
  * [CM automation recipes for MLOps and DevOps](https://access.cknowledge.org/playground/?action=scripts)
  * [Other CM tutorials](docs/tutorials)
* [Full documentation](docs/README.md)
* [CM development tasks](docs/taskforce.md#current-tasks)
* [CM and CK history](docs/history.md)


### Citing CM

If you found CM useful, please cite this article: 
[ [ArXiv](https://arxiv.org/abs/2406.16791) ], [ [BibTex](https://github.com/mlcommons/ck/blob/master/citation.bib) ].

You can learn more about the motivation behind these projects from the following articles and presentations:

* "Enabling more efficient and cost-effective AI/ML systems with Collective Mind, virtualized MLOps, MLPerf, Collective Knowledge Playground and reproducible optimization tournaments": [ [ArXiv](https://arxiv.org/abs/2406.16791) ] 
* ACM REP'23 keynote about the MLCommons CM automation framework: [ [slides](https://doi.org/10.5281/zenodo.8105339) ] 
* ACM TechTalk'21 about automating research projects: [ [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4) ] [ [slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2021/grigorifursin_techtalk_slides.pdf) ]

### Acknowledgments

Collective Knowledge (CK) and Collective Mind (CM) were created by [Grigori Fursin](https://cKnowledge.org/gfursin),
sponsored by cKnowledge.org and cTuning.org, and donated to MLCommons to benefit everyone. 
Since then, this open-source technology (CM, CM4MLOps, CM4MLPerf, CM4ABTF, CM4Research, etc)
is being developed as a community effort thanks to all our
[volunteers, collaborators and contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md)! 
