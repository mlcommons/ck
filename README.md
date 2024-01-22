[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)
[![Dockerfile update for CM scripts](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml)

### About

Collective Mind (CM) is a lightweight, non-intrusive and technology-agnostic workflow automation framework 
to run and manage AI/ML benchmarks, applications and research projects in a unified and fully automated way
on any platform with any software stack using a common, simple and human-readable interface.

CM is being developed by the [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
based on the feedback from the [research community](https://www.youtube.com/watch?v=7zpeIVwICa4), Google, AMD, Neural Magic, Nvidia, Qualcomm, Dell, HPE, Red Hat,
Intel, TTA, One Stop Systems, ACM and [other organizations and individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).

The goal is to help the community gradually convert all ad-hoc README files, papers, reports, Juputer notebooks and containers 
into [portable and reusable automation recipes (CM scripts)](https://github.com/mlcommons/ck/blob/master/cm-mlops/script)
that find and call existing scripts and tools via English-like language based on tags 
and glue them together via extensible JSON/YAML meta descriptions and simple Python logic.

For example, the following CM commands prepare and run image classification 
with ONNX on any platform with Linux, Windows and MacOS either natively or inside a containter:

```bash
pip install cmind
cm pull repo mlcommons@ck
cm run script "python app image-classification onnx" --input={some image.jpg}
```

Such approach requires minimal learning curve and minimal or no changes to existing projects while helping 
to dramatically reduce time to understand how to run and customize numerous AI/ML projects 
across diverse and continuously changing models, datasets, software and hardware from different vendors.

It also helps to gradually abstract, automate, unify and reuse all manual, tedious and repetitive MLOps and DevOps tasks
including *downloading artifacts, installing tools, substituting paths, updating environment variables, preparing run-time
environments, generating command lines, processing logs and sharing results*: see the 
[catalog of automation recipes shared by MLCommons](docs/list_of_scripts.md).

Please check this [Getting Started tutorial](docs/getting-started.md) to understand
how CM works and start using it.

Note that this project is under heavy development - feel free to get in touch
via [public Discord server](https://discord.gg/JjWNWXKxwT) if you have questions, 
suggestions and feature requests.


### Documentation

* [Getting Started Tutorial](docs/getting-started.md)
  * [CM interface for MLPerf benchmarks](docs/mlperf)
  * [CM interface for ML and Systems conferences](docs/tutorials/common-interface-to-reproduce-research-projects.md)
  * [CM automation recipes for MLOps and DevOps](cm-mlops/script)
  * [Other CM tutorials](docs/tutorials)
* [Full documentation](docs/README.md)
* [CM and CK history](docs/history.md)

### Motivation and concepts

* MLPerf inference submitter orientation: [slides](https://doi.org/10.5281/zenodo.8144274) 
* ACM REP'23 keynote about CM concepts: [slides](https://doi.org/10.5281/zenodo.8105339)

### Copyright

2022-2024 [MLCommons](https://mlcommons.org)

### License

[Apache 2.0](LICENSE.md)
