[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![arXiv](https://img.shields.io/badge/arXiv-2406.16791-b31b1b.svg)](https://arxiv.org/abs/2406.16791)
[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### About

Collective Mind (CM) is a collection of portable, extensible, technology-agnostic and ready-to-use automation recipes
with a human-friendly interface (aka CM scripts) to unify and automate all the manual steps required to compose, run, benchmark and optimize complex ML/AI applications 
on any platform with any software and hardware: see [CM4MLOps online catalog](https://access.cknowledge.org/playground/?action=scripts), 
[source code](https://github.com/mlcommons/ck/blob/master/cm-mlops/script), [ArXiv white paper]( https://arxiv.org/abs/2406.16791 ).

CM scripts require Python 3.7+ with minimal dependencies and are 
[continuously extended by the community and MLCommons members](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md)
to run natively on Ubuntu, MacOS, Windows, RHEL, Debian, Amazon Linux
and any other operating system, in a cloud or inside automatically generated containers
while keeping backward compatibility - please don't hesitate 
to report encountered issues [here](https://github.com/mlcommons/ck/issues) 
to help this collaborative engineering effort!

CM scripts were originally developed based on the following requirements from the
[MLCommons members](https://mlcommons.org) 
to help them automatically compose and optimize complex MLPerf benchmarks, applications and systems
across diverse and continuously changing models, data sets, software and hardware
from Nvidia, Intel, AMD, Google, Qualcomm, Amazon and other vendors:
* must work out of the box with the default options and without the need to edit some paths, environment variables and configuration files;
* must be non-intrusive, easy to debug and must reuse existing 
  user scripts and automation tools (such as cmake, make, ML workflows, 
  python poetry and containers) rather than substituting them; 
* must have a very simple and human-friendly command line with a Python API and minimal dependencies;
* must require minimal or zero learning curve by using plain Python, native scripts, environment variables 
  and simple JSON/YAML descriptions instead of inventing new workflow languages;
* must have the same interface to run all automations natively, in a cloud or inside containers.

[CM scripts](https://access.cknowledge.org/playground/?action=scripts) 
are used by MLCommons, cTuning.org and cKnowledge.org to modularize MLPerf inference benchmarks
(see [this white paper](https://arxiv.org/abs/2406.16791))
and help anyone run them across different models, datasets, software and hardware: 
https://docs.mlcommons.org/inference .

For example, you should be able to run the MLPerf inference benchmark on Linux, Windows and MacOS
using a few CM commands:

```bash

pip install cmind -U

cm pull repo mlcommons@cm4mlops --branch=dev

cm run script "run-mlperf-inference _r4.1 _accuracy-only _short" \
   --device=cpu \
   --model=resnet50 \
   --precision=float32 \
   --implementation=reference \
   --backend=onnxruntime \
   --scenario=Offline \
   --clean \
   --quiet \
   --time

cm run script "run-mlperf-inference _r4.1 _submission _short" \
   --device=cpu \
   --model=resnet50 \
   --precision=float32 \
   --implementation=reference \
   --backend=onnxruntime \
   --scenario=Offline \
   --clean \
   --quiet \
   --time

...

                                                                           0
Organization                                                         CTuning
Availability                                                       available
Division                                                                open
SystemType                                                              edge
SystemName                                                   ip_172_31_87_92
Platform                   ip_172_31_87_92-reference-cpu-onnxruntime-v1.1...
Model                                                               resnet50
MlperfModel                                                           resnet
Scenario                                                             Offline
Result                                                               14.3978
Accuracy                                                                80.0
number_of_nodes                                                            1
host_processor_model_name     Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz
host_processors_per_node                                                   1
host_processor_core_count                                                  2
accelerator_model_name                                                   NaN
accelerators_per_node                                                      0
Location                   open/CTuning/results/ip_172_31_87_92-reference...
framework                                                onnxruntime v1.18.1
operating_system               Ubuntu 24.04 (linux-6.8.0-1009-aws-glibc2.39)
notes                                     Automated by MLCommons CM v2.3.2.
compliance                                                                 1
errors                                                                     0
version                                                                 v4.1
inferred                                                                   0
has_power                                                              False
Units                                                              Samples/s


```

You can also run the same commands using a unified CM Python API:

```python
import cmind
output=cmind.access({
   'action':'run', 'automation':'script',
   'tags':'run-mlperf-inference,_r4.1,_performance-only,_short',
   'device':'cpu',
   'model':'resnet50',
   'precision':'float32',
   'implementation':'reference',
   'backend':'onnxruntime',
   'scenario':'Offline',
   'clean':True,
   'quiet':True,
   'time':True,
   'out':'con'
})
if output['return']==0: print (output)
```


We suggest you to use this [online CM interface](https://access.cknowledge.org/playground/?action=howtorun)
to generate CM commands that will prepare and run MLPerf benchmarks and AI applications across different platforms.


See more examples of CM scripts and workflows to download Stable Diffusion, GPT-J and LLAMA2 models, process datasets, install tools and compose AI applications:


```bash
pip install cmind -U

cm pull repo mlcommons@cm4mlops --branch=dev

cm show repo

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
cmr "get ml-model sdxl _fp16 _rclone"
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


cm rm repo mlcommons@cm4mlops
cm pull repo --url=https://zenodo.org/records/12528908/files/cm4mlops-20240625.zip

cmr "install llvm prebuilt" --version=17.0.6
cmr "app image corner-detection"

cm run experiment --tags=tuning,experiment,batch_size -- echo --batch_size={{VAR1{range(1,8)}}}
cm replay experiment --tags=tuning,experiment,batch_size

cmr "get conda"

cm pull repo ctuning@cm4research
cmr "reproduce paper micro-2023 victima _install_deps"
cmr "reproduce paper micro-2023 victima _run" 

```


See a few examples of modular containers and GitHub actions with CM commands:

* [GitHub action with CM commands to test MLPerf inference benchmark](https://github.com/mlcommons/inference/blob/master/.github/workflows/test-bert.yml)
* [Dockerfile to run MLPerf inference benchmark via CM](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference/dockerfiles/bert-99.9/ubuntu_22.04_python_onnxruntime_cpu.Dockerfile)


Please check the [**Getting Started Guide**](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md) 
to understand how CM automation recipes work, how to use them to automate your own projects,
and how to implement and share new automations in your public or private projects.


### Documentation

**MLCommons is updating the CM documentation based on user feedback - please stay tuned for more details**.

* [Getting Started Guide and FAQ](https://github.com/mlcommons/ck/tree/master/docs/getting-started.md)
  * [Common CM interface to run MLPerf inference benchmarks](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference)
  * [Common CM interface to re-run experiments from ML and Systems papers including MICRO'23 and the Student Cluster Competition @ SuperComputing'23](https://github.com/mlcommons/ck/tree/master/docs/tutorials/common-interface-to-reproduce-research-projects.md)
  * [Other CM tutorials](https://github.com/mlcommons/ck/tree/master/docs/tutorials)
* [Full documentation](https://github.com/mlcommons/ck/tree/master/docs/tutorials/README.md)

### Projects modularized and automated by CM

* [cm4research](https://github.com/ctuning/cm4research)
* [cm4mlops](https://github.com/mlcommons/cm4mlops)
* [cm4abtf](https://github.com/mlcommons/cm4abtf)

### License

[Apache 2.0](LICENSE.md)

### Citing CM

If you found CM useful, please cite this article: 
[ [ArXiv](https://arxiv.org/abs/2406.16791) ], [ [BibTex](https://github.com/mlcommons/ck/blob/master/citation.bib) ].

You can learn more about the motivation behind these projects from the following articles and presentations:

* "Enabling more efficient and cost-effective AI/ML systems with Collective Mind, virtualized MLOps, MLPerf, Collective Knowledge Playground and reproducible optimization tournaments": [ [ArXiv](https://arxiv.org/abs/2406.16791) ] 
* ACM REP'23 keynote about the MLCommons CM automation framework: [ [slides](https://doi.org/10.5281/zenodo.8105339) ] 
* ACM TechTalk'21 about automating research projects: [ [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4) ] [ [slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2021/grigorifursin_techtalk_slides.pdf) ]

### Acknowledgments

Collective Knowledge (CK) and Collective Mind (CM) were created by [Grigori Fursin](https://cKnowledge.org/gfursin),
sponsored by cKnowledge.org and cTuning.org, and donated to MLCommons to benefit everyone. 
Since then, this open-source technology (CM, CM4MLOps, CM4MLPerf, CM4ABTF, CM4Research, etc)
is being developed as a community effort thanks to all our
[volunteers, collaborators and contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md)! 
