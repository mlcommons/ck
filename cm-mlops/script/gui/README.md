**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/gui).**



Automatically generated README for this automation recipe: **gui**

Category: **GUI**

License: **Apache 2.0**

Developers: [Grigori Fursin](https://cKnowledge.org/gfursin)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=gui,605cac42514a4c69) ]*

---

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



---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/gui)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *cm,gui,cm-gui,script-gui,cm-script-gui,streamlit*
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

````cmr "cm gui cm-gui script-gui cm-script-gui streamlit" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=cm,gui,cm-gui,script-gui,cm-script-gui,streamlit`

`cm run script --tags=cm,gui,cm-gui,script-gui,cm-script-gui,streamlit[,variations] [--input_flags]`

*or*

`cmr "cm gui cm-gui script-gui cm-script-gui streamlit"`

`cmr "cm gui cm-gui script-gui cm-script-gui streamlit [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*


#### Input Flags

* --**script**=script tags
* --**app**=gui app

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "script":...}
```
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

`cm docker script "cm gui cm-gui script-gui cm-script-gui streamlit[variations]" [--input_flags]`

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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/gui/_cm.yaml)***
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
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/gui/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/gui/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/gui/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/gui/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/gui/_cm.yaml)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/gui/_cm.yaml)

___
### Script output
`cmr "cm gui cm-gui script-gui cm-script-gui streamlit [,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
