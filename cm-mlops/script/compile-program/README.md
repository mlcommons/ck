**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/compile-program).**



Automatically generated README for this automation recipe: **compile-program**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=compile-program,c05042ba005a4bfa) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-program)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *compile,program,c-program,cpp-program,compile-program,compile-c-program,compile-cpp-program*
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

````cmr "compile program c-program cpp-program compile-program compile-c-program compile-cpp-program" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=compile,program,c-program,cpp-program,compile-program,compile-c-program,compile-cpp-program`

`cm run script --tags=compile,program,c-program,cpp-program,compile-program,compile-c-program,compile-cpp-program `

*or*

`cmr "compile program c-program cpp-program compile-program compile-c-program compile-cpp-program"`

`cmr "compile program c-program cpp-program compile-program compile-c-program compile-cpp-program " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'compile,program,c-program,cpp-program,compile-program,compile-c-program,compile-cpp-program'
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

```cmr "cm gui" --script="compile,program,c-program,cpp-program,compile-program,compile-c-program,compile-cpp-program"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=compile,program,c-program,cpp-program,compile-program,compile-c-program,compile-cpp-program) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "compile program c-program cpp-program compile-program compile-c-program compile-cpp-program" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* SKIP_RECOMPILE: `no`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-program/_cm.json)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,compiler
       * CM names: `--adr.['compiler']...`
       - CM script: [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
     * get,compiler-flags
       - CM script: [get-compiler-flags](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-compiler-flags)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-program/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-program/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-program/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-program/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-program/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-program/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-program/_cm.json)

___
### Script output
`cmr "compile program c-program cpp-program compile-program compile-c-program compile-cpp-program "  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
