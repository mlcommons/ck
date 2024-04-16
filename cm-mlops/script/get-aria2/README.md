**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-aria2).**



Automatically generated README for this automation recipe: **get-aria2**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-aria2,d83419a90a0c40d0) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aria2)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *get,aria2,get-aria2*
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

````cmr "get aria2 get-aria2" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,aria2,get-aria2`

`cm run script --tags=get,aria2,get-aria2 [--input_flags]`

*or*

`cmr "get aria2 get-aria2"`

`cmr "get aria2 get-aria2 " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,aria2,get-aria2'
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

```cmr "cm gui" --script="get,aria2,get-aria2"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,aria2,get-aria2) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get aria2 get-aria2" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--install=value`  &rarr;  `CM_FORCE_INSTALL=value`
* `--src=value`  &rarr;  `CM_ARIA2_BUILD_FROM_SRC=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "install":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aria2/_cm.yaml)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aria2/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aria2/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aria2/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aria2/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aria2/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aria2/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aria2/_cm.yaml)

___
### Script output
`cmr "get aria2 get-aria2 " [--input_flags] -j`
#### New environment keys (filter)

* `+PATH`
* `CM_ARIA2_*`
#### New environment keys auto-detected from customize

* `CM_ARIA2_BIN_WITH_PATH`
* `CM_ARIA2_DOWNLOAD_DIR`
* `CM_ARIA2_DOWNLOAD_FILE`
* `CM_ARIA2_DOWNLOAD_FILE2`
* `CM_ARIA2_DOWNLOAD_URL`
* `CM_ARIA2_INSTALLED_PATH`
* `CM_ARIA2_INSTALLED_TO_CACHE`