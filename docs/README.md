# CK and CM documentation

**Collective Knowledge concept (CK)** provides a simple and non-intrusive way to share your software projects, 
experiments, knowledge and READMEs as a database of [reusable, portable and interconnected scripts and files](docs/list_of_scripts.md)
with a [human-readable CLI](docs/tutorials/sc22-scc-mlperf.md), Python API and JSON/YAML meta descriptions.

Motivated by our [tedious experience reproducing 150+ ML and Systems papers](https://learning.acm.org/techtalks/reproducibility), 
the goal is to provide a common and automated way to reproduce and reuse any experiment
on any platform with any software, hardware and data.

**Collective Mind framework (CM aka CK2)** is the second implementation 
of the CK concept being developed by the [open MLCommons taskforce](docs/mlperf-education-workgroup.md) 
as a [small Python library](https://github.com/mlcommons/ck/tree/master/cm/cmind) 
with a unified CLI and minimal dependencies.

CM helps you to assemble ML and AI Systems from [portable, reusable and interoperable CM scripts](docs/list_of_scripts.md)
and automate their benchmarking, optimization and deployment across rapidly evolving software, hardware and data
from the cloud to the edge.





## Introduction

* [Overview](overview.md)
* [Motivation](motivation.md)

## Getting started guide

* [Installation and customization](installation.md)
* [Trying CM (modular image classification)](tutorials/modular-image-classification.md)
* [List of CM automations](list_of_automations.md)

## Tutorials

* [Tutorial: portable CM scripts](tutorials/scripts.md)
  * [List of portable CM scripts](list_of_scripts.md)
* [Tutorial: CM database concepts](tutorials/concept.md)
* [Tutorial: modular MLPerf benchmark](tutorials/sc22-scc-mlperf.md)

## Developer guide

* [Contributing guidelines](../CONTRIBUTING.md)
* [CM specification](specification.md)
* [CM architecture and developer conventions](development.md)
* [CM core API](https://cknowledge.org/docs/cm/api/cmind.html)
* [Adding new artifacts, scripts and workflows to CM](../cm/docs/tutorial-scripts.md#adding-new-artifacts-scripts-and-workflows-to-cm) 


## On-going work

* [Modularizing ML&AI systems and automating their benchmarking, optimization and design space exploration](mlperf-education-workgroup.md)
  * [Minutes from weekly meetings](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw/edit)
  * [GitHub tickets](https://github.com/mlcommons/ck/issues)
* [Helping with artifact evaluation and reproducibility initiatives at conferences](https://cTuning.org/ae)




## Acknowledgments

This project is supported by [MLCommons](https://mlcommons.org), [OctoML](https://octoml.ai) 
and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
