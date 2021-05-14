# CK installation

You can install the Collective Knowledge framework on most platforms using PIP as follows:

```bash
pip install ck
```

You can also install CK using a specific Python version (for example, Python 3.6 or for Python 2.7):
```bash
python3.6 -m pip install ck
```
or
```bash
python2.7 -m pip install ck
```

*You may need to add flag "--user" to install the client in your user space:*
```bash
pip install ck --user
python3.6 -m pip install ck --user
```

You should now be able to run CK using one of the following alternative commands:
```bash
ck

python3.6 -m ck
```

If the installation is successful, you will see some internal information 
about the CK installation and a Python version used:

```
CK version: 1.15.0

Python executable used by CK: /usr/bin/python

Python version used by CK: 2.7.12 (default, Oct  8 2019, 14:14:10)
   [GCC 5.4.0 20160609]

Path to the default repo: /home/fursin/fggwork/ck/ck/repo
Path to the local repo:   /home/fursin/CK/local
Path to CK repositories:  /home/fursin/CK

Documentation:        https://github.com/ctuning/ck/wiki
CK Google group:      https://bit.ly/ck-google-group
CK Slack channel:     https://cKnowledge.org/join-slack
Stable CK components: https://cKnowledge.io
```

## Prerequisites

The CK framework requires minimal dependencies: Python 2.7+ or 3.x, PIP and Git. 

### Linux

You need to have the following packages installed (Ubuntu example):

```bash
sudo apt-get install python3 python3-pip git wget
```

### MacOS

```bash
brew install python3 python3-pip git wget
```

### Windows

* Download and install Git from [git-for-windows.github.io](https://git-for-windows.github.io).
* Download and install any Python from [www.python.org/downloads/windows](https://www.python.org/downloads/windows).

### Android (Linux host)

These dependencies are needed to cross-compile for Android (tested on Ubuntu 18.04 including Docker and Windows 10 Subsystem for Linux). 

```bash
 sudo apt update
 sudo apt install git wget libz-dev curl cmake
 sudo apt install gcc g++ autoconf autogen libtool
 sudo apt install android-sdk
 sudo apt install google-android-ndk-installer
```

## Docker

We prepared several Docker images with the CK framework and AI/ML CK workflows 
at the [cTuning Docker hub](https://hub.docker.com/u/ctuning).
Select the most relevant image and run it as follows:
```bash
docker run -p 3344:3344 -it {Docker image name from the above list} /bin/bash
```

## Virtual CK environments with templates

We suggest you to use [virtual CK environments](https://github.com/octoml/venv)
with various automation templates shared by the community such as MLPerf&trade; inference.

See https://github.com/octoml/venv for more details.


## Customization

Please check this [wiki](https://github.com/ctuning/ck/wiki/Customization)
to learn more about how to customize your CK installation.
