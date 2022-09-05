# Collective Mind toolkit (CM aka CK2)

[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Downloads](https://pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](https://github.com/mlcommons/ck/tree/master/cm)

[![Documentation](https://img.shields.io/badge/Documentation-available%20online-green)](https://cKnowledge.org/docs/cm)
[![CM(CK2) test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)


There are [many great automation tools and workflow frameworks](https://www.mihaileric.com/posts/mlops-is-a-mess) - 
some are good for researchers and some for engineers. 
The Collective Mind toolkit (CM) is [our community effort](../docs/mlperf-education-workgroup.md) 
to develop a portable meta-framework that is good for both.

CM helps researchers and engineers wrap ad-hoc DevOps and MLOps 
automation scripts and artifacts with a simple, human-readable
and platform-independent CLI, Python API and JSON/YAML meta description
to make them more understandable, portable, reusable, interoperable, deterministic and reproducible
across continuously changing hardware, software and data with minimal or no changes to existing projects.

Such wrappers can be automatically connected together into powerful and portable workflows, applications and web-services
to abstract developers and scientists from the rapidly evolving world of technology.

See an example of a modular image classification assembled from such components 
([portable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)) 
that will automatically detect, download, install and build all related artifacts and 
tools to adapt this workflow to a user platform with Linux, Windows or MacOS:

```bash
python3 -m pip install cmind

cm pull repo mlcommons@ck

cm run script --tags=app,image-classification,onnx,python --quiet
```

or using Python scripting:
```python
import cmind
r=cmind.access({'action':'run', 'automation':'script'
                'tags':['app','image-classification','onnx','python'],
                'quiet':True})
print (r)
```

It may take a few minutes to run this workflow for the first time and adapt it to your platform (depending on the Internet speed).
Note that all the subsequent runs will be much faster because CM automatically caches the output of all portable CM scripts to be quickly reused
in this and other CM workflows.

You can also force to install specific versions of ML artifacts 
(models, data sets, engines, libraries, tools, etc) 
using individual CM scripts to automatically plug them into the above ML task 
(see [image classification dependencies using CM database of scripts](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.json#L9)):

```bash
cm run script --tags=detect,os --out=json
cm run script --tags=get,python --version_min=3.9.1
cm run script --tags=install,python-venv --name=my-virtual-env
cm run script --tags=get,ml-model-onnx,resnet50
cm run script --tags=get,dataset,imagenet,original,_2012-500
cm run script --tags=get,onnxruntime,python-lib --version=1.12.0

cm show cache

cm run script --tags=app,image-classification,onnx,python (--input=my-image.jpg)
```

A few more examples to detect compilers and CUDA devices on Windows:
```bash
cm run script --tags=get,cl --path="C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin"
cm run script --tags=get,cuda --path="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\bin"

cm show cache

cm run script --tags=get,cuda-devices
```


CM is [motivated](docs/motivation.md) by our tedious and interesting experience
[reproducing 150+ ML and systems papers and validating them in the real world](https://learning.acm.org/techtalks/reproducibility)
during different [reproducibility initiatives and artifact evaluation](https://cTuning.org/ae).

The CM toolkit helps researchers and engineers transform their existing projects, Git repositories, Docker containers,
Jupyter notebooks and internal directories into an [open database of portable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
with a common API, extensible meta descriptions and a simple portability and interoperability layer
written in Python or shell scripts.

Such an evolutionary approach helps the community share their knowledge, experience, artifacts and scripts 
in a more unified, automated, portable, reusable and reproducible way while simplifying and automating 
the development and deployment of complex applications across rapidly evolving software and hardware stacks 
from the cloud to the edge.

The CM toolkit is the 2nd generation of the [Collective Knowledge framework (CK)]( https://arxiv.org/abs/2011.01149 )
that was [originally developed in collaboration with companies and universities]( https://cKnowledge.org/partners.html )
to enable collaborative and reproducible development, optimization and deployment
of Pareto-efficient ML Systems in terms of accuracy, latency, throughput, energy, size and costs
across continuously changing software, hardware, user environments, settings, models and data.


# Copyright

[MLCommons](https://mlcommons.org) 2022


# News

* **2022 September 1:** We developed a CM workflow to automate and modularize [MLPerf inference benchmark](docs/tutorial-modular-mlperf.md). 
  We continue these developments within a public [MLPerf education workgroup](../docs/mlperf-education-workgroup.md).

* **2022 July 25:** We updated tutorial about CM scripts: https://github.com/mlcommons/ck/blob/master/cm/docs/tutorial-scripts.md .

* **2022 July 21:** We have pre-released relatively stable scripts for portable DevOps and MLOps at https://github.com/mlcommons/ck/tree/master/cm-mlops/script .

* **2022 May 20:** We brainstormed the minimal set of [portable CM scripts](https://cknowledge.org/docs/cm/tutorial-scripts.html) to automate deployment of ML models across diverse hardware and software at [OctoML](https://OctoML.ai) in Seattle, WA.

* **2022 April 3:** We presented our approach to bridge the growing gap between ML Systems research and production 
  at the HPCA'22 workshop on [benchmarking deep learning systems](https://sites.google.com/g.harvard.edu/mlperf-bench-hpca22/home).

* **2022 March:** We were invited to present our concept to [enable collaborative and reproducible ML Systems R&D](https://meetings.siam.org/sess/dsp_programsess.cfm?SESSIONCODE=73126) 
  at the SIAM'22 workshop on "Research Challenges and Opportunities within Software Productivity, Sustainability, and Reproducibility"

* **2022 March:** We have released the first prototype of [the Collective Mind toolkit (aka CK2)](https://github.com/mlcommons/ck/tree/master/cm)
  based on your feedback and our practical experience [reproducing 150+ ML and Systems papers and validating them in the real world](https://learning.acm.org/techtalks/reproducibility).




# Documentation

* [Online docs](https://cknowledge.org/docs/cm)

# Tutorials

* [Understanding CM automation scripts](https://cknowledge.org/docs/cm/tutorial-scripts.html)
* [Understanding CM database of artifacts](https://cknowledge.org/docs/cm/tutorial-concept.html)







# Community developments

## CM core (database CLI and API)

We use [GitHub tickets](https://github.com/mlcommons/ck/issues) 
prefixed with *[CK2/CM core]* to improve and enhance the CM core 
that helps to organize projects as a collective database 
of reusable artifacts and automation scripts:

## CM automation scripts

CM provides a common playground and a common language to help researchers and engineers
discuss and learn how to connect numerous incompatible tools together and make them 
more deterministic, portable and reproducible across continuously changing software and hardware stacks.
We continue these discussions and developments within our [open workgroup](../docs/mlperf-education-workgroup.md):

* [CM scripts for portable MLOps and DevOps](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
* [CM automations](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation)


# Development meetings

* [Public notes](meetings/)
* [Regular conf-calls](meetings/conf-calls.md)


# Related resources

* [MLOps projects, articles and tools](docs/KB/MLOps.md)

# Contributing

The best way to contribute to this project is to join our [open workgroup](docs/mlperf-education-workgroup.md)
to help the community modularize AI, ML and other complex systems, 
share your ML artifacts and automations as [reusable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
and improve the core CM functionality.

# References

* [Journal article with CK/CM concepts and our long-term vision](https://arxiv.org/pdf/2011.01149.pdf)
* [ACM TechTalk with CK/CM intro moderated by Peter Mattson (MLCommons president)](https://www.youtube.com/watch?v=7zpeIVwICa4)
* [HPCA'22 presentation "MLPerf design space exploration and production deployment"](https://doi.org/10.5281/zenodo.6475385)

# Acknowledgments

We would like to thank [MLCommons](https://mlcommons.org), 
[OctoML](https://octoml.ai), all [contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) 
and [collaborators](https://cKnowledge.org/partners.html) for their support, fruitful discussions, 
and useful feedback! See more acknowledgments in the [CK journal article](https://arxiv.org/abs/2011.01149)
and our [ACM TechTalk](https://www.youtube.com/watch?v=7zpeIVwICa4).

# Maintainers

* [Grigori Fursin](https://cKnowledge.io@gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)

