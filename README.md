[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### Documentation and the Getting Started Guide

[Table of contents](docs/README.md)

### About

***Our mission is to connect academia and industry to solve the real-world problems by facilitating reproducible research 
and bridging the growing gap between research and production - [see our ACM REP'23 keynote to learn more about our vision](https://doi.org/10.5281/zenodo.8105339)!***

The "Collective Knowledge" project (CK) is motivated by the [feedback from researchers and practitioners](https://learning.acm.org/techtalks/reproducibility)
while reproducing results from more than 150 research papers and validating them in the real world - 
there is a need for a common and technology-agnostic language
that can facilitate reproducible research and simplify technology transfer to production
across diverse and rapidly evolving software, hardware, models, and data.
It consists of the following sub-projects:

* [Collective Mind scripting language (MLCommons CM)](cm) 
  is intended to help researchers and practitioners
  describe all the steps required to reproduce their experiments across any software, hardware, and data
  in a common and technology-agnostic way.
  It is powered by Python, JSON and/or YAML meta descriptions, and a unified CLI.
  CM can automatically generate unified README and synthesize unified containers with a common API
  while reducing all the tedious, manual, repetitive, and ad-hoc efforts to validate research projects in production.
  It is used in the same way in native environments, Python virtual environments, and containers.

  See a few real-world examples of using the CM scripting language:
  - [README to reproduce published IPOL'22 paper](cm-mlops/script/app-ipol-reproducibility-2022-439)
  - [README to reproduce MLPerf RetinaNet inference benchmark at Student Cluster Competition'22](docs/tutorials/sc22-scc-mlperf.md)
  - [Auto-generated READMEs to reproduce official MLPerf BERT inference benchmark v3.0 submission with a model from the Hugging Face Zoo](https://github.com/mlcommons/submissions_inference_3.0/tree/main/open/cTuning/code/huggingface-bert/README.md)
  - [Auto-generated Docker containers to run and reproduce MLPerf inference benchmark](cm-mlops/script/app-mlperf-inference/dockerfiles/retinanet)

* [Collective Mind scripts (MLCommons CM scripts)](cm-mlops/script) 
  provide a low-level implementation of the high-level and technology-agnostic CM language.

* [Collective Knowledge platform (MLCommons CK playground)](platform) 
  aggregates [reproducible experiments](https://access.cknowledge.org/playground/?action=experiments) 
  in the CM format, connects academia and industry to 
  [organize benchmarking, reproducibility, replicability and optimization challenges]( https://github.com/mlcommons/ck/tree/master/cm-mlops/challenge ),
  and help developers and users select Pareto-optimal end-to-end applications and systems based on their requirements and constraints
  (cost, performance, power consumption, accuracy, etc).


### Collaborative development

This open-source technology is being developed by the public
[MLCommons task force on automation and reproducibility](docs/taskforce.md)
led by [Grigori Fursin](https://cKnowledge.org/gfursin) and
[Arjun Suresh](https://www.linkedin.com/in/arjunsuresh).
The goal is to connect academia and industry to develop, benchmark, compare, synthesize, 
and deploy Pareto-efficient AI and ML systems and applications 
(optimal trade off between performance, accuracy, power consumption, and price)
in a unified, automated and reproducible way while slashing all development and operational costs.

* Join our [public Discord server](https://discord.gg/JjWNWXKxwT).
* Join our [public conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw).
* Check our [news](docs/news.md).
* Check our [presentation](https://doi.org/10.5281/zenodo.7871070) and [Forbes article](https://www.forbes.com/sites/karlfreund/2023/04/05/nvidia-performance-trounces-all-competitors-who-have-the-guts-to-submit-to-mlperf-inference-30/?sh=3c38d2866676) about our development plans.
* Read about our [CK concept (previous version before MLCommons)](https://arxiv.org/abs/2011.01149).

### Copyright

2021-2023 [MLCommons](https://mlcommons.org)

### License

[Apache 2.0](LICENSE.md)

### Acknowledgments

This project is currently supported by [MLCommons](https://mlcommons.org), [cTuning foundation](https://www.linkedin.com/company/ctuning-foundation),
[cKnowledge](https://www.linkedin.com/company/cknowledge) and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.
