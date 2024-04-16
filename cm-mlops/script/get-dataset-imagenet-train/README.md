**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-train).**



Automatically generated README for this automation recipe: **get-dataset-imagenet-train**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-dataset-imagenet-train,2bec165da5cc4ebf) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-train)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,imagenet,train,dataset,original*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "get imagenet train dataset original" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,imagenet,train,dataset,original`

`cm run script --tags=get,imagenet,train,dataset,original [--input_flags]`

*or*

`cmr "get imagenet train dataset original"`

`cmr "get imagenet train dataset original " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,imagenet,train,dataset,original'
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

```cmr "cm gui" --script="get,imagenet,train,dataset,original"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,imagenet,train,dataset,original) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get imagenet train dataset original" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--input=value`  &rarr;  `IMAGENET_TRAIN_PATH=value`
* `--torrent=value`  &rarr;  `CM_DATASET_IMAGENET_TRAIN_TORRENT_PATH=value`

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


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-train/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-train/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-train/_cm.json)***
     * download-and-extract,file,_extract
       * `if (CM_DATASET_IMAGENET_VAL_REQUIRE_DAE in ['yes', 'True'])`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
     * file,extract
       * `if (CM_DAE_ONLY_EXTRACT in ['yes', 'True'])`
       - CM script: [extract-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/extract-file)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-train/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-train/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-train/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-train/_cm.json)

___
### Script output
`cmr "get imagenet train dataset original " [--input_flags] -j`
#### New environment keys (filter)

* `CM_DATASET_IMAGENET_*`
* `CM_DATASET_PATH`
#### New environment keys auto-detected from customize

* `CM_DATASET_IMAGENET_PATH`
* `CM_DATASET_IMAGENET_TRAIN_PATH`
* `CM_DATASET_IMAGENET_TRAIN_REQUIRE_DAE`
* `CM_DATASET_IMAGENET_VAL_REQUIRE_DAE`
* `CM_DATASET_PATH`