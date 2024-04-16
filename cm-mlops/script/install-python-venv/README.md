**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/install-python-venv).**



Automatically generated README for this automation recipe: **install-python-venv**

Category: **Python automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-python-venv,7633ebada4584c6c) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-venv)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,python,get-python-venv,python-venv*
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

````cmr "install python get-python-venv python-venv" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,python,get-python-venv,python-venv`

`cm run script --tags=install,python,get-python-venv,python-venv[,variations] `

*or*

`cmr "install python get-python-venv python-venv"`

`cmr "install python get-python-venv python-venv [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,python,get-python-venv,python-venv'
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

```cmr "cm gui" --script="install,python,get-python-venv,python-venv"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,python,get-python-venv,python-venv) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install python get-python-venv python-venv[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_lto`
      - Workflow:
    * `_optimized`
      - Workflow:
    * `_shared`
      - Workflow:
    * `_with-custom-ssl`
      - Workflow:
    * `_with-ssl`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-venv/_cm.json)***
     * get,python,-virtual
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-venv/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-venv/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-venv/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-venv/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-venv/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-venv/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-venv/_cm.json)***
     * get,python3
       * CM names: `--adr.['register-python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)

___
### Script output
`cmr "install python get-python-venv python-venv [,variations]"  -j`
#### New environment keys (filter)

* `CM_PYTHON_BIN_WITH_PATH`
* `CM_VIRTUAL_ENV_*`
#### New environment keys auto-detected from customize

* `CM_PYTHON_BIN_WITH_PATH`
* `CM_VIRTUAL_ENV_DIR`
* `CM_VIRTUAL_ENV_PATH`
* `CM_VIRTUAL_ENV_SCRIPTS_PATH`