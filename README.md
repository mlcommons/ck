[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![arXiv](https://img.shields.io/badge/arXiv-2406.16791-b31b1b.svg)](https://arxiv.org/abs/2406.16791)
[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)
[![MLPerf inference resnet50](https://github.com/mlcommons/ck/actions/workflows/test-cm-mlperf-inference-resnet50.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-mlperf-inference-resnet50.yml)
[![CMX: image classification with ONNX](https://github.com/mlcommons/ck/actions/workflows/test-cmx-image-classification-onnx.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cmx-image-classification-onnx.yml)

### About

[Collective Knowledge (CK)](https://cKnowledge.org) in an educational project
to help researchers and engineers automate their repetitive, tedious and time-consuming tasks
to build, run, benchmark and optimize AI, ML and other applications and systems 
across diverse and continuously changing models, data, software and hardware.

CK consists of several sub-projects:

* [Collective Mind framework (CM)](cm) - a very lightweight Python-based framework with minimal dependencies
  to help users implement, share and reuse cross-platform automation recipes to 
  build, benchmark and optimize applications on any platform
  with any software and hardware. 

  * [CM interface to run MLPerf inference benchmarks](https://docs.mlcommons.org/inference)

  * [CM4MLOPS](https://github.com/mlcommons/cm4mlops) - 
    a collection of portable, extensible and technology-agnostic automation recipes
    with a human-friendly interface (aka CM scripts) to unify and automate all the manual steps required to compose, run, benchmark and optimize complex ML/AI applications 
    on diverse platforms with any software and hardware: see [online catalog at CK playground](https://access.cknowledge.org/playground/?action=scripts),
    [online MLCommons catalog](https://docs.mlcommons.org/cm4mlops/scripts) 

  * [CM4ABTF](https://github.com/mlcommons/cm4abtf) - a unified CM interface and automation recipes
    to run automotive benchmark across different models, data sets, software and hardware from different vendors.

* [CMX (the next generation of CM and CM4MLOps)](cm/docs/cmx) - we are developing the next generation of CM 
    to make it simpler and more flexible based on user feedback. Please follow 
    this project [here]( https://github.com/orgs/mlcommons/projects/46 ).


* [Collective Knowledge Playground](https://access.cKnowledge.org) - a unified platform
  to list CM scripts similar to PYPI, aggregate AI/ML Systems benchmarking results in a reproducible format with CM workflows, 
  and organize [public optimization challenges and reproducibility initiatives](https://access.cknowledge.org/playground/?action=challenges) 
  to co-design more efficient and cost-effiective software and hardware for emerging workloads.

* [Artifact Evaluation](https://cTuning.org/ae) - automating artifact evaluation and reproducibility initiatives at ML and systems conferences.



### License

[Apache 2.0](LICENSE.md)

### Copyright

* Copyright (c) 2021-2024 MLCommons
* Copyright (c) 2014-2021 cTuning foundation

### Maintainers

* CM/CM4Research/CM4MLPerf-results: [Grigori Fursin](https://cKnowledge.org/gfursin)
* CM4MLOps: [Arjun Suresh](https://github.com/arjunsuresh) and [Anandhu Sooraj](https://github.com/anandhu-eng)
* CMX (the next generation of CM) [Grigori Fursin](https://cKnowledge.org/gfursin)

### Citing our project

If you found the CM automation framework helpful, kindly reference this article:
[ [ArXiv](https://arxiv.org/abs/2406.16791) ], [ [BibTex](https://github.com/mlcommons/ck/blob/master/citation.bib) ].

To learn more about the motivation behind CK and CM technology, please explore the following presentations:

* "Enabling more efficient and cost-effective AI/ML systems with Collective Mind, virtualized MLOps, MLPerf, Collective Knowledge Playground and reproducible optimization tournaments": [ [ArXiv](https://arxiv.org/abs/2406.16791) ]
* ACM REP'23 keynote about the MLCommons CM automation framework: [ [slides](https://doi.org/10.5281/zenodo.8105339) ] 
* ACM TechTalk'21 about Collective Knowledge project: [ [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4) ] [ [slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2021/grigorifursin_techtalk_slides.pdf) ]


### CM Documentation

* [CM installation GUI](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide and FAQ](docs/getting-started.md)
  * [Common CM interface to run MLPerf inference benchmarks](docs/mlperf/inference)
  * [Common CM interface to re-run experiments from ML and Systems papers including MICRO'23 and the Student Cluster Competition @ SuperComputing'23](docs/tutorials/common-interface-to-reproduce-research-projects.md)
  * [CM automation recipes for MLOps and DevOps](https://access.cknowledge.org/playground/?action=scripts)
  * [Other CM tutorials](docs/tutorials)
* [Full documentation](docs/README.md)
* [CM development tasks](docs/taskforce.md#current-tasks)
* [CM and CK history](docs/history.md)


### Acknowledgments

The open-source Collective Knowledge project (CK, CM, CM4MLOps/CM4MLPerf, 
CM4Research and CMX) was created by [Grigori Fursin](https://cKnowledge.org/gfursin)
and sponsored by cTuning.org, OctoAI and HiPEAC.
Grigori donated CK to MLCommons to benefit the community
and to advance its development as a collaborative, community-driven effort.
We thank MLCommons and FlexAI for supporting this project,
as well as our dedicated [volunteers and collaborators](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md)
for their feedback and contributions!
