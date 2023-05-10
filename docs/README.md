# MLCommons CK and CM documentation

The Collective Knowledge project consists of 2 sub-projects:
[Collective Mind language (MLCommons CM)](#collective-mind-language-cm) 
and
[Collective Knowledge playground (MLCommons CK)](#collective-knowledge-playground-ck).


## Collective Mind language (CM)

CM is a simple, technology-agnostic, and English-like scripting language
powered by Python, JSON and/or YAML meta descriptions, and a unified CLI.
It is being developed by the [MLCommons Task Force on Automation and Reproducibility](taskforce.md)
to help researchers and practitioners describe, share, and reproduce experimental results 
in a unified and portable way across any rapidly evolving software, hardware, and data.

### Getting started guide

* [Brief motivation](motivation.md)
* [Installation and customization](installation.md)
* [Testing CM to run image classification on any platform with CPU and GPU](tutorials/modular-image-classification.md)
* [Understanding CM interface (CLI and Python API)](tutorials/cm-interface.md)
* [TBD: transforming your software project to the CM format](tutorials/transform-your-project-to-cm.md)
* [TBD: adding new portable scripts reusable by the community](tutorials/add-new-script.md) ([misc notes](tutorials/scripts.md#adding-new-artifacts-scripts-and-workflows-to-cm))
* [TBD: FAQ](faq.md)
* [Other tutorials](tutorials)

### Specification

* [CM format for software projects](specs/cm-repository.md)
* [CM CLI description](specs/cm-cli.md)
* [CM Python API](specs/cm-python-interface.md)
* [CM internal architecture](specs/cm-tool-architecture.md)
* [List of reusable CM automations](list_of_automations.md)
* [List of portable and reusable CM scripts](list_of_scripts.md)

## Collective Knowledge playground (CK)

Collective Knowledge playground (MLCommons CK)
is a free, open-source and technology-agnostic on-prem platform 
that aggregates [reproducible experiments](https://access.cknowledge.org/playground/?action=experiments) 
from the community unified by the [CM language](#collective-mind-language-cm).
CK helps to connect academia and industry to collaboratively improve reproduced experiments
via [public optimization challenges]( https://github.com/mlcommons/ck/tree/master/cm-mlops/challenge ).
It is being developed by the [MLCommons Task Force on Automation and Reproducibility](taskforce.md)
to help AI and ML users and developers generate Pareto-efficient AI and ML systems and applications
based on their requirements and constraints (optimal trade off between performance, power consumption, accuracy and costs).

*Note that this platform is under heavy development. Documentation will come soon. 
 In the meantime, please check our [plans](https://doi.org/10.5281/zenodo.7871070).*



## Collaborative development

This open-source technology is being developed by the open
[MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
led by [Grigori Fursin](https://cKnowledge.org/gfursin) and
[Arjun Suresh](https://www.linkedin.com/in/arjunsuresh):

* Join our [public Discord server](https://discord.gg/JjWNWXKxwT).
* Join our [public conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw).
* Check our [news](docs/news.md).
* Check our [presentation](https://doi.org/10.5281/zenodo.7871070) with development plans.
* Read about our [CK concept (previous version before MLCommons)](https://arxiv.org/abs/2011.01149).


## Copyright

2021-2023 [MLCommons](https://mlcommons.org)

## License

[Apache 2.0](../LICENSE.md)

## Acknowledgments

This project is currently supported by [MLCommons](https://mlcommons.org), [cTuning foundation](https://www.linkedin.com/company/ctuning-foundation),
[cKnowledge](https://www.linkedin.com/company/cknowledge) and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.
