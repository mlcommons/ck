# Documentation

We deeply believe in the power of open science and open source to solve the world's most challenging problems.

Following our [tedious experience reproducing 150 research papers and validating them in the real world](https://learning.acm.org/techtalks/reproducibility),
we have developed the Collective Knowledge framework to provide a common interface to access and reuse
all shared knowledge (research projects, experiments, AI/ML models, code and data), facilitate reproducible research, 
and simplify transfer to production across rapidly evolving models, software, hardware and data.

The [cTuning foundation](https://cTuning.org) donated the original [Collective Knowledge technology](https://github.com/mlcommons/ck/commit/e74f942012f3ae0825388511106fb5fd402afda7)
to MLCommons in 2021 to continue developments as a community effort in an [open and transparent way](docs/taskforce.md) and deprecated v1 in 2021 and v2 in 2022.

The latest Collective Knowledge technology v3 consists of three sub-projects:
[`Collective Mind automation language (CM)`](#collective-mind-automation-language-cm), 
[`Collective Knowledge platform (CK playground v3)`](#collective-knowledge-playground-ck) 
and [`Modular Inference Library (MIL)`](#modular-inference-library-mil)
to let everyone participate in collaborative benchmarking, optimization, co-design 
and deployment of the state-of-the-art AI solutions across any software, hardware, models and data from any vendor.

Check our [ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339) to learn about our vision and development plans.

*This project is supported by [MLCommons](https://mlcommons.org), [cTuning.org](https://linkedin.com/company/ctuning-foundation),
 [cKnowledge.org](https://www.linkedin.com/company/cknowledge) and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
 We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.*

The development is led by [Grigori Fursin](https://cKnowledge.org/gfursin) and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh).

**Copyright:** 2021-2023 [MLCommons](https://mlcommons.org)

**License:** [Apache 2.0](../LICENSE.md)


## Collective Mind automation language (CM)

* [Introduction](introduction-cm.md)
* [Installation and customization](installation.md)
* [Unified CLI and Python API](interface.md)
  * [CM "script" automation](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/script/README-extra.md)
  * [CM "cache" automation](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/cache/README-extra.md)
  * [CM "experiment" automation](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/experiment/README-extra.md)
  * [List of all unified CM automations from MLCommons](list_of_automations.md)
  * [List of all portable and reusable CM scripts from MLCommons](list_of_scripts.md)
* [Debugging](debugging.md)
* [Real-world use cases](use-cases.md)
* [Tutorials](tutorials/README.md)
* [Specifications](specs/README.md)
* [Source code](https://github.com/mlcommons/ck/tree/master/cm/cmind)
* [FAQ](faq.md)

## Collective Knowledge playground (CK)

*Note that this collaborative platform is under heavy development.*

* [Introduction](introduction-ck.md)
* [Open access via x.cKnowledge.org](https://x.cKnowledge.org)
  * [Participate in reproducibility and optimization challenges](https://access.cknowledge.org/playground/?action=challenges)
    * [GUI to run MLPerf inference benchmarks](http://cknowledge.org/mlperf-inference-gui)
    * [GUI to prepare MLPerf inference submissions](https://cknowledge.org/mlperf-inference-submission-gui)
    * [Prototype of the LLM-based assistant to run MLPerf benchmarks out-of-the-box](https://access.cKnowledge.org/assistant)
  * [See current leaderboard](https://access.cknowledge.org/playground/?action=contributors)
  * [Visualize and compare all past MLPerf results with derived metrics](https://access.cknowledge.org/playground/?action=experiments)
* [Development page](../platform)
* [Source code (CM script)](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/gui)


## Modular Inference Library (MIL)

*Note that this library is under heavy development.*

* [Development link](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-cpp/README-extra.md)

## Collaborative development

This open-source technology is being developed by the [MLCommons Task Force on Automation and Reproducibility](taskforce.md),
[cTuning.org](https://cTuning.org) and [cKnowledge.org](https://cKnowledge.org).

* Check our [ACM REP'23 keynote](https://doi.org/10.5281/zenodo.7871070) and [Forbes article](https://www.forbes.com/sites/karlfreund/2023/04/05/nvidia-performance-trounces-all-competitors-who-have-the-guts-to-submit-to-mlperf-inference-30/?sh=3c38d2866676) 
  to learn more about our vision and development plans.
* Join our [public Discord server](https://discord.gg/JjWNWXKxwT) and [public conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw).
* Follow our [news](docs/news.md).
* Read about the [previous version of the MLCommons CM automation language: cTuning CK framework (2014-2022)](https://arxiv.org/abs/2011.01149).
