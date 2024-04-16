**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-google-test).**



Automatically generated README for this automation recipe: **get-google-test**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-google-test,02945138a5614253) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-google-test)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,google-test,googletest,gtest,test,google*
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

````cmr "get google-test googletest gtest test google" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,google-test,googletest,gtest,test,google`

`cm run script --tags=get,google-test,googletest,gtest,test,google `

*or*

`cmr "get google-test googletest gtest test google"`

`cmr "get google-test googletest gtest test google " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,google-test,googletest,gtest,test,google'
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

```cmr "cm gui" --script="get,google-test,googletest,gtest,test,google"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,google-test,googletest,gtest,test,google) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get google-test googletest gtest test google" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `1.14.0`

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-google-test/_cm.json)***
     * get,cmake
       * CM names: `--adr.['cmake']...`
       - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
     * get,compiler
       * CM names: `--adr.['compiler']...`
       - CM script: [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-google-test/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-google-test/_cm.json)***
     * get,git,repo,_repo.https://github.com/google/googletest.git
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-google-test/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-google-test/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-google-test/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-google-test/_cm.json)

___
### Script output
`cmr "get google-test googletest gtest test google "  -j`
#### New environment keys (filter)

* `+C_INCLUDE_PATH`
* `+LD_LIBRARY_PATH`
* `CM_GOOGLE_TEST_INSTALL_PATH`
* `CM_GOOGLE_TEST_SRC_PATH`
#### New environment keys auto-detected from customize

* `CM_GOOGLE_TEST_INSTALL_PATH`
* `CM_GOOGLE_TEST_SRC_PATH`