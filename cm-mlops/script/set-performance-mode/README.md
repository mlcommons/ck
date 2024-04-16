**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/set-performance-mode).**



Automatically generated README for this automation recipe: **set-performance-mode**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=set-performance-mode,2c0ab7b64692443d) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-performance-mode)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *set,system,performance,power,mode*
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

````cmr "set system performance power mode" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=set,system,performance,power,mode`

`cm run script --tags=set,system,performance,power,mode[,variations] `

*or*

`cmr "set system performance power mode"`

`cmr "set system performance power mode [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'set,system,performance,power,mode'
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

```cmr "cm gui" --script="set,system,performance,power,mode"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=set,system,performance,power,mode) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "set system performance power mode[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_reproducibility`
      - Environment variables:
        - *CM_SET_OS_PERFORMANCE_REPRODUCIBILITY_MODE*: `yes`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_SET_PERFORMANCE_MODE_OF*: `cpu`
      - Workflow:

    </details>


  * Group "**performance-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_performance`** (default)
      - Environment variables:
        - *CM_SET_PERFORMANCE_MODE*: `performance`
      - Workflow:

    </details>


  * Group "**power**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_power`
      - Environment variables:
        - *CM_SET_PERFORMANCE_MODE*: `power`
      - Workflow:

    </details>


#### Default variations

`_cpu,_performance`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-performance-mode/_cm.json)***
     * detect-os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect-cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-performance-mode/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-performance-mode/_cm.json)
  1. ***Run native script if exists***
     * [run-ubuntu.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-performance-mode/run-ubuntu.sh)
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-performance-mode/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-performance-mode/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-performance-mode/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-performance-mode/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-performance-mode/_cm.json)

___
### Script output
`cmr "set system performance power mode [,variations]"  -j`
#### New environment keys (filter)

* `OMP_*`
#### New environment keys auto-detected from customize
