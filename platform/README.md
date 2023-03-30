# Collective Knowledge Platform

The [Collective Knowledge Playground (CK)](https://x.cknowledge.org) is a free, open-source and technology-agnostic on-prem platform
being developed by the [MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce).

Our goal is to help the community try, reproduce, optimize and compare any novel technology 
including new ML models and end-to-end AI applications across any rapidly evolving software, hardware and data(sets)
in a fully automated way via collaborative challenges.

For example, [the community](https://access.cknowledge.org/playground/?action=contributors) 
has successfully used CK to run and reproduce [MLPerf inference](https://access.cknowledge.org/playground/?action=experiments&tags=mlperf-inference,v3.0,community-submission,open,edge,image-classification,singlestream) 
using very diverse technology from Neural Magic, Qualcomm, Krai, cKnowledge, OctoML, Deelvin, DELL, HPE, Lenovo, Hugging Face, Nvidia and Apple across diverse CPUs, GPUs and DSPs with PyTorch, 
ONNX, QAIC, TF/TFLite, TVM and TensorRT using popular cloud providers (GCP, AWS, Azure) and individual servers and edge devices provided by volunteers
via our recent [open optimization challenge](https://access.cknowledge.org/playground/?action=challenges&name=optimize-mlperf-inference-v3.0-2023).

This platform is powered by the technology-agnostic and portable [MLCommons Collective Mind workflow automation framework (CM or CK2)](https://github.com/mlcommons/ck)
with [portable and reusable automation recipes](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
that we have developed to help the the community solve the "dependency hell" and automatically connect and unify 
their diverse and continuously changing models, software, hardware, data sets, best practices and optimization techniques 
in a transparent and non-intrusive way. 

The ultimate goal for our Collective Knowledge platform is to accelerate deep-tech innovation and make it available to anyone
by automatically generating the most efficient, reproducible and deployable 
full-stack AI/ML solutions using the most suitable SW/HW stack at any given time (model, framework, inference engine and any other related dependency) 
based on their requirements and constraints including costs, throughput, latency, power consumption, accuracy, target devices (cloud/edge/mobile/tiny), 
environment and data. See this [ACM tech talk](https://www.youtube.com/watch?v=7zpeIVwICa4) 
and [article](https://arxiv.org/abs/2011.01149) to learn more about our motivation.

*Note that this is on-going and heavily evolving project - please join our public
 [Discord server](https://discord.gg/JjWNWXKxwT) to brainstorm ideas,
 request new features, add support for your software and hardware,
 and participate in developments and collaborative 
 benchmarking and optimization of AI/ML Systems.*

## License

Apache 2.0

## Copyright

2023 MLCommons

## Source code

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

## Tech leads

* [Grigori Fursin](https://cKnowledge.org/gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)
