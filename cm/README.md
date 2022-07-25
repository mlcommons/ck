# Collective Mind toolkit (CM aka CK2)

[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Downloads](https://pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](https://github.com/mlcommons/ck/tree/master/cm)

The Collective Mind toolkit helps you to add and share [simple, human-readable  
and platform-independent CLI and JSON API](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) 
to existing DevOps and MLOps automation scripts and artifacts to make them more understandable, portable, reusable, interoperable, deterministic and reproducible
across continuously changing hardware, software and data with minimal or no changes to existing projects.

See an example of CM-based image classification that can run natively on any user platform with Linux, Windows and MacOS
while automatically adapting to a given software, hardware and data:

```
python3 -m pip install cmind
cm pull repo mlcommons@ck
cm run script --tags=detect,os --out=json
cm run script --tags=get,python --name=my-virtual-env
cm run script --tags=install,python-venv --name=my-virtual-env
cm run script --tags=get,ml-model-onnx,resnet50
cm run script --tags=get,dataset,imagenet,original,_2012-500
cm show cache
cm run script --tags=get,python --version=3.9.6
cm run script --tags=app,image-classification,onnx,python (--input=my-image.jpg)
```

CM is [motivated](docs/motivation.md) by our tedious and interesting experience
[reproducing 150+ ML and systems papers and validating them in the real world](https://learning.acm.org/techtalks/reproducibility)
during so-called [artifact evaluation](https://cTuning.org/ae).

The CM toolkit helps users to gradually transform their existing projects, Git repositories, Docker containers,
Jupyter notebooks and internal directories into an [open database of portable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
with a common API, extensible meta descriptions and a simple portability and interoperability layer
written in Python or shell scripts.

Such an evolutionary approach makes it easier to share ML, AI and other artifacts, knowledge and experience in a more unified, automated, portable, 
reusable and reproducible way while simplifying and automating the development and deployment of complex applications
across rapidly evolving software and hardware stacks from the cloud to the edge.

The CM toolkit is the 2nd generation of the [Collective Knowledge framework (CK)]( https://arxiv.org/abs/2011.01149 )
that was [originally validated in academia and industry in the past few years]( https://cKnowledge.org/partners.html )
to enable collaborative and reproducible development, optimization and deployment
of Pareto-efficient ML Systems in terms of accuracy, latency, throughput, energy, size and costs
across continuously changing software, hardware, user environments, settings, models and data.



# News

* **2022 July 25:** We updated tutorial about CM scripts: https://github.com/mlcommons/ck/blob/master/cm/docs/tutorial-scripts.md .

* **2022 July 21:** We have pre-released relatively stable scripts for portable DevOps and MLOps at https://github.com/mlcommons/ck/tree/master/cm-mlops/script .

* **2022 May 20:** We brainstormed the minimal set of [portable CM scripts](https://cknowledge.org/docs/cm/tutorial-scripts.html) to automate deployment of ML models across diverse hardware and software at [OctoML](https://OctoML.ai) in Seattle, WA.

* **2022 April 3:** We presented our approach to bridge the growing gap between ML Systems research and production 
  at the HPCA'22 workshop on [benchmarking deep learning systems](https://sites.google.com/g.harvard.edu/mlperf-bench-hpca22/home).

* **2022 March:** We were invited to present our concept to [enable collaborative and reproducible ML Systems R&D](https://meetings.siam.org/sess/dsp_programsess.cfm?SESSIONCODE=73126) 
  at the SIAM'22 workshop on "Research Challenges and Opportunities within Software Productivity, Sustainability, and Reproducibility"

* **2022 March:** We have released the first prototype of [the Collective Mind toolkit (aka CK2)](https://github.com/mlcommons/ck/tree/master/cm)
  based on your feedback and our practical experience [reproducing 150+ ML and Systems papers and validating them in the real world](https://learning.acm.org/techtalks/reproducibility).



# License

Apache 2.0



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
discuss and learn how to [make benchmarking, optimization, co-design and deployment 
of complex ML Systems](https://www.mihaileric.com/posts/mlops-is-a-mess) more deterministic, portable and reproducible across
continuously changing software and hardware stacks:

* [CM scripts for portable MLOps and DevOps](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
* [CM automations](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation)


## Development meetings

* [Public notes](meetings/)
* [Regular conf-calls](meetings/conf-calls.md)


# Related resources

* [MLOps projects, articles and tools](docs/KB/MLOps.md)


# Acknowledgments

We thank the [users and partners of the original CK framework](https://cKnowledge.org/partners.html), 
[OctoML](https://octoml.ai), [MLCommons](https://mlcommons.org) 
and all our colleagues for their valuable feedback and support!


# Contacts

* [Grigori Fursin](https://cKnowledge.io/@gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)
