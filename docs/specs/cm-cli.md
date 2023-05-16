[ [Back to Specs](README.md) ]

# CM command line interface

One of the main goals of the CM language is to provide a common, unified and human-readable CLI 
to access all software repositories shared in the [CM format](cm-repository.md).

## Format

The idea is to unify all shared READMEs, containers and Jupyter notebooks 
with CM commands to  to make it easier for the community to run software projects and reuse
individual automations across continuously changing software, hardware and data.

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

It is equivalent to using [CM Python API](cm-python-interface.md) except that CM will be in interactive mode. 
You can add a flag ```--out=json``` to print the output dictionary at the end of an automation action invoked via CLI.

You can test the CM interface using the following automation action that simply prints the unified CM input dictionary:
```
cm print-input automation artifact1 artifact2 --flag1=value1 --flag2 -- something
```

## Examples

```bash
cm 
cm help
cm {common automation action}
```

```bash
cm {common automation action} --help
```

```bash
cm {automation action} {automation}
```

```bash
cm {automation action} {automation} --help

```

```bash
cm {automation action} {automation} {artifact}
```

```bash
cm {automation action} {automation} {artifact} {artifact2} {artifact3} ...
```

```bash
cm {automation action} {automation} {artifact} --test --meta.a=b @input.json @input.yaml
```

The command line arguments are converted into a unified CM dictionary
using [this function](https://github.com/mlcommons/ck/blob/master/cm/cmind/cli.py#L48).

Flags are converted to the dictionary keys and their argument to the string value.

If a flag doesn't have an argument, CM will use boolean value "true".

If a flag has ".", it will be treated as dictionary with multiple subkeys separated by ".".

If a flag ends with ",", tis argument will be treated as a list of values separated by ",".

The CM dictionary is then passed to the 
[unified CM "access" function](https://github.com/mlcommons/ck/blob/master/cm/cmind/core.py#L134)
similar to micro-services and REST API.


## Understanding CM names

The {artifact} has the following format:

* "artifact alias" (str): may change in the future
* "artifact UID" (16 lowercase hex digits): the same since the creation of the artifact
* "alias,UID":  in such case, UID is used to search for an artifact or automation while alias is used as a user-friendly reminder

It is possible to reference an artifact in a specific CM repository as follows:

* "repo alias:artifact"
* "repo UID:artifact"
* "repo alias,repo UID:artifact"

Note that automation has the same format as an artifact and is stored as a CM artifact 
in the CM repositories in the "automation" directory.

CM repository also has the same format as an artifact: *alias | UID | alias,UID*.



## Using CM CLI inside a CM repository

If you are inside a CM repository, you can use "." to tell CM to detect a repository, automation and
artifact in the current directory to avoid writing the names explicitly in the command line.

For example, you can add a new artifact in the current repository as following:
```bash
cm add {some automation} .:{some artifact}
```

or if you are inside a directory with CM automations, you can use the following:
```bash
cm add . {some artifact}
```






## CM automations

CM automations are kept as CM artifacts in "automation" directories 
(see [this example](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation)).

You can add a new automation as follows:
```bash
cm add automation {new automation name}
```

A related CM artifact will be created in the "local" CM repository.
You can create it in the other CM repository as follows:
```bash
cm add automation {target CM repository}:{new automation name}
```

You can also move the new automation from local repository to the existing one as follows:
```bash
cm move automation local:{new automation name} {target CM repository}:
```

The automation artifact has a Python *module.py* that implements automation actions:
```bash
ls `cm find automation {new automation name}`
_cm.json
module.py
```

By default, it has a "test" action that prints the input dictionary that is aggregated 
from the CM CLI. It helps you understand the CM CLI and how it is converted into a unified input dictionary.

You can add a new function "new_action" in a similar way as "test" to make it a new automation action
that can be invoked from the command line as follows:
```bash
cm new_action {new automation name} ...
```
 or
```bash
cm new-action {new automation name} ...
```


## CM common automation actions

All CM automations inherit common database function from this 
[Automation class](https://github.com/mlcommons/ck/blob/master/cm/cmind/automation.py).

### add

Add new artifact:

```bash
cm add automation (repo:)artifact
```

API: [CM docs](https://cknowledge.org/docs/cm/api/cmind.html#cmind.automation.Automation.add)

### delete

Remove artifact:

```bash
cm delete automation (repo:)artifact
```
or
```bash
cm rm automation (repo:)artifact
```
or
```bash
cm remove automation (repo:)artifact
```

API: [CM docs](https://cknowledge.org/docs/cm/api/cmind.html#cmind.automation.Automation.delete)

### find

Find artifact(s):

```bash
cm find automation (repo:)artifact(s) (--tags=tag1,tag2,...)
```
or
```bash
cm search automation (repo:)artifact(s)
```
or
```bash
cm ls automation (repo:)artifact(s)
```

You can use wildcards.

You can also list all available artifacts in all repositories as follows:
```bash
cm find * *
```

You can find all artifact in the current repository as follows:
```bash
cm find .
```

API: [CM docs](https://cknowledge.org/docs/cm/api/cmind.html#cmind.automation.Automation.search)

### load

Load artifact meta description:

```bash
cm load automation (repo:)artifact
```
API: [CM docs](https://cknowledge.org/docs/cm/api/cmind.html#cmind.automation.Automation.load)



### update

Load artifact meta description:

```bash
cm update automation (repo:)artifact --meta.{key}={value} (@input.json) (@input.yaml)
```

API: [CM docs](https://cknowledge.org/docs/cm/api/cmind.html#cmind.automation.Automation.update)



### rename

Rename or move artifacts:

```bash
cm move automation src-artifact (new repo:)target-artifact
```

API: [CM docs](https://cknowledge.org/docs/cm/api/cmind.html#cmind.automation.Automation.move)



## CM internal automations

### repo

This automation deals with CM repositories. You can list available actions in this automation as follows:
```bash
cm help repo
```

You can get an API/CLI for a specific automation as follows:
```bash
cm init repo --help
```


### automation

This automation helps you to add new automations as follows:
```bash
cm add automation {new-automation}
```


### core

This automation has some common actions for the CM core including "test":
```bash
cm help core
```

For example, you can test the CM as follows:
```bash
cm test core
```
