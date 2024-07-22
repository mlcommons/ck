**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/activate-python-venv).**



Automatically generated README for this automation recipe: **activate-python-venv**

Category: **Python automation**

License: **Apache 2.0**

Developers: [Grigori Fursin](https://cKnowledge.org/gfursin)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=activate-python-venv,fcbbb84946f34c55) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/activate-python-venv)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *activate,python-venv*
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

````cmr "activate python-venv" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=activate,python-venv`

`cm run script --tags=activate,python-venv `

*or*

`cmr "activate python-venv"`

`cmr "activate python-venv " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'activate,python-venv'
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

```cmr "cm gui" --script="activate,python-venv"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=activate,python-venv) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "activate python-venv" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/activate-python-venv/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/activate-python-venv/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/activate-python-venv/_cm.json)***
     * install,python-venv
       * CM names: `--adr.['python-venv']...`
       - CM script: [install-python-venv](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-venv)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/activate-python-venv/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/activate-python-venv/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/activate-python-venv/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/activate-python-venv/_cm.json)

___
### Script output
`cmr "activate python-venv "  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
