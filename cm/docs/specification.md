# Specification

## CM repository

### Root directory

* *cmr.yaml &| cmr.json* - CM repository description

```json
{
  alias (str): CM name to find this repository
  uid (str): unique ID to find this repository

  (desc) (str): user-friendly description
  (git) (bool): True, if it's a Git repository
  (prefix) (str): sub-directory inside this repository to keep CM artifacts
}
```

Examples: 

* [Internal CM repository description](https://github.com/mlcommons/ck/blob/master/cm/cmind/repo/cmr.yaml) 
* [octoml@cm-mlops repository description](https://github.com/octoml/cm-mlops/blob/main/cmr.yaml)

### First level directories

* CM automation names, i.e. artifact type (alias or UID)

Examples: 

* [Internal CM repository](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo) 
* [CM repository for MLOps and DevOps](https://github.com/mlcommons/ck/tree/master/cm-mlops)

### Second level directories

* CM artifact names (alias or UID)

Examples: 

* [Internal CM repository](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation) 
* [CM repository for MLOps and DevOps](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)

### Third level files

* *_cm.yaml &| _cm.json* - CM artifact meta description

```json
{
  alias (str): CM name to find this artifact
  uid (str): unique ID to find this artifact

  automation_alias (str): CM automation name for this artifact
  automation_uid (str): unique ID for the automation for this artifact

  (_base) (str): preload meta description from this base artifact in format "{automation}::{artifact}" 
                 and then merge the current meta description with the base.
                 This mechanism enables simple inheritance of artifact meta descriptions.

  tags (list): list of tags to characterize and find this artifact

  ... 
}
```

## CM command line

CM uses a unified CLI to access all automation actions and artifacts:

``bash
cm {action} {automation} {artifact(s)} {--flags} @input.yaml @input.json
```

Examples:

```bash
$ cm 
$ cm help
$ cm {common automation action}
```

```bash
$ cm {common automation action} --help
```

```bash
$ cm {automation action} {automation}
```

```bash
$ cm {automation action} {automation} --help

```

```bash
$ cm {automation action} {automation} {artifact}
```

```bash
$ cm {automation action} {automation} {artifact} {artifact2} {artifact3} ...
```

```bash
$ cm {automation action} {automation} {artifact} --test --meta.a=b @input.json @input.yaml
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


### Understanding CM names

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



### Using CM CLI inside a CM repository

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




## CM Python JSON interface

CM automations can be executed from a Python as follows:
```python

import cmind as cm

r = cm.access({'action':'find', 'automation':'repo'})
if r['return']>0: cm.halt(r)

print (r)
 
r = cm.access('find repo --out=con')
if r['return']>0: cm.halt(r)

```

or

```python
import cmind

cm = cmind.CM()

r = cm.access({'action':'find', 'automation':'repo'})
if r['return']>0: cm.halt(r)

print (r)

```


## CM automation

CM automations are kept as CM artifacts in "automation" directories 
(see [this example](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation)).

You can add a new automation as follows:
```bash
$ cm add automation {new automation name}
```

A related CM artifact will be created in the "local" CM repository.
You can create it in the other CM repository as follows:
```bash
$ cm add automation {target CM repository}:{new automation name}
```

You can also move the new automation from local repository to the existing one as follows:
```bash
$ cm move automation local:{new automation name} {target CM repository}:
```

The automation artifact has a Python *module.py* that implements automation actions:
```bash
$ ls `cm find automation {new automation name}`
_cm.json
module.py
```

By default, it has a "test" action that prints the input dictionary that is aggregated 
from the CM CLI. It helps you understand the CM CLI and how it is converted into a unified input dictionary.

You can add a new function "new_action" in a similar way as "test" to make it a new automation action
that can be invoked from the command line as follows:
```bash
$ cm new_action {new automation name} ...
```
 or
```bash
$ cm new-action {new automation name} ...
```


## CM common automation actions

All CM automations inherit common database function from the 
[Automation class](https://github.com/mlcommons/ck/blob/master/cm/cmind/automation.py)

### add

Add new artifact:

```bash
$ cm add automation (repo:)artifact
```

API: [CM docs](https://cknowledge.org/docs/cm/api/cmind.html#cmind.automation.Automation.add)

### delete

Remove artifact:

```bash
$ cm delete automation (repo:)artifact
```
or
```bash
$ cm rm automation (repo:)artifact
```
or
```bash
$ cm remove automation (repo:)artifact
```

API: [CM docs](https://cknowledge.org/docs/cm/api/cmind.html#cmind.automation.Automation.delete)

### find

Find artifact(s):

```bash
$ cm find automation (repo:)artifact(s) (--tags=tag1,tag2,...)
```
or
```bash
$ cm search automation (repo:)artifact(s)
```
or
```bash
$ cm ls automation (repo:)artifact(s)
```

You can use wildcards.

You can also list all available artifacts in all repositories as follows:
```bash
$ cm find * *
```

You can find all artifact in the current repository as follows:
```bash
$ cm find .
```

API: [CM docs](https://cknowledge.org/docs/cm/api/cmind.html#cmind.automation.Automation.search)

### load

Load artifact meta description:

```bash
$ cm load automation (repo:)artifact
```
API: [CM docs](https://cknowledge.org/docs/cm/api/cmind.html#cmind.automation.Automation.load)



### update

Load artifact meta description:

```bash
$ cm update automation (repo:)artifact --meta.{key}={value} (@input.json) (@input.yaml)
```

API: [CM docs](https://cknowledge.org/docs/cm/api/cmind.html#cmind.automation.Automation.update)



### rename

Rename or move artifacts:

```bash
$ cm move automation src-artifact (new repo:)target-artifact
```

API: [CM docs](https://cknowledge.org/docs/cm/api/cmind.html#cmind.automation.Automation.move)



## CM internal automations

### repo

This automation deals with CM repositories. You can list available actions in this automation as follows:
```bash
$ cm help repo
```

You can get an API/CLI for a specific automation as follows:
```bash
$ cm init repo --help
```


### automation

This automation helps you to add new automations as follows:
```bash
$ cm add automation {new-automation}
```


### core

This automation has some common actions for the CM core including "test":
```bash
$ cm help core
```

For example, you can test the CM as follows:
```bash
$ cm test core
```
