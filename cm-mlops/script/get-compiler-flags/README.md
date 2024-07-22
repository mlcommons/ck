**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-compiler-flags).**



Automatically generated README for this automation recipe: **get-compiler-flags**

Category: **Compiler automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-compiler-flags,31be8b74a69742f8) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-compiler-flags)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,compiler-flags*
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

````cmr "get compiler-flags" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,compiler-flags`

`cm run script --tags=get,compiler-flags `

*or*

`cmr "get compiler-flags"`

`cmr "get compiler-flags " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,compiler-flags'
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

```cmr "cm gui" --script="get,compiler-flags"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,compiler-flags) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get compiler-flags" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-compiler-flags/_cm.json)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,compiler
       * `if (CM_C_COMPILER_BIN  != on)`
       * CM names: `--adr.['compiler']...`
       - CM script: [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-compiler-flags/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-compiler-flags/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-compiler-flags/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-compiler-flags/_cm.json)

___
### Script output
`cmr "get compiler-flags "  -j`
#### New environment keys (filter)

* `+ CFLAGS`
* `+ CXXFLAGS`
* `+ FFLAGS`
* `+ LDFLAGS`
* `+CM_HOST_OS_DEFAULT_INCLUDE_PATH`
#### New environment keys auto-detected from customize
