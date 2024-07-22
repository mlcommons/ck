**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-lib-protobuf).**



Automatically generated README for this automation recipe: **get-lib-protobuf**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-lib-protobuf,db45f1eb73934f91) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-protobuf)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,google-protobuf,protobuf,lib,lib-protobuf,google*
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

````cmr "get google-protobuf protobuf lib lib-protobuf google" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,google-protobuf,protobuf,lib,lib-protobuf,google`

`cm run script --tags=get,google-protobuf,protobuf,lib,lib-protobuf,google[,variations] `

*or*

`cmr "get google-protobuf protobuf lib lib-protobuf google"`

`cmr "get google-protobuf protobuf lib lib-protobuf google [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,google-protobuf,protobuf,lib,lib-protobuf,google'
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

```cmr "cm gui" --script="get,google-protobuf,protobuf,lib,lib-protobuf,google"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,google-protobuf,protobuf,lib,lib-protobuf,google) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get google-protobuf protobuf lib lib-protobuf google[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_branch.#`
      - Environment variables:
        - *CM_TMP_GIT_CHECKOUT*: `#`
      - Workflow:
    * `_tag.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT_TAG*: `#`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `1.13.0`

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-protobuf/_cm.json)***
     * get,cmake
       - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
     * get,gcc
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-protobuf/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-protobuf/_cm.json)***
     * get,git,repo,_repo.https://github.com/google/protobuf.git
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-protobuf/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-protobuf/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-protobuf/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-protobuf/_cm.json)

___
### Script output
`cmr "get google-protobuf protobuf lib lib-protobuf google [,variations]"  -j`
#### New environment keys (filter)

* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+LD_LIBRARY_PATH`
* `CM_GOOGLE_PROTOBUF_INSTALL_PATH`
* `CM_GOOGLE_PROTOBUF_SRC_PATH`
#### New environment keys auto-detected from customize

* `CM_GOOGLE_PROTOBUF_INSTALL_PATH`
* `CM_GOOGLE_PROTOBUF_SRC_PATH`