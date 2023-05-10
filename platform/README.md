# Collective Knowledge Playground

### Introduction

The [Collective Knowledge Playground (CK)](https://x.cknowledge.org) is a free, open-source, and technology-agnostic on-prem platform
being developed by the [MLCommons task force on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce).
It is intended to connect academia and industry to benchmark, optimize and compare AI, ML and other emerging applications
across diverse and rapidly evolving models, software, hardware and data from different vendors
in terms of costs, performance, power consumption, accuracy, size 
and other metrics in a unified, collaborative, automated, and reproducible way.

This platform is powered by the portable and technology-agnostic [Collective Mind scripting language (MLCommons CM)]( https://github.com/mlcommons/ck/tree/master/cmind )
with [portable and reusable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
developed by the community to solve the "AI/ML dependency hell". CM scripts help to automatically connect 
diverse and continuously changing models, software, hardware, data sets, best practices and optimization techniques 
into end-to-end applications in a transparent and non-intrusive way. 

We thank [the community](https://access.cknowledge.org/playground/?action=contributors) 
for helping us to validate a prototype of the MLCommons CK playground by running and reproducing 
[MLPerf inference v3.0 benchmarks](https://access.cknowledge.org/playground/?action=experiments&tags=mlperf-inference,v3.0,community-submission,open,edge,image-classification,singlestream):
CK has helped to automatically interconnect very diverse technology from Neural Magic, Qualcomm, Krai, cKnowledge, OctoML, Deelvin, DELL, HPE, Lenovo, Hugging Face, Nvidia and Apple 
and run it across diverse CPUs, GPUs and DSPs with PyTorch, 
ONNX, QAIC, TF/TFLite, TVM and TensorRT using popular cloud providers (GCP, AWS, Azure) and individual servers and edge devices 
via our recent [open optimization challenge](https://access.cknowledge.org/playground/?action=challenges&name=optimize-mlperf-inference-v3.0-2023).

### Public GUI

* [Platform preview](https://x.cKnowledge.org)
* [GUI to run MLPerf inference benchmarks](http://cknowledge.org/mlperf-inference-gui)
* [GUI to prepare MLPerf inference submissions](https://cknowledge.org/mlperf-inference-submission-gui)

### Collaborative development

This open-source technology is being developed by the open
[MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
led by [Grigori Fursin](https://cKnowledge.org/gfursin) and
[Arjun Suresh](https://www.linkedin.com/in/arjunsuresh):

* Join our [public Discord server](https://discord.gg/JjWNWXKxwT).
* Join our [public conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw).
* Check our [news](docs/news.md).
* Check our [presentation](https://doi.org/10.5281/zenodo.7871070) with development plans.
* Read about our [CK concept (previous version before MLCommons)](https://arxiv.org/abs/2011.01149).

#### Source code for on-prem use

This platform is implemented as a [portable automation recipe](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui) 
using the MLCommons CM scripting language.

#### Public challenges

Discuss your challenge in Discord, add your challenge [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/challenge)
and create a PR.

#### Private challenges

You can use this platform to organize private challenges between your internal teams and external partners.

Install the MLCommons CK2 (CM) framework as described [here](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Pull CM repository with portable MLOps automation recipes from the community:
```bash
cm pull repo mlcommons@ck
```

Run CK playground GUI on your local machine to aggregate, visualize and reproduce experiments:
```bash
cm run script "gui _playground" 
```

Check [this script](scripts/2-run-in-a-cloud.sh) If you want to run the CK playground 
as a public or private server to run optimization experiments
with your colleagues, external teams and users.


### Copyright

2021-2023 [MLCommons](https://mlcommons.org)

### License

[Apache 2.0](LICENSE.md)

### Acknowledgments

This project is currently supported by [MLCommons](https://mlcommons.org), [cTuning foundation](https://cTuning.org),
[cKnowledge](https://cKnowledge.org) and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.
