[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
Coverage: [![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

Introduction
============

We believe in the power of collaborative, systematic and reproducible R&D to solve the World's most challenging problems!

We created Collective Knowledge (CK) as an open-source workflow framework 
to speed up collaborative and reproducible R&D with reusable, customizable,
portable and non-virtualized components. 
Trusted by a growing number of [academic and industrial partners](http://cKnowledge.org/partners.html),
CK helps to automate [artifact evaluation](http://cTuning.org/ae) 
and accelerate complex experiments such as benchmarking, co-design and optimization 
of the whole SW/HW stack for [AI/ML](http://cKnowledge.org/ai.html).
Give it [a try](https://github.com/ctuning/ck/wiki/First-steps)!

Note that CK is basically a low-level collection of unified APIs
shared via Git(Hub) and accessible from the command line or from
Python and other languages. The community can integrate CK 
with their own local and cloud projects, or develop more user-friendly 
front-ends similar to [Overleaf web front-end](https://www.overleaf.com/)
for [LaTeX](https://www.latex-project.org/) or [GitHub](https://github.com) 
and [TortoiseGit GUI](https://tortoisegit.org) for [Git projects](https://git-scm.com/).
For example, see [web front-end for live CK repository](http://cKnowledge.org/repo)
and this [GUI for CK-based DNN crowd-benchmarking](https://github.com/dividiti/ck-crowdsource-dnn-optimization).

CK framework is based on agile, DevOps, [FAIR](https://www.nature.com/articles/sdata201618) and Wikipedia principles helping users to:

* decompose complex software projects with ad-hoc scripts into portable, customizable and reusable components and workflows (<a href="http://cKnowledge.org/shared-packages.html">packages</a>, <a href="http://cKnowledge.org/shared-soft-detection-plugins.html">software detection plugins</a>, <a href="http://cKnowledge.org/shared-modules.html">modules</a> and <a href="http://cKnowledge.org/shared-programs.html">workflows</a>) with a unified Python JSON API and an <a href="https://github.com/ctuning/ck/wiki/Portable-workflows">integrated package manager</a>;
* organize all their local components (artifacts) in open [CK repositories](http://cKnowledge.org/shared-repos.html) and continuously exchange them with the community via GitHub, GitLab, BitBucket, BitTorrent, [ACM DL](https://dl.acm.org/docs/reproducibility.cfm), etc. to encourage artifact reuse;
* collaboratively improve all shared components and their JSON descriptions similar to Wikipedia while always keeping APIs backward compatible similar to Java;
* quickly prototype research ideas from shared components (such as [customizable, multi-objective, machine-learning based and input-aware autotuning](http://cKnowledge.org/rpi-crowd-tuning));
* enable <a href="https://github.com/ctuning/ck/wiki/Portable-workflows">universal virtual CK environment</a> where multiple versions of different software can easily co-exist;
* crowdsource different experiments across diverse data sets, models and platforms provided by volunteers (such as [crowd-benchmarking deep learning](http://cKnowledge.org/dnn-crowd-benchmarking-results));
* convert existing benchmarks into portable and customizable CK workflows adaptable to any platform with Linux, Windows, MacOS and Android using (see [ACM ReQuEST initiative](https://portalparts.acm.org/3230000/3229762/fm/frontmatter.pdf));
* [unify access to predictive analytics](http://cKnowledge.org/ai) (TensorFlow, TFLite, MXNet, Caffe, Caffe2, CNTK, scikit-learn, R, DNN, etc) via unified CK JSON API and CK web services;
* enable reproducible, interactive and "live" articles as shown in this [interactive CK report with Raspberry Pi foundation](http://cKnowledge.org/rpi-crowd-tuning); 
* automate and unify [Artifact Evaluation](http://cTuning.org/ae) at systems, ML and AI conferences;
* support open, reproducible and multi-objective co-design competitions of the whole SW/HW stack for emerging workloads such as AI (see [ACM ReQuEST tournaments](http://cKnowledge.org/request)). 

Please, check out the [latest ACM ReQuEST-ASPLOS'18 report about results of the 1st CK-powered competition on co-designing Pareto-efficient SW/HW stack for deep learning](https://portalparts.acm.org/3230000/3229762/fm/frontmatter.pdf), 
[CK motivation slides](https://slideshare.net/GrigoriFursin/enabling-open-and-reproducible-computer-systems-research-the-good-the-bad-and-the-ugly) 
and [CK use cases](http://cKnowledge.org/use_cases.html) from our [partners](http://cKnowledge.org/partners.html)
including [reproducible ACM tournaments on reproducible SW/HW co-design of emerging workloads](http://cKnowledge.org/request)
and [artifact sharing via ACM Digital Library](https://dl.acm.org/docs/reproducibility.cfm).

Join the [CK consortium](http://cknowledge.org/contacts.html) to influence CK long-term developments 
and standardization of APIs and meta descriptions of all shared CK workflows and components!

CK resources
============

* [cKnowledge.org - project website with the latest news](http://cKnowledge.org)
* [Academic and industrial partners with their use-cases](http://cKnowledge.org/partners.html)
* [CK documentation including "Getting Started Guide"](https://github.com/ctuning/ck/wiki)
  * [Shared CK programs (workflows)](http://cKnowledge.org/shared-programs.html)
  * [Shared CK repositories with reusable workflows and artifacts](http://cKnowledge.org/shared-repos.html)
  * [Reusable CK modules (plugins)](http://cKnowledge.org/shared-modules.html)
    * [Exposed CK kernel productivity functons](http://cKnowledge.org/ck-kernel-functions.html)
  * [Reusable software detection plugins](http://cKnowledge.org/shared-soft-detection-plugins.html)
  * [Reusable CK packages to automate installation of workflows across diverse platforms](http://cKnowledge.org/shared-packages.html)
* [Reproducible SW/HW co-design competitions for deep learning and other emerging workloads using CK](http://cKnowledge.org/request)
* [Live Scoreboard with results from crowd-sourced experiments such as SW/HW co-design of deep learning](http://cKnowledge.org/repo)
* [CK-powered AI benchmarking and optimization](http://cKnowledge.org/ai)
* [CK-related publications](https://github.com/ctuning/ck/wiki/Publications)
* [CK Mailing list](https://groups.google.com/forum/#!forum/collective-knowledge)
* [CK slack](https://collective-knowledge.slack.com)

Minimal installation
====================

The minimal installation requires:

* Python 2.7 or 3.3+ (limitation is mainly due to unitests)
* Git command line client
* wget (Linux/MacOS)

### Linux/MacOS

You can install CK in your local user space as follows:

```
$ git clone http://github.com/ctuning/ck
$ export PATH=$PWD/ck/bin:$PATH
$ export PYTHONPATH=$PWD/ck:$PYTHONPATH
```

You can also install CK via PIP with sudo to avoid setting up environment variables yourself:

```
$ sudo pip install ck
```

Finally, start from Ubuntu 18.10, you can install it via apt:
```
$ sudo apt install python-ck
 or
$ sudo apt install python3-ck
```

### Windows

First you need to download and install a few dependencies from the following sites:

* Git: https://git-for-windows.github.io
* Minimal Python: https://www.python.org/downloads/windows

You can then install CK as follows:
```
 $ pip install ck
```

or


```
 $ git clone https://github.com/ctuning/ck.git ck-master
 $ set PATH={CURRENT PATH}\ck-master\bin;%PATH%
 $ set PYTHONPATH={CURRENT PATH}\ck-master;%PYTHONPATH%
```

### Customization and troubleshooting

You can find troubleshooting notes or other ways to install CK 
such as via pip [here](https://github.com/ctuning/ck/wiki/Getting-started-guide#Quick_CK_installation).
You can find how to customize your CK installation [here](https://github.com/ctuning/ck/wiki/Customization).

Getting first feeling about portable and customizable workflows for collaborative benchmarking
==============================================================================================

Test ck:

```
$ ck version
```

Get shared [ck-tensorflow](https://github.com/ctuning/ck-tensorflow) repo with all dependencies:
```
$ ck pull repo:ck-tensorflow
```

List CK repos:
```
$ ck ls repo | sort
```

Find where CK repos are installed on your machine:
```
$ ck where repo:ck-tensorflow
```

Detect your platform properties via extensible CK plugins as follows 
(needed to unify benchmarking across diverse platforms
with Linux, Windows, MacOS and Android):

```
$ ck detect platform
```

Now detect available compilers on your machine and register virtual environments in the CK:
```
$ ck detect soft --tags=compiler,gcc
$ ck detect soft --tags=compiler,llvm
$ ck detect soft --tags=compiler,icc
```

See virtual environments in the CK:
```
$ ck show env
```

We recommend to setup CK to install new packages inside CK virtual env entries:
```
$ ck set kernel var.install_to_env=yes
```

Now install CPU-version of TensorFlow via CK packages:
```
$ ck install package --tags=lib,tensorflow,vcpu,vprebuilt
```

Check that it's installed fine:

```
$ ck show env --tags=lib,tensorflow
```

You can find a path to a given entry (with TF installation) as follows:
```
$ ck find env:{env UID from above list}
```

Run CK virtual environment and test TF:
```
$ ck virtual env --tags=lib,tensorflow
$ ipython
> import tensorflow as tf
```

Run CK classification workflow example using installed TF:

```
$ ck run program:tensorflow --cmd_key=classify
```

Now you can try a more complex example to build Caffe with CUDA support
and run classification. Note that CK should automatically detect your CUDA compilers, 
libraries and other deps or install missing packages:

```
$ ck pull repo --url=https://github.com/dividiti/ck-caffe
$ ck install package:lib-caffe-bvlc-master-cuda-universal
$ ck run program:caffe --cmd_key=classify
```

You can see how to install Caffe for Linux, MacOS, Windows and Android via CK
[here](https://github.com/dividiti/ck-caffe/wiki/Installation).

Finally, compile, run, benchmark and crowd-tune some C program (see shared optimization cases in http://cKnowledge.org/repo):
```
$ ck pull repo:ck-crowdtuning

$ ck ls program
$ ck ls dataset

$ ck compile program:cbench-automotive-susan --speed
$ ck run program:cbench-automotive-susan

$ ck benchmark program:cbench-automotive-susan

$ ck crowdtune program:cbench-automotive-susan
```

You can also quickly your own program/workflow using provided templates as follows:
```
$ ck add program:my-new-program
```

When CK asks you to select a template, please choose "C program "Hello world". 
You can then immediately compile and run your C program as follows:

```
$ ck compile program:my-new-program --speed
$ ck run program:my-new-program
$ ck run program:my-new-program --env.CK_VAR1=222
```

Find and reuse other shared CK workflows and artifacts:

* [Shared CK repositories](https://github.com/ctuning/ck/wiki/Shared-repos)
* [Shared CK deep learning workflows from ReQuEST tournaments](https://github.com/ctuning/ck-request-asplos18-results)
* [Shared CK modules (plugins)](https://github.com/ctuning/ck/wiki/Shared-modules)
* [Shared software detection plugins](https://github.com/ctuning/ck/wiki/Shared-soft-descriptions)
* [Shared CK packages to automate installation of workflows across diverse platforms](https://github.com/ctuning/ck/wiki/Shared-packages)

Further details:
* [Getting Started Guides](https://github.com/ctuning/ck/wiki),
* [ReQuEST tournaments](http://cKnowledge.org/request)
* [ReQuEST live scoreboard with benchmarking results](http://cKnowledge.org/repo)

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
simply as follows:
```
 $ (sudo) docker run ck-crowdtune-gcc
 $ (sudo) docker run ck-crowdtune-llvm
```

You can then browse top shared optimization results on the live CK scoreboard: http://cKnowledge.org/repo

Open ACM ReQuEST tournaments are now using our approach and technology 
to co-design efficient SW/HW stack for deep learning and other emerging workloads: http://cKnowledge.org/request

You can also download and view one of our CK-based interactive and reproducible articles as follows:
```
 $ ck pull repo:ck-docker
 $ ck run docker:ck-interactive-article --browser (--sudo)
```

See the list of other CK-related Docker images [here](https://hub.docker.com/u/ctuning).

However note that the main idea behind CK is to let the community collaboratively
improve common experimental workflows while making them 
[adaptable to latest environments and hardware](https://github.com/ctuning/ck/wiki/Portable-workflows),
and gradually fixing reproducibility issues as described [here](http://cknowledge.org/rpi-crowd-tuning)!

Citing CK (BibTeX)
==================

* [PDF 1](https://arxiv.org/abs/1801.08024)
* [PDF 2](https://www.researchgate.net/publication/304010295_Collective_Knowledge_Towards_RD_Sustainability)

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
