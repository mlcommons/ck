# Collective Knowledge Framework (CK)

**CK websites: [cKnowledge.org](https://cKnowledge.org) and [ReproIndex.com](https://ReproIndex.com)**

[![Downloads](https://pepy.tech/badge/ck)](https://pepy.tech/project/ck)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2459444.svg)](https://doi.org/10.5281/zenodo.2459444)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Linux/MacOS: [![Build Status](https://travis-ci.org/ctuning/ck.svg?branch=master)](https://travis-ci.org/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)
Coverage: [![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)

## Introduction

After struggling to reproduce experimental results and reuse artifacts 
from published papers (ML, AI, systems and quantum computing), 
we decided to develop the open-source Collective Knowledge framework (CK) 
to help the community share any knowledge (data, models, code,  best practices, 
and repetitive and painful tasks) in the form of automated, portable and reusable 
components with a unified Python API, CLI, JSON meta description 
and connectors from C, C++, Fortran, Java and other languages.
See the [online index of shared components](https://ReproIndex.com/components)
from [reproduced papers](https://ReproIndex.com/papers).

Such components can be continuously improved by the community and connected together 
into portable and automated workflows to collaboratively solve real world problems: 
see some [CK use cases from GM, Arm, IBM, Raspberry Pi, ACM/IEEE/NIPS and MLPerf](http://cKnowledge.org/partners.html)
and [CK dashboard with crowdsourced experiments](http://cKnowledge.org/dashboard).

See our [FOSDEM'19 presentation](https://zenodo.org/record/2556147#.XMViWKRS9PY) 
and [CK publications](https://github.com/ctuning/ck/wiki/Publications) 
to find out more about CK concepts and our long-term vision.

## Community

**CK is a collaborative project and not a magic ;)** - if some third-party automation fails 
or misses some functionality (software detection, package installation, benchmarking and autotuning workflow, etc),
the CK concept is to continuously and collaboratively improve such reusable components! 
Please provide your feedback and report bugs in the respective [GitHub repositories](https://ReproIndex.com/components)!

Feel free to discuss CK or ask for help using our [public mailing list](https://groups.google.com/forum/#!forum/collective-knowledge) 
and the [Slack channel](http://bit.ly/ck-slack).

## Documentation

[CK wiki](https://github.com/ctuning/ck/wiki) - major revision is planned in 2019. 

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
$ ck install package:lib-tensorflow-1.12.0-cpu
$ ck run program:tensorflow-classification
```

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

Please follow this [guide](https://github.com/ctuning/ck/wiki) to add your workflows and components. Note that major revision to simplify this guide based on your feedback is planned in 2019!

Feel free to provide your suggestions using our [public mailing list](https://groups.google.com/forum/#!forum/collective-knowledge) 
and the [Slack channel](http://bit.ly/ck-slack)!
