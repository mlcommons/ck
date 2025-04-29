[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)
[![arXiv](https://img.shields.io/badge/arXiv-2406.16791-b31b1b.svg)](https://arxiv.org/abs/2406.16791)

[![CMX image classification test](https://github.com/mlcommons/ck/actions/workflows/test-cmx-image-classification-onnx.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cmx-image-classification-onnx.yml)
[![CMX MLPerf inference resnet-50 test](https://github.com/mlcommons/ck/actions/workflows/test-cmx-mlperf-inference-resnet50.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cmx-mlperf-inference-resnet50.yml)
[![CMX MLPerf inference r-GAT test](https://github.com/mlcommons/ck/actions/workflows/test-cmx-mlperf-inference-rgat.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cmx-mlperf-inference-rgat.yml)
[![CMX MLPerf inference BERT deepsparse test](https://github.com/mlcommons/ck/actions/workflows/test-cmx-mlperf-inference-bert-deepsparse-tf-onnxruntime-pytorch.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cmx-mlperf-inference-bert-deepsparse-tf-onnxruntime-pytorch.yml)

## Collective Knowledge project (CK)

[Collective Knowledge (CK)](https://cKnowledge.org) 
is a community-driven project dedicated to supporting open science, enhancing reproducible research, 
and fostering collaborative learning on how to run AI, ML, and other emerging workloads in the most efficient and cost-effective way
across diverse models, data sets, software and hardware:
[ [white paper](https://arxiv.org/abs/2406.16791) ].

It includes the following sub-projects.

### Collective Mind project (MLCommons CM)

The [Collective Mind automation framework (CM)](https://github.com/mlcommons/ck/tree/master/cm)
was developed to support open science and facilitate
collaborative, reproducible, and reusable research, development, 
and experimentation based on [FAIR principles](https://en.wikipedia.org/wiki/FAIR_data).

It helps users non-intrusively convert their software projects 
into file-based repositories of portable and reusable artifacts 
(code, data, models, scripts) with extensible metadata
and reusable automations, a unified command-line interface, 
and a simple Python API.

Such artifacts can be easily chained together into portable 
and technology-agnostic automation workflows, enabling users to 
rerun, reproduce, and reuse complex experimental setups across diverse and rapidly evolving models, datasets,
software, and hardware. 

For example, CM helps to modularize, automate and customize MLPerf benchmarks.

#### Legacy CM API and CLI (2021-2024)

See the [project page](https://github.com/mlcommons/ck/blob/master/cm/README.CM.md) for more details.

Legacy and simplified CM and MLPerf automations were donated to MLCommons by Grigori Fursin, the cTuning foundation and OctoML.
They are now supported by the MLCommons Infra WG (MLCFlow, MLC scripts, mlcr ...).

#### New CM API and CLI (CMX, 2025+)

[Collective Mind eXtension or Common Metadata eXchange (CMX)](https://github.com/mlcommons/ck/tree/master/cmx) 
is the next evolution of the [Collective Mind automation framework (MLCommons CM)](https://github.com/mlcommons/ck/tree/master/cm) 
designed to enhance simplicity, flexibility, and extensibility of automations 
based on user feedback. It is backwards compatible with CM, released along with CM 
in the [cmind package](https://pypi.org/project/cmind/) and can serve as drop-in replacement 
for CM and legacy MLPerf automations while providing a simpler and more robust interface.

See the [project page](https://github.com/mlcommons/ck/tree/master/cmx) 
and [CMX4MLOps automations](https://github.com/mlcommons/ck/tree/master/cmx4mlops) for more details.

### MLOps and MLPerf automations

We have developed a collection of portable, extensible and technology-agnostic automation recipes
with a common CLI and Python API (CM scripts) to unify and automate 
all the manual steps required to compose, run, benchmark and optimize complex ML/AI applications 
on diverse platforms with any software and hardware. 

The two key automations are *script* and *cache*:
see [online catalog at CK playground](https://access.cknowledge.org/playground/?action=scripts),
[online MLCommons catalog](https://docs.mlcommons.org/cm4mlops/scripts).

CM scripts extend the concept of `cmake` with simple Python automations, native scripts
and JSON/YAML meta descriptions. They require Python 3.8+ with minimal dependencies and are 
[continuously extended by the community and MLCommons members](https://github.com/mlcommons/ck/blob/master/CONTRIBUTORS.md)
to run natively on Ubuntu, MacOS, Windows, RHEL, Debian, Amazon Linux
and any other operating system, in a cloud or inside automatically generated containers
while keeping backward compatibility.

See the [online MLPerf documentation](https://docs.mlcommons.org/inference) 
at MLCommons to run MLPerf inference benchmarks across diverse systems using CMX.
Just install `pip install cmx4mlperf` and substitute the following commands and flags:
* `cm` -> `cmx`
* `mlc` -> `cmlc`
* `mlcr` -> `cmlcr`
* `-v` -> `--v`

### Collective Knowledge Playground

[Collective Knowledge Playground](https://access.cKnowledge.org) - 
a unified and open-source platform designed to [index all CM/CMX automations](https://access.cknowledge.org/playground/?action=scripts) 
similar to PYPI and assist users in preparing CM/CMX commands to:

* aggregate, process, visualize, and compare [MLPerf benchmarking results](https://access.cknowledge.org/playground/?action=experiments) for AI and ML systems
* [run MLPerf benchmarks](https://access.cknowledge.org/playground/?action=howtorun)
* organize [open and reproducible optimization challenges and tournaments](https://access.cknowledge.org/playground/?action=challenges). 

### Artifact Evaluation and Reproducibility Initiatives

[Artifact Evaluation automation](https://cTuning.org/ae) - a community-driven initiative 
leveraging CK, CM and CMX to automate artifact evaluation 
and support reproducibility efforts at ML and systems conferences.


## Legacy projects 

* [CM-MLOps](https://github.com/mlcommons/ck/tree/master/cm-mlops) (2021)
* [CM4MLOps](https://github.com/mlcommons/cm4mlops) (2022-2024)
* [CK automation framework v1 and v2](https://github.com/mlcommons/ck/tree/master/ck)


## License

[Apache 2.0](LICENSE.md)

## Copyright

Copyright (c) 2021-2025 MLCommons

Grigori Fursin, the cTuning foundation and OctoML donated this project to MLCommons to benefit everyone.

Copyright (c) 2014-2021 cTuning foundation

## Author

* [Grigori Fursin](https://cKnowledge.org/gfursin)

## Maintainers

* Legacy CM, CM4MLOps and MLPerf automations: [MLCommons infra WG](https://mlcommons.org)
* CMX (the next generation of CM since 2025): [Grigori Fursin](https://cKnowledge.org/gfursin)

## Concepts

To learn more about the motivation behind this project, please explore the following articles and presentations:

* HPCA'25 article "MLPerf Power: Benchmarking the Energy Efficiency of Machine Learning Systems from Microwatts to Megawatts for Sustainable AI": [ [Arxiv](https://arxiv.org/abs/2410.12032) ], [ [tutorial to reproduce results using CM/CMX](https://github.com/aryatschand/MLPerf-Power-HPCA-2025/blob/main/measurement_tutorial.md) ]
* NeuralMagic's vLLM MLPerf inference 4.1 submission automated by CM: [ [README] ](https://github.com/mlcommons/inference_results_v4.1/blob/main/open/NeuralMagic/measurements/4xH100-SXM-80GB_vLLM_FP8-reference-cpu-pytorch-v2.3.1-default_config/llama2-70b-99/server/README.md)
* SDXL MLPerf inference 4.1 submission automated by CM: [ [README] ](https://github.com/mlcommons/inference_results_v4.1/tree/main/open/CTuning/code/stable-diffusion-xl)
* "Enabling more efficient and cost-effective AI/ML systems with Collective Mind, virtualized MLOps, MLPerf, Collective Knowledge Playground and reproducible optimization tournaments": [ [ArXiv](https://arxiv.org/abs/2406.16791) ]
* ACM REP'23 keynote about the MLCommons CM automation framework: [ [slides](https://doi.org/10.5281/zenodo.8105339) ] 
* ACM TechTalk'21 about Collective Knowledge project: [ [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4) ] [ [slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2021/grigorifursin_techtalk_slides.pdf) ]
* Journal of Royal Society'20: [ [paper](https://royalsocietypublishing.org/doi/10.1098/rsta.2020.0211) ]

### Acknowledgments

This open-source project was created by [Grigori Fursin](https://cKnowledge.org/gfursin)
and sponsored by cTuning.org, OctoAI and HiPEAC.
Grigori donated this project to MLCommons to modularize and automate MLPerf benchmarks,
benefit the community, and foster its development as a collaborative, community-driven effort.

We thank [MLCommons](https://mlcommons.org), [FlexAI](https://flex.ai) 
and [cTuning](https://cTuning.org) for supporting this project,
as well as our dedicated [volunteers and collaborators](https://github.com/mlcommons/ck/blob/master/CONTRIBUTORS.md)
for their feedback and contributions!

If you found the CM, CMX and MLPerf automations helpful, kindly reference this article:
[ [ArXiv](https://arxiv.org/abs/2406.16791) ], [ [BibTex](https://github.com/mlcommons/ck/blob/master/citation.bib) ].

You are welcome to contact the [author](https://cKnowledge.org/gfursin) to discuss long-term plans and potential collaboration.
