# MLCommons CK and CM documentation

The Collective Knowledge project consists of 2 sub-projects:

* [Collective Mind (MLCommons CM)](#collective-mind-language-cm) 
  is an open-source, intuitive, technology-agnostic, and English-like language to help researchers and practitioners
  describe and reproduce experimental results in a unified way across any rapidly evolving
  software, hardware, and data.
  
* [Collective Knowledge playground (MLCommons CK)](#collective-knowledge-playground-ck)
  is a free, open-source and technology-agnostic on-prem platform that 
  aggregates [reproducible experiments](https://access.cknowledge.org/playground/?action=experiments) 
  in the CM format. 
  It is intended to connect academia and industry to collaboratively improve reproduced experiments
  via [public optimization challenges]( https://github.com/mlcommons/ck/tree/master/cm-mlops/challenge ).
  CK is being developed by MLCommons to help users select Pareto-optimal end-to-end AI and ML applications and systems 
  based on their requirements and constraints (performance, power consumption, accuracy and costs).

## Collective Mind language (CM)

### Getting started guide

* [Installing and customizing CM](installation.md)
* [Testing CM to run image classification on any platform with CPU and GPU](tutorials/modular-image-classification.md)
* [Understanding CM interface (CLI and Python API)](tutorials/cm-interface.md)
* [TBD: transforming your software project to the CM format](tutorials/transform-your-project-to-cm.md)
* [TBD: adding new portable scripts reusable by the community](tutorials/add-new-script.md) ([misc notes](tutorials/scripts.md#adding-new-artifacts-scripts-and-workflows-to-cm))
* [TBD: FAQ](faq.md)

### Specification

* [CM format for software projects](specs/cm-repository.md)
* [CM CLI description](specs/cm-cli.md)
* [CM Python API](specs/cm-python-interface.md)
* [CM internal architecture](specs/cm-tool-architecture.md)

### Catalog of reusable components

* [List of reusable CM automations](list_of_automations.md)
* [List of portable and reusable CM scripts](list_of_scripts.md)

### On-going projects

* [Modularizing MLPerf and automating benchmarking, optimization, design space exploration and submissions](mlperf-education-workgroup.md)
  * [Minutes from weekly meetings](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw/edit)
  * [GitHub tickets](https://github.com/mlcommons/ck/issues)
* [Supporting artifact evaluation and reproducibility initiatives at conferences](https://cTuning.org/ae)

### Tutorials

We plan to update them soon.

* [Tutorial: understanding portable CM scripts](tutorials/scripts.md)
* [Tutorial: understanding CM database concepts](tutorials/concept.md)
* [Tutorial: trying modular MLPerf benchmark via CM interface](tutorials/sc22-scc-mlperf.md)
* [Tutorial: customizing MLPerf inference benchmark and preparing submission](tutorials/mlperf-inference-submission.md)
* [Tutorial: measuring power during MLPerf inference benchmarks](tutorials/mlperf-inference-power-measurement.md)




## Collective Knowledge playground (CK)



## Misc

* [Project overview](overview.md)
* [History](history.md)


## Collaborative development

This open-source technology is being developed by the open
[MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
led by [Grigori Fursin](https://cKnowledge.org/gfursin) and
[Arjun Suresh](https://www.linkedin.com/in/arjunsuresh).

## Copyright

2021-2023 [MLCommons](https://mlcommons.org)

## License

[Apache 2.0](../LICENSE.md)

## Acknowledgments

This project is currently supported by [MLCommons](https://mlcommons.org), [cTuning foundation](https://www.linkedin.com/company/ctuning-foundation),
[cKnowledge](https://www.linkedin.com/company/cknowledge) and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.
