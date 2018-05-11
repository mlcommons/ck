[![logo](https://github.com/ctuning/ck-guide-images/blob/master/logo-validated-by-the-community-simple.png)](http://cTuning.org)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
Coverage: [![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

Introduction
============

We are developing the Collective Knowledge framework (CK)
to enable collaborative, reproducible, sustainable and agile
research and experimentation for [our partners](http://cKnowledge.org/partners.html)
and to automate [Artifact Evaluation at systems and ML/AI conferences](http://cTuning.org/ae)
based on Wikipedia and DevOps principles.
After a growing number of [use cases](http://cKnowledge.org/use_cases.html),
we decided to continue it as a community effort to help
researchers and developers:

* share their artifacts as portable, customizable and reusable Python plugins with a unified JSON API and meta information (programs, benchmarks, data sets, libraries, tools, predictive models, etc);
* quickly prototype research workflows from shared artifacts (such as [customizable, multi-objective and input-aware autotuning](https://hal.inria.fr/hal-01054763) and [crowdsource/reproduce/build upon various experiments](http://cKnowledge.org/repo) across diverse hardware and software stack provided by volunteers;
* make their research workflows portable and adaptable to any platform with Linux, Windows, MacOS and Android using
[CK cross-platform customizable package and environment manager](https://github.com/ctuning/ck/wiki/Portable-workflows);
* [unify access to predictive analytics](http://cKnowledge.org/ai) (TensorFlow, Caffe, scikit-learn, R, DNN, etc) via unified CK JSON API and CK web service;
* enable reproducible, interactive and "live" articles (see [example](http://cKnowledge.org/rpi-crowd-tuning)); 
* support [Artifact Evaluation](http://cTuning.org/ae) at systems and ML conferences;
* support open, reproducible and multi-objective benchmarking, optimization and co-design competitions for the whole AI/SW/HW stack (see [ReQuEST](http://cKnowledge.org/request)). 

We collaborate with [the CK community](http://cKnowledge.org/partners.html), [Systems/ML/AI conferences](http://cTuning.org/ae), 
[reproducible tournaments](http://cKnowledge.org/request) and [ACM](https://dl.acm.org/docs/reproducibility.cfm) 
to gradually standardize APIs and meta description of all shared artifacts and workflows, 
and enable [open, reproducible and reusable research]( https://slideshare.net/GrigoriFursin/enabling-open-and-reproducible-computer-systems-research-the-good-the-bad-and-the-ugly).

CK resources
============

* [cKnowledge.org - project website with the latest news](http://cKnowledge.org)
* [Academic and industrial partners with their use-cases](http://cKnowledge.org/partners.html)
* [CK documentation including "Getting Started Guide"](https://github.com/ctuning/ck/wiki)
  * [Shared CK repositories](https://github.com/ctuning/ck/wiki/Shared-repos)
  * [Shared CK plugins](https://github.com/ctuning/ck/wiki/Shared-modules)
  * [Shared software detection plugins](https://github.com/ctuning/ck/wiki/Shared-soft-descriptions)
  * [Shared CK packages to automate installation of workflows across diverse platforms](https://github.com/ctuning/ck/wiki/Shared-packages)
* [Reproducible SW/HW co-design competitions for deep learning and other emerging workloads using CK](http://cKnowledge.org/request)
* [CK-powered AI hub](http://cKnowledge.org/ai)
* [CK-related publications]( https://github.com/ctuning/ck/wiki/Publications )
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

License
=======
* Permissive 3-clause BSD license. (See `LICENSE.txt` for more details).

Testimonials and awards
=======================
* 2017: [Test of time award for our ACM CGO'07 paper that led to creating CK](http://dividiti.blogspot.com/2017/02/we-received-test-of-time-award-for-our.html)
* 2017: [ARM video about CK-powered optimization of DNN at the Embedded Vision Summit](http://dividiti.blogspot.com/2017/09/video-from-arm-presenting-our.html)
* 2017: [ACM evaluates CK technology to share experimental workflows in Digital Libraries](http://dl.acm.org/docs/reproducibility.cfm)
* 2017: CK-powered experimental workflow from the UCambridge received a distinguished artifact award at the CGO'17: [GitHub](https://github.com/SamAinsworth/reproduce-cgo2017-paper), [PDF](http://ctuning.org/ae/resources/paper-with-distinguished-ck-artifact-and-ae-appendix-cgo2017.pdf), [CK dashboard snapshot](https://github.com/SamAinsworth/reproduce-cgo2017-paper/files/618737/ck-aarch64-dashboard.pdf)
* 2016: Imperial College London colleagues won [HiPEAC TT award](https://www.hipeac.net/press/6801/hipeac-tech-transfer-awards-announced) for their CK-based project to crowdsource OpenCL bug detection: [GitHub](https://github.com/ctuning/ck-clsmith);
* 2016: General Motors and dividiti use CK to crowdsource benchmarking and optimization of CAFFE: [public CK repo](https://github.com/dividiti/ck-caffe)
* 2015: ARM and the cTuning foundation use CK to accelerate computer engineering: [HiPEAC Info'45 page 17](https://www.hipeac.net/assets/public/publications/newsletter/hipeacinfo45.pdf), [ARM TechCon'16 presentation and demo](http://schedule.armtechcon.com/session/know-your-workloads-design-more-efficient-systems), [public CK repo](https://github.com/ctuning/ck-wa)
* 2014: [HiPEAC technology transfer award](https://www.hipeac.net/research/technology-transfer-awards/2014)

Acknowledgments
===============

CK development is coordinated by the [cTuning foundation](http://cTuning.org) (non-profit research organization)
and [dividiti](http://dividiti.com). We would like to thank the [EU TETRACOM 609491 Coordination Action](http://tetracom.eu) 
for initial funding, Microsoft for sponsoring the hosting of a [public CK optimization repository](http://cKnowledge.org/repo) in the Azure cloud, and [all our partners](http://cKnowledge.org/partners.html) for continuing support. 
We are also extremely grateful to all volunteers for their valuable feedback and contributions.

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

Getting first feeling about portable and customizable benchmarking
==================================================================

* [Getting Started Guide](https://github.com/ctuning/ck/wiki/First-feeling) 


Trying CK using Docker image
============================

If you would like to try CK without installing it, 
you can run the following Docker image:

```
 $ docker run -it ctuning/ck
```

Also note that we added Docker automation to CK 
(to help evaluate artifacts at the conferences, share interactive 
and reproducible articles or crowdsource experiments for example). 

Please check 'ck-docker' repository at GitHub:

```
 $ ck show repo:ck-docker
```

You can download and view one of our CK-based interactive and reproducible articles as following:
```
 $ ck pull repo:ck-docker
 $ ck run docker:ck-interactive-article --browser (--sudo)
```

See the list of other CK-related Docker images [here](https://hub.docker.com/u/ctuning).

However note that the main idea behind CK is to make experimental workflows
and artifacts [adaptable to any latest user environment and hardware](https://github.com/ctuning/ck/wiki/Portable-workflows).
Thus, rather than just being archived, they can be continuously reused,
customized, improved and built upon based on Wikipedia and DevOps principles!

Practical use cases
===================

See the [list of real use cases](http://cKnowledge.org/partners.html) 
by our academic and industrial partners.

Discussions/questions/comments
==============================
* Slack channel: https://collective-knowledge.slack.com ; to get an invitation please send an email to admin@cTuning.org with a subject "invitation to the CK Slack channel"
* Mailing list for open, collaborative and reproducible R&D including knowledge preservation, sharing and reuse:
  http://groups.google.com/group/collective-knowledge
* Mailing list for software and hardware multi-objective (performance/energy/accuracy/size/reliability/cost)
  benchmarking, autotuning, crowdtuning and run-time adaptation: http://groups.google.com/group/ctuning-discussions
* Public wiki with CK-powered open challenges in computer engineering:
  https://github.com/ctuning/ck/wiki/Research-and-development-challenges

CK authors
==========
* [Grigori Fursin](http://fursin.net/research.html), cTuning foundation / dividiti
* [Anton Lokhmotov](https://www.hipeac.net/~anton), dividiti
