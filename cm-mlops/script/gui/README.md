<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM GUI](#cm-gui)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Input description](#input-description)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! Use `README-extra.md` to add more info.*

### Description

This CM script provides a unified GUI to run CM scripts using [Streamlit library](https://streamlit.io).

If you want to run it in a cloud (Azure, AWS, GCP), you need to open some port and test that you can reach it from outside.

By default, streamlit uses port 8501 but you can change it as follows:

```bash
cm run script "cm gui" --port 80
```

If you have troubles accessing this port, use this simple python module to test if your port is open:
```bash
python3 -m http.server 80
```


#### Information

* Category: *GUI.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *cm,gui,cm-gui,script-gui,cm-script-gui,streamlit*
* Output cached?: *False*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=cm,gui,cm-gui,script-gui,cm-script-gui,streamlit[,variations] [--input_flags]`

2. `cm run script "cm gui cm-gui script-gui cm-script-gui streamlit[,variations]" [--input_flags]`

3. `cm run script 605cac42514a4c69 [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'cm,gui,cm-gui,script-gui,cm-script-gui,streamlit'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### CM GUI

```cm run script --tags=gui --script="cm,gui,cm-gui,script-gui,cm-script-gui,streamlit"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=cm,gui,cm-gui,script-gui,cm-script-gui,streamlit) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * Group "**app**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_graph`
      - Environment variables:
        - *CM_GUI_APP*: `graph`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * get,generic-python-lib,_matplotlib
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_mpld3
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_main`
      - Environment variables:
        - *CM_GUI_APP*: `app`
      - Workflow:
    * `_playground`
      - Environment variables:
        - *CM_GUI_APP*: `playground`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * get,generic-python-lib,_matplotlib
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_mpld3
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_streamlit_option_menu
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_pandas
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


#### Input description

* --**script** script tags
* --**app** gui app

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "script":...}
```

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--address=value`  &rarr;  `CM_GUI_ADDRESS=value`
* `--app=value`  &rarr;  `CM_GUI_APP=value`
* `--no_browser=value`  &rarr;  `CM_GUI_NO_BROWSER=value`
* `--no_run=value`  &rarr;  `CM_GUI_NO_RUN=value`
* `--port=value`  &rarr;  `CM_GUI_PORT=value`
* `--prefix=value`  &rarr;  `CM_GUI_SCRIPT_PREFIX_LINUX=value`
* `--script=value`  &rarr;  `CM_GUI_SCRIPT_TAGS=value`
* `--title=value`  &rarr;  `CM_GUI_TITLE=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "address":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GUI_EXTRA_CMD: ``
* CM_GUI_SCRIPT_PREFIX_LINUX: `gnome-terminal --`
* CM_GUI_APP: `app`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_cmind
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_streamlit
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui/_cm.yaml)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui/_cm.yaml)
</details>

___
### Script output
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)