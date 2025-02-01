[ [Back to index](../../../docs/README.md) ]

# CM "cache" automation

*We suggest you to check [CM introduction](https://github.com/mlcommons/ck/blob/master/docs/introduction-cm.md) 
 and [CM CLI/API](https://github.com/mlcommons/ck/blob/master/docs/interface.md) to understand CM motivation and concepts.*

## CM script CLI

Whenever a [given CM script]() caches the output, you can find it 

Whenever a [CM script](https://access.cknowledge.org/playground/?action=scripts) 
caches its output (such as downloaded model or pre-processed data set or built code),
you can find it using the CM "cache" automation as follows:

```bash
cm show cache
```

You can prune cache entries by tags and variations:
```bash
cm show cache --tags=ml-model
cm show cache --tags=python
```

You can find a path to a given cache artifact as follows:
```bash
cm find cache --tags=ml-model,bert
```

You can delete one or more cache artifacts as follows:
```bash
cm rm cache --tags=ml-model
```

You can skip user prompt by adding `-f` flag as follows:
```bash
cm rm cache --tags=ml-model -f
```

You can clean the whole cache as follows:
```bash
cm rm cache -f
```

## CM python API

You can access the same functionality via CM Python API as follows:

```python

import cmind

output = cmind.access({'action':'show',
                       'automation':'cache,541d6f712a6b464e'})

if output['return']>0: 
    cmind.error(output)

artifacts = output['list']

for artifact in artifacts:
    print ('')
    print (artifact.path)
    print (artifact.meta)

```

## Related

* [CM "script" automation](../script/README-extra.md)
