[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)
[![Dockerfile update for CM scripts](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml)
[![MLPerf inference resnet50](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-resnet50.yml/badge.svg?branch=master&event=pull_request)](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-resnet50.yml)
[![MLPerf inference retinanet](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-retinanet.yml/badge.svg?branch=master&event=pull_request)](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-retinanet.yml)
[![MLPerf inference bert](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-bert.yml/badge.svg?event=pull_request)](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-bert.yml)
[![MLPerf inference rnnt](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-rnnt.yml/badge.svg?event=pull_request)](https://github.com/mlcommons/ck/actions/workflows/test-mlperf-inference-rnnt.yml)


Collective Mind (CM) is a very light-weight, non-intrusive and
technology-agnostic workflow automation framework with a human-readable
interface to manage complex AI/ML projects, run experiments and exchange
knowledge on any platform with any software stack in a unified way.

For example, the following commands should prepare and run image classification 
with ONNX on Linux, Windows and MacOS in a native environment:


```bash
pip install cmind
cm pull repo mlcommons@ck
cmr "python app image-classification onnx"
```


### Some projects modularized and automated by CM

* [A unified way to run MLPerf inference benchmarks with different models, software and hardware](docs/mlperf/inference). See [current coverage](https://github.com/mlcommons/ck/issues/1052).
* [A unitied way to run MLPerf training benchmarks](docs/tutorials/reproduce-mlperf-training.md) *(prototyping phase)*
* [A unified way to run MLPerf tiny benchmarks](docs/tutorials/reproduce-mlperf-tiny.md) *(prototyping phase)*
* A unified CM to run automotive benchmarks *(prototyping phase)*
* [An open-source platform to aggregate, visualize and compare MLPerf results](https://access.cknowledge.org/playground/?action=experiments)
  * [Leaderboard for community contributions](https://access.cknowledge.org/playground/?action=contributors)
* [Artifact Evaluation and reproducibility initiatives](https://cTuning.org/ae) at ACM/IEEE/NeurIPS conferences:
  * [A unified way to run experiments and reproduce results from ACM/IEEE MICRO'23 and ASPLOS papers](https://github.com/ctuning/cm-reproduce-research-projects)
  * [Student Cluster Competition at SuperComputing'23](https://github.com/mlcommons/ck/blob/master/docs/tutorials/scc23-mlperf-inference-bert.md)
  * [CM automation to reproduce IPOL paper](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/reproduce-ipol-paper-2022-439/README-extra.md)


### CM documentation

* [CM installation](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM tutorials](https://github.com/mlcommons/ck/blob/master/docs/tutorials/README.md)
* [Table of Contents](docs/README.md)



### Motivation

* [CK vision (ACM Tech Talk at YouTube)](https://www.youtube.com/watch?v=7zpeIVwICa4) 
* [CK concepts (Philosophical Transactions of the Royal Society)](https://arxiv.org/abs/2011.01149) 
* [CM workflow automation introduction (slides from ACM REP'23 keynote)](https://doi.org/10.5281/zenodo.8105339)
* [MLPerf inference submitter orientation (slides)](https://doi.org/10.5281/zenodo.8144274) 



Feel free to add the following badge to your projects if it can be accessed and managed by the CM interface and automation workflows:
[![Supported by CM](https://img.shields.io/badge/Supported_by-MLCommons%20CM-blue)](https://github.com/mlcommons/ck).



### Acknowledgments

The MLCommons Collective Mind is being developed by the [MLCommons Task Force on Automation and Reproducibility](docs/taskforce.md)
led by [Grigori Fursin](https://cKnowledge.org/gfursin) and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) 
with many great contributions from [the community](CONTRIBUTING.md).
