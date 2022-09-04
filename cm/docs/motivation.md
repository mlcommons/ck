# Motivation

CM is motivated by our tedious experience reproducing [150+ Systems and Machine Learning papers](https://learning.acm.org/techtalks/reproducibility)
when [our colleagues](https://ctuning.org/ae/committee.html) have spent many frustrating months communicating with each other 
and trying to understand numerous technical reports, README files, specifications, dependencies, 
ad-hoc scripts, tools, APIs, models and data sets of all shared projects 
to be able to [validate experimental results](https://cknowledge.io/?q=%22reproduced-papers%22) 
and adapt these projects to the real world with very diverse 
software, hardware, user environments, settings and data sets.

![](https://cKnowledge.org/images/cm-gap-beween-mlsys-research-and-production.png?id=1)

![](https://cKnowledge.org/images/cm-gap-beween-mlsys-research-and-production2a.png)

We have noticed that while there many great automation tools and workflow automation frameworks out there,
some of them are good only for researchers and some are good only for engineers.

## Community effort

The open-source Collective Mind toolkit (CM aka CK2) is our community effort to develop a simple meta-framework 
that can solve above problems and make existing tools easier to use for both researchers and engineers.

CM provides a unified CLI, API and extensible meta descriptions to existing artifacts and automation scripts 
for DevOps and MLOps to make them more portable, interoperable, deterministic, reusable, reproducible and understandable
with minimal or no changes to existing projects!

The CM toolkit helps users gradually transform their existing projects, Git repositories, Docker containers,
Jupyter notebooks and internal directories into an [open database of portable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
with a common API, extensible meta descriptions and a simple portability and interoperability layer
written in Python or shell scripts.

Such evolutionary approach helps to avoid vendor lock-in on specific workflow frameworks and platforms
while simplifying and automating the development, optimization and deployment of complex applications
across rapidly evolving software and hardware stacks from the cloud to the edge.

![](https://cKnowledge.org/images/cm-gap-beween-mlsys-research-and-production3a.png)

## The 2nd generation of the CK framework

The open-source CM unification framework is the 2nd generation of the [Collective Knowledge framework (CK)]( https://arxiv.org/abs/2011.01149 )
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
* ["Collaboratively Benchmarking and Optimizing Deep Learning Implementations" (General Motors; Jun 2017)]( https://youtu.be/1ldgVZ64hEI )
