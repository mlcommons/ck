**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-any-mlperf-inference-implementation).**



Automatically generated README for this automation recipe: **benchmark-any-mlperf-inference-implementation**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=benchmark-any-mlperf-inference-implementation,8d3cd46f54464810) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-any-mlperf-inference-implementation)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *benchmark,run,natively,all,inference,any,mlperf,mlperf-implementation,implementation,mlperf-models*
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

````cmr "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=benchmark,run,natively,all,inference,any,mlperf,mlperf-implementation,implementation,mlperf-models`

`cm run script --tags=benchmark,run,natively,all,inference,any,mlperf,mlperf-implementation,implementation,mlperf-models[,variations] [--input_flags]`

*or*

`cmr "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models"`

`cmr "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'benchmark,run,natively,all,inference,any,mlperf,mlperf-implementation,implementation,mlperf-models'
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

```cmr "cm gui" --script="benchmark,run,natively,all,inference,any,mlperf,mlperf-implementation,implementation,mlperf-models"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=benchmark,run,natively,all,inference,any,mlperf,mlperf-implementation,implementation,mlperf-models) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_aws-dl2q.24xlarge,qualcomm`
      - Workflow:
    * `_mini,power`
      - Workflow:
    * `_orin,power`
      - Workflow:
    * `_phoenix,nvidia`
      - Workflow:
    * `_phoenix,power`
      - Workflow:
    * `_phoenix,reference`
      - Workflow:
    * `_rb6,power`
      - Workflow:
    * `_rb6,qualcomm`
      - Workflow:
    * `_rpi4,power`
      - Workflow:
    * `_sapphire-rapids.24c,nvidia`
      - Workflow:

    </details>


  * Group "**implementation**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse`
      - Environment variables:
        - *DIVISION*: `open`
        - *IMPLEMENTATION*: `deepsparse`
      - Workflow:
    * `_intel`
      - Environment variables:
        - *IMPLEMENTATION*: `intel`
      - Workflow:
    * `_mil`
      - Environment variables:
        - *IMPLEMENTATION*: `mil`
      - Workflow:
    * `_nvidia`
      - Environment variables:
        - *IMPLEMENTATION*: `nvidia-original`
      - Workflow:
    * `_qualcomm`
      - Environment variables:
        - *IMPLEMENTATION*: `qualcomm`
      - Workflow:
    * `_reference`
      - Environment variables:
        - *IMPLEMENTATION*: `reference`
      - Workflow:
    * `_tflite-cpp`
      - Environment variables:
        - *IMPLEMENTATION*: `tflite_cpp`
      - Workflow:

    </details>


  * Group "**power**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_performance-only`** (default)
      - Workflow:
    * `_power`
      - Environment variables:
        - *POWER*: `True`
      - Workflow:

    </details>


  * Group "**sut**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_aws-dl2q.24xlarge`
      - Workflow:
    * `_macbookpro-m1`
      - Environment variables:
        - *CATEGORY*: `edge`
        - *DIVISION*: `closed`
      - Workflow:
    * `_mini`
      - Workflow:
    * `_orin`
      - Workflow:
    * `_orin.32g`
      - Environment variables:
        - *CATEGORY*: `edge`
        - *DIVISION*: `closed`
      - Workflow:
    * `_phoenix`
      - Environment variables:
        - *CATEGORY*: `edge`
        - *DIVISION*: `closed`
      - Workflow:
    * `_rb6`
      - Workflow:
    * `_rpi4`
      - Workflow:
    * `_sapphire-rapids.24c`
      - Environment variables:
        - *CATEGORY*: `edge`
        - *DIVISION*: `closed`
      - Workflow:

    </details>


#### Default variations

`_performance-only`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--backends=value`  &rarr;  `BACKENDS=value`
* `--category=value`  &rarr;  `CATEGORY=value`
* `--devices=value`  &rarr;  `DEVICES=value`
* `--division=value`  &rarr;  `DIVISION=value`
* `--extra_args=value`  &rarr;  `EXTRA_ARGS=value`
* `--models=value`  &rarr;  `MODELS=value`
* `--power_server=value`  &rarr;  `POWER_SERVER=value`
* `--power_server_port=value`  &rarr;  `POWER_SERVER_PORT=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "backends":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* DIVISION: `open`
* CATEGORY: `edge`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-any-mlperf-inference-implementation/_cm.yaml)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-any-mlperf-inference-implementation/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-any-mlperf-inference-implementation/_cm.yaml)
  1. ***Run native script if exists***
     * [run-template.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-any-mlperf-inference-implementation/run-template.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-any-mlperf-inference-implementation/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-any-mlperf-inference-implementation/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-any-mlperf-inference-implementation/_cm.yaml)

___
### Script output
`cmr "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models [,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
