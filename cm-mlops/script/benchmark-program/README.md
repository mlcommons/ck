**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-program).**



Automatically generated README for this automation recipe: **benchmark-program**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=benchmark-program,19f369ef47084895) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *benchmark,program*
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

````cmr "benchmark program" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=benchmark,program`

`cm run script --tags=benchmark,program[,variations] `

*or*

`cmr "benchmark program"`

`cmr "benchmark program [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'benchmark,program'
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

```cmr "cm gui" --script="benchmark,program"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=benchmark,program) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "benchmark program[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_numactl`
      - Workflow:
    * `_numactl-interleave`
      - Workflow:
    * `_profile`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,profiler
             - *Warning: no scripts found*

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_ENABLE_NUMACTL: `0`
* CM_ENABLE_PROFILING: `0`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program/_cm.json)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * set,performance,mode,_performance
       * `if (CM_SET_PERFORMANCE_MODE in ['on', 'yes', 'True', True])`
       - CM script: [set-performance-mode](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program/_cm.json)
  1. ***Run native script if exists***
     * [run-ubuntu.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program/run-ubuntu.sh)
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program/_cm.json)

___
### Script output
`cmr "benchmark program [,variations]"  -j`
#### New environment keys (filter)

* `CM_RUN_CMD`
#### New environment keys auto-detected from customize

* `CM_RUN_CMD`