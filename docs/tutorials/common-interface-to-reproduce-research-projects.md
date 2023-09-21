[ [Back to index](../README.md) ]

<details>
<summary>Click here to see the table of contents.</summary>

* [Tutorial: Adding a common interface to reproduce research projects](#tutorial-adding-a-common-interface-to-reproduce-research-projects)
  * [Motivation](#motivation)
  * [Examples:](#examples)
  * [Installing CM language](#installing-cm-language)
  * [First approach: adding CM script to a common repository](#first-approach-adding-cm-script-to-a-common-repository)
    * [Fork main repository](#fork-main-repository)
    * [Copy demo script](#copy-demo-script)
    * [Edit wrappers](#edit-wrappers)
    * [Set up virtual environment before running experiments](#set-up-virtual-environment-before-running-experiments)
    * [Run experiments](#run-experiments)
  * [Second approach: adding CM interface to your research project](#second-approach-adding-cm-interface-to-your-research-project)
    * [Local directory](#local-directory)
    * [Git project](#git-project)
  * [Adding CM script to prepare and run your experiment](#adding-cm-script-to-prepare-and-run-your-experiment)
  * [Testing and extending CM script](#testing-and-extending-cm-script)
  * [Adding extra Git repositories with artifacts to dependencies](#adding-extra-git-repositories-with-artifacts-to-dependencies)
  * [Sharing this script with the community and artifact evaluators](#sharing-this-script-with-the-community-and-artifact-evaluators)
  * [Automating experiments, autotuning and visualization](#automating-experiments-autotuning-and-visualization)
  * [Participating in discussions and developments](#participating-in-discussions-and-developments)

</details>

# Tutorial: Adding a common interface to reproduce research projects

## Motivation

While working with the community to reproduce and/or replicate [150+ research papers](https://learning.acm.org/techtalks/reproducibility) 
during [artifact evaluation](https://cTuning.org/ae), we have seen that reviewers spend most of their time
at the kick-the-tires phase deciphering numerous ad-hoc READMEs and scripts to figure out how to prepare and run shared applications. 

That motivated us to develop a [simple automation language (Collective Mind)](https://doi.org/10.5281/zenodo.8105339) 
to provide the same common interface to prepare, run and visualize experiments
from any paper or research project.

The goal is to make it easier for the community and evaluators 
to start reproducing/replicating research results 
and even fully automate this process in the future.

## Examples:

* [CM tutorial](reproduce-research-paper-ipol.md) to reproduce an IPOL journal paper.
* [CM script](../../cm-mlops/script/reproduce-micro-paper-2023-victima) to reproduce results from a MICRO paper.


## Installing CM language

CM requires minimal dependencies (Python 3+ and Git) and it should be straightforward to install it
on Linux, MacOS, Windows and any other platform using this [guide](../installation.md).

If you encounter any issue, please don't hesitate to tell us via [Discord server](https://discord.gg/JjWNWXKxwT) 
and/or open a ticket [here](https://github.com/mlcommons/ck/issues).



## First approach: adding CM script to a common repository


### Fork main repository

You can simply add a new CM script to the [MLCommons repository](https://github.com/mlcommons/ck) 
to prepare, run and visualize your experiments without any changes required to your original repository.

First, create your fork of [this repository](https://github.com/ctuning/mlcommons-ck)
and pull it via CM:
```bash
cm pull repo --url={fork of https://github.com/ctuning/mlcommons-ck}
```

### Copy demo script

You can then copy [the CM script "reproduce-micro-paper-2023-victima"
from a MICRO paper with Artifact Evaluation](../../cm-mlops/script/reproduce-micro-paper-2023-victima)
to a new script with your paper/artifact name as follows:
```bash
cm copy script reproduce-micro-paper-2023-victima reproduce-micro-paper-2023-{new name}
```

### Edit wrappers

You can then find its directory and edit `_cm.yaml`, `install_deps.sh`, `run.sh` and `plot.sh`
to pull your Git repository with your artifacts and call your scripts to install dependencies,
run experiments and plot results from above wrappers:
```bash
cm find script reproduce-micro-paper-2023-{new name}
```

You can now add this directory to your fork and create a PR.

### Set up virtual environment before running experiments

We suggest to use virtual environment installed via CM as follows:
```bash
cm run script "install python-venv" --name=ae
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=ae"
```

### Run experiments

Each paper should have a CM script with the following variations:
`install_deps`, `run` and `plot`

It's possible to run them as follows:
```bash
cm find script --tags=reproduce,paper
cm run script {name from above list} --tags=_{variation}
```




## Second approach: adding CM interface to your research project

First, you also need to install the following CM repository with reusable CM scripts 
shared by the MLCommons task force on automation and reproducibility
to make it easier to run and reproduce ML and Systems applications and benchmarks
across diverse software and hardware:

```bash
cm pull repo ctuning@mlcommons-ck
```


### Local directory

To initialize a CM repository/interface in a local project directory,
you need to go there and run the following CM command
while substituting `my-research-project` with a unique name:

```bash
cm init repo my-research-project --path=. --prefix=cmr
```

If this research project is associated with artifact evaluation, we suggest to use
the name of the conference and your paper ID such as `micro-2023-038` for ACM MICRO.

This command will create a `cmr.yaml` file with a description and unique ID of this repository,
and will register it in the CM. Note that all CM automations and artifacts will be located
in the `cmr` sub-directory to avoid contaminating your project. They can be deleted
or moved to another project at any time.

### Git project

If you use Git for your project, we suggest to initialize your repository
as follows:
```bash
cm pull repo my-research-project --url={Git URL}
```

In such case, CM will pull your Git repository, initialize CM interface and register it in the CM.

You can see your registered CM repositories as follows:
```bash
cm list repo
```

You can find the location of your Git repository in CM for further editing as follows:
```bash
cm find repo my-research-project
```


## Adding CM script to prepare and run your experiment

You can now add CM interface ([CM scripts](../../cm-mlops/automation/script/README-extra.md)) 
to your CM-compatible research project to wrap your native scripts and run experiments as follows:

```bash
cm add script my-research-project:reproduce-paper-micro-2023-016 \
           --tags=reproduce,paper,micro,2023,016 \
           --script_name={name of your script} \
           --template=ae-python
```

Please add `--json` flag if you prefer to describe your dependencies and execution workflow in JSON instead of YAML format (default).

You can now find and edit the newly created template script using its alias as follows:
```bash
cm find script reproduce-paper-micro-2023-016
```
You can also use tags to find your template script (preferred way since alias may change in the future):
```bash
cm find script --tags=reproduce,paper,micro,2023,016
```

You must update the script after editing it's meta to cache it for fast search:
```bash
cm update script reproduce-paper-micro-2023-016
```

If you use extra frameworks and libraries such as PyTorch and CUDA, you can create a new script with a template "pytorch" as follows:

```bash
cm add script my-research-project:reproduce-paper-micro-2023-016-2 \
           --tags=reproduce,paper,micro,2023,016-2
           --template=pytorch
```

It will include all the necessary CM dependencies to detect and/or install Python, CUDA, PyTorch, etc.

If you use Python, we suggest to use virtual environment installed via CM as follows:
```bash
cm run script "install python-venv" --name=ae
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=ae"
```


## Testing and extending CM script

You can already run your native script via CM interface and pass environment variables as follows:

```bash
cm run script "reproduce micro 2023 paper 016" --env.KEY1=VAL1 --env.KEY2=VAL2 ...
```

Furthermore, you can run extra dummy scripts automatically generated for you via so-called CM variations
(`install_deps, run, reproduce, plot, analyze,  validate`):
```bash
cm run script "reproduce micro 2023 paper 016 _{variation}" --env.KEY1=VAL1 --env.KEY2=VAL2 ...
```

Each variation invokes an associated script `{variation}.sh` or `{variation}.bat` and can be extended by a user.

From this moment, you can extend meta description of this script (`_cm.json` or `_cm.yaml`)
to add dependencies on other CM scripts to detect and/or install tools, data sets, models and other artifacts,
extend `customize.py` to update environment variables based on dependencies and run other native scripts
before executing the main native script, post-process and unify output, etc.

You can read about the CM script concept [here](../../cm-mlops/automation/script/README-extra.md)
and use the [most related CM scripts](../../cm-mlops/script) as examples/templates 
to extend your own script.


## Adding extra Git repositories with artifacts to dependencies

If you artifact/experiment depends on various Git repositories, you can add them
as dependencies to your script in `_cm.yaml` or `_cm.json`to be automatically downloaded and cached
as shown in the following example:


```yaml
deps:
- tags: get,git,repo,_repo.https://github.com/CMU-SAFARI/Victima
  env:
    CM_GIT_ENV_KEY: 'CMU_SAFARI_VICTIMA'
  extra_cache_tags: micro23,artifact,ae,cmu,safari,victima

```

The path to this cached GitHub repository will be available in your native scripts 
via `CM_GIT_REPO_CMU_SAFARI_VICTIMA_CHECKOUT_PATH` environment variable.

You can also find cached repo via CM CLI as follows:
```bash
cm find cache --tags=get,git,cmu,safari,victima
```


## Sharing this script with the community and artifact evaluators

You just need to share/commit `cmr` directory and `cmr.yaml` to your project.
Another user or artifact evaluator will need to install CM and pull `mlcommons@ck` repository and your repository as follows:
```
python3 -m pip install cmind -U

cm pull repo mlcommons@ck
cm pull repo --url={Git URL of your project}
```

It is now possible to run your CM script in the same way as on your platform:
```bash
cm run script "reproduce micro 2023 paper 016" --env.KEY1=VAL1 --env.KEY2=VAL2 ...
```

CM will attempt to resolve all dependencies, install the missing ones and then run your native script
while adapting to a new platform.

If some issue is encountered, CM makes it easier for evaluators and users to work with your 
to fix not only a given CM script for your paper but also [improve and fix other shared CM scripts](../../cm-mlops/script) 
thus helping the community gradually improve portability, reproducibility, replicability and reusability of all research projects 
across different environments!

It is also possible to use CM automation language in containers and README files 
thus helping the community quickly understand how to prepare and run
diverse projects.




## Automating experiments, autotuning and visualization

We are developing CM "experiment" as a higher-level wrapper to CM scripts 
to automate experimentation, autotuning, design space exploration,
visualization and comparison of experiments.

Please follow [this tutorial](../../cm-mlops/automation/experiment/README-extra.md) 
to learn about how to use the CM experiment automation.

Fee free to check [other tutorials](README.md) to understand and apply CM automation 
to your projects.





## Participating in discussions and developments

Note that this is an on-going and heavily evolving project - we are working with the community
to add and improve CM automations, templates and tutorials.

Please join the [MLCommons task force on automation and reproducibility](../taskforce.md)
via this public [Discord server](https://discord.gg/JjWNWXKxwT) to stay tuned, provide your feedback,
and get help to add CM interface to your research projects, reuse and/or extend [shared CM scripts](../../cm-mlops/script), 
add the new ones, and participate in our [open benchmarking, optimization and reproducibility challenges](https://access.cknowledge.org/playground/?action=challenges).
