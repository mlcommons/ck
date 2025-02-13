[ [Back to documentation](README.md) ]

# Getting Started with CMX

## Understanding Common Metadata eXchange (CMX)

CMX allows users to embed any metadata into any artifact—such as programs, datasets, models, and scripts—within their projects
using `_cm.yaml` and/or `_cm.json` files (Common Metadata).

This common metadata includes extensible tags, a user-friendly alias, and an automatically generated unique ID (16 lowercase hexadecimal characters), 
enabling everyone to find and reuse both public and private artifacts in accordance with [FAIR principles](https://en.wikipedia.org/wiki/FAIR_data) 
(findable, accessible, interoperable, and reusable).

At the same time, CMX allows users to share and reuse common automations 
with a unified CLI and Python API, applying them to related artifacts
based on their common metadata.

## Understanding CMX repositories

A [typical CMX-based GitHub repository](https://github.com/mlcommons/ck/tree/master/cmx4mlops/cmx4mlops),
which includes common metadata and automations in the CMX format, is structured as follows:

```bash
│   cmr.yaml
│   
├───automation
│   └───script
│           COPYRIGHT.md
│           module.py
│           README.md
│           _cm.json
│               
│           
└───script
    ├───app-image-classification-torch-py
    │   │   COPYRIGHT.md
    │   │   README.md
    │   │   requirements.txt
    │   │   run.bat
    │   │   run.sh
    │   │   _cm.yaml
    │   │   
    │   └───src
    │           pytorch_classify_preprocessed.py
    │           
    ├───app-mlperf-inference
    │       COPYRIGHT.md
    │       customize.py
    │       README.md
    │       run.sh
    │       _cm.yaml
    │       
    ├───compile-program
    │       COPYRIGHT.md
    │       customize.py
    │       run.bat
    │       run.sh
    │       _cm.yaml
    │       
    └───detect-os
            COPYRIGHT.md
            customize.py
            _cm.yaml
            
```

All CMX repositories follow a file-based structure with a two-level directory hierarchy. 
Each repository includes a `cmr.yaml` file (Common Metadata Repository), 
which contains a unique ID and a user-friendly alias for easy identification.

All CMX repositories are structured as a file-based system with a two-level
directory hierarchy and a `cmr.yaml` (Common Metadata Repository)
with a unique ID and user-friendly alias for this repository . 

The first-level directories categorize artifacts and
include their relevant automation, while the second-level directories
house the specific artifacts within each category.

In the above example, we have common CMX artifacts called `script`, along
with a related CMX `automation` of the same name.

Each subdirectory within the `script` directory always contains either 
a `_cm.yaml` file (typically manually generated), a `_cm.json` file 
(usually automatically generated), or both. 
If both are present, CMX first reads `_cm.yaml` and then merges it with `_cm.json`. 
These files describe a given artifact and include all related user files associated with it.

For CMX scripts, we typically have native scripts and an optional `customize.py` file. 
The `customize.py` enables the unification of environment variables and APIs before executing 
a given script via CMX automation, ensuring it runs consistently across different operating 
systems through a standardized CMX interface.

After installing CMX and cloning this repository from GitHub, you can find all shared `script` artifacts 
as follows:

```bash
fursin@laptop:~$ pip install cmind
fursin@laptop:~$ cmx pull repo mlcommons@ck --dir=cmx4mlops/cmx4mlops
fursin@laptop:~$ cmx find script

/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/script/app-image-classification-torch-py
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/script/app-mlperf-inference
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/script/compile-program
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/script/detect-os
...
```

You can also find all categories (automations) for shared artifacts as follows:
```bash
fursin@laptop:~$ cmx find automation

/home/fursin/cmx/lib/python3.12/site-packages/cmind/repo/automation/automation
/home/fursin/cmx/lib/python3.12/site-packages/cmind/repo/automation/ckx
/home/fursin/cmx/lib/python3.12/site-packages/cmind/repo/automation/core
/home/fursin/cmx/lib/python3.12/site-packages/cmind/repo/automation/repo
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/automation/cache
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/automation/cfg
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/automation/challenge
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/automation/data
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/automation/docker
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/automation/experiment
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/automation/report
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/automation/script
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/automation/utils
...
```

By default, when you pull repositories via CMX, they are stored in the `$HOME/CM` directory. 
This default location helps CMX efficiently search for all shared artifacts and automations.

You can change this directory by setting the `CM_REPOS` environment variable.

Additionally, you can pull multiple public and private repositories with CMX artifacts, 
allowing you to reuse artifacts and automations across different projects.

## Understanding CMX metadata

All CMX artifacts contain a minimal set of keys in their metadata files.

For example, the CMX script artifact `app-image-classification-torch-py`, 
which includes PyTorch code for classifying images using the reference ResNet50 model, 
has the following `_cm.yaml` format:


```yaml
uid: e3986ae887b84ca8
alias: app-image-classification-torch-py

automation_alias: script
automation_uid: 5b4e0237da074764

tags:
- app
- image-classification
- torch
- python

...
```

This metadata allows users to find this artifact from command line using the following CMX commands:
```bash
$ cmx find script app-image-classification-torch-py
$ cmx find script e3986ae887b84ca8
$ cmx find script app-image-classification-torch-py,e3986ae887b84ca8
$ cmx find script *image-classification-torch*
$ cmx find script --tags=app,image-classification,torch
$ cmx find script "python app image-classification torch"

/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/script/app-image-classification-torch-py
```

You can also use a simple Python API to locate these artifacts as follows:

```bash
$ python

import cmind

r = cmind.x({'action':'find', 'automation':'script', 'artifact':'app-image-classification-torch-py,e3986ae887b84ca8'})
if r['return']>0: cmind.errorx(r)

artifacts = r['list']

for artifact in artifacts:
     print (artifact.path)
     print (artifact.meta)
```

```bash
/home/fursin/CM/repos/mlcommons@ck/cmx4mlops/cmx4mlops/repo/script/app-image-classification-torch-py
{'alias': 'app-image-classification-torch-py', 'automation_alias': 'script', 'automation_uid': '5b4e0237da074764', ...

```

## Understanding CMX automations







To be continued...
