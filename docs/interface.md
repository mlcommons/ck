[ [Back to index](README.md) ]

# CM interface

*Please check [CM introduction](introduction-cm.md) to understand CM motivation and concepts.*

After [installing CM scripting language](installation.md), you can use it 
to manage research projects and run shared automation actions (recipes)
on any platform natively or inside containers 
via a unified CM [CLI](#cli) or [Python API](#python-api):

## CLI

Here is format of a unified CM command line 
to run any [reusable automation action](list_of_automations.md) 
from any software project on Linux, Windows and MacOS:

```bash
cm {action} {automation alias | UID | alias,UID} 
  ({artifact name(s) | sub-action | argument}) 
  (--flag1=value1) (--flag2.key2=value2) (--flag3,=value3,value4) (--flag4)
  (@input.json | @input.yaml)
  (-- extra CMD)
```

First, CM will [parse CM CLI](https://github.com/mlcommons/ck/blob/master/cm/cmind/cli.py#L54) into a unified CM input dictionary:

```json
{
  "action":"automation action",
  "automation":"automation alias | UID | alias,UID",

  "artifact":{above artifact name or sub-action},

  "flag1":"value1",
  "flag2":{"key2":"value2"},
  "flag3":["value3","value4"],
  "flag4":True,
  ...
  "unparsed_cmd": [
    list of strings in extra CMD
   ]
}
```

When a user specify one or more input files with @ prefix, they will be loaded 
and merged with the CM input in the same order as in command line.

CM will then call a [unified CM Python "access" function](https://github.com/mlcommons/ck/blob/master/cm/cmind/core.py#L138) 
with this input dictionary to perform some automation action. 

It is equivalent to using [CM Python API](#python-api) except that CM will be in interactive mode. 
You can add a flag ```--out=json``` to print the output dictionary at the end of an automation action invoked via CLI.

You can test the CM interface using the following automation action that simply prints the unified CM input dictionary:
```
cm print-input automation artifact1 artifact2 --flag1=value1 --flag2 -- something
```

## Python API

All [CM automations](list_of_automations.md) can be accessed in a unified way either via CLI as shown above or via Python API:

```python

import cmind

input={
  "action":"automation action",
  "automation":"automation alias | UID | alias,UID",
  ...
}

output = cmind.access(input)

if output['return']>0:
    cmind.error(output)

print (output)
```

The output CM dictionary always has an integer key ```return```.

If a given automation action succeeded, the ```output['return']``` is equal to zero 
and the output dictionary contains the output of this action.

Otherwise, ```output['return'] > 0``` and ```output['error']``` 
contains some text explaining CM automation error.


### Example

For example, we can list all CM automations, their meta descriptions and paths as follows:

```python

import cmind

output = cmind.access({'action':'search',
                       'automation':'automation,bbeb15d8f0a944a4'})

if output['return']>0: 
    cmind.error(output)

artifacts = output['list']

for artifact in artifacts:
    print ('')
    print (artifact.path)
    print (artifact.meta)

```


## Reusable automation actions

CM automation actions are implemented as standard Python functions with unified CM input and output dictionaries.

They can call other CM automation actions simply by using the same ```(dict) = cmind.access(dict)``` function shown above.

Such actions are shared in software projects in ```module.py``` files inside ```automation/artifact alias``` directories 
as can be seen in the [internal CM repository](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation)
or [MLCommons CM-MLOps project](https://github.com/ctuning/mlcommons-ck/tree/master/cm-mlops/automation).

Note that CM converts software projects and directories into a database of artifacts abstracted by common automations:
Such artifacts are shared in ```automation alias/artifact alias``` directories to provide 
a simple, common and extensible directory format for shared projects based on [FAIR principles](https://www.go-fair.org/fair-principles).
CM automations are also stored and accessed as CM artifacts where ```artifact alias``` is simply the automation name.

Each CM artifact directory contains ```_cm.json``` or ```_cm.yaml``` file to help CM find and run a given automation action
or an artifact either by unique ID or alias or a combination of both separated by comma
(in the last case, only UID is used
to find automation action while alias is used as a user-friendly name that can be changed over time
without breaking automation workflows):

```json
{
  "uid": "55c3e27e8a140e48",
  "alias": "repo",

  "automation_alias": "automation",
  "automation_uid": "bbeb15d8f0a944a4",
  
  "desc": "Managing CM repositories and software projects",

  "tags": [
    "automation",
    "repo"
  ]
}
```

By default, when users install CM via PIP, they have an access to 2 repositories:
* ["internal CM repository"](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo)
  with a minimal set of [reusable automation actions](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation) 
  to manage CM repositories and software projects. 
* "local CM repository" in ```$HOME/CM/repos/local``` that serves as a scratch pad for automation actions

When CM is used to pull Git repositories or download zip/tar files with research projects or regiser some local directory as a CM repository,
the path will be automatically registered in ```$HOME/CM/repos.json``` and used by CM to search for CM automation actions and other artifacts.

For example, a user can pull a [MLCommons CM-MLOps repository](https://github.com/mlcommons/ck/tree/master/cm-mlops) from GitHub using the following CM commands:
```bash
cm pull repo --url=https://github.com/mlcommons/ck
```

or shorter as follows:

```bash
cm pull repo mlcommons@ck
```

This repository contains a [```cmr.yaml``` file](https://github.com/mlcommons/ck/blob/master/cmr.yaml) 
telling CM to search in the ```cm-mlops``` directory for automation actions and artifacts
(defined by ```prefix``` key to non-intrusively embedd CM inside existing software projects).

It is possible to list registered CM repositories using the following automation action:
```bash
cm search repo
```
or

```bash
cm search repo mlcommons@ck
```

This automation action is implemented in [this Python function]( https://github.com/mlcommons/ck/blob/master/cm/cmind/repo/automation/repo/module.py#L94 ) 
in the [```repo``` automation artifact](https://github.com/mlcommons/ck/blob/master/cm/cmind/repo/automation/repo) from the internal CM repository.

After pulling ```mlcommons@ck``` repository, users will have an access to more reusable automations:
```bash
cm search automation
```

or using the equivalent automation action name ```find```

```bash
cm find automation
```

It is possible to find automations only in a given repository as follows:
```bash
cm find automation mlcommons@ck:
```

Note that ":" shows that mlcommons@ck is a CM repository and not an artifact. 
It is possible to tell CM to search for a given automation or an artifact from the specific repository as follows:
```bash
cm find {CM repository alias | UID | alias,UID}:automation 
        {CM repository alias | UID | alias,UID}:{artifact1 alias | UID | alias, UID}
        {CM repository alias | UID | alias,UID}:{artifact2 alias | UID | alias, UID}
        ...
```

For example, let's find an automation "repo" from the "internal" CM repository using wildcards:
```bash
cm find automation internal:rep*
```

Note that all automations in CM are abstracted by the following [```Automation class```](https://github.com/mlcommons/ck/blob/master/cm/cmind/automation.py#L10)
and has a number of default actions:

* ```add``` - add a new artifact to a CM repository
* ```delete``` == ```rm``` - delete existing artifact from a CM repository
* ```load``` - load meta information (```_cm.json``` or ```_cm.yaml```) for a given artifact
* ```update``` - update meta information (```_cm.json``` or ```_cm.yaml```) for a given artifact
* ```move``` == ```rename``` == ```mv``` - rename a given artifact or move it to another CM repository
* ```copy``` == ```cp``` - copy a given artifact to an artifact with a different name or to another CM repository
* ```search``` == ```list``` == ```find``` - search for automations or artifacts in CM repositories

For example, let's add and find a CM automation "world" in the "local" CM repository,

```bash
cm add automation world
cm find automation world
```

By default, CM will add ```test``` action to this automation to let you use it as a template for other actions:
```bash
cm test world
```

You can now add an artifact called ```open``` for this automation in the "local" CM repository 
with some tags ```hello,cool``` as follows:
```bash
cm add world open --tags=hello,cool
cm find world
cm find world open
cm find world --tags=cool

```

You can find the command line flags or Python API for any given automation action from the command line as follows:
``bash
cm {action} {automation} --help
```

For example, you can obtain help for all above internal (common) automation actions:
```bash
cm add world --help
cm delete world --help
cm load world --help
cm update world --help
cm move world --help
cm copy world --help
cm search world --help
```

You can also customize all above functions in the new automation 
by simply adding those functions in a new `module.py` and then
calling the original action with the input key `common`:True.

For example, the CM automation `script` overloads `add` function
not only to add a new CM script but also copy `run.sh`, `run.bat`,
`customize.py` and `README-extra.md` there. You can study 
and reuse this code [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/script/module.py#L1978).



This minimal information covers most of the basic CM functionality. 

However, it turned out to be enough to enable collaboration between academia and industry
to modularize benchmarking, optimiation and design space exploration of AI/ML systems
and make it more portable, reproducible and comparable across very diverse and rapidly evolving
software and hardware using just 2 extra CM automations: [CM scipt and cache](specs/cm-automation-script.md).

You can see the use of CM in these real-world examples:
- [README to reproduce published IPOL'22 paper](cm-mlops/script/reproduce-ipol-paper-2022-439)
- [README to reproduce MLPerf RetinaNet inference benchmark at Student Cluster Competition'22](docs/tutorials/sc22-scc-mlperf.md)
- [Auto-generated READMEs to reproduce official MLPerf BERT inference benchmark v3.0 submission with a model from the Hugging Face Zoo](https://github.com/mlcommons/submissions_inference_3.0/tree/main/open/cTuning/code/huggingface-bert/README.md)
- [Auto-generated Docker containers to run and reproduce MLPerf inference benchmark](cm-mlops/script/app-mlperf-inference/dockerfiles/retinanet)

## Further reading

* [CM specification](specs/README.md)
* [Article with the concept of a common automation language based on previous version of CM language before MLCommons](https://doi.org/10.1098/rsta.2020.0211)
