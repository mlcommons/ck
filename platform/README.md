# Collective Knowledge Playground

*This project is under heavy development led by the [MLCommons Task Force on Automation and Reproducibility](../docs/taskforce.md),
 [cTuning.org](https://cTuning.org) and [cKnowledge.org](cKnowledge.org) - please join the [public Discord server]() to discuss this project!*



### Introduction

The [Collective Knowledge Playground (CK)](https://access.cknowledge.org) is a free, open-source, and technology-agnostic on-prem platform
being developed by the [MLCommons task force on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce)
to benchmark, optimize and compare AI, ML and other emerging applications
across diverse and rapidly evolving models, software, hardware and data from different vendors
in terms of costs, performance, power consumption, accuracy, size 
and other metrics in a unified, collaborative, automated, and reproducible way.

This platform is powered by the [Collective Mind automation framework (MLCommons CM)](https://github.com/mlcommons/ck)
with [portable, reusable and technology-agnostic automation recipes (CM scripts)](https://access.cknowledge.org/playground/?action=scripts)
developed by the [community](https://access.cknowledge.org/playground/?action=contributors) to solve the "AI/ML dependency hell". 

### Public GUI

* [Platform preview](https://access.cKnowledge.org)
* [GUI to run MLPerf inference benchmarks](http://cknowledge.org/mlperf-inference-gui)
* [GUI to prepare MLPerf inference submissions](https://cknowledge.org/mlperf-inference-submission-gui)



### Collaborative development

#### Source code for on-prem use

This platform is implemented as a [portable automation recipe](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui) 
using the MLCommons CM scripting language.

#### Public challenges

Discuss your challenge in Discord, add your challenge [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/challenge)
and create a PR.


#### Private challenges

You can use this platform to organize private challenges between your internal teams and external partners.

Install the MLCommons CM framework as described [here](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

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


### License

[Apache 2.0](LICENSE.md)
