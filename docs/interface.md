[ [Back to index](README.md) ]

# CM interface

After [installing CM scripting language](installation.md), you can use it via a unified [CLI](#cli) or [Python API](#python-api):

## CLI

Here is the minimal format of a unified CM command line to run 
[reusable automation actions](list_of_automations.md) on Linux, Windows and MacOS:

```bash
cm {action} {automation} ({artifact name(s) | sub-action}) (flags)
```

First, CM will [parse CM CLI](https://github.com/mlcommons/ck/blob/master/cm/cmind/cli.py#L54) into a unified CM input dictionary:

```json
{
  "action":{above action},
  "automation":{above automation},
  "artifact":{above artifact name or sub-action},
  "flag":"value",
  ...
}
```

CM will then call a [unified CM Python "access" function](https://github.com/mlcommons/ck/blob/master/cm/cmind/core.py#L138) 
with this input dictionary to perform some automation action. 

It is equivalent to using [CM Python API](#python-api) except that CM will be in interactive mode. 
Use flag ```--out=json``` to print the output dictionary at the end of this automation action.

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

The output CM dictionary always has an integer key "return".

If a given automation action succeeded, the ```output['return']``` is equal to zero 
and the output dictionary contains the output of this action.

Otherwise, ```output['return'] > 0``` and ```output['error']``` contains some text
explaining CM automation error.




## Further reading

* [CM specification: CLI](specs/cm-cli.md)
* [CM specification: Python API](specs/cm-cli.md)