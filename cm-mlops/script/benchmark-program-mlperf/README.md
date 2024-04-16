**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-program-mlperf).**



Automatically generated README for this automation recipe: **benchmark-program-mlperf**

Category: **Modular MLPerf inference benchmark pipeline**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=benchmark-program-mlperf,cfff0132a8aa4018) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program-mlperf)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *mlperf,benchmark-mlperf*
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

````cmr "mlperf benchmark-mlperf" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=mlperf,benchmark-mlperf`

`cm run script --tags=mlperf,benchmark-mlperf[,variations] `

*or*

`cmr "mlperf benchmark-mlperf"`

`cmr "mlperf benchmark-mlperf [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'mlperf,benchmark-mlperf'
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

```cmr "cm gui" --script="mlperf,benchmark-mlperf"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=mlperf,benchmark-mlperf) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "mlperf benchmark-mlperf[variations]" `

___
### Customization


#### Variations

  * Group "**power-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_no-power`** (default)
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * benchmark-program,program
             * CM names: `--adr.['benchmark-program']...`
             - CM script: [benchmark-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)
    * `_power`
      - Environment variables:
        - *CM_MLPERF_POWER*: `yes`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * benchmark-program,program
             * CM names: `--adr.['benchmark-program']...`
             - CM script: [benchmark-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)
        1. ***Read "post_deps" on other CM scripts***
           * run,mlperf,power,client
             * `if (CM_MLPERF_LOADGEN_MODE  == performance)`
             * CM names: `--adr.['mlperf-power-client']...`
             - CM script: [run-mlperf-power-client](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client)

    </details>


#### Default variations

`_no-power`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program-mlperf/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program-mlperf/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program-mlperf/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program-mlperf/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program-mlperf/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program-mlperf/_cm.json)

___
### Script output
`cmr "mlperf benchmark-mlperf [,variations]"  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
