[ [Back to index](README.md) ]

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


