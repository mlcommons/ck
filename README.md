# Collective Knowledge Framework (CK)

[![Downloads](https://pepy.tech/badge/ck)](https://pepy.tech/project/ck)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2459444.svg)](https://doi.org/10.5281/zenodo.2459444)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
Coverage: [![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

## News

***[Codereef](https://codereef.ai) is building an [open PyPI-like repository](https://dev.codereef.ai/portal) to simplify the creation, sharing and reuse of CK components, workflows and reproduced results - feel free to subscribe as a beta tester!***

## Introduction

<img src="https://github.com/ctuning/ck-guide-images/blob/master/ck-example.gif">

Collective Knowledge (CK) is a small, cross-platform and community-driven Python framework 
to help you add, share and reuse standardized CLI actions with Python/C/Java APIs, UIDs 
and JSON meta descriptions for any code and data in a non-intrusive way. 

Such actions can be connected into platform-agnostic, portable, customizable, reusable and reproducible workflows,
and can be easily integrated with existing production and legacy systems.

Our long-term goal is to help users automate their tedious, repetitive and time-consuming R&D tasks,
and enable collaborative, reproducible, sustainable and production-ready research 
based on DevOps principles.

See [CK real use cases](https://cKnowledge.org/partners.html), 
[publications](https://github.com/ctuning/ck/wiki/Publications)
and the [FOSDEM'19 presentation](https://zenodo.org/record/2556147#.XMViWKRS9PY) for more details.

Some important CK features:

* CK actions can be shared and reused across research projects:
  see the [list of available actions and modules](https://dev.codereef.ai/portal/search/?q=module_uoa%3Amodule).

* Standardized CK APIs and meta-descriptions help  users 
  to easily connect actions into automated, portable and customizable workflows, 
  and quickly integrate them with practically all major tools, frameworks and Continuous Integration Services: 
  see the [list of shared repositories with CK workflows and actions](https://dev.codereef.ai/portal/search/?q=module_uoa%3A%22cr-repo%22).

* CK helps to perform reproducible experiments and generate papers with reusable research components:
  see [the list of articles with CK workflows](https://dev.codereef.ai/portal/search/?q=%22reproduced-papers%22) 
  and the [CK-based interactive report with the Raspberry Pi foundation](https://dev.codereef.ai/portal/c/report/rpi3-crowd-tuning-2017-interactive).

* CK can be used to crowdsource autotuning and co-design of efficient software, hardware, and models
  for emerging AI, ML and quantum computing workloads in terms of speed, accuracy, energy, and costs: 
  see the [live CK dashboard with results from different Hackathons, tournaments and crowd-tuning campaigns](https://dev.codereef.ai/portal/search/?q=%22codereef-result%22).

## Our community

Don't hesitate to ask questions using our [public mailing list](https://groups.google.com/forum/#!forum/collective-knowledge) 
and the [Slack channel](https://cKnowledge.org/join-slack).

You are also welcome to help the community fix or improve third-party components (actions, modules, packages, software plugins, workflows) 
when they fail on new platforms or miss some functionality - you can provide your feedback and report bugs 
in the respective [GitHub CK dev repositories](https://dev.codereef.ai/portal/search/?q=module_uoa%3A%22cr-repo%22)!

## Documentation

[CK wiki](https://github.com/ctuning/ck/wiki) - a major revision is planned.

## Installation

You can install CK from PyPi via ``pip install ck`` or ``pip install ck --user``.

You can then test that it works from the command line via ``ck version`` or from your python environment as follows:
```
$ python

> import ck.kernel as ck
> ck.version({})
```

CK requires just a few tools in your PATH:

* Python 2.7 or 3.3+ with PIP (limitation is mainly due to unitests). CK automatically adapts to Python 2 or 3 and provides extra API to let users write workflows for any Python version;
* Git command line client;
* wget (Linux/MacOS).

Example of installing dependencies and CK across different platforms:

| | Ubuntu | MacOS | Windows | 
|-|-|-|-|
| Third-party | ```sudo apt-get install python3 python3-pip git wget``` | ``brew install python3 git wget`` | 1) Download and install Git from https://git-for-windows.github.io<br>2) Download and install any Python from https://www.python.org/downloads/windows |
| PyPi | ``sudo pip install ck``<br>or<br>``pip install ck --user``<br><br>Check that ck is in your PATH: ``ck version`` | ``pip install ck`` | ``pip install ck``<br><br>You can also download a [CK installer](https://zenodo.org/record/2555622/files/ck-git-2.20.1-python-3.7.2.zip) which already includes Git 2.20.1 and Python 3.7.2<br><br>Just unzip it and run ``install-pip.bat`` to install CK via PIP<br>This script will install Python in your dedicated directory and will ask you to add several environment variables to your system (just copy/paste them) - that's all! |
| GitHub | ``git clone http://github.com/ctuning/ck``<br>``export PATH=$PWD/ck/bin:$PATH``<br>``export PYTHONPATH=$PWD/ck:$PYTHONPATH``<br><br>You can also set CK environment variables and test dependencies using provided script as follows:<br><br>``git clone http://github.com/ctuning/ck``<br>``. ./set-env.sh`` | Similar to Ubuntu | ``git clone https://github.com/ctuning/ck.git ck-master``<br>``set PATH={CURRENT PATH}\ck-master\bin;%PATH%``<br>``set PYTHONPATH={CURRENT PATH}\ck-master;%PYTHONPATH%``<br><br>You can also download a [CK installer](https://zenodo.org/record/2555622/files/ck-git-2.20.1-python-3.7.2.zip) which already includes Git 2.20.1 and Python 3.7.2<br><br>Just unzip it and run ``install-github.bat`` to install CK from GitHub<br>This script will install Python in your dedicated directory and will ask you to add several environment variables to your system (just copy/paste them)|

CK allows very flexible customization to adapt to your platform and different requirements as described [here](https://github.com/ctuning/ck/wiki/Customization).
For example, you can change directories where to store CK repositories or install CK packages, change search paths during software detection (useful for HPC setups) 
and so on. 

If you experience problems with installation and customization, please [tell us](https://groups.google.com/forum/#!forum/collective-knowledge) 
or open a [GitHub issue](https://github.com/ctuning/ck/issues).

## Usage

When you see an archive or a repository with a badge [![compatibility](https://github.com/ctuning/ck-guide-images/blob/master/ck-compatible.svg)](https://github.com/ctuning/ck), 
it means you can reuse its functionality (code, data, models, packages, workflows) via unified CK interfaces, and integrate it with your own projects.

For example, you can pull [ck-tensorflow](https://github.com/ctuning/ck-tensorflow) and use different automation 
tasks such detecting or rebuilding different TensorFlow versions across diverse platforms, running AI/ML workflows
and many more:

```
$ ck pull repo:ck-tensorflow

$ ck detect platform

$ ck install package:lib-tensorflow-1.12.0-cpu

$ ck run program:tensorflow-classification

$ ck show env
```

**Note that tensorflow 1.12.0 can work only with Python version<=3.6 - please select an appropriate Python version during automatic environment detection**

You can find a non-exhaustive index of CK-compatible repositories at [ReproIndex.com](https://ReproIndex.com/components) - 
just follow their READMEs to find out more about shared components and workflows!

Please check our [Getting Started Guide](https://github.com/ctuning/ck/wiki/First-steps) to try different CK examples.




## Examples of popular and reusable CK-based automation tasks

Pull one of [CK repositories](https://ReproIndex.com/components) with shared benchmarks, data sets, software detection plugins, packages, etc:

```
$ ck pull repo:ck-crowdtuning
```

See the list of installed CK repos:
```
$ ck ls repo | sort
```

Find where CK repository with benchmarks is installed on your machine and browse it to get familiar with the structure (consistent across all repos):
```
$ ck where repo:ctuning-programs
```

Detect your platform properties via extensible CK plugins as follows 
(needed to unify benchmarking across diverse platforms
with Linux, Windows, MacOS and Android):

```
$ ck detect platform
```

Check JSON output 

```
$ ck detect platform --out=json
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

Find and explore CK env entries:
```
$ ck search env --tags=compiler
```

We recommend to setup CK to install new packages inside CK virtual env entries:
```
$ ck set kernel var.install_to_env=yes
```

Try to install LLVM binary via CK packages:
```
$ ck install package --tags=llvm
```

Check available data sets:
```
$ ck search dataset
$ ck search dataset --tags=jpeg

```

Now you can compile and run shared benchmarks with some data sets, benchmark and crowd-tune some C program.
```
$ ck ls program
```

Let's check the CK JSON meta for benchmark "cbench-automotive-susan":
```
$ ck load program:cbench-automotive-susan --min
```

Now let's compile and run it:

```
$ ck compile program:cbench-automotive-susan --speed
$ ck run program:cbench-automotive-susan
```

You can now benchmark this program (CK will execute several times while monitoring the state of the system):
```
$ ck benchmark program:cbench-automotive-susan
```

Finally, you can autotune this program using shared CK autotuning scenarios, record results and reply them:
```
$ ck autotune program:cbench-automotive-susan
```

You can also crowdtune this program, i.e. autotune it while sharig best results in the [public repository](http://cKnowledge.org/repo):
```
$ ck crowdtune program:cbench-automotive-susan
```

You can now add (and later customize) your own program workflow using shared templates as follows:
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





## Example of a unified image classification via TensorFlow and Caffe

Get shared [ck-tensorflow](https://github.com/ctuning/ck-tensorflow) repository with all dependencies:

```
$ ck pull repo:ck-tensorflow
```

Now install CPU-version of TensorFlow via CK packages:
```
$ ck install package --tags=lib,tensorflow,vcpu,vprebuilt,v1.11.0
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





## Adding your own repository and API:

You can make your existing Git repository compatible with CK as follows:

```
$ ck pull repo --url={URL of your Git repository}
```

CK will add *.ckr.json* file to the root of your repository which you should commit back to your repository - that's all!

You can then add CK components to your repository using it's public Git name, for example *my-repo*:

For example, you can now add a CK module to prepare APIs:
```
$ ck add my-repo:module:hello
```

It will create an entry "module:hello" in the my-repo with a dummy module.py:
```
$ ls `ck find module:hello`
```

Now you can add "say" API to the CK python module "hello":
```
$ ck add_action module:hello --func=say
```

CK will add a dummy function "say" in the module.py in "module:hello" which you can immediately use (!):
```
$ ck say hello
$ ck say hello --out=json
```

Furthermore, you can now create a data entry for your module "hello":
```
$ ck add hello:world --tags=cool,api

$ ck search hello --tags=api

$ ck say hello:world

$ ck ren hello:world hello:team

$ ck say hello:team
```


Alternatively, you can create a local (non-shared) repository to gradually organize your code and data in the CK format as follows:
```
$ ck add repo:my-repo --quiet

$ ck where repo:my-repo

$ ck ls repo:my-*
```


Such simple approach allowed [our partners](http://cKnowledge.org/partners.html) to gradually abstract 
complex AI, ML, and quantum experiments via shared [CK APIs](https://ReproIndex.com/components),
crowdsource [experiments](https://cKnowledge.org/dashboard), and even automatically generate 
[reproducible](https://ReproIndex.com/papers) and [interactive articles](http://cKnowledge.org/rpi-crowd-tuning) 
with reusable research components!



## Calling CK functions from other languages

We developed a small [OpenME](https://github.com/ctuning/openme) library 
to connect CK with different languages including C, C++, Fortran and Java. 




## Trying CK from a Docker image

You can try CK using the following Docker image:

```
 $ (sudo) docker run -it ctuning/ck-ubuntu-18.04
```

Note that we added Docker automation to CK to help evaluate 
artifacts at the conferences, share interactive 
and reproducible articles, crowdsource experiments and so on.

For example, you can participate in GCC or LLVM crowd-tuning on your machine as follows:
```
 $ (sudo) docker run ck-crowdtune-gcc
 $ (sudo) docker run ck-crowdtune-llvm
```

Top optimization results are continuously aggregated in the live CK repository: http://cKnowledge.org/repo .


## Contributing

Please follow this [guide](https://github.com/ctuning/ck/wiki) to add your workflows and components. Note that we plan to rewrite it and add tutorials as soon as we have more resources!

Feel free to provide your suggestions using our [public mailing list](https://groups.google.com/forum/#!forum/collective-knowledge) 
and the [Slack channel](https://cKnowledge.org/join-slack)!

Contact [Grigori Fursin](mailto:grigori.fursin@codereef.ai) about the long-term vision and development plans.
