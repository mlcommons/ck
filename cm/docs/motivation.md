# Motivation

CM is motivated by our tedious experience reproducing [150+ Systems and Machine Learning papers](https://learning.acm.org/techtalks/reproducibility)
and running [MLPerf benchmarks](https://mlcommons.org).

We and our colleagues have to spend many weeks and even months communicating with each other
to understand numerous technical reports, README files, specifications, dependencies, 
ad-hoc scripts, tools, APIs, models and data sets of all shared projects 
to be able to run experiments and [reproduce results and benchmarking numbers](https://cknowledge.io/?q=%22reproduced-papers%22) 
across continuously changing software, hardware and data.

![](https://cKnowledge.org/images/cm-gap-beween-mlsys-research-and-production.png?id=1)

![](https://cKnowledge.org/images/cm-gap-beween-mlsys-research-and-production2a.png)

## Cross-platform meta-framework

This experience motivated us to develop a simple and cross-platform meta-framework
that can help researchers and engineers solve above problems with miminal effort.

Such meta-framework provides a unified CLI, API and extensible meta descriptions to existing artifacts and automation scripts 
to make them more portable, interoperable, deterministic, reusable, reproducible and understandable
with minimal or no changes to existing projects!

Our goal is help users gradually transform their existing projects, Git repositories, Docker containers,
Jupyter notebooks and internal directories into an [open database of portable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
with a common API, extensible meta descriptions and a simple portability and interoperability layer
written in Python or shell scripts.

Such approach helps users to abstract and protect their applications and scripts 
from continuously changing software and hardware.

![](https://cKnowledge.org/images/cm-gap-beween-mlsys-research-and-production3a.png)

## The 2nd generation of the CK framework

The open-source CM meta-framework is the 2nd generation of the [Collective Knowledge framework (CK)]( https://arxiv.org/abs/2011.01149 )
that was [validated in academia and industry]( https://cKnowledge.org/partners.html ) in the past years 
to enable unified, interchangeable, collaborative and reproducible development, optimization and deployment
of Pareto-efficient ML Systems in terms of accuracy, latency, throughput, energy, size and costs
across continuously changing software and hardware.

It helps to transform Git repositories, Docker containers, Jupyter notebooks, zip/tar files
and any local directory into a collective database of reusable artifacts 
and automation scripts with a unified interface and extensible meta descriptions.

Our long-term goal is to make it easier for researchers and engineers to exchange their artifacts, knowledge, 
experience and best practices in a more automated, reusable, portable and unified way
across rapidly evolving computer systems.


See related articles and videos:
* ["MLOps Is a Mess But That's to be Expected" (March 2022)](https://www.mihaileric.com/posts/mlops-is-a-mess)
* ["Reproducing 150 Research Papers and Testing Them in the Real World: Challenges and Solutions" (ACM TechTalk; Feb 2021)](https://learning.acm.org/techtalks/reproducibility)
* ["Automating MLPerf design space exploration and production deployment" (HPCA'22)](https://doi.org/10.5281/zenodo.6475385)
* ["Collaboratively Benchmarking and Optimizing Deep Learning Implementations" (General Motors; Jun 2017)]( https://youtu.be/1ldgVZ64hEI )


## Acknowledgments

We would like to thank [MLCommons](https://mlcommons.org), 
[OctoML](https://octoml.ai), all [contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) 
and [collaborators](https://cKnowledge.org/partners.html) for their support, fruitful discussions, 
and useful feedback! See more acknowledgments in the [CK journal article](https://arxiv.org/abs/2011.01149)
and our [ACM TechTalk](https://www.youtube.com/watch?v=7zpeIVwICa4).
