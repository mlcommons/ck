**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/push-mlperf-inference-results-to-github).**



Automatically generated README for this automation recipe: **push-mlperf-inference-results-to-github**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=push-mlperf-inference-results-to-github,36c2ffd5df5d453a) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-mlperf-inference-results-to-github)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *push,mlperf,mlperf-inference-results,publish-results,inference,submission,github*
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

````cmr "push mlperf mlperf-inference-results publish-results inference submission github" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=push,mlperf,mlperf-inference-results,publish-results,inference,submission,github`

`cm run script --tags=push,mlperf,mlperf-inference-results,publish-results,inference,submission,github [--input_flags]`

*or*

`cmr "push mlperf mlperf-inference-results publish-results inference submission github"`

`cmr "push mlperf mlperf-inference-results publish-results inference submission github " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'push,mlperf,mlperf-inference-results,publish-results,inference,submission,github'
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

```cmr "cm gui" --script="push,mlperf,mlperf-inference-results,publish-results,inference,submission,github"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=push,mlperf,mlperf-inference-results,publish-results,inference,submission,github) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "push mlperf mlperf-inference-results publish-results inference submission github" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--branch=value`  &rarr;  `CM_GIT_BRANCH=value`
* `--commit_message=value`  &rarr;  `CM_MLPERF_RESULTS_REPO_COMMIT_MESSAGE=value`
* `--repo_branch=value`  &rarr;  `CM_GIT_BRANCH=value`
* `--repo_url=value`  &rarr;  `CM_MLPERF_RESULTS_GIT_REPO_URL=value`
* `--submission_dir=value`  &rarr;  `CM_MLPERF_INFERENCE_SUBMISSION_DIR=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "branch":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_RESULTS_GIT_REPO_URL: `https://github.com/ctuning/mlperf_inference_submissions_v4.0`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-mlperf-inference-results-to-github/_cm.json)***
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-sys-util,_rsync
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,mlperf,submission,dir
       * `if (CM_MLPERF_INFERENCE_SUBMISSION_DIR  != on)`
       * CM names: `--adr.['get-mlperf-submission-dir']...`
       - CM script: [get-mlperf-inference-submission-dir](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-submission-dir)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-mlperf-inference-results-to-github/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-mlperf-inference-results-to-github/_cm.json)***
     * get,git,repo
       * CM names: `--adr.['get-git-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-mlperf-inference-results-to-github/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-mlperf-inference-results-to-github/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-mlperf-inference-results-to-github/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-mlperf-inference-results-to-github/_cm.json)

___
### Script output
`cmr "push mlperf mlperf-inference-results publish-results inference submission github " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
