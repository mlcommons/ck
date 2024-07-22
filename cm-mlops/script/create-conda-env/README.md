**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/create-conda-env).**



Automatically generated README for this automation recipe: **create-conda-env**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=create-conda-env,e39e0b04c86a40f2) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-conda-env)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *create,get,env,conda-env,conda-environment,create-conda-environment*
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

````cmr "create get env conda-env conda-environment create-conda-environment" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=create,get,env,conda-env,conda-environment,create-conda-environment`

`cm run script --tags=create,get,env,conda-env,conda-environment,create-conda-environment[,variations] `

*or*

`cmr "create get env conda-env conda-environment create-conda-environment"`

`cmr "create get env conda-env conda-environment create-conda-environment [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'create,get,env,conda-env,conda-environment,create-conda-environment'
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

```cmr "cm gui" --script="create,get,env,conda-env,conda-environment,create-conda-environment"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=create,get,env,conda-env,conda-environment,create-conda-environment) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "create get env conda-env conda-environment create-conda-environment[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_name.#`
      - Environment variables:
        - *CM_CONDA_ENV_NAME*: `#`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-conda-env/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,conda
       * CM names: `--adr.['conda']...`
       - CM script: [get-conda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-conda)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-conda-env/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-conda-env/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-conda-env/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-conda-env/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-conda-env/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-conda-env/_cm.json)

___
### Script output
`cmr "create get env conda-env conda-environment create-conda-environment [,variations]"  -j`
#### New environment keys (filter)

* `+LD_LIBRARY_PATH`
* `+PATH`
* `CM_CONDA_BIN_PATH`
* `CM_CONDA_LIB_PATH`
* `CM_CONDA_PREFIX`
* `CONDA_PREFIX`
#### New environment keys auto-detected from customize

* `CM_CONDA_BIN_PATH`
* `CM_CONDA_LIB_PATH`
* `CM_CONDA_PREFIX`