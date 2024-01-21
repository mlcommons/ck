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

Our goal is to reduce time required to understand how to run, customize and optimize numerous AI/ML projects 
across diverse and continuously changing models, datasets, software and hardware from different vendors
while automating all manual, tedious and repetitive tasks (*downloading artifacts,
installing tools, substituting paths, updating environment variables, preparing run-time
environments, generating command lines, processing logs and sharing results*)
via [portable and reusable automation recipes (CM scripts)](https://github.com/mlcommons/ck/blob/master/cm-mlops/script).

For example, the following commands should prepare and run image classification 
with ONNX on any platform with Linux, Windows and MacOS either natively or inside a containter:

```bash
pip install cmind
cm pull repo mlcommons@ck
cm run script "python app image-classification onnx" --input={some image.jpg}
```

### Documentation

* [Getting Started Tutorial](docs/getting-started.md)
  * [CM interface for MLPerf benchmarks](docs/mlperf)
  * [CM interface for ML and Systems conferences](docs/tutorials/common-interface-to-reproduce-research-projects.md)
  * [CM automation recipes for MLOps and DevOps](cm-mlops/script)
* [Full documentation](docs/README.md)
* [CM and CK history](docs/history.md)

### Motivation and concepts

* MLPerf inference submitter orientation: [slides](https://doi.org/10.5281/zenodo.8144274) 
* ACM REP'23 keynote about CM concepts: [slides](https://doi.org/10.5281/zenodo.8105339)

### Copyright

2022-2024 [MLCommons](https://mlcommons.org)

### License

[Apache 2.0](LICENSE.md)

### Public discussions and developments

Follow [official GitHub repository](https://github.com/mlcommons/ck) 
and join [public Discord server](https://discord.gg/JjWNWXKxwT).
