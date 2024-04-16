**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-zendnn).**



Automatically generated README for this automation recipe: **get-zendnn**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-zendnn,d1c6feb0ee684b09) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zendnn)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,zendnn,amd,from.src*
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

````cmr "get zendnn amd from.src" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,zendnn,amd,from.src`

`cm run script --tags=get,zendnn,amd,from.src `

*or*

`cmr "get zendnn amd from.src"`

`cmr "get zendnn amd from.src " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,zendnn,amd,from.src'
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

```cmr "cm gui" --script="get,zendnn,amd,from.src"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,zendnn,amd,from.src) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get zendnn amd from.src" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zendnn/_cm.json)***
     * get,amd,aocl
       * CM names: `--adr.['aocl']...`
       - CM script: [get-aocl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-aocl)
     * get,lib,blis,_amd
       - CM script: [get-blis](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-blis)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,git,_repo.https://github.com/amd/ZenDNN.git
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zendnn/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zendnn/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zendnn/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zendnn/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zendnn/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zendnn/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zendnn/_cm.json)

___
### Script output
`cmr "get zendnn amd from.src "  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
