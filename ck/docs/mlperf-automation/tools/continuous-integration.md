**[ [TOC](../README.md) ]**

# Continuous integration for CK workflows

All CK modules and automation actions are accessible as a micro-service with a unified JSON I/O API.

For example, have a look at these CLI-based CK commands:
```
ck pull repo:mlcommons@ck-mlops
ck search dataset --tags=jpeg
ck compile program:image-corner-detection --speed
ck run program:image-corner-detection --env.XYZ=abc
```

They can be implemented in Python as follows:

```
import ck.kernel as ck

r=ck.access({'action':'pull', 'module_uoa':'repo', 'data_uoa':'mlcommons@ck-mlops})
if r['return']>0: ck.err(r)

r=ck.access({'action':'search', 'module_uoa':'dataset', 'tags':'jpeg'})
if r['return']>0: ck.err(r)
print (r['lst'])

r=ck.access({'action':'compile', 'module_uoa':program', 'data_uoa':'image-corner-detection', 'speed':'yes'})
if r['return']>0: ck.err(r)

r=ck.access({'action':'run', 'module_uoa':program', 'data_uoa':'image-corner-detection', 'env':{'XYZ':'abc'}})
if r['return']>0: ck.err(r)

```

This allows one to use CK automation actions and workflows as web services or connect them with any CI platform.

# Examples

Python-based CK integration with web platforms:
* [cKnowledge.io platform](https://cknow.io) uses CK framework as a database of CK objects and micro-services.

CMD-based CK integration with CLI platforms:

* [Travis for Linux and MacOS (CK ML repository)](https://github.com/mlcommons/ck-mlops/blob/main/.travis.yml)
* [AppVeyor for Windows (CK ML repository)](https://github.com/mlcommons/ck-mlops/blob/main/appveyor.yml)
