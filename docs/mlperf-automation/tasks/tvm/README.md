# TVM-based MLPerf benchmark automation

## Install CK framework

Install [CK](https://github.com/ctuning/ck) and dependencies as described [here](https://ck.readthedocs.io/en/latest/src/installation.html)
(make sure that your version is >= 2.5.3):

```bash
pip3 install ck
```
or 
```bash
python3 -m pip install ck
```
or
```bash
pip3 install ck
```

Check that ck is accessible from the command line:
```bash
fursin@ck:~$ ck

CK version: 2.5.7

Python executable used by CK: /usr/bin/python3

Python version used by CK: 3.6.9 (default, Jan 26 2021, 15:33:00)
   [GCC 8.4.0]

Path to the CK kernel:    /home/gfursin/.local/lib/python3.6/site-packages/ck/kernel.py
Path to the default repo: /home/gfursin/.local/lib/python3.6/site-packages/ck/repo
Path to the local repo:   /mnt/CK/local
Path to CK repositories:  /mnt/CK

Documentation:        https://github.com/ctuning/ck/wiki
CK Google group:      https://bit.ly/ck-google-group
CK Slack channel:     https://cKnowledge.org/join-slack
Stable CK components: https://cKnowledge.io
```

Note that you may need to restart your shell after this installation
or add *~.local/bin/ck* to your *PATH* environment variable manually.

## Pull CK repo for virtual environments

```bash
ck pull repo:octoml@venv
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
ck create venv:mlperf-tvm --template=mlperf-inference-1.1-tvm
ck activate venv:mlperf-tvm
```

This CK automation will create a virtual environment and install 
[necessary dependencies](https://github.com/octoml/venv/blob/main/venv.template/mlperf-inference-dev-tvm/script.sh)
 for the MLPerf inference benchmark 
([OctoML's dev TVM branch](https://github.com/octoml/mlcommons-inference))

## Pull OctoML's MLOps repo

```bash
ck pull repo:octoml@mlops
```

## Install related CK packages (dataset, model, framework, compiler)

```bash
ck install package --tags=lib,python-package,onnxruntime-cpu,1.7.0
ck install package --tags=lib,python-package,onnx,1.9.0

ck install package --tags=lib,python-package,scipy
ck install package --tags=tool,cmake,prebuilt,v3.18.2

ck install package --tags=compiler,llvm,prebuilt,v12.0.0

ck install package --tags=compiler,tvm,dev --j=8

```

TVM installation can be customized as follows:
```bash
ck install package --tags=compiler,tvm,dev \
                     --env.USE_RELAY_DEBUG=ON \
                     --env.USE_GRAPH_RUNTIME_DEBUG=ON \
                     --env.USE_GRAPH_EXECUTOR_DEBUG=ON
```


*Note that all above steps can be automated via CK virtual environments too.
 However, we describe these manual steps to let users experiment 
 with different versions of dependencies for DSE.* 


## MLPerf tasks

* [Image Classification](mlperf-image-classification.md)
* [Object Detection](mlperf-object-detection.md)




# TBD

Tasks are available on [GitHub]( https://github.com/octoml/mlcommons-inference/issues/1 )
