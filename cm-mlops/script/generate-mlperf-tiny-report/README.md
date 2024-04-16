**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-mlperf-tiny-report).**



Automatically generated README for this automation recipe: **generate-mlperf-tiny-report**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Developers: [Grigori Fursin](https://cKnowledge.org/gfursin)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=generate-mlperf-tiny-report,709c3f3f9b3e4783) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-report)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *generate,mlperf,tiny,mlperf-tiny,report*
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

````cmr "generate mlperf tiny mlperf-tiny report" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=generate,mlperf,tiny,mlperf-tiny,report`

`cm run script --tags=generate,mlperf,tiny,mlperf-tiny,report [--input_flags]`

*or*

`cmr "generate mlperf tiny mlperf-tiny report"`

`cmr "generate mlperf tiny mlperf-tiny report " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'generate,mlperf,tiny,mlperf-tiny,report'
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

```cmr "cm gui" --script="generate,mlperf,tiny,mlperf-tiny,report"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=generate,mlperf,tiny,mlperf-tiny,report) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "generate mlperf tiny mlperf-tiny report" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--repo_tags=value`  &rarr;  `CM_IMPORT_TINYMLPERF_REPO_TAGS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "repo_tags":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_IMPORT_TINYMLPERF_REPO_TAGS: `1.1-private`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-report/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_xlsxwriter
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_pandas
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-report/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-report/_cm.yaml)
  1. ***Run native script if exists***
     * [run_submission_checker.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-report/run_submission_checker.bat)
     * [run_submission_checker.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-report/run_submission_checker.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-report/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-report/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-report/_cm.yaml)

___
### Script output
`cmr "generate mlperf tiny mlperf-tiny report " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
