[ [Back to index](README.md) ]

# CM interface

*Please check the [CM introduction](introduction-cm.md) to understand CM motivation and concepts.*

After [installing CM scripting language](installation.md), you can use it 
to manage research projects and run shared automation actions (recipes)
on any platform natively or inside containers 
via a unified CM [CLI](#cli) or [Python API](#python-api):

## CLI

Here is the minimal format of a unified CM command line 
to run any [reusable automation action](list_of_automations.md) 
from any software project on Linux, Windows and MacOS:

```bash
cm {action} {automation alias | UID | alias,UID} 
  ({artifact name(s) | sub-action | argument}) 
  (--flag1=value1) (--flag2) ...
  (@input.json | @input.yaml)
  (-- extra CMD)
```

First, CM will [parse CM CLI](https://github.com/mlcommons/ck/blob/master/cm/cmind/cli.py#L54) into a unified CM input dictionary:

```json
{
  "action":"automation action",
  "automation":"automation alias | UID | alias,UID",

  ("artifact":{above artifact name or sub-action},)

  ("flag1":"value1",)
  ("flag2":True,)
  ...
  ("unparsed_cmd": [
    list of strings in extra CMD
   ]) 
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
  "action":{some action},
  "automation":{some automation},
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


## Automation actions

CM automation actions are implemented as Python modules added to software projects under ```automation``` directory.


* internal
* from shared repos




## Further reading

* [CM specification](specs/README.md)
