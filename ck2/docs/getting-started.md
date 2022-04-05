***Under preparation ...***

# Getting Started with Collective Mind

Here we describe a few simple steps to help you install CM, 
share your artifact as a database inside your Git project, 
reuse it and share some common automation 
to reusable artifacts.


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

You will then likely create a README.md describing the structure 
and the content of your repository,
and how you ran your experiment.

Another person will need to read this README file to understand the structure
of your repository and either reproduce results or use some artifacts
in his or her own project.

### With CM

The idea behind CM is to perform very similar steps but just prefixed by *cm* 
to let CM index artifacts, add Unique IDs and extensible JSON/YAML meta descriptions,
and make them findable and reusable:

```bash
$ cm repo pull my-cool-project --url={GitHub repo URL} 
```

CM will pull this repository to *$HOME/CM/my-coolproject* and will register this location
in the CM-compatible repository index *$HOME/CM/repos.json*. 

This is needed to let CM automatically search for reusable artifacts and automations
in all CM-compatible directories.

However, if you forget the location, you can always find it using the following CM command:`
```bash
$ cm repo find my-cool-project
```

You can list all CM-compatible repositories and their locations as follows:
```bash
$ cm repo list
```
or
```bash
$ cm repo ls | sort

default = C:\!Progs\Python39\lib\site-packages\cmind-0.5.2-py3.9.egg\cmind\repo
local = C:\Users\grigo\CM\repos\local
my-cool-project = C:\Users\grigo\CM\repos\my-cool-project
octoml@mlops = C:\Users\grigo\CM\repos\octoml@mlops
```

Note that you always have at least 2 CM-compatible repositories after you use CM for the first time:
* '''default''' is a CM repository with reusable artifacts and automations that were moved 
  [inside the CM toolkit](https://github.com/mlcommons/ck/tree/master/ck2/cmind/repo) 
  to ensure their stability because they are frequently used by the community.

* '''local''' is a CM scratchpad repository where all new artifacts and automations 
  are created if a repository is not specified.




You can then use CM to create a similar structure as in the original Git repository:

```
$ cm images add my-cool-project:cool-cat --tags=dataset,image,cool,cat
```

CM created a directory *images/cool-cat* inside *my-cool-project* and added *_cm.json* with extensible meta description:
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

Note that CM also generated unique ID for this artifact. You can now find this artifact using its alias, UID or tags:
```bash
$ cm images find cool-cat
$ cm images find 780abfe6b8084327
$ cm images find *cat*
$ cm images find --tags=image,cat
``` 

You can now copy your cool-cat.jpeg to this directory:
```bash
$ cp cool-cat.jpeg `ck images find my-cool-project:


To be continued ...


## Reuse others' artifacts

[![CM artifact](https://img.shields.io/badge/Artifact-automated%20and%20reusable-blue)](https://github.com/mlcommons/ck/tree/master/ck2)
[![CM repository](https://img.shields.io/badge/Collective%20Mind-compatible-blue)](https://github.com/mlcommons/ck/tree/master/ck2)

### From command line

### From Python

### In Docker container

### In Jupyter notebook

### From zip file 


## Add reusable automations to related artifacts 


## Extend meta descriptions

## Extend automations

## Further thoughts

