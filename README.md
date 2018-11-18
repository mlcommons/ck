[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
Coverage: [![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

Collective Knowledge (CK) is a community effort to develop the universal, portable, customizable 
and automated workflow framework with "plug&play" components to enable collaborative and reproducible R&D
based on agile, DevOps, [FAIR](https://www.nature.com/articles/sdata201618) and Wikipedia principles
(see [CK motivation](https://github.com/ctuning/ck/wiki/Motivation), 
[main features](https://github.com/ctuning/ck/wiki/Features)
and [RESCUE-HPC workshop](http://rescue-hpc.org)).

The idea is to let the community collaboratively improve common experimental workflows and components
via Git while making them [adaptable to new environments and platforms](https://github.com/ctuning/ck/wiki/Portable-workflows),
and gradually fixing [reproducibility issues](http://cknowledge.org/rpi-crowd-tuning)!

CK supports [our long-term vision](https://www.slideshare.net/GrigoriFursin/accelerating-open-science-and-ai-with-automated-portable-customizable-and-reusable-research-components-and-workflows) 
to connect academia and industry to solve the real-world challenges.
For example, see several important use cases from [our partners](http://cKnowledge.org/partners.html):
* IBM: ["Reproducing Quantum results from Nature - how hard could it be?"](https://www.linkedin.com/pulse/reproducing-quantum-results-from-nature-how-hard-could-lickorish/)
* General Motors: ["Collaboratively Benchmarking and Optimizing Deep Learning Implementations"](https://www.youtube.com/watch?v=1ldgVZ64hEI)
* Amazon: ["Scaling deep learning on AWS using C5 instances with MXNet, TensorFlow, and BigDL: From the edge to the cloud"](https://conferences.oreilly.com/artificial-intelligence/ai-eu/public/schedule/detail/71549)
* Arm: [ARM Demonstration of Collaboratively Optimizing Deep Learning Applications](https://www.youtube.com/watch?v=f4CfMrGPJPY)
* Raspberry Pi foundation: [interactive and reproducible article about "a Collective Knowledge workflow for collaborative research into multi-objective autotuning and machine learning techniques"](http://cKnowledge.org/rpi-crowd-tuning)
* ACM, IEEE and NIPS conferences: [automating artifact evaluation](http://cTuning.org/ae)
* ACM and dividiti:[ReQuEST tournaments to co-design efficient SW/HW stacks for deep learning across diverse models, data sets and platforms from cloud to edge](http://cKnowledge.org/request), [organizers' report](https://portalparts.acm.org/3230000/3229762/fm/frontmatter.pdf)
* dividiti: [CK-based public benchmarking of Quantum systems and algorithms](http://cKnowledge.org/quantum)

Just **[give it a try](https://github.com/ctuning/ck/wiki/First-feeling.mediawiki)** 
and do not hesitate to provide your feedback to the CK community
via [public CK discussion group](https://groups.google.com/forum/#!forum/collective-knowledge)!

# CK resources

* Project website: [cKnowledge.org](http://cKnowledge.org)
* CK [motivation](https://github.com/ctuning/ck/wiki/Motivation) and [main features](https://github.com/ctuning/ck/wiki/Features)
* [Real world use cases from the CK community](http://cKnowledge.org/partners.html)
* [CK documentation](https://github.com/ctuning/ck/wiki)
  * [Shared CK programs (workflows)](http://cKnowledge.org/shared-programs.html)
  * [Shared CK repositories with reusable workflows and artifacts](http://cKnowledge.org/shared-repos.html)
  * [Reusable CK modules (plugins)](http://cKnowledge.org/shared-modules.html)
    * [Exposed CK kernel productivity functions](http://cKnowledge.org/ck-kernel-functions.html)
  * [Reusable software detection plugins](http://cKnowledge.org/shared-soft-detection-plugins.html)
  * [Reusable CK packages to automate installation of workflows across diverse platforms](http://cKnowledge.org/shared-packages.html)
* [Reproducible SW/HW co-design competitions for deep learning and other emerging workloads using CK](http://cKnowledge.org/request)
* [Live Scoreboard with results from crowd-sourced experiments such as SW/HW co-design of deep learning](http://cKnowledge.org/repo)
* [CK publications](https://github.com/ctuning/ck/wiki/Publications)
* CK [mailing list](https://groups.google.com/forum/#!forum/collective-knowledge) and [Slack](https://collective-knowledge.slack.com)

# Installation

## Dependencies

The minimal CK installation requires:

* Python 2.7 or 3.3+ with PIP (limitation is mainly due to unitests)
* Git command line client
* wget (Linux/MacOS)

### Ubuntu

```
$ sudo apt-get install python3 python3-pip git wget
```

### MacOS

```
$ brew install python3
$ brew install git
$ brew install wget
```

### Windows

* Download and install Git from https://git-for-windows.github.io
* Download and install Python from https://www.python.org/downloads/windows

## Installation from GitHub

### Linux/MacOS

You can install CK in your local user space as follows:

```
$ git clone http://github.com/ctuning/ck
$ export PATH=$PWD/ck/bin:$PATH
$ export PYTHONPATH=$PWD/ck:$PYTHONPATH
```

### Windows

```
 $ git clone https://github.com/ctuning/ck.git ck-master
 $ set PATH={CURRENT PATH}\ck-master\bin;%PATH%
 $ set PYTHONPATH={CURRENT PATH}\ck-master;%PYTHONPATH%
```

## Installation via PIP

### Ubuntu

You can also install CK via PIP with sudo to avoid setting up environment variables yourself:

```
$ sudo pip install ck
```

Starting from Ubuntu 18.10, you can install it via apt:
```
$ sudo apt install python-ck
 or
$ sudo apt install python3-ck
```

### MacOS/Windows

```
$ pip install ck
```

## Installation customization

Check [this documentation](https://github.com/ctuning/ck/wiki/Customization)
about CK customization. For example, you can change directories with CK repositories
and packages or change search paths during software detection (useful for HPC setups).

# Basic usage example

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

# Trying CK from Docker images

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

# Citing CK

See [CK publications](https://github.com/ctuning/ck/wiki/Publications).

# CK authors

* [Grigori Fursin](http://fursin.net/research.html), cTuning foundation and dividiti
* [Anton Lokhmotov](https://uk.linkedin.com/in/lokhmotov), dividiti

# License

* Permissive 3-clause BSD license. (See `LICENSE.txt` for more details).

# Acknowledgments

CK development is coordinated by the [cTuning foundation](https://en.wikipedia.org/wiki/CTuning_foundation)
and [dividiti](http://dividiti.com). We would like to thank the [TETRACOM 609491 Coordination Action](http://tetracom.eu) 
for initial funding and [all our partners](http://cKnowledge.org/partners.html) for continuing support. 
We are also extremely grateful to all volunteers for their valuable feedback and contributions.
