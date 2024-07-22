**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/install-terraform-from-src).**



Automatically generated README for this automation recipe: **install-terraform-from-src**

Category: **Cloud automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-terraform-from-src,d79d47a074f34428) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-terraform-from-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,terraform,from-src*
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

````cmr "install terraform from-src" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,terraform,from-src`

`cm run script --tags=install,terraform,from-src `

*or*

`cmr "install terraform from-src"`

`cmr "install terraform from-src " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,terraform,from-src'
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

```cmr "cm gui" --script="install,terraform,from-src"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,terraform,from-src) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install terraform from-src" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `main`

* `main`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-terraform-from-src/_cm.json)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,tool,go
       - CM script: [get-go](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-go)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-terraform-from-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-terraform-from-src/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-terraform-from-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-terraform-from-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-terraform-from-src/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-terraform-from-src/_cm.json)

___
### Script output
`cmr "install terraform from-src "  -j`
#### New environment keys (filter)

* `+PATH`
* `CM_TERRAFORM_*`
#### New environment keys auto-detected from customize

* `CM_TERRAFORM_BIN_WITH_PATH`
* `CM_TERRAFORM_INSTALLED_PATH`