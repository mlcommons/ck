***Note that the current prototype of the CM toolkit is under heavy development and may change over time ...***



***UNDER PREPARATION!***



# Concept

Here we describe a few simple steps to help you understand the CM concept. 
You will install CM v0.7.7+, transform your local directory, GitHub project, Docker container 
and Jupyter notebook into a database of reusable artifacts, share it with others
and implement some common automation to reusable artifacts.


## Install CM

CM toolkit is implemented as a small Python library with a unified CLI and a simple API.

It requires minimal dependencies (Python 3+, pip, pyyaml and a Git client) 
and should work with any OS including Linux, CentOS, Debian, RedHat and Windows.

```bash
$ pip3 install cmind
```

You can find more details about the installation process [here](installation.md).

## Share some artifacts

### Without CM

Image you want to share with your colleagues an image of a cat, some machine learning model
and a JSON file with some experimental results including inference time and image classification
via some GitHub repository.

First, you will likely create a GitHub repository and clone it on your local machine:

```bash
$ git clone {GitHub repo URL} my-cool-project
```
 
You may then create some directories to store your image, model and experiment:

```bash
$ cd my-cool-project

$ mkdir images
$ cp cool-cat.jpeg images

$ mkdir models
$ cp my-cool-model.onnx models

$ mkdir experiments
$ cp my-cool-result-20220404.json experiments
```

You will then likely create a *README.md* describing the structure 
and the content of your repository, and how someone can run your experiment.

Another person will need to read this README file to understand the structure
of your repository and either reproduce results or use some artifacts
in his or her own project.

### With CM

#### Initializing CM-compatible repository in the directory

The idea behind CM is to perform very similar steps from the command line 
but just prefixed by *cm* to let CM index artifacts, add Unique IDs 
and extensible JSON/YAML meta descriptions,
and make them findable, interconnectable and reusable:

You can initialize a CM repository in a given directory as follows:

```bash
$ cm init repo
```

CM will use the name of this directory as an alias of this CM repository. 
You can list already registered CM repositories as follows:
```
$ cm ls repo

local,9a3280b14a4285c9 = ...
internal,36b263b05174aef9 = ...
my-cool-project, ...
```

You can find a path to this repository as follows:
```bash
$ cm find repo my-cool-project
```

#### Converting Git project to CM repository

If you already have a Git repository you can pull and register it as follows:

```bash
$ cm pull repo my-cool-project --url={GitHub repo URL} 
```

CM will pull this repository to *$HOME/CM/repos/my-cool-project*, 
will add *cmr.yaml* file with a global unique ID to let the community
know that this repository is CM-compatible,
and will register this location in the CM-compatible repository index *$HOME/CM/repos.json*. 

This is needed to let CM automatically search for reusable artifacts and automations
in all CM-compatible directories on your machine and plug them into modular CM projects.

However, if you forget the location, you can always find it using the following CM command:`
```bash
$ cm find repo my-cool-project
```

You can list all CM-compatible repositories and their locations as follows:
```bash
$ cm list repo
```
or
```bash
$ cm ls repo | sort

default = C:\!Progs\Python39\lib\site-packages\cmind-0.5.2-py3.9.egg\cmind\repo
local = C:\Users\grigo\CM\repos\local
my-cool-project = C:\Users\grigo\CM\repos\my-cool-project
octoml@mlops = C:\Users\grigo\CM\repos\octoml@mlops
```

Note that you always have at least 2 CM-compatible repositories after you use CM for the first time:
* *internal* is a CM repository with reusable artifacts and automations that were moved 
  [inside the CM toolkit](https://github.com/mlcommons/ck/tree/master/ck2/cmind/repo) 
  to ensure their stability because they are frequently used by the community.

* *local* is a CM scratchpad repository where all new artifacts and automations 
  are created if a repository is not specified.






#### Creating CM artifact

You can then use CM to create a similar structure as in your original Git repository:

```
$ cm add images my-cool-project:cool-cat --tags=dataset,image,cool,cat
```

CM created a directory *images/cool-cat* inside *my-cool-project* repository and added *_cm.json* with extensible meta description:
```json
{
  "alias": "cool-cat",
  "automation_alias": "images",
  "automation_uid": "",
  "tags": [
    "dataset",
    "image",
    "cool",
    "cat"
  ],
  "uid": "780abfe6b8084327"
}
```

Note that since such artifact will become reusable in the world (collective database) where similar name may exists, 
CM also generated a unique ID for this artifact. You can now find this artifact on your system using its alias, UID or tags:

#### Finding CM artifact


```bash
$ cm find images cool-cat
$ cm find images 780abfe6b8084327
$ cm find images *cat*
$ cm find images --tags=image,cat
``` 

You can now copy your cool-cat.jpeg to this directory:
```bash
$ cp cool-cat.jpeg `cm find images cool-cat`
```

#### Viewing CM meta description

You can use the following CM command to view the meta description of a given artifact:

```bash
$ cm load images cool-cat

{
  "alias": "cool-cat",
  "automation_alias": "images",
  "automation_uid": "",
  "tags": [
    "dataset",
    "image",
    "cool",
    "cat"
  ],
  "uid": "780abfe6b8084327"
}

```

#### Creating more CM artifacts

Similarly, you can create CM artifacts for your model
```bash
$ cm add models my-cool-model --tags=model,ml,onnx,image-classification

$ cm list models

$ cp my-cool-model.onnx `cm find models my-cool-model`/model.onnx

$ ls `cm find models my-cool-model`

_cm.json
model.onnx

```

```bash
$ cm add experiments cool-result --tags=experiment,inference,image-classification,cat,20220404

$ cm ls experiments

$ cp my-cool-result-20220404.json `cm find experiments cool-result`

$ ls `cm find experiments cool-result`

_cm.json
my-cool-result-20220404.json

```

You can now update the README.md of this repository to specify CM commands 
and you can add the following badges to tell others that it is CM-compatible repository
with reusable artifacts and automations:

[![CM artifact](https://img.shields.io/badge/Artifact-automated%20and%20reusable-blue)](https://github.com/mlcommons/ck/tree/master/ck2)
[![CM repository](https://img.shields.io/badge/Collective%20Mind-compatible-blue)](https://github.com/mlcommons/ck/tree/master/ck2)









## Reuse others' artifacts

Whenever you see a CM-compatible repository you can install it via CM,
start using familiar cm commands similar to having a common language 
across all research projects, and automatically plug its artifacts 
and automations into our own modular projects as described later.

You may still need to follow the README.md file with the cm commands 
but even these steps can be also fully automated using a GUI or via
integration with existing DevOps and MLOps platforms and tools.

### From command line

```bash
$ cm pull repo my-cool-project --url={GitHub repo URL} 
$ cm ls experiments
$ cm load experiments cool-result
```

### From Python and Jupyter notebooks

CM provides a simple and unified access function to all CM repositories similar to micro-services
and [ElasticSearch]( https://www.elastic.co ) with input as dictionary

```python
import cmind

# List repositories

r=cmind.access({'action':'list', 'automation':'repo'})
if r['return']>0: cmind.error(r)

print (r)

# Find an artifact 

r=cmind.access({'action':'load', 'automation':'images', 'artifact':'cool-cat'})
if r['return']>0: cmind.error(r)

print (r['path'])
```

```json
{ 
  'return': 0, 
  'path': 'C:\\Users\\grigo\\CM\\repos\\my-cool-project\\images\\cool-cat', 
  'meta': {
    'alias': 'cool-cat', 
    'automation_alias': 'images', 
    'automation_uid': '', 
    'tags': [], 
    'uid': 'f94970b1af7c49db'
  }, 
  'artifact': <cmind.artifact.Artifact object at 0x000002A1B499AE20>
}
```

### In Docker containers

We can use CM commands to create modular containers:

```
# Adaptive container with the CM interface

FROM ubuntu:20.04

LABEL maintainer="Grigori Fursin <grigori@octoml.ai>"

SHELL ["/bin/bash", "-c"]

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y --no-install-recommends \
           apt-utils \
           git wget zip bzip2 libz-dev libbz2-dev cmake curl unzip \
           openssh-client vim mc tree \
           gcc g++ autoconf autogen libtool make libc6-dev build-essential patch \
           gfortran libblas-dev liblapack-dev \
           libsndfile1-dev libssl-dev libbz2-dev libxml2-dev libtinfo-dev libffi-dev \
           python3 python3-pip python3-dev \
           libtinfo-dev \
           python-is-python3 \
           libncurses-dev \
           sudo

RUN pip3 install cmind

RUN cm pull repo my-cool-project --url={GitHub repo URL} 

RUN cm list images

RUN cm ...
```


### From zip file 

You can pack your CM repository to a zip file as follows:
```bash
$ cm pack repo my-cool-project

Packing repo from C:\Users\grigo\CM\repos\my-cool-project to cm.zip ...
```

You can then share *cm.zip* with your colleagues who can unpack it 
and install on their system using the following CM command:
```bash
$ cm unpack repo

$ cm list images
$ cm list experiments

```


## Add reusable automations to related artifacts 

Systematize, reuse and interconnect similar to Wikipedia


## Extend meta descriptions

## Extend automations

## Further thoughts

