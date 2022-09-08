# Tutorial: understanding CM database concepts

Here we describe a few simple steps to let you try CM (aka CK2) and help you understand the CM [motivation](motivation.md)
and concepts.

You will install CM v0.7.24+, transform your local directory into a database of reusable artifacts, 
share it with others, implement some common automation actions to reusable artifacts,
run CM automations from Python and Jupyter Notebooks, and convert any Git repository 
into the CM format.




## Installing CM

CM toolkit is implemented as a small Python library with a unified CLI and a simple API.

It requires minimal dependencies (Python 3+, pip, pyyaml and a Git client) 
and should work with any OS including Linux, MacOS, CentOS, Debian, RedHat and Windows.

```bash
pip3 install cmind
```

You can find more details about the installation process [here](installation.md).




## Organizing your artifacts

We use CM to provide a common structure to software projects and organize all related artifacts 
in such a way that it is possible to share, find, reuse and extend them across different teams and projects
with a minimal effort.



### Without CM

Let's imagine that you want to share with your colleagues some machine learning model, an image of a cat, 
and a JSON file with some experimental results including inference time and image classification
via some GitHub repository.

You will [likely](https://www.youtube.com/watch?v=7zpeIVwICa4), 
create some local directory "my-cool-project" in your $HOME directory to organize related artifacts:

```bash
mkdir my-cool-project
cd my-cool-project
```
 
You will then create some ad-hoc directories to store your ML model, image and experimental data:

```bash
mkdir images
cp cool-cat.jpeg images

mkdir models
cp my-cool-model.onnx models

mkdir experiments
cp my-cool-result-20220404.json experiments
```

You will then likely create a *README.md* describing the structure 
and the content of your repository, and how someone can run your experiment.

You will then pack this repository or push it to GitHub to share it with someone else.

Another person will need to read your README file to understand the structure
of your repository, reproduce results, customize your code and reuse some artifacts
in another project.

However, since most colleagues [are very busy with their own projects](https://doi.org/10.5281/zenodo.6475385), 
they will unlikely to have time to read yet another ad-hoc ReadMe and will unlikely to try your project
unless they are forced to ;) ...

![](https://i.pinimg.com/564x/17/45/68/174568bf0002b8832b20fd995898f8ce.jpg)

Based on our [related experience](https://www.youtube.com/watch?v=7zpeIVwICa4),
we believe that having a common format and command line interface 
for projects and READMEs will make it easier for the community 
to try your project and reuse your artifacts.



### With CM

#### Initializing CM-compatible repository in the directory

The idea behind CM is to convert directories and projects into a simple
database of [reusable](https://www.go-fair.org/fair-principles) 
artifacts and automations with a common CLI.

We want you to perform very similar steps from the command line as above
but just prefixed by *cm* to let CM index artifacts, add Unique IDs 
and extensible JSON/YAML meta descriptions,
and make them findable, interoperable and reusable:

You can initialize a CM repository in your working directory as follows:

```bash
cm init repo
```

CM will create a *cmr.yaml* file with a global unique ID and will register 
this location in the CM-compatible repository index *$HOME/CM/repos.json*. 

This is needed to let CM automatically search for reusable artifacts and automations
in all CM-compatible directories on your machine and plug them into modular CM projects.

However, if you forget the location, you can always find it using the following CM command:
```bash
cm find repo my-cool-project
```

Note that CM will use the name of your current directory as an alias of this CM repository. 
You can list already registered CM repositories as follows:
```bash
cm ls repo
```
 or
```bash
cm ls repo | sort

local = C:\Users\grigo\CM\repos\local
internal = C:\!Progs\Python39\lib\site-packages\cmind-0.7.7-py3.9.egg\cmind\repo
my-cool-project = ...
```


You can also create a repository with a specific name in $HOME/CM/repos directory as follows:
```bash
cm init repo another-cool-project
cm find repo *cool*
```

#### Converting existing Git project to the CM repository

If you already have a Git repository you can pull it via CM and make it a CM-compatible repository as follows:

```bash
cm pull repo my-cool-project --url={Git repo URL} 
cm find repo 
```

CM will pull this repository to *$HOME/CM/repos/my-cool-project*, 
will add *cmr.yaml* file with a global unique ID to let the community
know that this repository is CM-compatible,
and will register this location in the CM-compatible repository index *$HOME/CM/repos.json*. 


Note that you always have at least 2 CM-compatible repositories after you use CM for the first time:
* *internal* is a CM repository with reusable artifacts and automations that were moved 
  [inside the CM toolkit](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo) 
  to ensure their stability because they are frequently used by the community.

* *local* is a CM scratchpad repository where all new artifacts and automations 
  are created if a repository is not specified.





#### Creating CM artifacts

You can now use CM to create a very similar structure as in your original Git repository
but with some meta information in JSON and/or YAML format to describe your artifacts.

The format of the CM to add artifacts is the following:
```bash
cm add {some artifact type} {artifact name} 
```

By default, CM will create new artifacts in the "local" CM repository (scratchpad).
You can specify another CM repository as follows:
```bash
cm add {some artifact type} {CM repo}:{artifact name}
```

You can also add some tags to describe a given artifact as follows:
```bash
cm add {some artifact type} {CM repo}:{artifact name} --tags=tag1,tag2,tag3...
```

In our case, let's use "images" as our artifact type. Note that you can either use 
any name to organize your artifacts or reuse an existing artifact type 
with some common automations shared by the community or within workgroups 
as described later in this tutorial.


```bash
cm add images my-cool-project:cool-cat --tags=dataset,image,cool,cat
```

CM will create a directory *images/cool-cat* inside *my-cool-project* repository and added *_cm.json* with extensible meta description:
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

Note that you will a different UID on your system - you should use it instead of "780abfe6b8084327"

Note that CM also generated a unique ID for this artifact - the reason is that any CM artifact can be reusable
in the world similar to a global database where another artifact with a similar name (alias) may already exist.
In such case, we can use UID in our projects to make sure that we find and reuse a unique artifact.

Also note that if you want to create another artifact in a CM repository, you can tell CM to use
current CM repository and artifact type using "." instead of tying the full names:

```bash
cd automation
cm add . cool-cat-v2 --tags=dataset,image,cool,cat-v2
```

CM will create *cool-cat-v2* in the current CM repository rather than in the "local" repository.

#### Finding CM artifacts

Since CM keeps track of CM-compatible repositories, it is now possible to find any artifact 
using its name (alias), UID or tags:


```bash
cm find images cool-cat
cm find images 780abfe6b8084327
cm find images *cat*
cm find images --tags=image,cat
``` 

Note that you can also reference your CM artifact by alias and UID at the same time:
```bash
cm find images cool-cat,780abfe6b8084327
```

In such case, CM will ignore above alias and will search for an artifact by UID. 
However, you can still see the original name of the artifact instead of a cryptic UID.
If this name (alias) changes in the future, CM will still be able to find it using its UID!

You can now use this CM artifact directory as a findable placeholder for your raw artifacts.
For example, you can You can now copy your cool-cat.jpeg and any related files to this directory:
```bash
cp cool-cat.jpeg `cm find images cool-cat`
```

Now, we will be able to find any artifact on our own machines or in a cloud even years later!

Furthermore, we can use the same command line language to describe our repository
in different READMEs thus providing a common artifact management language for projects.


#### Renaming artifact

You can now rename your artifact using CM to keep UID intact as follows:
```bash
cm rename images cool-cat-v2 cool-cat-v3
```

#### Moving artifacts to another CM repository

Unlike CK, you can move an artifact to any CM repository using standard OS commands.
However, you can also use CM CLI for your convenience:

```bash
cm move images cool-cat-v3 local:
```
This command will move *images::cool-cat-v3* artifact to "local" repository.


#### Deleting artifact

Unlike CK, you can also delete your artifacts using standard OS commands.
 
However, you can also use CM CLI for your convenience:

```bash
cm rm images cool-*-v3
```
This command will remove *images::cool-cat-v3* artifact.


#### Copying artifact to another artifact

The idea of CM is to use existing artifacts as templates for new artifacts. 
You can copy an artifact to another one with a new alias (new UID will be generated automatically)
as follows:

```bash
cm copy images cool-cat-v3 .:cool-cat-v4
```
This command will copy *images::cool-cat-v4* artifact to 
*images::cool-cat-v4** in the same repository (specified by *.*)




#### Viewing CM meta description

You can use the following CM command to view the meta description of a given artifact:

```bash
cm load images cool-cat

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

or
```bash
cm load images --tags=cool,cat
```




#### Creating other types of artifacts

Similarly, you can create CM artifacts for your ML model
```bash
cm add models my-cool-model --tags=model,ml,onnx,image-classification

cm find models my-cool-project:*

cp my-cool-model.onnx `cm find models my-cool-model`/model.onnx

ls `cm find models my-cool-model`

_cm.json
model.onnx

```

```bash
cm add experiments cool-result --tags=experiment,inference,image-classification,cat,20220404

cm ls experiments

cp my-cool-result-20220404.json `cm find experiments cool-result`

ls `cm find experiments cool-result`

_cm.json
my-cool-result-20220404.json

```

You can now update the README.md of your repository to specify CM commands 
and you can add the following badges to tell the community 
that it is CM compatible:

[![CM artifact](https://img.shields.io/badge/Artifact-automated%20and%20reusable-blue)](https://github.com/mlcommons/ck/tree/master/cm)
[![CM repository](https://img.shields.io/badge/Collective%20Mind-compatible-blue)](https://github.com/mlcommons/ck/tree/master/cm)

This will signal other colleagues that they can now understand your README 
and deal with your project using CM CLI or Python API:





## Reusing others' artifacts in the CM format

Whenever you see a CM-compatible repository you can install it via CM,
start using familiar cm commands similar to having a common language 
across all research projects, and automatically plug its artifacts 
and automations into our own modular projects as described later.

You may still need to follow the README.md file with the cm commands 
but even these steps can be also fully automated using a GUI or via
integration with existing DevOps and MLOps platforms and tools.




### From command line

```bash
cm pull repo my-cool-project --url={GitHub repo URL} 
cm find experiments
cm load experiments cool-result
```

### From Python and Jupyter notebooks

CM provides a simple and unified access function to all CM repositories similar to micro-services
and [ElasticSearch]( https://www.elastic.co ) with an input as a dictionary:

```python
import cmind

# List repositories

r=cmind.access({'action':'find', 'automation':'repo'})
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

You can see the Python class for a CM artifact [here](https://github.com/mlcommons/ck/blob/master/cm/cmind/artifact.py#L7).

Note that "automation_uid" is empty because CM doesn't know yet if your artifact types exists globally and thus can't add CM UID.
We will explain how to reuse shared artifact types and automations later in this tutorial.

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

RUN cm pull repo mlcommons@ck

RUN cm find automation

RUN cm ...
```


### From zip file 

You can pack your CM repository to a zip file as follows:
```bash
cm pack repo my-cool-project

Packing repo from C:\Users\grigo\CM\repos\my-cool-project to cm.zip ...
```

You can then share *cm.zip* with your colleagues who can unpack it 
and install on their system using the following CM command:
```bash
cm unpack repo

cm find images
cm find experiments

```





## Adding reusable automations for related artifacts 

One of the goals of the [Collective Mind project (aka CK2)](https://arxiv.org/abs/2011.01149) 
is to gradually systematize all available artifacts and provide reusable automation actions 
to similar artifact types.

To be able to add automation actions to your artifact types and reuse them with others,
you need to add a *CM automation* for your artifact type as follows:

```bash
cm add automation {artifact type}
```

For example, you can add the following automations for this tutorial:
```bash
cm add automation images
cm add automation experiments
cm add automation models
```

Note that CM will add those automations to the "local" CM repository.
You can add them to another public or private repository as follows:
```bash
cm add automation my-cool-project:images
```

Or you can move your existing automation to another CM repository as follows:
```bash
cm move automation local:images my-cool-project:
```

Now, whenever you add a new artifact with an associated automation,
CM will find this automation and record "automation_uid" in the meta description 
of the newly created artifact!




## Adding reusable automation actions

We use Python as a simplified and portable DSL to implement reusable automation actions
for similar artifact types. 

You can find a Python module for your automation as follows:
```bash
cm find automation images
```

This directory will include a meta description of this automation in *_cm.json*
and a *module.py* with the automation actions.

This module inherits default "CM database actions" from the [Automation class](https://github.com/mlcommons/ck/blob/master/cm/cmind/automation.py) 
in the CM package such as "add", "rm", "find", "rename", etc.

It also includes a "test" automation action to help you understand the CM CLI:
```bash
cm test images

{
  "action": "test",
  "automation": "images",
  "out": "con",
  "parsed_automation": [
    [
      "images",
      "..."
    ]
  ]
}
```

You can add your own functions to this module that will be immediately accessible 
from the command line:
```bash
cm {my-new-automation} images
...
```
Note that all '-' characters in the automation action from the CLI will be converted into '_'.

Please check the following examples of internal CM automations to understand how to write
your own automation actions and apply them to artifacts: [CM internal repo](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation)

Now you can share your automation for a given artifact type in your private repository
with your colleagues or in your public repository with the whole world.

Others can pull your repository via *cm pull repo ...* and start reusing
the common automations and artifacts in their own projects.

Furthermore, everyone can now extend existing automation actions 
or contribute the new ones instead of reinventing the wheel!





## Extending meta descriptions of artifacts

Besides adding new common automation actions, the community can also gradually 
extend JSON or YAML files of shared artifacts to find a better way to describe them
when reusing them across different projects.

We hope that such Wikipedia-style mechanisms will help the community to gradually decompose 
all complex software and research projects into a collection of reusable artifacts and automation actions.







## Next steps

We are working with the community to develop [portable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
and help make ML Systems benchmarking, experimentation and MLOps more portable, deterministic, collaborative and reproducible
without the need for complex workflows: [tutorial for CM scripts](tutorial-scripts.md).
