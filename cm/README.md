[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![arXiv](https://img.shields.io/badge/arXiv-2406.16791-b31b1b.svg)](https://arxiv.org/abs/2406.16791)
[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)


### Common Metadata eXchange (CMX)

The [CMX framework](https://github.com/mlcommons/ck/tree/master/cmx) 
facilitates the decomposition of complex software systems and benchmarks such as MLPerf
into portable, reusable, and interconnected automation recipes for MLOps and DevOps. 
These recipes are developed and continuously improved by the community.

***Starting in 2025, CMX V4.0.0 serves as drop-in, backward-compatible replacement 
   for the earlier [Collective Mind framework (CM)](https://github.com/mlcommons/ck/tree/master/cm),
   while providing a simpler and more robust interface.***

CMX is a lightweight, Python-based toolset that provides a unified
command-line interface (CLI), a Python API, and minimal dependencies.
It is designed to help researchers and engineers automate repetitive,
time-consuming tasks such as building, running, benchmarking, and
optimizing AI, machine learning, and other applications across diverse and
constantly evolving models, data, software, and hardware.

CMX is continuously enhanced through public and private Git repositories,
providing automation recipes and artifacts that are seamlessly accessible
via its unified interface.

CMX is a part of [Collective Knowledge (CK)](https://github.com/mlcommons/ck) - 
an educational community project to learn how to run AI, ML and other emerging workloads 
in the most efficient and cost-effective way across diverse 
and ever-evolving systems using the MLPerf benchmarking methodology.

### Legacy Collective Mind automation framework (CM)

* [GitHub](https://github.com/mlcommons/ck/tree/master/cm)

### MLOps and MLPerf automations

We have developed a collection of portable, extensible and technology-agnostic automation recipes
with a common CLI and Python API (CM scripts) to unify and automate 
all the manual steps required to compose, run, benchmark and optimize complex ML/AI applications 
on diverse platforms with any software and hardware. 

The two key automations are *script* and *cache*:
see [online catalog at CK playground](https://access.cknowledge.org/playground/?action=scripts),
[online MLCommons catalog](https://docs.mlcommons.org/cm4mlops/scripts).

CM scripts extend the concept of `cmake` with simple Python automations, native scripts
and JSON/YAML meta descriptions. They require Python 3.7+ with minimal dependencies and are 
[continuously extended by the community and MLCommons members](https://github.com/mlcommons/ck/blob/master/CONTRIBUTORS.md)
to run natively on Ubuntu, MacOS, Windows, RHEL, Debian, Amazon Linux
and any other operating system, in a cloud or inside automatically generated containers
while keeping backward compatibility.

See the [online documentation](https://docs.mlcommons.org/inference) 
at MLCommons to run MLPerf inference benchmarks across diverse systems using CMX.
Just install `pip install cmind` and substitute the following commands with `cmx`:
* `cm` -> `cmx`
* `mlc` -> `cmx run mlc`
* `mlcr` -> `cmx run mlcr`

### MLPerf results visualization

[CM4MLPerf-results powered by CM](https://github.com/mlcommons/cm4mlperf-results) - 
a simplified and unified representation of the past MLPerf results 
in the CM format for further visualization and analysis using [CK graphs](https://access.cknowledge.org/playground/?action=experiments).

### Collective Knowledge Playground

[Collective Knowledge Playground](https://access.cKnowledge.org) - 
a unified and open-source platform designed to [index all CM scripts](https://access.cknowledge.org/playground/?action=scripts) similar to PYPI,
assist users in preparing CM commands to:

* aggregate, process, visualize, and compare [MLPerf benchmarking results](https://access.cknowledge.org/playground/?action=experiments) for AI and ML systems
* [run MLPerf benchmarks](https://access.cknowledge.org/playground/?action=howtorun)
* organize [open and reproducible optimization challenges and tournaments](https://access.cknowledge.org/playground/?action=challenges). 

These initiatives aim to help academia and industry
collaboratively enhance the efficiency and cost-effectiveness of AI systems.

### Artifact Evaluation and Reproducibility Initiatives

[Artifact Evaluation automation](https://cTuning.org/ae) - a community-driven initiative 
leveraging the Collective Mind framework to automate artifact evaluation 
and support reproducibility efforts at ML and systems conferences.


## License

[Apache 2.0](LICENSE.md)

## Copyright

Copyright (c) 2021-2025 MLCommons

Grigori Fursin, the cTuning foundation and OctoML donated this project to MLCommons to benefit everyone.

Copyright (c) 2014-2021 cTuning foundation

## Author

* [Grigori Fursin](https://cKnowledge.org/gfursin) (FlexAI, cTuning)

## Maintainers

* CM, CM4MLOps and MLPerf automations: [MLCommons infra WG](https://mlcommons.org)
* CMX (the next generation of CM since 2025): [Grigori Fursin](https://cKnowledge.org/gfursin)

## Long-term vision

To learn more about the motivation behind this project, please explore the following presentations:

* "Enabling more efficient and cost-effective AI/ML systems with Collective Mind, virtualized MLOps, MLPerf, Collective Knowledge Playground and reproducible optimization tournaments": [ [ArXiv](https://arxiv.org/abs/2406.16791) ]
* ACM REP'23 keynote about the MLCommons CM automation framework: [ [slides](https://doi.org/10.5281/zenodo.8105339) ] 
* ACM TechTalk'21 about Collective Knowledge project: [ [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4) ] [ [slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2021/grigorifursin_techtalk_slides.pdf) ]
* Journal of Royal Society'20: [ [paper](https://royalsocietypublishing.org/doi/10.1098/rsta.2020.0211) ]

## Documentation

* [White paper](https://arxiv.org/abs/2406.16791)
* [CMX architecture](https://github.com/mlcommons/ck/tree/master/docs/specs/cm-diagram-v3.5.1.png)
* [CMX installation GUI](https://access.cknowledge.org/playground/?action=install)

*TBD*


### Acknowledgments

This open-source project was created by [Grigori Fursin](https://cKnowledge.org/gfursin)
and sponsored by cTuning.org, OctoAI and HiPEAC.
Grigori donated this project to MLCommons to modularize and automate MLPerf benchmarks,
benefit the community, and foster its development as a collaborative, community-driven effort.

We thank [MLCommons](https://mlcommons.org), [FlexAI](https://flex.ai) 
and [cTuning](https://cTuning.org) for supporting this project,
as well as our dedicated [volunteers and collaborators](https://github.com/mlcommons/ck/blob/master/CONTRIBUTORS.md)
for their feedback and contributions!

If you found the CM automations helpful, kindly reference this article:
[ [ArXiv](https://arxiv.org/abs/2406.16791) ], [ [BibTex](https://github.com/mlcommons/ck/blob/master/citation.bib) ].
