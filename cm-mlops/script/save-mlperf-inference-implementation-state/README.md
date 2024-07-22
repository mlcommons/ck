**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/save-mlperf-inference-implementation-state).**



Automatically generated README for this automation recipe: **save-mlperf-inference-implementation-state**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=save-mlperf-inference-implementation-state,b14b813229c444f8) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/save-mlperf-inference-implementation-state)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *save,mlperf,inference,implementation,state*
* Output cached? *False*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "save mlperf inference implementation state" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=save,mlperf,inference,implementation,state`

`cm run script --tags=save,mlperf,inference,implementation,state `

*or*

`cmr "save mlperf inference implementation state"`

`cmr "save mlperf inference implementation state " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'save,mlperf,inference,implementation,state'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### Run this script via GUI

```cmr "cm gui" --script="save,mlperf,inference,implementation,state"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=save,mlperf,inference,implementation,state) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "save mlperf inference implementation state" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/save-mlperf-inference-implementation-state/_cm.yaml)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/save-mlperf-inference-implementation-state/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/save-mlperf-inference-implementation-state/_cm.yaml)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/save-mlperf-inference-implementation-state/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/save-mlperf-inference-implementation-state/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/save-mlperf-inference-implementation-state/_cm.yaml)

___
### Script output
`cmr "save mlperf inference implementation state "  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
