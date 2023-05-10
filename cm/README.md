[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![Downloads](https://pepy.tech/badge/cmind/month)](https://pepy.tech/project/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### About

[Collective Mind scripting language (MLCommons CM)](https://github.com/mlcommons/ck/tree/master/cm/cmind) 
is a part of the [MLCommons Collective Knowledge project](https://github.com/mlcommons/ck).
It is motivated by the [feedback from researchers and practitioners](https://learning.acm.org/techtalks/reproducibility)
when reproducing experiments from more than 150 research papers and validating them in the real world - 
there is a need for a common, human-readable and technology-agnostic interface to run any software project 
on any platform with any software, hardware, and data.

CM is being developed by the [public MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md) 
as a simple, intuitive, technology-agnostic, and English-like scripting language that provides
a universal interface to any software project and transform it into a [database of portable and reusable CM scripts]( https://github.com/mlcommons/ck/tree/master/cm-mlops/script )
in a transparent and non-intrusive way.

CM also helps to solve the "dependency hell" for ML and AI systems while automatically generating 
unified README files and synthesize unified containers with a common API.
It is used to automate [reproducibility initiatives and artifact evaluation at AI, ML and Systems conferences](https://cTuning.org/ae)
while reducing all the tedious, manual, repetitive, and ad-hoc efforts to reproduce research projects and validate them in production.

CM powers the [Collective Knowledge platform (MLCommons CK playground)](https://access.cKnowledge.org)
to aggregate [reproducible experiments](https://access.cknowledge.org/playground/?action=experiments),
connect academia and industry to [organize reproducibility and optimization challenges]( https://github.com/mlcommons/ck/tree/master/cm-mlops/challenge ),
and help developers and users select Pareto-optimal end-to-end applications and systems based on their requirements and constraints
(cost, performance, power consumption, accuracy, etc).


### Documentation and the Getting Started Guide

[Table of contents](https://github.com/mlcommons/ck/tree/master/docs/README.md)

### Discussions


This open-source technology is being developed by the open
[MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
led by [Grigori Fursin](https://cKnowledge.org/gfursin) and
[Arjun Suresh](https://www.linkedin.com/in/arjunsuresh):

* Join our [public Discord server](https://discord.gg/JjWNWXKxwT).
* Join our [public conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw).
* Check our [news](docs/news.md).
* Check our [presentation](https://doi.org/10.5281/zenodo.7871070) with development plans.
* Read about our [CK concept (previous version before MLCommons)](https://arxiv.org/abs/2011.01149).

### Copyright

2021-2023 [MLCommons](https://mlcommons.org)

### License

[Apache 2.0](LICENSE.md)

### Acknowledgments

This project is currently supported by [MLCommons](https://mlcommons.org), [cTuning foundation](https://cTuning.org),
[cKnowledge](https://cKnowledge.org) and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.
