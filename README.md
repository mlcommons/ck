[![logo](https://github.com/ctuning/ck-guide-images/blob/master/logo-validated-by-the-community-simple.png)](http://cTuning.org)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
Coverage: [![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

Introduction
============

Collective Knowledge is our "swiss knife" for open, collaborative and reproducible experimentation.
CK is a small, portable and customizable research SDK to
* share artifacts as reusable and indexable Python components with unified JSON API and meta information (programs, benchmarks, data sets, tools, predictive models, etc) - see [Artifact Evaluation website](http://ctuning.org/ae/submission.html) and [Reusable AI artifacts](http://cKnowledge.org/ai); 
* automate detection or installation of all software dependencies on Linux, Windows, MacOS, Android while enabling co-existence of different versions (compilers, benchmarks, libraries, tools) for a given experimental workflow across diverse Linux, Windows and Android based platforms via [CK cross-platform customizable package and environment manager](https://github.com/ctuning/ck/wiki/Portable-workflows);
* quickly prototype experimental workflows from shared components (such as customizable and multi-objective autotuning for DSL, OpenCL, CUDA, MPI, OpenMP and compiler flags) across diverse hardware and software ([CK repo](https://github.com/ctuning/ck-autotuning));
* crowdsource experiments across diverse hardware and workloads provided by volunteers and validate ideas or report unexpected behavior and bugs ([CK repo](https://github.com/ctuning/ck-crowdtuning));
* reuse and collaborative improve JSON description of all existing platforms from IoT to supercomputers ([CK repo](https://github.com/ctuning/ck-crowdtuning-platforms));
* abstract access to continuously evolving software and hardware stack ([CK repo](https://github.com/ctuning/ck-env));
* automate, reproduce and crowdsource empirical experiments using CK JSON-based web services ([live repo](http://cKnowledge.org/repo));
* unify access to predictive analytics (scikit-learn, R, DNN, etc) via unified JSON API and CK web services ([CK repo](https://github.com/ctuning/ck-analytics));
* enable reproducible and interactive articles ([CK repo](https://github.com/ctuning/ck-web)). 

We use CK to gradually develop common API and meta for reproducible computer systems research together with the community and [ACM](https://dl.acm.org/docs/reproducibility.cfm)!

Feel free to [contact us](http://cKnowledge.org/contacts.html) if you need free help to convert your artifacts and workflows to the CK format.

Useful links
============

* [cKnowledge.org - project website with the latest news](http://cKnowledge.org)
* [News archive](https://github.com/ctuning/ck/wiki/News-archive)
* [Practical use cases](http://cKnowledge.org/use_cases.html)
* [CK-powered AI hub](http://cKnowledge.org/ai)
* [Academic and industrial partners](http://cKnowledge.org/partners.html)
* [Documentation including "Getting Started Guide"](https://github.com/ctuning/ck/wiki)
* [CK motivation](https://github.com/ctuning/ck/wiki/Motivation)
* [Development plans](https://github.com/ctuning/ck/wiki/Plans)
* [CK-related publications](https://github.com/ctuning/ck/wiki/Publications)
* [CK-powered open research challenges](https://github.com/ctuning/ck/wiki/Research-and-development-challenges)
* [Previous deprecated version (Collective Mind)](http://c-mind.org)
* [CK Mailing list](https://groups.google.com/forum/#!forum/collective-knowledge)

Reference article
=================
* [Online PDF](https://www.researchgate.net/publication/304010295_Collective_Knowledge_Towards_RD_Sustainability)

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

License
=======
* Permissive 3-clause BSD license. (See `LICENSE.txt` for more details).

Testimonials and awards
=======================
* 2017: [Test of time award for our ACM CGO'07 paper that led to creating CK](http://dividiti.blogspot.com/2017/02/we-received-test-of-time-award-for-our.html)
* 2017: [ARM video about CK-powered optimization of DNN at the Embedded Vision Summit](http://dividiti.blogspot.com/2017/09/video-from-arm-presenting-our.html)
* 2017: [ACM evaluates CK technology to share experimental workflows in Digital Libraries](http://dl.acm.org/docs/reproducibility.cfm)
* 2017: CK-powered experimental workflow from the UCambridge received distinguished artifact award at the CGO'17: [GitHub](https://github.com/SamAinsworth/reproduce-cgo2017-paper), [PDF](http://ctuning.org/ae/resources/paper-with-distinguished-ck-artifact-and-ae-appendix-cgo2017.pdf), [CK dashboard snapshot](https://github.com/SamAinsworth/reproduce-cgo2017-paper/files/618737/ck-aarch64-dashboard.pdf)
* 2016: Imperial College London colleagues won [HiPEAC TT award](https://www.hipeac.net/press/6801/hipeac-tech-transfer-awards-announced) for their CK-based project to crowdsource OpenCL bug detection: [GitHub](https://github.com/ctuning/ck-clsmith);
* 2016: General Motors and dividiti use CK to crowdsource benchmarking and optimization of CAFFE: [public CK repo](https://github.com/dividiti/ck-caffe)
* 2015: ARM and the cTuning foundation use CK to accelerate computer engineering: [HiPEAC Info'45 page 17](https://www.hipeac.net/assets/public/publications/newsletter/hipeacinfo45.pdf), [ARM TechCon'16 presentation and demo](http://schedule.armtechcon.com/session/know-your-workloads-design-more-efficient-systems), [public CK repo](https://github.com/ctuning/ck-wa)
* 2014: [HiPEAC technology transfer award](https://www.hipeac.net/research/technology-transfer-awards/2014)

Acknowledgments
===============

CK development is coordinated by the [cTuning foundation](http://cTuning.org) (non-profit research organization)
and [dividiti](http://dividiti.com). We would like to thank the [EU TETRACOM 609491 Coordination Action](http://tetracom.eu) 
for initial funding, Microsoft for sponsoring hosting of a CK public
repository in the Azure cloud, and all our partners for continuing support.
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

You can now install stable CK version via PIP simply as following
(you may need to prefix it with "sudo" on Linux):

```
$ pip install ck
```

Alternatively, you can install development CK version in your local user space
via GIT as following:

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

However note that the main idea behind CK is to be able to rebuild user experimental workflows
natively, take advantage of the latest software environment and hardware,
and enable open research via collaborative reuse and agile improvement 
of all shared artifacts and workflows.

Practical use cases
===================

See the [list of real use cases](http://cKnowledge.org/use_cases.html) 
by the [growing CK community](http://cKnowledge.org/partners.html).

Questions/comments/discussions?
===============================
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
