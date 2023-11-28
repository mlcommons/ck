<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
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

*Note that this README is automatically generated - don't edit!*

### About

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


#### Summary

* Category: *GUI.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *cm,gui,cm-gui,script-gui,cm-script-gui,streamlit*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=cm,gui,cm-gui,script-gui,cm-script-gui,streamlit[,variations] [--input_flags]`

2. `cmr "cm gui cm-gui script-gui cm-script-gui streamlit[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="cm,gui,cm-gui,script-gui,cm-script-gui,streamlit"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=cm,gui,cm-gui,script-gui,cm-script-gui,streamlit) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "cm gui cm-gui script-gui cm-script-gui streamlit[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * Group "**app**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_chatgpt`
      - Environment variables:
        - *CM_GUI_APP*: `chatgpt`
      - Workflow:
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
           * get,generic-python-lib,_package.plotly
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.streamlit-aggrid
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
* `--exp_key_c=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_AXIS_KEY_C=value`
* `--exp_key_s=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_AXIS_KEY_S=value`
* `--exp_key_x=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_AXIS_KEY_X=value`
* `--exp_key_y=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_AXIS_KEY_Y=value`
* `--exp_max_results=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_MAX_RESULTS=value`
* `--exp_name=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_NAME=value`
* `--exp_tags=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_TAGS=value`
* `--exp_title=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_TITLE=value`
* `--exp_uid=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_RESULT_UID=value`
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
`cmr "cm gui cm-gui script-gui cm-script-gui streamlit[,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)