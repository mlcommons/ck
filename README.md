[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### About

The "Collective Knowledge" project (CK) is motivated by the [feedback from researchers and practitioners](https://learning.acm.org/techtalks/reproducibility)
while reproducing results from more than 150 research papers and validating them in the real world - 
there is a need for a common and technology-agnostic framework
that can facilitate reproducible research and simplify technology transfer to production
across diverse and rapidly evolving software, hardware, models, and data.

CK is being developed by the public [MLCommons task force on automation and reproducibility](docs/taskforce.md) 
to connect academia and industry to develop, benchmark, compare, and deploy Pareto-efficient AI and ML systems and applications 
(optimal trade off between performance, accuracy, power consumption, and price)
in a unified, automated and reproducible way while slashing all development and operational costs.

The CK projects consists of the following sub-projects:

* [Collective Mind scripting language (MLCommons CM)](cm) 
  is intended to help researchers and practitioners
  describe all the steps required to reproduce their experiments across any software, hardware, and data
  in a common and technology-agnostic way.
  CM can automatically generate unified README and synthesize unified containers with a common API
  while reducing all the tedious, manual, repetitive, and ad-hoc efforts to validate research projects in production.

* [Collective Mind scripts (MLCommons CM scripts)](cm-mlops/script) 
  provide a low-level implementation of the high-level and technology-agnostic CM language.

* [Collective Knowledge platform (MLCommons CK playground)](platform) 
  aggregates [reproducible experiments](https://access.cknowledge.org/playground/?action=experiments) 
  in the CM format, connects academia and industry to 
  [organize reproducibility and optimization challenges]( https://github.com/mlcommons/ck/tree/master/cm-mlops/challenge ),
  and help developers and users select Pareto-optimal end-to-end applications and systems based on their requirements and constraints
  (cost, performance, power consumption, accuracy, etc).

### Documentation and the Getting Started Guide

[Table of contents](https://github.com/mlcommons/ck/tree/master/docs/README.md)

### Discussions

* Join our [public Discord server](https://discord.gg/JjWNWXKxwT).
* Join our [public conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw).
* Check our [news](docs/news.md).
* Check our [presentation](https://doi.org/10.5281/zenodo.7871070) with development plans.
* Read about our [CK concept (previous version before MLCommons)](https://arxiv.org/abs/2011.01149).

### Collaborative development

This open-source technology is being developed by the open
[MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
led by [Grigori Fursin](https://cKnowledge.org/gfursin) and
[Arjun Suresh](https://www.linkedin.com/in/arjunsuresh).

### Copyright

2021-2023 [MLCommons](https://mlcommons.org)

### License

[Apache 2.0](LICENSE.md)

### Acknowledgments

This project is currently supported by [MLCommons](https://mlcommons.org), [cTuning foundation](https://www.linkedin.com/company/ctuning-foundation),
[cKnowledge](https://www.linkedin.com/company/cknowledge) and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.
