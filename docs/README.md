# CK and CM documentation

The Collective Knowledge project (CK) is motivated by our tedious experience reproducing experiments 
from [150 research papers](https://learning.acm.org/techtalks/reproducibility)
and validating them in the real world - we decided to develop a universal and human-readable 
interface to access any software project and run it on any platform with any software, hardware and data.

The [Collective Mind tool (CM)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
helps users to add this universal interface to their software projects and transform them into a 
[database of portable and reusable components](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md)
in a transparent and non-intrusive way.

CM is being developed by the [open MLCommons taskforce](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md) 
to solve the "dependency hell" for ML and AI systems, reduce their development, benchmarking, optimization and deployment time,
and automate [reproducibility initiatives and artifact evaluation at conferences](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md).


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


### Misc

* [Project overview](overview.md)
* [History](history.md)


## Contacts

* [Open MLCommons taskforce](mlperf-education-workgroup.md)
* [Maintainers of the CM tool](../README.md#maintainers)
* [CK project mailing list](https://groups.google.com/forum/#!forum/collective-knowledge)

### Acknowledgments

This project is supported by [MLCommons](https://mlcommons.org), [cTuning foundation](https://cTuning.org),
[cKnowledge](https://cKnowledge.org) and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
