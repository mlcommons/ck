[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)
[![Dockerfile update for CM scripts](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml)

### About

Collective Mind (CM) is a lightweight, non-intrusive and technology-agnostic workflow automation framework 
to run and manage AI/ML benchmarks, applications and research projects in a unified and fully automated way
on any platform with any software stack using a common, simple and human-readable interface.

CM is being developed by the [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
based on the feedback from the [research community](https://www.youtube.com/watch?v=7zpeIVwICa4), Google, AMD, Neural Magic, OctoML, Nvidia, Qualcomm, Dell, HPE, Red Hat,
Intel, TTA, One Stop Systems, ACM and [other organizations and individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).

The goal is to help the community gradually convert all ad-hoc README files, papers, reports, Juputer notebooks and containers 
into [portable and reusable automation recipes (CM scripts)](https://github.com/mlcommons/ck/blob/master/cm-mlops/script)
that find and call existing scripts and tools via English-like language based on tags 
and glue them together via extensible JSON/YAML meta descriptions and simple Python logic.

For example, the following CM commands prepare and run image classification 
with ONNX on any platform with Linux, Windows and MacOS either natively or inside a containter:

```bash
pip install cmind

cm pull repo mlcommons@ck

cm run script "python app image-classification onnx"

cmr "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e
cmr "python app image-classification onnx" --input=computer_mouse.jpg -j

cm docker script "python app image-classification onnx" --input=computer_mouse.jpg
cm docker script "python app image-classification onnx" --input=computer_mouse.jpg -j

cmr "get coco dataset _val _2014"

cmr "get ml-model huggingface zoo _model-stub.alpindale/Llama-2-13b-ONNX" --model_filename=FP32/LlamaV2_13B_float32.onnx

cm show cache


```

*Note that `cmr` is a shortcut for `cm run script`.*

You can also run all above CM commands via a simple Python API with JSON input/output:
```python
import cmind

output=cmind.access({'action':'run', 'automation':'script',
                     'tags':'python,app,image-classification,onnx',
                     'input':'computer_mouse.jpg'})
if output['return']==0: print (output)
```

Such approach requires minimal learning curve and minimal or no changes to existing projects while helping 
to dramatically reduce time to understand how to run and customize numerous AI/ML projects 
across diverse and continuously changing models, datasets, software and hardware from different vendors.

It also helps to gradually abstract, automate, unify and reuse all manual, tedious and repetitive MLOps and DevOps tasks
including *downloading artifacts, installing tools, substituting paths, updating environment variables, preparing run-time
environments, generating command lines, processing logs and sharing results*: see the 
[catalog of automation recipes shared by MLCommons](docs/list_of_scripts.md).

Please check this [Getting Started tutorial](docs/getting-started.md) to understand
how CM works and start using it.

### Documentation

* [Getting Started tutorial](docs/getting-started.md)
  * [CM interface for MLPerf benchmarks](docs/mlperf)
  * [CM interface for ML and Systems conferences](docs/tutorials/common-interface-to-reproduce-research-projects.md)
  * [CM automation recipes for MLOps and DevOps](cm-mlops/script)
  * [Other CM tutorials](docs/tutorials)
* [Full documentation](docs/README.md)
* [CM and CK history](docs/history.md)

### Motivation and concepts

* MLPerf inference submitter orientation: [slides](https://doi.org/10.5281/zenodo.8144274) 
* ACM REP'23 keynote about CM concepts: [slides](https://doi.org/10.5281/zenodo.8105339)

### Copyright

2022-2024 [MLCommons](https://mlcommons.org)

### License

[Apache 2.0](LICENSE.md)

### Discord server

This project is under heavy development based on user feedback - 
feel free to get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT) 
if you have questions, suggestions and feature requests.
