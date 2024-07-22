**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/truncate-mlperf-inference-accuracy-log).**



Automatically generated README for this automation recipe: **truncate-mlperf-inference-accuracy-log**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=truncate-mlperf-inference-accuracy-log,9d5ec20434084d14) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/truncate-mlperf-inference-accuracy-log)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *run,mlc,mlcommons,mlperf,inference,mlperf-inference,truncation,truncator,truncate,accuracy,accuracy-log,accuracy-log-trancation,accuracy-log-truncator,mlc-accuracy-log-trancation,mlc-accuracy-log-truncator*
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

````cmr "run mlc mlcommons mlperf inference mlperf-inference truncation truncator truncate accuracy accuracy-log accuracy-log-trancation accuracy-log-truncator mlc-accuracy-log-trancation mlc-accuracy-log-truncator" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=run,mlc,mlcommons,mlperf,inference,mlperf-inference,truncation,truncator,truncate,accuracy,accuracy-log,accuracy-log-trancation,accuracy-log-truncator,mlc-accuracy-log-trancation,mlc-accuracy-log-truncator`

`cm run script --tags=run,mlc,mlcommons,mlperf,inference,mlperf-inference,truncation,truncator,truncate,accuracy,accuracy-log,accuracy-log-trancation,accuracy-log-truncator,mlc-accuracy-log-trancation,mlc-accuracy-log-truncator [--input_flags]`

*or*

`cmr "run mlc mlcommons mlperf inference mlperf-inference truncation truncator truncate accuracy accuracy-log accuracy-log-trancation accuracy-log-truncator mlc-accuracy-log-trancation mlc-accuracy-log-truncator"`

`cmr "run mlc mlcommons mlperf inference mlperf-inference truncation truncator truncate accuracy accuracy-log accuracy-log-trancation accuracy-log-truncator mlc-accuracy-log-trancation mlc-accuracy-log-truncator " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mlc,mlcommons,mlperf,inference,mlperf-inference,truncation,truncator,truncate,accuracy,accuracy-log,accuracy-log-trancation,accuracy-log-truncator,mlc-accuracy-log-trancation,mlc-accuracy-log-truncator'
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

```cmr "cm gui" --script="run,mlc,mlcommons,mlperf,inference,mlperf-inference,truncation,truncator,truncate,accuracy,accuracy-log,accuracy-log-trancation,accuracy-log-truncator,mlc-accuracy-log-trancation,mlc-accuracy-log-truncator"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,mlc,mlcommons,mlperf,inference,mlperf-inference,truncation,truncator,truncate,accuracy,accuracy-log,accuracy-log-trancation,accuracy-log-truncator,mlc-accuracy-log-trancation,mlc-accuracy-log-truncator) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run mlc mlcommons mlperf inference mlperf-inference truncation truncator truncate accuracy accuracy-log accuracy-log-trancation accuracy-log-truncator mlc-accuracy-log-trancation mlc-accuracy-log-truncator" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--input=value`  &rarr;  `CM_MLPERF_INFERENCE_SUBMISSION_DIR=value`
* `--submission_dir=value`  &rarr;  `CM_MLPERF_INFERENCE_SUBMISSION_DIR=value`
* `--submitter=value`  &rarr;  `CM_MLPERF_SUBMITTER=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "input":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/truncate-mlperf-inference-accuracy-log/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,mlperf,submission,dir
       * `if (CM_MLPERF_INFERENCE_SUBMISSION_DIR  != on)`
       * CM names: `--adr.['get-mlperf-submission-dir']...`
       - CM script: [get-mlperf-inference-submission-dir](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-submission-dir)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/truncate-mlperf-inference-accuracy-log/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/truncate-mlperf-inference-accuracy-log/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/truncate-mlperf-inference-accuracy-log/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/truncate-mlperf-inference-accuracy-log/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/truncate-mlperf-inference-accuracy-log/_cm.json)

___
### Script output
`cmr "run mlc mlcommons mlperf inference mlperf-inference truncation truncator truncate accuracy accuracy-log accuracy-log-trancation accuracy-log-truncator mlc-accuracy-log-trancation mlc-accuracy-log-truncator " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
