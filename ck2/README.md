# Collective Mind toolkit

The Collective Mind toolkit (CM or CK2) transforms Git repositories, Docker containers, Jupyter notebooks and zip/tar files
into a collective database of reusable artifacts and automation scripts with a unified interface and extensible meta descriptions.

It is motivated by our tedious experience reproducing [150+ ML and Systems papers](https://www.youtube.com/watch?v=7zpeIVwICa4)
when our colleagues have spent many months analyzing the structure of ad-hoc projects, reproducing results
and [validating them in the real world](https://cKnowledge.org/partners.html) 
with different and continuously changing software, hardware, environments, data sets and settings.

That is why we have decided to develop a simple toolkit to help you share your artifacts, knowledge, 
experience and best practices with the whole world in a more reusable, automated, 
portable and reproducible way.

The CM toolkit is based on the [Collective Knowledge concept]( https://arxiv.org/abs/2011.01149 )
that was successfully validated in the past few years to 
[enable collaborative ML and Systems R&D](https://cKnowledge.org/partners.html),
modularize the [MLPerf inference benchmark](https://github.com/mlcommons/ck/tree/master/docs/mlperf-automation),
and [automate the development and deployment of Pareto-efficient ML Systems](https://www.youtube.com/watch?v=1ldgVZ64hEI).

See [related slides](docs/motivation.md) and a related article 
about ["MLOps Is a Mess But That's to be Expected"](https://www.mihaileric.com/posts/mlops-is-a-mess/) (March 2022).



# License

Apache 2.0



# How it works

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





# News

* **2022 April 20:** Join us at the public MLCommons community meeting. Register [here](https://docs.google.com/spreadsheets/d/1bb7qWgWM-6gop1Mwjm4u8LZtC7uqbee8C30DHipkkms/edit#gid=533252977).

* **2022 April 3:** We presented our approach to bridge the growing gap between ML Systems research and production 
  at the HPCA'22 workshop on [benchmarking deep learning systems](https://sites.google.com/g.harvard.edu/mlperf-bench-hpca22/home).

* **2022 March:** We presented our concept to [enable collaborative and reproducible ML Systems R&D](https://meetings.siam.org/sess/dsp_programsess.cfm?SESSIONCODE=73126) 
  at the SIAM'22 workshop on "Research Challenges and Opportunities within Software Productivity, Sustainability, and Reproducibility"

* **2022 March:** we've released the first prototype of [our toolkit ](https://github.com/mlcommons/ck/tree/master/ck2)
  based on your feedback and our practical experience [reproducing 150+ ML and Systems papers and validating them in the real world](https://www.youtube.com/watch?v=7zpeIVwICa4).
! 


# Research and development

## CM core enhancements

We use [GitHub tickets](https://github.com/mlcommons/ck/issues) 
to improve and enhance the CM core based on the feedback from our users!
Please don't hesitate to share your ideas and report encountered issues!

## CM-based automation scripts

* We work with the community to transform R&D projects [from ML and Systems papers](https://cTuning.org/ae) 
  into [reusable CM artifacts and automation scripts](docs/reusable-components.md). 
  Feel free to suggest your own automation recipes to be reused by the community.

## CM-based projects

* [Universal benchmarking of computational systems](docs/projects/universal-benchmarking.md).
* [Towards modular MLPerf benchmark](docs/projects/modular-mlperf.md).
* [MLPerf design space exploration](docs/projects/mlperf-dse.md).
* [Automated deployment of Pareto-efficient ML Systems](docs/projects/production-deployment.md).

# Resources

* [MLOps projects](docs/KB/MLOps.md)

# Acknowledgments

We thank the [users and partners of the original CK framework](https://cKnowledge.org/partners.html), 
[OctoML](https://octoml.ai), [MLCommons](https://mlcommons.org) 
and all our colleagues for their valuable feedback and support!

# Contacts

* [Grigori Fursin](https://cKnowledge.io/@gfursin) - author and coordinator
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) - coordinator and maintainer
