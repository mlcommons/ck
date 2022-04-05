# Getting Started


## Install CM

CM toolkit is implemented as a small Python library with a unified CLI and a simple API.

It requires minimal dependencies (Python 3+, pip, pyyaml and a Git client) 
and should work with any OS including Linux, CentOS, Debian, RedHat and Windows.

```bash
$ pip3 install cmind
```

You can find more details about the installation process [here](docs/installation.md).

## Share some artifact 

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

### Using CM

The idea behind CM is to let you perform similar steps just prefixed by *cm* 
to let CM index artifacts and make them findable and reusable:

```bash
$ cm repo pull my-cool-project --url={GitHub repo URL} 
```

CM will pull and register this repository. You can find where it is located on your system using CM command:`
```bash
$ cm repo find my-cool-project
```

You can then use CM to create similar structure:
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



