**[ [TOC](../README.md) ]**

## Pull MLOps automation repo

```bash
ck pull repo:mlcommons@ck-mlops
```

## Install CK packages with Transformers library

```bash
ck install package --tags=lib,python-package,transformers,4.9.1
```

### Install any available version
```bash
ck install package --tags=lib,python-package,transformers
```


## Notes
CK makes it possible to install multiple versions of different packages at the same time.
CK workflows can then automatically plug in different versions of packages (frameworks, libraries, models, data sets)
to enable collaborating testing, benchmarking and optimization of ML Systems.
