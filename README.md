[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)
[![Dockerfile update for CM scripts](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml)

### License

[Apache 2.0](LICENSE.md)

### Copyright

2022-2024 [MLCommons](https://mlcommons.org)

### About

Collective Mind (CM) is a [community project](CONTRIBUTING.md) to develop 
a [collection of portable, extensible and reusable automation recipes 
with a human-friendly interface (aka CM scripts)](https://github.com/mlcommons/ck/tree/master/docs/list_of_scripts.md) 
to make it easier to modularize, build, run, benchmark and optimize complex AI/ML applications 
across diverse and continuously changing models, data sets, software and hardware
from Nvidia, Intel, AMD, Google, Qualcomm, Amazon and other vendors.

CM was originally designed based on the following feedback and requirements
from MLCommons engineers and researchers to have a common and technology-agnostic automation 
that help them simplify and automate development of complex MLPerf benchmarks and AI applications with diverse ML models:

* [CM automations](https://github.com/mlcommons/ck/tree/master/docs/list_of_scripts.md) 
  should run on any platform with any operating system either natively or inside containers
  in a unified and automated way;
* should require minimal learning curve and minimal software dependencies;
* should be non-intrusive and require minimal or no changes to existing projects;
* should automate all manual steps to prepare and run AI projects including detection and installation of dependencies, 
  substituting local paths, updating environment variables and generating command lines
  for a given platform;
* should be able to run native user scripts while unifying input/output to reuse all existing work;
* should avoid using complex Domain Specific Languages (DSL);
* should use plain Python with simple JSON/YAML configurations for portable automations;
* should be easily understandable and extensble even by non-specialists;
* should have a human-friendly command line with a very simple Python API.

However, the community also started using and extending 
[individual CM automation recipes](https://github.com/mlcommons/ck/tree/master/docs/list_of_scripts.md) 
to modularize and run other software projects and reproduce [research papers at Systems and ML conferences]( https://cTuning.org/ae/micro2023.html ) -
please check the [**Getting Started Guide**](docs/getting-started.md) 
to understand how they work, how to reuse and extend them for your projects,
and how to share your own automations in your public or private projects.


Just to give you a flavor of the [CM automation recipes](https://github.com/mlcommons/ck/tree/master/docs/list_of_scripts.md)
that can be chained into more complex automation workflows [using simple JSON or YAML](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml), 
here are a few most commonly used automation examples from the CM users 
that you can try yourself on Linux, MacOS, Windows and other platforms
with any hardware (you only need Python 3.7+, git, wget and PIP installed 
on your platform - check the [installation guide](docs/installation.md) for more details):

<details open>
<summary><b>CM human-friendly command line:</b></summary>


<sup>

```bash
pip install cmind

cm pull repo mlcommons@ck

cm run script "python app image-classification onnx"
cmr "python app image-classification onnx"

cmr "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e
cmr "python app image-classification onnx" --input=computer_mouse.jpg
cmr "python app image-classification onnx" --input=computer_mouse.jpg --debug

cm find script "python app image-classification onnx"
cm load script "python app image-classification onnx" --yaml

cmr "get python" --version_min=3.8.0 --name=mlperf-experiments
cmr "install python-venv" --version_max=3.10.11 --name=mlperf

cmr "get ml-model stable-diffusion"
cmr "get ml-model huggingface zoo _model-stub.alpindale/Llama-2-13b-ONNX" --model_filename=FP32/LlamaV2_13B_float32.onnx --skip_cache
cmr "get dataset coco _val _2014"
cmr "get dataset openimages" -j

cm show cache
cm show cache "get ml-model stable-diffusion"

cmr "get generic-python-lib _package.onnxruntime" --version_min=1.16.0
cmr "python app image-classification onnx" --input=computer_mouse.jpg

cm rm cache -f
cmr "python app image-classification onnx" --input=computer_mouse.jpg --adr.onnxruntime.version_max=1.16.0

cmr "get cuda" --version_min=12.0.0 --version_max=12.3.1
cmr "python app image-classification onnx _cuda" --input=computer_mouse.jpg

cm gui script "python app image-classification onnx"

cm docker script "python app image-classification onnx" --input=computer_mouse.jpg
cm docker script "python app image-classification onnx" --input=computer_mouse.jpg -j -docker_it

cm docker script "get coco dataset _val _2017" --to=d:\Downloads\COCO-2017-val --store=d:\Downloads --docker_cm_repo=ctuning@mlcommons-ck

cmr "run common mlperf inference" --implementation=nvidia --model=bert-99 --category=datacenter --division=closed
cm find script "run common mlperf inference"

cmr "get generic-python-lib _package.torch" --version=2.1.2
cmr "get generic-python-lib _package.torchvision" --version=0.16.2
cmr "python app image-classification torch" --input=computer_mouse.jpg

cm rm repo mlcommons@ck
cm pull repo --url=https://zenodo.org/records/10581696/files/cm-mlops-repo-20240129.zip

cmr "install llvm prebuilt" --version=17.0.6
cmr "app image corner-detection"

cmr "get conda"

cm pull repo ctuning@cm-reproduce-research-projects
cmr "reproduce paper micro-2023 victima _install_deps"
cmr "reproduce paper micro-2023 victima _run" 

```

</sup>

</details>

<details open>
<summary><b>CM unified Python API:</b></summary>

<sup>

```python
import cmind
output=cmind.access({'action':'run', 'automation':'script',
                     'tags':'python,app,image-classification,onnx',
                     'input':'computer_mouse.jpg'})
if output['return']==0: print (output)
```
</sup>

</details>


<details open>
<summary><b>Modular containers and GitHub actions with CM commands:</b></summary>

<small>

* https://github.com/mlcommons/inference/blob/master/.github/workflows/test-bert.yml
* https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference/dockerfiles/bert-99.9/ubuntu_22.04_python_onnxruntime_cpu.Dockerfile

</small>

</details>


### Documentation

* [Getting Started Guide](docs/getting-started.md)
  * [CM interface for MLPerf benchmarks](docs/mlperf)
  * [CM interface for ML and Systems conferences](docs/tutorials/common-interface-to-reproduce-research-projects.md)
  * [CM automation recipes for MLOps and DevOps](cm-mlops/script)
  * [Other CM tutorials](docs/tutorials)
* [Full documentation](docs/README.md)
* [CM and CK history](docs/history.md)

### Motivation and concepts

* ACM REP'23 keynote about MLCommons CM: [slides](https://doi.org/10.5281/zenodo.8105339)
* ACM TechTalk'21 about automating research projects: [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4)
* MLPerf inference submitter orientation: [slides](https://doi.org/10.5281/zenodo.8144274) 

### Get in touch

Collective Mind is a community project being developed by the 
[MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
with great help from [MLCommons members](https://mlcommons.org)
and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) -
our goal is to help everyone automate all manual and repetitive tasks 
to build, run, benchmark and optimize AI systems including 
downloading artifacts, installing tools, resolving dependencies, 
running experiments, processing logs, and reproducing results
on any software/hardware stack - you can reach us via [public Discord server](https://discord.gg/JjWNWXKxwT)
to discuss this project.
