[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![arXiv](https://img.shields.io/badge/arXiv-2406.16791-b31b1b.svg)](https://arxiv.org/abs/2406.16791)
[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)
[![MLPerf inference resnet50](https://github.com/mlcommons/ck/actions/workflows/test-cm-mlperf-inference-resnet50.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-mlperf-inference-resnet50.yml)
[![CMX: image classification with ONNX](https://github.com/mlcommons/ck/actions/workflows/test-cmx-image-classification-onnx.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cmx-image-classification-onnx.yml)

## Collective Knowledge

[Collective Knowledge (CK, CM, CM4MLOps, CM4MLPerf and CMX)](https://cKnowledge.org) 
is an educational community project to learn how to run AI, ML and other emerging workloads 
in the most efficient and cost-effective way across diverse models, data sets, software and hardware:
[ [white paper](https://arxiv.org/abs/2406.16791) ].

It includes the following sub-projects.

### Collective Minds (CM)

The Collective Mind (CM) project, or Collective Minds, facilitates the
decomposition of complex software systems into portable, reusable, and
interconnected automation recipes. These recipes are developed and
continuously improved by the community.

#### CM automation framework

The [Collective Mind framework](https://github.com/mlcommons/ck/tree/master/cm) 
is a lightweight, Python-based toolset featuring 
a unified command-line interface (CLI), Python API, and minimal dependencies. 
It is designed to assist researchers and engineers in automating repetitive, time-consuming 
tasks such as building, running, benchmarking, and optimizing AI, machine learning, 
and other applications across diverse and continuously changing models, data, software and hardware.

Collective Mind is continuously enhanced through public and private Git repositories
with CM automation recipes and artifacts accessible via unified CM interface.

#### CMX automation framework

[CMX](https://github.com/mlcommons/ck/tree/master/cmx) is the next evolution 
of the Collective Mind framework designed to enhance simplicity, flexibility, and extensibility of automations 
based on user feedback. It is backwards compatible with CM, released along with CM 
in the [cmind package](https://pypi.org/project/cmind/) and can serve as drop-in replacement for CM.

The CM/CMX architecture diagram is available for viewing 
[here](https://github.com/mlcommons/ck/tree/master/docs/specs/cm-diagram-v3.5.1.png).



### Notable CM use cases

#### MLOps and MLPerf automations

[CM4MLOPS repository powered by CM](https://github.com/mlcommons/ck/tree/master/cm-mlops) - 
a collection of portable, extensible and technology-agnostic automation recipes
with a common CLI and Python API (CM scripts) to unify and automate 
all the manual steps required to compose, run, benchmark and optimize complex ML/AI applications 
on diverse platforms with any software and hardware. 

The two key automations are *script" and *cache*:
see [online catalog at CK playground](https://access.cknowledge.org/playground/?action=scripts),
[online MLCommons catalog](https://docs.mlcommons.org/cm4mlops/scripts).

CM scripts extend the concept of `cmake` with simple Python automations, native scripts
and JSON/YAML meta descriptions. They require Python 3.7+ with minimal dependencies and are 
[continuously extended by the community and MLCommons members](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md)
to run natively on Ubuntu, MacOS, Windows, RHEL, Debian, Amazon Linux
and any other operating system, in a cloud or inside automatically generated containers
while keeping backward compatibility.

See the [online documentation](https://docs.mlcommons.org/inference) 
at MLCommons to run MLPerf inference benchmarks across diverse systems using CM.

#### MLCommons ABTF automation

[CM4ABTF repository powered by CM](https://github.com/mlcommons/cm4abtf) - 
a collection of portable automations and CM scripts to run the upcoming 
automotive MLPerf benchmark across different models, data sets, software 
and hardware from different vendors.

#### MLPerf results visualization

[CM4MLPerf-results powered by CM](https://github.com/mlcommons/cm4mlperf-results) - 
a simplified and unified representation of the past MLPerf results 
in the CM format for further visualization and analysis using [CK graphs](https://access.cknowledge.org/playground/?action=experiments).

#### Collective Knowledge Playground

[Collective Knowledge Playground](https://access.cKnowledge.org) - 
a unified and open-source platform designed to [index all CM scripts](https://access.cknowledge.org/playground/?action=scripts) similar to PYPI,
assist users in preparing CM commands to:

* [run MLPerf benchmarks](https://access.cknowledge.org/playground/?action=howtorun)
* aggregate, process, visualize, and compare [benchmarking results](https://access.cknowledge.org/playground/?action=experiments) for AI and ML systems
* organize [open, reproducible optimization challenges and tournaments](https://access.cknowledge.org/playground/?action=challenges). 

These initiatives aim to help academia and industry
collaboratively enhance the efficiency and cost-effectiveness of AI systems.

#### Artifact Evaluation

[Artifact Evaluation automation](https://cTuning.org/ae) - a community-driven initiative 
leveraging the Collective Mind framework to automate artifact evaluation 
and support reproducibility efforts at ML and systems conferences.

* [CM4Research repository powered by CM](https://github.com/ctuning/cm4research) - 
a unified interface designed to streamline the preparation, execution, and reproduction of experiments in research projects.


## Legacy projects 

### CM-MLOps (now CM4MLOps)

You can find CM-MLOps original dev directory [here](https://github.com/mlcommons/ck/tree/master/cm-mlops).
We moved it to [CM4MLOps](https://github.com/mlcommons/ck/tree/master/cm4mlops) in 2024.
In 2025, we aggregate all CM and CMX automations in the [new CMX4MLOps repository](https://github.com/mlcommons/ck/tree/master/cmx4mlops).

### CK automation framework v1 and v2

You can find the original CK automation framework v1 and v2 directory [here](https://github.com/mlcommons/ck/tree/master/ck).
It was deprecated for the [CM framework](https://github.com/mlcommons/ck/tree/master/cm)
and later for the [CMX workflow automation framework (backwards compatible with CM)](https://github.com/mlcommons/ck/tree/master/cmx)


## License

[Apache 2.0](LICENSE.md)

## Copyright

Copyright (c) 2021-2024 MLCommons

Grigori Fursin, the cTuning foundation and OctoML donated this project to MLCommons to benefit everyone.

Copyright (c) 2014-2021 cTuning foundation

## Author

* [Grigori Fursin](https://cKnowledge.org/gfursin) (FlexAI, cTuning)

## Long-term vision

To learn more about the motivation behind CK and CM technology, please explore the following presentations:

* "Enabling more efficient and cost-effective AI/ML systems with Collective Mind, virtualized MLOps, MLPerf, Collective Knowledge Playground and reproducible optimization tournaments": [ [ArXiv](https://arxiv.org/abs/2406.16791) ]
* ACM REP'23 keynote about the MLCommons CM automation framework: [ [slides](https://doi.org/10.5281/zenodo.8105339) ] 
* ACM TechTalk'21 about Collective Knowledge project: [ [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4) ] [ [slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2021/grigorifursin_techtalk_slides.pdf) ]
* Journal of Royal Society'20: [ [paper](https://royalsocietypublishing.org/doi/10.1098/rsta.2020.0211) ]

## Documentation

* [White paper](https://arxiv.org/abs/2406.16791)
* [CM/CMX architecture](https://github.com/mlcommons/ck/tree/master/docs/specs/cm-diagram-v3.5.1.png)
* [CM/CMX installation GUI](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide and FAQ](https://github.com/mlcommons/ck/tree/master/docs/getting-started.md)
  * [Common CM interface to run MLPerf inference benchmarks](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference)
  * [Common CM interface to re-run experiments from ML and Systems papers including MICRO'23 and the Student Cluster Competition @ SuperComputing'23](https://github.com/mlcommons/ck/tree/master/docs/tutorials/common-interface-to-reproduce-research-projects.md)
  * [CM4MLOps automation recipes for MLOps and DevOps](https://access.cknowledge.org/playground/?action=scripts)
  * [Other CM tutorials](https://github.com/mlcommons/ck/tree/master/docs/tutorials)
* [Full documentation](https://github.com/mlcommons/ck/tree/master/docs/README.md)
* [CM taskforce](https://github.com/mlcommons/ck/tree/master/docs/taskforce.md)
* History: [CK](https://github.com/mlcommons/ck/tree/master/docs/history.md), [CM and CM automations for MLOps and MLPerf](https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md)


### Acknowledgments

This open-source project was created by [Grigori Fursin](https://cKnowledge.org/gfursin)
and sponsored by cTuning.org, OctoAI and HiPEAC.
Grigori donated CK to MLCommons to benefit the community
and to advance its development as a collaborative, community-driven effort.

We thank [MLCommons](https://mlcommons.org), [FlexAI](https://flex.ai) 
and [cTuning](https://cTuning.org) for supporting this project,
as well as our dedicated [volunteers and collaborators](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md)
for their feedback and contributions!

If you found the CM automations helpful, kindly reference this article:
[ [ArXiv](https://arxiv.org/abs/2406.16791) ], [ [BibTex](https://github.com/mlcommons/ck/blob/master/citation.bib) ].
