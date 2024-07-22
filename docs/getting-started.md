[ [Back to documentation](README.md) ]

# Collective Mind Getting Started Guide and FAQ

<details>
<summary>Click here to see the table of contents.</summary>

* [Collective Mind Getting Started Guide and FAQ](#collective-mind-getting-started-guide-and-faq)
  * [Why CM?](#why-cm?)
  * [CM automation recipe for image classification](#cm-automation-recipe-for-image-classification)
  * [How CM scripts works?](#how-cm-scripts-works?)
  * [How CM runs automation recipes?](#how-cm-runs-automation-recipes?)
  * [How CM unifies inputs, outputs and environment variables?](#how-cm-unifies-inputs-outputs-and-environment-variables?)
  * [How CM chains automation recipes into portable workflows?](#how-cm-chains-automation-recipes-into-portable-workflows?)
  * [How to add new CM scripts?](#how-to-add-new-cm-scripts?)
  * [How to customize CM scripts using variations?](#how-to-customize-cm-scripts-using-variations?)
  * [How to cache and reuse CM scripts' output?](#how-to-cache-and-reuse-cm-scripts'-output?)
  * [How to use CM with Python virtual environments?](#how-to-use-cm-with-python-virtual-environments?)
  * [How to debug CM scripts?](#how-to-debug-cm-scripts?)
  * [How to extend/improve CM scripts?](#how-to-extend/improve-cm-scripts?)
  * [How to use CM with containers?](#how-to-use-cm-with-containers?)
  * [How to use CM GUI to run automation recipes?](#how-to-use-cm-gui-to-run-automation-recipes?)
  * [How to run MLPerf benchmarks via CM?](#how-to-run-mlperf-benchmarks-via-cm?)
  * [How to use CM to reproduce research papers?](#how-to-use-cm-to-reproduce-research-papers?)
  * [How to use CM as a common interface to other projects?](#how-to-use-cm-as-a-common-interface-to-other-projects?)
  * [Where to read about the CM vision and history?](#where-to-read-about-the-cm-vision-and-history?)
  * [How to get in touch with the CM community?](#how-to-get-in-touch-with-the-cm-community?)

</details>


## Why CM?

Collective Mind (CM) is a [community project](../CONTRIBUTING.md) to develop 
a [collection of portable, extensible, technology-agnostic and ready-to-use automation recipes
for MLOps and DevOps with a human-friendly interface (aka CM scripts)](https://access.cknowledge.org/playground/?action=scripts)
that can help to automate all the manual steps required to prepare, build, run, benchmark and optimize complex ML/AI applications 
on any platform with any software and hardware. 
They require Python 3.7+ with minimal dependencies and can run natively on Ubuntu, MacOS, Windows, RHEL, Debian, Amazon Linux
and any other operating system, in a cloud or inside automatically generated containers.

CM scripts were originally developed based on the following requirements from the
[MLCommons engineers and researchers](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md) 
to help them automatically build, benchmark and optimize complex MLPerf benchmarks
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

Let's use a relatively simple image classification example to explain how CM achieves that
and how it helps to automate much more complex projects including [MLPerf benchmarks](mlperf)
and [reproducibility initatives](https://cTuning.org/ae/micro2023.html)
at ML and Systems conferences.

<details closed>
<summary><b>Expand to see the feedback and requirements from MLCommons researchers and engineers</b></summary>


While image classification sounds like a trivial example nowadays, it may still require many manual steps
to download some validation data sets and models, install frameworks and low-level dependencies
and update various environment variables and paths depending on your platform and target hardware 
(for example CPU vs CUDA).

You may also need to make sure that all dependencies are compatible (for example that ONNX run-time 
or PyTorch framework is compatible with your CUDA version, etc).
Of course, you can also develop a container and fix all the versions but what if you or someone else 
want to try a different CUDA version or newer ONNX/TF/PyTorch framework or different operating system
or different model or different data set or different framework or different hardware?

While helping MLCommons automate [MLPerf inference benchmarks](https://github.com/mlcommons/inference) 
and run them across diverse models, data sets, software and hardware, 
we've realized that there is no portable and technology-agnostic automation tool 
that can handle such cases.

The feedback from [MLCommons engineers and researchers](taskforce.md) motivated us
to develop a simple automation framework that can help them 
assemble, run, benchmark and optimize complex AI/ML applications 
across diverse and continuously changing models, data sets, software and hardware
from Nvidia, Intel, AMD, Google, Qualcomm, Amazon and other vendors.

</details>

## CM automation recipe for image classification

We designed CM as a [small Python library](https://github.com/mlcommons/ck/tree/master/cm) 
with a human-friendly command line, simple Python API and minimal dependencies 
needed to implement automation recipes (Python 3.7+, PIP, pyyaml, git, wget)
and chain them into portable workflows. CM scripts can run natively (development mode) 
or inside containers that CM generates on the fly (stable mode).

Most of the time, these dependencies are already installed on your platform.
In such case, you should be able to prepare and run image classification with ONNX,
ImageNet validation data set and ResNet-50 on Linux, MacOS, Windows and any other
operating system using a few CM commands:

<sup>

```bash
pip install cmind
cm pull repo mlcommons@cm4mlops --checkout=dev
cm run script "python app image-classification onnx _cpu"
```

</sup>

*Note that you may need to re-login when you install cmind for the first time
 to let your platform pick up path to the `cm` command line front-end.*

You can also run and customize above automation recipe in alternative ways as follows:

<sup>

```bash
cm run script "python app image-classification onnx _cpu" --help

cm run script "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e
cm run script "python app image-classification onnx _cpu" --input=computer_mouse.jpg

cmr "python app image-classification onnx _cpu" --input=computer_mouse.jpg
cmr --tags=python,app,image-classification,onnx,_cpu --input=computer_mouse.jpg
cmr 3d5e908e472b417e --input=computer_mouse.jpg

cm docker script "python app image-classification onnx _cpu" --input=computer_mouse.jpg

cm gui script "python app image-classification onnx _cpu"

```

</sup>

If you encounter some issues, please check [CM installation guide](installation.md) - 
if it doesn't help you, please report your issues [here](https://github.com/mlcommons/ck/issues) 
and/or contact us via our [public Discord server](https://discord.gg/JjWNWXKxwT) - 
CM is a [community project](../CONTRIBUTING.md) being developed 
and improved across diverse software and hardware  based on your feedback! 



## How CM scripts works?

Next, we briefly explain how CM commands work - it will help you understand
what happens when you see similar commands in MLPerf results, README files, 
technical reports, research papers, Jupyter notebooks, 
Google colab, containers, scripts and artifact appendices.

Whenever you run `cm run script "python app image-classification onnx _cpu"` 
or `cmr "python app image-classification onnx _cpu"`, 
the [CM script automation](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/script/module.py) 
will simply search for `_cm.yaml` and `_cm.json` files (CM meta-description dictionary) in all `script` 
directories in all software projects registered in CM via `cm pull repo`.

In our case, we've pulled [github.com/mlcommons/ck project](https://github.com/mlcommons/ck)
that has most MLCommons' CM automation recipes embedded 
in a [`cm-mlops/script` directory](https://github.com/mlcommons/ck/tree/master/cm-mlops/script). 

*Note that you can pull any public or private Git repository, download any software project
 or register any local directory in the CM to search for embedded automation recipes.*

CM will then try to match all your tags without `_` prefix (`_` in tags mark 
the so-called CM script variations that customize a give script behavior 
and will be described later)  with a `tags` list in the CM meta-description dictionary.
In our case, it will match the corresponding [`_cm.yaml`](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L9) 
in `$HOME/CM/repos/mlcommons@cm4mlops/script/app-image-classification-onnx-py/_cm.yaml` - 
a wrapper for a given CM automation recipe.

*Note that if you use unique ID instead of tags to identify automation (such as `3d5e908e472b417e`), 
 CM will try to match `uid` string in the CM meta descriptions instead of tags.*


## How CM runs automation recipes?

Whenever CM finds a directory with a requested automation recipe, 
it performs the following steps:
* run `preprocess` function in `customize.py` if exists
* run `run.sh` (Linux) or `run.bat` (Windows) if exists
* run `postprocess` function in `customize.py` if exists

Such organization makes it possible to use either Python or native OS scripts or
both to implement CM automation recipes while minimizing the learning curve
for CM understanding, development and debugging as requested by CM users.

Furthermore, CM scripts can keep the source code of
image classification (as shown [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py/src))
that we can easily move around
between projects without hardwiring paths and names.

## How CM unifies inputs, outputs and environment variables?

CM allows you to pass environment variables to `customize.py`
and native scripts using `--env.ENV=VALUE`. 

When you use some flags such as `--input` in our image classification
example, it will be also converted into an environment variable
using [`input_mapping` dictionary](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L78) 
in the CM meta description of this script.

All environment variables are aggregated in `env` dictionary inside CM
and then passed to `preprocess` function in `customize.py` where you can modify
it programmatically. 

They are then passed to the `run` script. Since new environment variables
are not preserved after `run` script, one can pass new environment variables
back to CM using `tmp-run-env.out` with ENV=KEY strings as shown [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/run.sh#L37)
or using `tmp-run-state.json` as shown [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/src/onnx_classify.py#L171).

## How CM chains automation recipes into portable workflows?

CM scripts provide a technology-agnostic wrapper with simple tags, CLI and Python API to prepare and run 
user code snippets and native scripts/tools while unifying their inputs and outputs, paths and environment variables.

Such architecture makes it possible to easily chain existing user scripts and tools into portable, technology-agnostic and powerful workflows
instead of substituting or rewriting them.

It is possible to chain CM scripts using simple 
[`deps` list](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L21) 
in a meta description of a given script:

<sup>

```yaml
deps:
- tags: detect,os
- tags: get,sys-utils-cm
- names:
  - python
  - python3
  tags: get,python3

- tags: get,cuda
  names:
  - cuda
  enable_if_env:
    USE_CUDA:
    - yes
- tags: get,cudnn
  names:
  - cudnn
  enable_if_env:
    USE_CUDA:
    - yes

- tags: get,dataset,imagenet,image-classification,original
- tags: get,dataset-aux,imagenet-aux,image-classification
- tags: get,ml-model,resnet50,_onnx,image-classification
  names:
  - ml-model

- tags: get,generic-python-lib,_package.Pillow
- tags: get,generic-python-lib,_package.numpy
- tags: get,generic-python-lib,_package.opencv-python


- tags: get,generic-python-lib,_onnxruntime
  names:
  - onnxruntime
  skip_if_env:
    USE_CUDA:
    - yes
- tags: get,generic-python-lib,_onnxruntime_gpu
  names:
  - onnxruntime
  enable_if_env:
    USE_CUDA:
    - yes

```

</sup>

Each entry in this list is a dictionary that specifies which CM script to run using `tags`.
Internally, CM will be updating `env` dictionary (flat environment) and `state` dictionary 
(to let scripts exchange complex data structures besides environment variables).

If you run CM via command line, you can see internal `env` and `state` dictionaries by adding `-j` flag:

```bash
cmr "python app image-classification onnx _cpu" --input=computer_mouse.jpg -j
```

*Note that we use similar approach for updating environment variables similar 
 to calling native scripts - by default, they do not alter environment
 variables at the host. However, CM allows you to do that 
 by explicitly specifying which environment variables and state keys
 will be updated at the host using `new_env_keys` and `new_state_keys`
 in the meta of a given script as shown [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L83).
 This helped us make behavior of complex CM workflows more deterministic
 and reproducible.*

Each sub-dependency can be turned on or off using environment variables
using `enable_if_env` dictionary or `disable_if_env` dictionary.

You can also specify `version_min`, `version_max` and `version` in these
dependencies. You can also give them some specific names such as `python`
and pass versions and environment variables only to a specific script in a pipeline as follows:
```bash
cmr "python app image-classification onnx _cpu" --input=computer_mouse.jpg --adr.python.version_min=3.9
```

This functionality is usually implemented inside ad-hoc bash or shell scripts 
with many hardwired paths and names - CM simply makes such scripts and tools 
portable and reusable while enabling technology-agnostic automation workflows 
with a unified interface that can adapt to any operating system and are easy 
to understand.

We can now assemble complex automation workflows by reusing all portable
scripts from [the community](https://access.cknowledge.org/playground/?action=scripts).

In our example, we reused CM scripts to [detect OS features](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os), 
install system dependencies on [any supported OS](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm) 
(Ubuntu, MacOS, RHEL, Arch, Debian, SLES, Windows, etc),
detect or install Python and PIP packages, download and preprocess data sets and models, etc.



## How to add new CM scripts?

One the main requirement for CM was to provide a very light-weight connectors 
between existing automation scripts and tools rather than substituting them.

You can add your own scripts and tools to CM using the following command
that will create a ready-to-use dummy CM script:

```bash
cm add script my-script --tags=my,script
```

You can already run this dummy script and plug it into other CM workflows:
```bash
cmr "my script"
```

You can also run it from python as follows:
```bash
import cmind
output=cmind.access({'action':'run', 
                     'automation':'script', 
                     'tags':'my,script})
if output['return']==0: print (output)
```


## How to customize CM scripts using variations?

Sometimes we need to set multiple environment variables or run a set of extra CM scripts
for a specific purpose (different hardware target or model or dataset).

We introduced special tags with `_`, called *variations* or *variation tags*, 
that allow you to update a set of environment variables and add extra scripts
to the chain of dependencies.

Such variations are defined using [`variations` dictionary](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L66) 
in the meta description of a given CM script.

For example, our script has 2 variations `_cuda` and `_cpu`.

If you want to use CUDA implementation of the image classification example, 
you can add this variation to the tags that will set `USE_CUDA` environment to `yes`
and will turn on a specific CM script in `deps` to install ONNX for CUDA:

```bash
cmr "python app image-classification onnx _cuda" --input=computer_mouse.jpg
```

## How to cache and reuse CM scripts' output?

By default, CM scripts run in the current directory and record all new files there.

For example, the following universal download script will download 
computer mouse image to the current directory:

<sup>

```bash
cm run script "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e
```

</sup>

In some cases, we want to cache and reuse the output of automation recipes (such as downloading models, preprocessing data sets or building some applications)
rather than just downloading it to the current directory.

Following the feedback from our users, we implemented a `cache` automation in CM similar to `script`.
Whenever CM encounters `"cache":true` in a meta description of a given script, it will create
a `cache` directory in `$HOME/CM/repos/local` with some unique ID and the same tags as `script`,
and will execute that script there to record all the data in cache. 

Whenever the same CM script is executed and CM finds an associated cache entry, 
it will skip execution and will reuse files from that entry.

Furthermore, it is possible to reuse large cached files in other projects that call the same CM scripts!

You can see cache entries and find a specific one as follows:

```bash
cmr "get ml-model resnet50 _onnx" -j

cm show cache
cm show cache "get ml-model resnet50 _onnx" 
cm find cache "download file ml-model resnet50 _onnx" 
cm info cache "download file ml-model resnet50 _onnx" 
```

You can clean some cache entries as follows:
```bash
cm rm cache --tags=ml-model,resnet50
```

You can also clean all CM `cache` entries and start from scratch as follows:
```bash
cm rm cache -f
```

In fact, you can remove `$HOME/CM` to reset CM framework completely
and remove all downloaded repositories and cached entries.



## How to use CM with Python virtual environments?


Using CM `cache` makes it possible to run CM automations for multiple virtual environments
installed inside CM `cache` entries. It is possible to run CM automations with different Python
virtual environments transparently to users while avoiding messing up native user environment.

We created the following CM automation recipe to create virtual environments:

```bash
cmr "install python-venv" --name=mlperf
cm show cache "python-venv name-mlperf"
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```

If you now run our image classification automation recipe, 
it will reuse model and dataset from the cache, but will
use 


## How to debug CM scripts?

One of the requirements from CM users was to avoid new and/or complex ways to debug CM automations.
Using native scripts and Python code makes it possible to apply standard techniques and tools to debug CM automations.

We were also asked to add `--debug` flag to open a shell after the last native script is executed - 
this allows users to rerun the last command line with all environment variables and paths assembled by CM
while having a full and native access to change environment and run the final command 
(such as pinning threads, changing batch sizes, modifying files, etc).

You can try it as follows on Linux, MacOS, Windows or other operating system as follows:

```bash
cmr "python app image-classification onnx _cpu" --input=computer_mouse.jpg --debug

```

You can also use GDB via environment variable `--env.CM_RUN_PREFIX="gdb --args "`
to run the final command via GDB.



## How to extend/improve CM scripts?

CM is a [community project](../CONTRIBUTING.md) where [CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) 
are continuously improved to run on different hardware with different software 
while keeping backward compatibility through the unified CM interface, tags and variations.

Whenever you encounter an issue or want to have support for your own project and environment, 
please update these scripts and send a PR to the [CM GitHub](https://github.com/mlcommons/ck).

You can also reach us via [public Discord server](https://discord.gg/JjWNWXKxwT) 
if you questions or suggestions.





## How to use CM with containers?

One of the key requirements for CM was to run automation natively or inside containers in the same way.

We want CM scripts to adapt to the current/latest environment natively or run in the
container automatically generated on the fly when requested by user for more stability and determinism.

In such case, we can get rid of separate development of native scripts/workflows and Dockerfile 
and use the same CM commands instead.

To run a given script in an automatically-generated container, you can simply substitute `cm run script` 
with `cm docker script` or `cmr` with `cmrd`:

```bash
cm docker script "python app image-classification onnx _cpu"
```

CM will automatically generate a Dockerfile with Ubuntu 22.04 in the `dockerfiles` 
directory of a given script, will build container with the same CM command
and will run it inside container.

* If you want to stay in the container, you can add flag `--docker_it`.
* You can change OS inside container using `--docker_base_image`, `--docker_os` and `--docker_os_version`.

The tricky part is when we want to use host files and directories with a given CM script inside container. 
To make it easier for users, we have implemented automatic detection and mounting of files and directories 
in CM script.

Developers of a CM script just need to specify which flags and environment variables are local files or directories
using `input_paths` in `docker` dictionary of the meta-description of this script:

```yaml
docker:
  skip_run_cmd: 'no'
  all_gpus: 'yes'
  input_paths:
    - input
    - env.CM_IMAGE
    - output
  skip_input_for_fake_run:
    - input
    - env.CM_IMAGE
    - output
    - j
  pre_run_cmds:
    - echo \"CM pre run commands\"
```

When you run the same script via container with the local computer_mouse.jpg file as an input,
CM will automatically mount current directory and will update the input to the CM script
inside container with the internal path:

<sup>

```bash
cm docker script "python app image-classification onnx _cpu" --input=computer_mouse.jpg

...

docker build  -f D:\Work1\CM\ck\cm-mlops\script\app-image-classification-onnx-py\dockerfiles\ubuntu_22.04.Dockerfile \
              -t cknowledge/cm-script-app-image-classification-onnx-py:ubuntu-22.04-latest .

...

Container launch command:
docker run  --entrypoint ""  --gpus=all -v D:\Work1\CM\ck\docs\computer_mouse.jpg:/cm-mount/Work1/CM/ck/docs/computer_mouse.jpg 
                            cknowledge/cm-script-app-image-classification-onnx-py:ubuntu-22.04-latest 
                            bash -c "echo \"CM pre run commands\" && 
                            cm run script --tags=python,app,image-classification,onnx,_cpu 
                            --input=/cm-mount/Work1/CM/ck/docs/computer_mouse.jpg "

CM pre run commands


```

</sup>

It is now possible to download large data sets and models to the host from CM containers
or pass host scratch pads and data to CM containers transparently to a user!



## How to use CM GUI to run automation recipes?

Another request from CM/MLCommons users was to have a simple GUI that can generate CM commands with user-friendly selector.

We've implemented a CM script called [`gui`](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui) 
that provides a universal Streamlit GUI for any CM script. 

You just need to describe the inputs for a given script via [meta-description](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L91)
as shown for our image classification example:

```yaml
input_description:
  input: 
    desc: "Path to JPEG image to classify"
  output: 
    desc: "Output directory (optional)"
  j:
    desc: "Print JSON output"
    boolean: true
```

You can run this GUI for your CM script as follows:
```bash
cm gui script "python app image-classification onnx _cpu"
```

This GUI will allow you to customize your script and run it on your host.


## How to run MLPerf benchmarks via CM?

CM was originally designed to make it easier to run [MLPerf inference benchmarks](https://arxiv.org/abs/1911.02549).

While MLPerf inference has a common benchmarking engine called [loadgen](https://github.com/mlcommons/inference/tree/master/loadgen),
setting up a given platform, installing all tools, downloading and preprocessing all models and data sets, 
updating paths and environment variables, figuring out default parameters for various scenarios, preparing a loadgen command line,
keeping track of continuous updates in MLPerf rules, running multiple experiments and submitting results
is a major challenge for old and new submitters (see [MLPerf inference v4.0 submitter orientation for automation](https://doi.org/10.5281/zenodo.10605079).

We created several CM scripts to prepare and run different implementations of MLPerf inference (reference, Nvidia, Intel, Qualcomm, Deep Sparse, etc)
with a master CM script to run them all out-of-the-box natively or inside automatically-generated containers 
[run-mlperf-inference-app](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app).
CM helped us to implement it as a simple pipeline with a common and human-friendly interface while reusing all existing automation recipes.

This script was successfully validated to [modularize MLPerf inference benchmarks](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/README.md) 
and help the community automate more than 95% of all performance and power submissions in the v3.1 round
across more than 120 system configurations (models, frameworks, hardware) 
while reducing development and maintenance costs.

Please check this [documentation](mlperf/inference) for more details.


## How to use CM to reproduce research papers?

Following the successful validation of CM concept to modularize and run MLPerf inference benchmarks across diverse software and hardware,
the community test it to make it easier to reproduce results from research papers during artifact evaluation and other reproducibility
initiatives at [systems conferences](https://ctuning.org/ae/micro2023.html).

The idea is to provide a common interface to prepare and run experiments from research papers.
See the latest CM scripts to rerun some experiments from the [ACM/IEEE MICRO'23 conference](https://github.com/ctuning/cm4research/tree/main/script)
and from the [Student Cluster Competition at Supercomputing'23](tutorials/scc23-mlperf-inference-bert.md).


## How to use CM as a common interface to other projects?

While CM was successfully validated to unify, modularize and automate MLPerf benchmarks,
it turned out to be applicable to any software project. 

The community started using CM as a common and human-friendly interface to run other software projects 
and manage experiments across diverse models, data sets, software and hardware while making them more modular, 
portable and reusable.

Please check [other CM tutorials](tutorials), [CM documentation](README.md) and our [ACM REP'23 keynote](https://www.youtube.com/watch?v=7zpeIVwICa4)
for more details.


## Where to read about the CM vision and history?

* ACM REP'23 keynote about MLCommons CM: [slides](https://doi.org/10.5281/zenodo.8105339) [YouTube](https://youtu.be/_1f9i_Bzjmg)
* ACM TechTalk'21 about automating research projects: [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4) [slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2021/grigorifursin_techtalk_slides.pdf)
* [Project history](history.md)


## How to get in touch with the CM community?

This is a community project being developed by the [MLCommons Task Force on Automation and Reproducibility](taskforce.md)
based on your feedback and [contributions](../CONTRIBUTING.md) - please join our [public Discord server](https://discord.gg/JjWNWXKxwT) if you 
would like to help with developments or have questions, suggestions and feature requests.
