[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
Coverage: [![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

NEWS
====
* ARM uses CK as a front-end for systematic and reproducible benchmarking and tuning of real workloads: [GitHub](https://github.com/ctuning/ck-wa), [ARM TechCon'16 presentation](http://schedule.armtechcon.com/session/know-your-workloads-design-more-efficient-systems); 
* CK-powered open challenges in computer engineering have been updated: [link](https://github.com/ctuning/ck/wiki/Research-and-development-challenges);
* Fully updated documentation is now available: [Wiki](http://github.com/ctuning/ck/wiki), [Getting Started Guide](http://github.com/ctuning/ck/wiki/Getting-started-guide), [Portable workflows](http://github.com/ctuning/ck/wiki/Portable-workflows);
* We have moved Open Science resources [here](http://github.com/ctuning/ck/wiki/Enabling-Open-Science);
* We have added continuous integration for Linux and Windows;
* General Motors and dividiti shared CK workflow to crowdsource benchmarking and optimization of CAFFE (DNN framework) [here](https://github.com/dividiti/ck-caffe);
* CK supports [Jupyter notebooks](http://jupyter.org) and [Docker](http://github.com/ctuning/ck-docker);
* cTuning foundation and ARM has received [HiPEAC technology transfer award](https://www.hipeac.net/research/technology-transfer-awards/2014) for the CK concept.

Introduction
============

Collective Knowledge is our "swiss knife" for open, collaborative and reproducible experimentation.
CK is a small, portable and customizable research platform to
* share artifacts as reusable and indexable Python components with unified JSON API and meta information (programs, benchmarks, data sets, tools, predictive models, etc); 
* quickly prototype experimental workflows from shared components (such as customizable and multi-objective autotuning for DSL, OpenCL, CUDA, MPI, OpenMP and compiler flags);
* crowdsource experiments across diverse hardware and workloads provided by volunteers, and report "interesting" or unexpected behavior;
* unify and abstract access to continuously evolving software across Windows, Linux and Android (tools, programs, libraries);
* use the latest environment for experiments (rather than using quickly outdated virtual images);
* automate, reproduce and crowdsource empirical experiments (using CK JSON-based web services);
* unify access to predictive analytics via unified JSON API and CK web services (scikit-learn, R, DNN, etc);
* enable reproducible and interactive articles. 

Project homepage: 
* http://cknowledge.org
* http://cTuning.org

License
=======
* Permissive 3-clause BSD license. (See `LICENSE.txt` for more details).

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

Experiment crowdsourcing example
================================

You can now test CK by pulling and executing one of multiple shared research scenarios.

```
 $ ck pull repo:ck-crowdtuning
 $ ck crowdsource experiment
```

For example, you can execute shared workflow for collaborative program optimization
with all related artifacts, and start participating in multi-objective crowdtuning 
simply as following: 

```
 $ ck crowdtune program
```

You can also crowd-tune GCC on Windows as following:
```
 $ ck crowdtune program --gcc --target_os=mingw-64
```

If you have GCC or LLVM compilers installed, you can start continuously crowd-tune 
their optimization heuristics in a quiet mode (for example overnight) via

```
$ ck crowdtune program --llvm --quiet
$ ck crowdtune program --gcc --quiet
```

This experimental workflow will be optimizing different shared workloads
for multiple objectives (execution time, code size, energy, compilation time, etc)
using all exposed design and optimization knobs, while sending best performing 
optimizations to the public CK-based server:

* http://cTuning.org/crowd-results
* http://cknowledge.org/interactive-report

CK server will, in turn, perform on-line learning to classify optimization 
versus workloads which can be useful for compiler/hardware designers and 
performance engineers (described in more detail in http://arxiv.org/abs/1506.06256 ).

You can even participate in collaborative experiments using your Android mobile phone
by installing the following application from the Google Play Store:

* https://play.google.com/store/apps/details?id=openscience.crowdsource.experiments

You can find already shared artifacts and repositories here:
* List of shared repositories: https://github.com/ctuning/ck/wiki/Shared-repos
* List of shared modules: https://github.com/ctuning/ck/wiki/Shared-modules

Please check out CK getting started guides and CK wiki for further details:
* https://github.com/ctuning/ck/wiki/Getting-started-guide
* https://github.com/ctuning/ck/wiki/Portable-workflows
* https://github.com/ctuning/ck/wiki

Trying CK using Docker image
============================

If you would like to try CK without installing it, 
you can run the following Docker image:

```
 $ docker run -it ctuning/ck
```

However, the idea of CK is to be able to rebuild user experimental workflows
natively to take advantage of the latest software environment.

Also note that we added Docker automation to CK (to help 
evaluate artifacts at the conferences, share interactive 
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

Testing CK
==========
You can test CK functionality via
```
 $ ck run test
```

Our related initiatives
=======================

* Artifact Evaluation for computer systems' conferences: http://cTuning.org/ae
* New publication model with the community-driven public reviewing: http://adapt-workshop.org

Plans
===================
* https://github.com/ctuning/ck/wiki/Plans

Motivation
==========
* https://github.com/ctuning/ck/wiki/Motivation

Authors
=======
* Grigori Fursin, http://fursin.net
* Anton Lokhmotov, https://www.hipeac.net/~anton

Questions/comments/discussions?
===============================
* Public wiki with open challenges in computer engineering:
  https://github.com/ctuning/ck/wiki/Research-and-development-challenges
* Mailing list for open, collaborative and reproducible R&D including knowledge preservation, sharing and reuse:
  http://groups.google.com/group/collective-knowledge
* Mailing list for software and hardware multi-objective (performance/energy/accuracy/size/reliability/cost)
  benchmarking, autotuning, crowdtuning and run-time adaptation: http://groups.google.com/group/ctuning-discussions

Publications
============
The concepts have been described in the following publications:

* http://arxiv.org/abs/1506.06256 (CPC'15)
* http://tinyurl.com/zyupd5v (DATE'16)
* http://hal.inria.fr/hal-01054763 (Journal of Scientific Programming'14)

* http://bit.ly/ck-multiprog16 (MULTIPROG'16)
* http://cknowledge.org/interactive-report
* http://arxiv.org/abs/1406.4020 (TRUST'14 @ PLDI'14)
* https://hal.inria.fr/inria-00436029 (GCC Summit'09)

If you found CK useful, feel free to reference 
any of the above publications. You can download 
all above references in one BibTex file 
[here](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/collective-knowledge-refs.bib).

Testimonials and awards
=======================
* 2016: General Motors and dividiti use CK to crowdsource benchmarking and optimization of CAFFE: [public CK repo](https://github.com/dividiti/ck-caffe)
* 2015: ARM and the cTuning foundation use CK to accelerate computer engineering: [HiPEAC Info'45 page 17](https://www.hipeac.net/assets/public/publications/newsletter/hipeacinfo45.pdf), [ARM TechCon'16 presentation and demo](http://schedule.armtechcon.com/session/know-your-workloads-design-more-efficient-systems), [public CK repo](https://github.com/ctuning/ck-wa)
* 2014: HiPEAC technology transfer award: [HiPEAC TT winners](https://www.hipeac.net/research/technology-transfer-awards/2014)

Acknowledgments
===============

CK development is coordinated by the [cTuning
foundation](http://cTuning.org) (non-profit research organization). 
We thank the [EU TETRACOM 609491 Coordination
Action](http://tetracom.eu) for initial funding and
[dividiti](http://dividiti.com) for continuing support. We would also like to
thank Microsoft Research program for one-year grant to host the CK public
repository in the Azure cloud.  We are also extremely grateful to all
volunteers for their valuable feedback and contributions.

![logo](https://github.com/ctuning/ck-guide-images/blob/master/logo-validated-by-the-community-simple.png)
