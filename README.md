[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
Coverage: [![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

Introduction
============

We are developing the Collective Knowledge framework (CK)
to enable collaborative, reproducible and sustainable 
research and experimentation particularly at [systems and ML/AI conferences](http://cTuning.org/ae)
based on agile, DevOps and Wikipedia principles.
After a growing number of [use cases](http://cKnowledge.org/use_cases.html),
we decided to continue it as a community effort to help
researchers and developers:

* share artifacts as portable, customizable and reusable Python plugins with a unified JSON API and meta information (programs, benchmarks, data sets, libraries, tools, predictive models, etc);
* quickly prototype research workflows from shared artifacts (such as [customizable, multi-objective and input-aware autotuning](https://hal.inria.fr/hal-01054763) and [crowdsource/reproduce/build upon various experiments](http://cKnowledge.org/repo) across diverse hardware and software stack provided by volunteers;
* make benchmarks and research workflows portable, customizable and adaptable to any platform with Linux, Windows, MacOS and Android using
[CK cross-platform customizable package and environment manager](https://github.com/ctuning/ck/wiki/Portable-workflows);
* [unify access to predictive analytics](http://cKnowledge.org/ai) (TensorFlow, Caffe, scikit-learn, R, DNN, etc) via unified CK JSON API and CK web service;
* enable reproducible, interactive and "live" articles (see [example](http://cKnowledge.org/rpi-crowd-tuning)); 
* automate [Artifact Evaluation](http://cTuning.org/ae) at systems and ML conferences;
* support open, reproducible and multi-objective benchmarking, optimization and co-design competitions for the whole AI/SW/HW stack (see [ACM ReQuEST tournaments](http://cKnowledge.org/request)). 

We collaborate with [the CK community](http://cKnowledge.org/partners.html), 
[Systems/ML/AI conferences](http://cTuning.org/ae), 
[reproducible tournaments](http://cKnowledge.org/request) and [ACM](https://dl.acm.org/docs/reproducibility.cfm) 
to gradually standardize APIs and meta description of all shared artifacts and workflows, 
and enable [open, reproducible and reusable research]( https://slideshare.net/GrigoriFursin/enabling-open-and-reproducible-computer-systems-research-the-good-the-bad-and-the-ugly).

CK resources
============

* [cKnowledge.org - project website with the latest news](http://cKnowledge.org)
* [Academic and industrial partners with their use-cases](http://cKnowledge.org/partners.html)
* [CK documentation including "Getting Started Guide"](https://github.com/ctuning/ck/wiki)
  * [Shared CK repositories](https://github.com/ctuning/ck/wiki/Shared-repos)
  * [Shared CK modules (plugins)](https://github.com/ctuning/ck/wiki/Shared-modules)
  * [Shared software detection plugins](https://github.com/ctuning/ck/wiki/Shared-soft-descriptions)
  * [Shared CK packages to automate installation of workflows across diverse platforms](https://github.com/ctuning/ck/wiki/Shared-packages)
* [Reproducible SW/HW co-design competitions for deep learning and other emerging workloads using CK](http://cKnowledge.org/request)
* [Live Scoreboard with results from crowd-sourced experiments such as SW/HW co-design of deep learning](http://cKnowledge.org/repo)
* [CK-powered AI benchmarking and optimization](http://cKnowledge.org/ai)
* [CK-related publications](https://github.com/ctuning/ck/wiki/Publications)
* [CK Mailing list](https://groups.google.com/forum/#!forum/collective-knowledge)
* [CK slack](https://collective-knowledge.slack.com)

Citing CK
=========

```
@inproceedings{ck-date16,
    title = {{Collective Knowledge}: towards {R\&D} sustainability},
    author = {Fursin, Grigori and Lokhmotov, Anton and Plowman, Ed},
    booktitle = {Proceedings of the Conference on Design, Automation and Test in Europe (DATE'16)},
    year = {2016},
    month = {March},
    url = {https://www.researchgate.net/publication/304010295_Collective_Knowledge_Towards_RD_Sustainability}
}
```

```
@inproceedings{cm:29db2248aba45e59:c4b24bff57f4ad07,
   author = {{Fursin}, Grigori and {Lokhmotov}, Anton and {Savenko}, Dmitry and {Upton}, Eben},
    title = "{A Collective Knowledge workflow for collaborative research into multi-objective autotuning and machine learning techniques}",
  journal = {ArXiv e-prints},
archivePrefix = "arXiv",
   eprint = {1801.08024},
 primaryClass = "cs.CY",
 keywords = {Computer Science - Computers and Society, Computer Science - Software Engineering},
     year = 2018,
    month = jan,
    url = {https://arxiv.org/abs/1801.08024},
   adsurl = {http://adsabs.harvard.edu/abs/2018arXiv180108024F}
}

```

Some ideas were also originally presented in this [2009 paper](https://hal.inria.fr/inria-00436029).

Getting first feeling about portable and customizable benchmarking
==================================================================

* [Getting Started Guide](https://github.com/ctuning/ck/wiki/First-feeling) 

Minimal installation
====================

The minimal installation requires:

* Python 2.7 or 3.3+ (limitation is mainly due to unitests)
* Python PIP (if you would like to install CK via PIP)
* Git command line client.

On Ubuntu, you can install these dependencies via

```
$ apt-get install -y python python-pip git
```

On Windows, you can download and install these tools from the following sites:

* Git: https://git-for-windows.github.io
* Minimal Python: https://www.python.org/downloads/windows
* Anaconda scientific Python with all packages: https://www.continuum.io/downloads#_windows

You can now install a stable CK version via PIP simply as following
(you may need to prefix it with "sudo" on Linux):

```
$ pip install ck
```

Alternatively, you can install a development CK version 
in your local user space via GIT as following:

```
 $ git clone https://github.com/ctuning/ck.git ck
```
and then add CK to PATH on Linux as following:
```
 $ export PATH=$PWD/ck/bin:$PATH
```
or on Windows as following:

```
 $ set PATH={CURRENT PATH}\ck\bin;%PATH%
```

Further installation details can be found [here](https://github.com/ctuning/ck/wiki/Getting-started-guide#Quick_CK_installation).

Practical use cases
===================

See the [list of real use cases](http://cKnowledge.org/partners.html) 
by our academic and industrial partners.

Trying CK using Docker image
============================

You can try CK using the following Docker image:

```
 $ (sudo) docker run -it ctuning/ck
```

Note that we added Docker automation to CK to help evaluate 
artifacts at the conferences, share interactive 
and reproducible articles, crowdsource experiments and so on.

For example, you can participate in GCC or LLVM crowd-tuning on your machine
simply as following:
```
 $ (sudo) docker run ck-crowdtune-gcc
 $ (sudo) docker run ck-crowdtune-llvm
```

You can then browse top shared optimization results on the live CK scoreboard: http://cKnowledge.org/repo

Open ACM ReQuEST tournaments are now using our approach and technology 
to co-design efficient SW/HW stack for deep learning and other emerging workloads: http://cKnowledge.org/request

You can also download and view one of our CK-based interactive and reproducible articles as following:
```
 $ ck pull repo:ck-docker
 $ ck run docker:ck-interactive-article --browser (--sudo)
```

See the list of other CK-related Docker images [here](https://hub.docker.com/u/ctuning).

However note that the main idea behind CK is to let the community collaboratively
improve common experimental workflows while making them 
[adaptable to latest environments and hardware](https://github.com/ctuning/ck/wiki/Portable-workflows),
and gradually fixing reproducibility issues as described [here](http://cknowledge.org/rpi-crowd-tuning)!

Discussions/questions/comments
==============================
* Slack channel: https://collective-knowledge.slack.com ; please send an email to admin@cTuning.org with a subject "invitation to the CK Slack channel" to get an invite
* Mailing list about CK, common experimental workflows and artifact/workflows sharing, customization and reuse:
  http://groups.google.com/group/collective-knowledge
* Mailing list related to collaborative optimization and co-design of efficient SW/HW stack for emerging workloads:
  http://groups.google.com/group/ctuning-discussions
* Public wiki with CK-powered open challenges in computer engineering:
  https://github.com/ctuning/ck/wiki/Research-and-development-challenges

CK authors
==========
* [Grigori Fursin](http://fursin.net/research.html), cTuning foundation / dividiti
* [Anton Lokhmotov](https://www.hipeac.net/~anton), dividiti

License
=======
* Permissive 3-clause BSD license. (See `LICENSE.txt` for more details).

Acknowledgments
===============

CK development is coordinated by the [cTuning foundation](http://cTuning.org) (non-profit research organization)
and [dividiti](http://dividiti.com). We would like to thank the [TETRACOM 609491 Coordination Action](http://tetracom.eu) 
for initial funding and [all our partners](http://cKnowledge.org/partners.html) for continuing support. 
We are also extremely grateful to all volunteers for their valuable feedback and contributions.
