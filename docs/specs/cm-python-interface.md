[ [Back to Specs](README.md) ]

# CM Python API

All [CM automations](../list_of_automations.md) can be accessed in a unified way either via CLI as shown above or via Python API:

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
