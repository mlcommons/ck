[ [Back to index](../README.md) ]

<details>
<summary>Click here to see the table of contents.</summary>

* [Tutorial: Adding a common interface to reproduce research projects](#tutorial-adding-a-common-interface-to-reproduce-research-projects)
  * [Motivation](#motivation)
  * [Installing CM language](#installing-cm-language)
  * [Adding CM interface to your research project](#adding-cm-interface-to-your-research-project)
    * [Local directory](#local-directory)
    * [Git project](#git-project)
  * [Adding CM script to prepare and run your experiment](#adding-cm-script-to-prepare-and-run-your-experiment)
  * [Testing and extending CM script](#testing-and-extending-cm-script)
  * [Sharing this script with the community and artifact evaluators](#sharing-this-script-with-the-community-and-artifact-evaluators)
  * [Automating experiments, autotuning and visualization](#automating-experiments-autotuning-and-visualization)
  * [Participating in discussions and developments](#participating-in-discussions-and-developments)

</details>

# Tutorial: Adding a common interface to reproduce research projects

## Motivation

While helping the community to reproduce and replicate [many research papers](https://learning.acm.org/techtalks/reproducibility) 
during [artifact evaluation](https://cTuning.org/ae), we have seen that reviewers spend most of their time
deciphering numerous ad-hoc READMEs to figure out how to prepare and run shared applications. 

That motivated us to develop a [human readable language (Collective Mind)](../README.md#collective-mind-language-cm) 
to automate and unify the [most commonly used tasks](../list_of_scripts.md) 
to reproduce or replicate shared applications across the same or different software, hardware, models and data.

The goal of our common automation and reproducibility interface is to make it easier for the community 
to reproduce/replicate research results and apply them in the real world.
You can see an example of using CM automation language to reproduce an IPOL journal paper 
in this [tutorial](reproduce-research-paper-ipol.md).



## Installing CM language

CM requires minimal dependencies (Python 3+ and Git) and it should be straightforward to install it
on Linux, MacOS, Windows and any other platform using this [guide](../installation.md).

If you encounter any issue, please don't hesitate to tell us via [Discord server](https://discord.gg/JjWNWXKxwT) 
and/or open a ticket [here](https://github.com/mlcommons/ck/issues).

You also need to install the following CM repository with reusable CM scripts 
shared by the MLCommons task force on automation and reproducibility
to make it easier to run and reproduce ML and Systems applications and benchmarks
across diverse software and hardware:
```bash
cm pull repo mlcommons@ck
```



## Adding CM interface to your research project

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
           --script_name={name of your script}
```

Please add `--json` flag if you prefer to describe your dependencies and execution workflow in JSON instead of YAML format (default).

You can now find and edit the newly created template script using its alias as follows:
```bash
cm find script reproduce-paper-micro-2023-016
```
or tags
```bash
cm find script --tags=reproduce,paper,micro,2023,016
```

You must update the script after editing it's meta to cache it for fast search:
```bash
cm update script reproduce-paper-micro-2023-016
```

If you use Python and/or frameworks such as PyTorch and CUDA, you can create a new script with a template "python" or "pytorch" as follows:

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

From this moment, you can extend meta description of this script (`_cm.json` or `_cm.yaml`)
to add dependencies on other CM scripts to detect and/or install tools, data sets, models and other artifacts,
extend `customize.py` to update environment variables based on dependencies and run other native scripts
before executing the main native script, post-process and unify output, etc.

You can read about the CM script concept [here](../../cm-mlops/automation/script/README-extra.md)
and use the [most related CM scripts](../../cm-mlops/script) as examples/templates 
to extend your own script.




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
