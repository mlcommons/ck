**[ [TOC](../README.md) ]**

# Common setup for the MLPerf inference benchmark

## Install CK framework

Install [CK](https://github.com/mlcommons/ck) and dependencies as described [here](https://ck.readthedocs.io/en/latest/src/installation.html)
(make sure that your version is >= 2.5.3):

```bash
pip3 install ck -U
```
or 
```bash
python3 -m pip install ck
```
or
```bash
python3 -m pip install ck --user
```

Check that ck is accessible from the command line:
```bash
fursin@ck:~$ ck

CK version: 2.5.8

Python executable used by CK: /usr/bin/python3

Python version used by CK: 3.6.9 (default, Jan 26 2021, 15:33:00)
   [GCC 8.4.0]

Path to the CK kernel:    /home/gfursin/.local/lib/python3.6/site-packages/ck/kernel.py
Path to the default repo: /home/gfursin/.local/lib/python3.6/site-packages/ck/repo
Path to the local repo:   /mnt/CK/local
Path to CK repositories:  /mnt/CK

Documentation:        https://github.com/mlcommons/ck/wiki
CK Google group:      https://bit.ly/ck-google-group
CK Slack channel:     https://cKnowledge.org/join-slack
Stable CK components: https://cknow.io
```

Note that you may need to restart your shell after this installation
or add *~.local/bin/ck* to your *PATH* environment variable manually.

## Pull CK repo for virtual environments

```bash
ck pull repo:mlcommons@ck-venv
```

## Check your Python version 

Check your python version:
```bash
python3 --version
```

If your Python version is < 3.6, we suggest you to install python via CK to be used in the virtual environment:
```bash
ck install package --tags=compiler,python,src
```

You can buid python with enabled optimizations though be careful since it may take 30..50 minutes:
```bash
ck install package --tags=compiler,python,src --env.ENABLE_OPTS
```


## Set up CK virtual environment

```bash
ck create venv:mlperf-inference --template=mlperf-inference-1.1-tvm
ck activate venv:mlperf-inference
```

This CK automation will create a virtual environment and install 
the [necessary dependencies](https://github.com/mlcommons/ck-venv/blob/master/venv.template/mlperf-inference-1.1/script.sh)
for the [MLPerf inference benchmark v1.1](https://github.com/mlcommons/inference).

## Pull MLOps automation repo

```bash
ck pull repo:mlcommons@ck-mlops
```

## Misc

You can find the installation directories for MLPerf and other packages as follows:
```bash
ck locate env --tags=mlperf,source
```

CK allows you to have multiple versions of all packages installed at the same time.
Each directory contains *env.sh* or *env.bat* with a preset environment variables
for a given version. 

CK program workflows will automatically load these files when resolving dependencies
thus allowing users to run the same MLPerf workflow with different versions
of compilers, frameworks, libraries, models and data sets.

*Note that all above steps can be automated via CK virtual environments too.
 However, we describe these manual steps to let users experiment 
 with different versions of dependencies for DSE.* 

