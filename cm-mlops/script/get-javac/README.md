**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-javac).**



Automatically generated README for this automation recipe: **get-javac**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-javac,509280c497b24226) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-javac)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,javac*
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

````cmr "get javac" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,javac`

`cm run script --tags=get,javac[,variations] [--input_flags]`

*or*

`cmr "get javac"`

`cmr "get javac [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,javac'
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

```cmr "cm gui" --script="get,javac"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,javac) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get javac[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_install`
      - Environment variables:
        - *CM_JAVAC_PREBUILT_INSTALL*: `on`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--install=value`  &rarr;  `CM_JAVAC_PREBUILT_INSTALL=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "install":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_JAVAC_PREBUILT_VERSION: `19`
* CM_JAVAC_PREBUILT_BUILD: `36`
* CM_JAVAC_PREBUILT_URL: `https://download.java.net/openjdk/jdk${CM_JAVAC_PREBUILT_VERSION}/ri/`
* CM_JAVAC_PREBUILT_FILENAME: `openjdk-${CM_JAVAC_PREBUILT_VERSION}+${CM_JAVAC_PREBUILT_BUILD}_${CM_JAVAC_PREBUILT_HOST_OS}-x64_bin`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-javac/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-javac/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-javac/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-javac/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-javac/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-javac/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-javac/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-javac/_cm.json)

___
### Script output
`cmr "get javac [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `+PATH`
* `CM_JAVAC_*`
* `CM_JAVA_*`
* `JAVA_HOME`
#### New environment keys auto-detected from customize

* `CM_JAVAC_BIN`
* `CM_JAVAC_CACHE_TAGS`
* `CM_JAVAC_PREBUILT_EXT`
* `CM_JAVAC_PREBUILT_FILENAME`
* `CM_JAVAC_PREBUILT_HOST_OS`
* `CM_JAVAC_PREBUILT_URL`
* `CM_JAVA_BIN`
* `CM_JAVA_BIN_WITH_PATH`