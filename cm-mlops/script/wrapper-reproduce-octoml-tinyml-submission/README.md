*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Versions](#versions)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
  * [ Script input flags mapped to environment](#script-input-flags-mapped-to-environment)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Modular MLPerf benchmarks.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml

___
### Versions
Default version: *r1.0*

___
### Default environment

___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)***
     * get,python
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)
___
### New environment export

___
### New environment detected from customize

___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml"`

*or*

`cm run script "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml"`

*or*

`cm run script b946001e289c4480`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* flash --> **CM_FLASH_BOARD**
* recreate_binary --> **CM_RECREATE_BINARY**

Examples:

```bash
cm run script "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml" --flash=...
```
```python
r=cm.access({... , "flash":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)