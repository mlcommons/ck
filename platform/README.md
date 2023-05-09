# Collective Knowledge Platform

*Note that this is on-going and heavily evolving project - please join our public
 [Discord server](https://discord.gg/JjWNWXKxwT) 
 or contact [Grigori Fursin and Arjun Suresh](mailto:gfursin@cKnowledge.org;asuresh@cTuning.org)
 to prepare the 1st open MLPerf inference optimization tournament in spring/summer 2023,
 brainstorm ideas,  request new features, add support for your software and hardware,
 and participate in developments and collaborative 
 benchmarking and optimization of AI/ML Systems.*

The [Collective Knowledge Playground (CK)](https://x.cknowledge.org) is a free, open-source and technology-agnostic on-prem platform
being developed by the [MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce).

Our goal is to let the community benchmark, optimize and compare AI, ML and other emerging applications
across diverse and rapidly evolving models, software, hardware and data from different vendors
in terms of costs, performance, power consumption, accuracy, size 
and other metrics in a unified, collaborative, automated and reproducible way.

This platform is powered by the portable and technology-agnostic [MLCommons Collective Mind automation framework (CM aka CK2)](https://github.com/mlcommons/ck)
with [portable and reusable automation recipes](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
developed by the community to solve the "AI/ML dependency hell" and automatically connect 
diverse and continuously changing models, software, hardware, data sets, best practices and optimization techniques 
into end-to-end applications in a transparent and non-intrusive way. 

We thank [the community](https://access.cknowledge.org/playground/?action=contributors) 
for helping us to validate our prototype by running and reproducing 
[MLPerf inference v3.0 benchmarks](https://access.cknowledge.org/playground/?action=experiments&tags=mlperf-inference,v3.0,community-submission,open,edge,image-classification,singlestream).
CK has helped to automatically interconnect very diverse technology from Neural Magic, Qualcomm, Krai, cKnowledge, OctoML, Deelvin, DELL, HPE, Lenovo, Hugging Face, Nvidia and Apple 
and run it across diverse CPUs, GPUs and DSPs with PyTorch, 
ONNX, QAIC, TF/TFLite, TVM and TensorRT using popular cloud providers (GCP, AWS, Azure) and individual servers and edge devices 
via our recent [open optimization challenge](https://access.cknowledge.org/playground/?action=challenges&name=optimize-mlperf-inference-v3.0-2023).

Our vision for the CK platform is to help researchers, engineers and entrepreneurs 
accelerate innovation by automatically generating the most efficient, reproducible and deployable 
full-stack AI/ML applications using the most suitable software/hardware stack 
at any given time (model, framework, inference engine and any other related dependency) 
based on their requirements and constraints including costs, throughput, latency, power consumption, accuracy, target devices (cloud/edge/mobile/tiny), 
environment and data while slashing their development and operational costs by 10..100 times.

See this [ACM tech talk](https://www.youtube.com/watch?v=7zpeIVwICa4) 
and [journal article](https://arxiv.org/abs/2011.01149) to learn more about our motivation.

## Links

* [Platform preview](https://x.cKnowledge.org)
* [GUI to run MLPerf inference benchmarks](http://cknowledge.org/mlperf-inference-gui)
* [GUI to prepare MLPerf inference submissions](https://cknowledge.org/mlperf-inference-submission-gui)

## Source code for on-prem use

This platform is implemented as a portable automation recipe using the MLCommons CM (CK2) workflow automation framework: 
https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui

## Use cases

### Public challenges

Discuss your challenge in Discord, add your challenge [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/challenge)
and create a PR.

### Private challenges

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



### Documentation and the Getting Started Guide

[Table of contents](https://github.com/mlcommons/ck/tree/master/docs/README.md)

### Discussions

* Join our [public Discord server](https://discord.gg/JjWNWXKxwT).
* Join our [public conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw).
* Check our [news](docs/news.md).

### Collaborative development

This open-source technology is being developed by the open
[MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
led by [Grigori Fursin](https://cKnowledge.org/gfursin) and
[Arjun Suresh](https://www.linkedin.com/in/arjunsuresh).

### Copyright

2021-2023 [MLCommons](https://mlcommons.org)

### License

[Apache 2.0](LICENSE.md)

### Acknowledgments

This project is currently supported by [MLCommons](https://mlcommons.org), [cTuning foundation](https://cTuning.org),
[cKnowledge](https://cKnowledge.org) and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.
