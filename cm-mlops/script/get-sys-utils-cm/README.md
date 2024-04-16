**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-sys-utils-cm).**



Automatically generated README for this automation recipe: **get-sys-utils-cm**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-sys-utils-cm,bc90993277e84b8e) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,sys-utils-cm*
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

````cmr "get sys-utils-cm" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,sys-utils-cm`

`cm run script --tags=get,sys-utils-cm[,variations] [--input_flags]`

*or*

`cmr "get sys-utils-cm"`

`cmr "get sys-utils-cm [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,sys-utils-cm'
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

```cmr "cm gui" --script="get,sys-utils-cm"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,sys-utils-cm) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get sys-utils-cm[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_user`
      - Environment variables:
        - *CM_PYTHON_PIP_USER*: `--user`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--skip=value`  &rarr;  `CM_SKIP_SYS_UTILS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "skip":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm/_cm.json)
  1. ***Run native script if exists***
     * [run-arch.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm/run-arch.sh)
     * [run-debian.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm/run-debian.sh)
     * [run-macos.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm/run-macos.sh)
     * [run-rhel.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm/run-rhel.sh)
     * [run-sles.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm/run-sles.sh)
     * [run-ubuntu.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm/run-ubuntu.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm/_cm.json)

___
### Script output
`cmr "get sys-utils-cm [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `+PATH`
#### New environment keys auto-detected from customize
