# CK and CM documentation

The goal of the [Collective Knowledge project (CK)](https://learning.acm.org/techtalks/reproducibility) 
is to make software projects more portable, reproducible and reusable 
across continuously changing software, hardware and data.

The [Collective Mind tool (CM)](cm/cmind) 
provides a simple and non-intrusive way to transform any software project
into a database of [reusable, portable and interconnected scripts and files](list_of_scripts.md)
with a [human-readable CLI](tutorials/sc22-scc-mlperf.md), 
unified Python API and extensible JSON/YAML meta descriptions.

It is being developed by the [open MLCommons taskforce](mlperf-education-workgroup.md) 
to reduce development, benchmarking, optimization and deployment time for ML and AI systems,
and automate [reproducibility initiatives and artifact evaluation at conferences](tutorials/sc22-scc-mlperf.md).



## Getting started guide

* [Installing and customizing CM](installation.md).
* [Using CM to run image classification on any platform](tutorials/modular-image-classification.md).
* TBD: transforming your software project to the CM format.
* TBD: adding new portable scripts reusable by the community ([notes](../cm/docs/tutorial-scripts.md#adding-new-artifacts-scripts-and-workflows-to-cm)).

## Specification

* [CM repository structure](specs/cm-repository.md)
* [CM command line](specs/cm-cli.md)
* [CM Python interface](specs/cm-python-interface.md)
* [CM tool architecture](specs/cm-tool-architecture.md)
* [CM tool API](https://cknowledge.org/docs/cm/api/cmind.html)
* [CM scripts](specs/cm-script.md)

## On-going projects

* [Modularizing ML and AI systems and reducing their development, benchmarking, optimization and deployment time and costs](mlperf-education-workgroup.md)
  * [Minutes from weekly meetings](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw/edit)
  * [GitHub tickets](https://github.com/mlcommons/ck/issues)
* [Supporting artifact evaluation and reproducibility initiatives at conferences](https://cTuning.org/ae)

## References

* [List of reusable CM automations](list_of_automations.md).
* [List of reusable CM scripts](list_of_scripts.md).

## Tutorials

We plan to update them soon.

* [Tutorial: understanding portable CM scripts](tutorials/scripts.md)
* [Tutorial: understanding CM database concepts](tutorials/concept.md)
* [Tutorial: trying modular MLPerf benchmark via CM interface](tutorials/sc22-scc-mlperf.md)


## Misc

* [Project overview](overview.md)
* [History](history.md)



## Acknowledgments

This project is supported by [MLCommons](https://mlcommons.org), [OctoML](https://octoml.ai) 
and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
