[ [Back to documentation](README.md) ]

# CMX commands (automation actions) applicable to all artifacts


## CMX command line

```bash
$ cmx {action} {automation} [CMX options] [CMX automation action flags]
```

CMX options have format -key=value or -key (value=True)

CMX automation flags have format --key=value or --key (value=True) 

Common actions for all artifacts and automations (`cmx -h`):
 * `find` automation (artifact) - find artifacts based on alias, UID and tags
 * `load` automation (artifact) - load metadata of a give artifact referenced either by alias or UID or alias,UID or --tags
 * `update` automation (artifact) - update metadata of a given artifact 
 * `add` automation (artifact) - add new artifact
 * `rm` automation (artifact) - remove artifact(s)
 * `mv` automation (repo:)artifact (new_repo:)new_artifact - rename artifact or move to another CMX repository
 * `copy`automation (repo:)artifact (new repo:)new_artifact - copy artifact to another repository with a new UID
 * `help` automation - print available actions for a given automation

You can add -h to above actions to see related flags for a given automation action

*These actions are inherited by all CMX automations from this 
 [CMX Automation Class](https://github.com/mlcommons/ck/blob/master/cm/cmind/automation.py).*

## Default automations

When you install [CMX/CM](https://access.cknowledge.org/playground/?action=install), you have the following automations
available by default inside the [`default` repository](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo) embedded in cmind package: 

* `core` - core CMX automations such as generating UID
* `repo` - CMX automations to manage CMX repositories (pull, rm, pack ...)
* `automation` - CMX automation to manage automations (add, rm, mv ...

You can list all pulled repositories as follows:
```bash
cmx find repo
```

You can also show extra information about repositories as follows:
```bash
cmx show repo
```

You can list all available automations as follows:
```bash
cmx find {automation}
```

You can list available actions for a given automation as follows:
```bash
cmx help {automation}
```

You can list available flags for a given automation action as follows:
```bash
cmx {action} {automation} -h
```

## Python API

CMX provides a simple Python JSON API to manage artifacts, automations and metadata
that converts above command line into 1 call with a unified Dictionary input and Dictionary output:

```bash
import cmind

r = cmind.x({'action':'my action',
             'automation':'my automation',
             'key1':'value1',
             'key2':'value2'})
if r['return']>0: handle error in r['error']

...
```