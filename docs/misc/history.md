[ [Back to index](../README.md) ]

# Motivation

[Collective Knowledge concept (CK)](https://arxiv.org/pdf/2011.01149.pdf) is motivated by our tedious experience reproducing 
[150+ Systems and Machine Learning papers](https://learning.acm.org/techtalks/reproducibility)
and automating [MLPerf benchmarks](https://mlcommons.org).

We have spent many months communicating with researchers and developers
to understand their technical reports, README files, ad-hoc scripts, tools, command lines, APIs,
specifications, dependencies, data formats, models and data 
to be able to [reproduce their experiments](https://cknow.io/?q=%22reproduced-papers%22) 
and reuse their artifacts across continuously changing software, hardware and data.

![](https://cKnowledge.org/images/cm-gap-beween-mlsys-research-and-production.png?id=1)

![](https://cKnowledge.org/images/cm-gap-beween-mlsys-research-and-production2a.png)

## The 1st generation of the CK automation meta-framework

This experience motivated us to develop a simple and cross-platform meta-framework (Collective Knowledge)
that can help researchers and engineers solve above problems by transforming their
projects into a database of portable, reusable and customizable components.

All such components provide a unified CLI, Python API and extensible JSON/YAML meta descriptions to existing artifacts, 
native scripts and workflows to make them more interoperable, deterministic, reusable and reproducible 
across continuously changing software and hardware.

![](https://cKnowledge.org/images/cm-gap-beween-mlsys-research-and-production3a.png)

We have donated the CK framework to the [MLCommons foundation](https://mlcommons.org)
to benefit everyone after it was successfully validated by Qualcomm, Arm, General Motors,
OctoML, Krai, HPE, Dell, Lenovo and [other partners](https://cKnowledge.org/partners.html)  
to enable collaborative and reproducible development, optimization and deployment
of Pareto-efficient ML Systems in terms of accuracy, latency, throughput, energy, size and costs.



After this approach was successfully validated by Qualcomm, Arm, General Motors,
OctoML, Krai, HPE, Dell, Lenovo and other organizations to modularize and automate MLPerf benchmarks,
we have donated our prototype to the [MLCommons foundation](https://mlcommons.org) 
to continue developing it as a community effort.

## The 2nd generation of the CK framework (aka CM)

Collective Mind workflow automation meta-framework (CM aka CK2)  is the 2nd implementation 
of the [CK concept](https://arxiv.org/pdf/2011.01149.pdf) being developed
by the [open MLCommons taskforce on automation and reproducibility](docs/taskforce.md).

This taskforce is using and enhancing CM to modularize ML and AI systems and automate their benchmarking, 
optimization and deployment across continuously changing software, hardware and data.

## Related resources and references

* [Blog article about "MLOps Is a Mess But That's to be Expected" (March 2022)](https://www.mihaileric.com/posts/mlops-is-a-mess)
* [Journal article describing the CK concept](https://arxiv.org/pdf/2011.01149.pdf)
* ["Reproducing 150 Research Papers and Testing Them in the Real World" (ACM TechTalk; Feb 2021)](https://learning.acm.org/techtalks/reproducibility)
* ["Automating MLPerf design space exploration and production deployment" (HPCA'22)](https://doi.org/10.5281/zenodo.6475385)
* ["Collaboratively Benchmarking and Optimizing Deep Learning Implementations" (General Motors; Jun 2017)]( https://youtu.be/1ldgVZ64hEI )
* [MLOps projects, articles and tools](https://github.com/mlcommons/ck/tree/master/cm/docs/KB/MLOps.md)


## Acknowledgments

We would like to thank [MLCommons](https://mlcommons.org), 
[OctoML](https://octoml.ai), all [contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) 
and [collaborators](https://cKnowledge.org/partners.html) for their support, fruitful discussions, 
and useful feedback! See more acknowledgments in the [CK journal article](https://doi.org/10.1098/rsta.2020.0211)
and our [ACM TechTalk](https://www.youtube.com/watch?v=7zpeIVwICa4).
