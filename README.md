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

Collective Mind (CM) is a human-friendly interface to help everyone run, manage and reuse
a [growing number of MLPerf, MLOps and DevOps scripts](https://github.com/mlcommons/ck/tree/master/docs/list_of_scripts.md)
from [MLCommons projects](https://mlcommons.org) and [research papers](https://cTuning.org/ae)
in a unified way on any operating system with any software and hardware
either natively or inside containers.

Here are a few most commonly used examples from the CM users 
that should run in the same way on Linux, MacOS, Windows and other platforms
(see [Gettings Started Guide](docs/getting-started.md) to understand 
how they work and how to reuse them in your projects):

```bash
pip install cmind

cm pull repo mlcommons@ck

cm run script "python app image-classification onnx"
cmr "python app image-classification onnx"

cmr "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e
cmr "python app image-classification onnx" --input=computer_mouse.jpg
cmr "python app image-classification onnx" --input=computer_mouse.jpg --debug

cm find script "python app image-classification onnx"

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

cmr "cm gui" --script="python app image-classification onnx"

cm docker script "python app image-classification onnx" --input=computer_mouse.jpg
cm docker script "python app image-classification onnx" --input=computer_mouse.jpg -j -docker_it

cmr "run common mlperf inference" --implementation=nvidia --model=bert-99 --category=datacenter --division=closed
cm find script "run common mlperf inference"

cmr "install llvm prebuilt" --version=17.0.6
cmr "app image corner-detection"

cmr "get conda"

cm pull repo ctuning@cm-reproduce-research-projects
cmr "reproduce paper micro-2023 victima _install_deps"
cmr "reproduce paper micro-2023 victima _run" 


```

```python
import cmind
output=cmind.access({'action':'run', 'automation':'script',
                     'tags':'python,app,image-classification,onnx',
                     'input':'computer_mouse.jpg'})
if output['return']==0: print (output)
```


Collective Mind is a community project being developed by the 
[MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
with great help from [MLCommons (70+ AI organizations)](https://mlcommons.org/,
[research community]( https://www.youtube.com/watch?v=7zpeIVwICa4 )
and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) -
we want to have a simple, non-intrusive, technology-agnostic, portable and easily-extensible interface 
to automate all our manual and repetitive tasks including 
downloading artifacts, installing tools, resolving dependencies, 
running experiments, processing logs, and reproducing results
without thinking where and how they run.

That is why we implemented CM as a [small Python library](https://github.com/mlcommons/ck/tree/master/cm) 
with minimal dependencies (Python 3.7+, git, wget), simple Python API, GUI and human-friendly command line.
CM simply searches for CM scripts by tags or Unique IDs in all pulled Git repositories, automatically generates command lines 
for a given script or tool on a given platform, updates all paths and environment variables, 
runs a given automation either natively or inside automatically-generated containers
and unifies input and output as a Python dictionary or JSON/YAML file.

Our goal is to make it easier to prototype, build, run, benchmark, optimize and manage complex AI/ML applications
across diverse and rapidly evolving models, data sets, software and hardware simply by chaining these 
unified CM scripts into [portable, human-readable and reusable workflows](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml).

For example, our [automation recipes](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md) 
helped [modularize MLPerf inference benchmark](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/README.md) 
and were successfully validated in the MLPerf inference benchmark v3.1 round
helping the community automatically submit more >95% of all performance and power results across
more than 120 system configurations (models, frameworks, hardware) while reducing their development
and maintainence costs.

Please check this [Getting Started tutorial](docs/getting-started.md) 
to understand how CM works and start using it.

Feel free to join [public Discord server](https://discord.gg/JjWNWXKxwT) 
if you would like to participate in collaborative developments
or have questions and suggestions.

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
