**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/detect-cpu).**



Automatically generated README for this automation recipe: **detect-cpu**

Category: **Platform information**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=detect-cpu,586c8a43320142f7) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-cpu)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *detect,cpu,detect-cpu,info*
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

````cmr "detect cpu detect-cpu info" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=detect,cpu,detect-cpu,info`

`cm run script --tags=detect,cpu,detect-cpu,info `

*or*

`cmr "detect cpu detect-cpu info"`

`cmr "detect cpu detect-cpu info " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'detect,cpu,detect-cpu,info'
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

```cmr "cm gui" --script="detect,cpu,detect-cpu,info"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=detect,cpu,detect-cpu,info) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "detect cpu detect-cpu info" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-cpu/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-cpu/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-cpu/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-cpu/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-cpu/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-cpu/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-cpu/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-cpu/_cm.json)

___
### Script output
`cmr "detect cpu detect-cpu info "  -j`
#### New environment keys (filter)

* `CM_HOST_CPU_*`
* `CM_HOST_DISK_CAPACITY`
* `CM_HOST_MEMORY_CAPACITY`
#### New environment keys auto-detected from customize

* `CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET`
* `CM_HOST_CPU_SOCKETS`
* `CM_HOST_CPU_THREADS_PER_CORE`
* `CM_HOST_CPU_TOTAL_LOGICAL_CORES`