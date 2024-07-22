**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/wrapper-reproduce-octoml-tinyml-submission).**



Automatically generated README for this automation recipe: **wrapper-reproduce-octoml-tinyml-submission**

Category: **Reproduce MLPerf benchmarks**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=wrapper-reproduce-octoml-tinyml-submission,b946001e289c4480) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml*
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

````cmr "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml`

`cm run script --tags=run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml [--input_flags]`

*or*

`cmr "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml"`

`cmr "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

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

</details>


#### Run this script via GUI

```cmr "cm gui" --script="run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--flash=value`  &rarr;  `CM_FLASH_BOARD=value`
* `--recreate_binary=value`  &rarr;  `CM_RECREATE_BINARY=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "flash":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `r1.0`

* `r1.0`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)

___
### Script output
`cmr "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
