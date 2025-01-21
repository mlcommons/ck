# gui
Automatically generated README for this automation recipe: **gui**

Category: **[GUI](..)**

License: **Apache 2.0**

Developers: [Grigori Fursin](https://cKnowledge.org/gfursin)


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


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/gui/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "cm gui cm-gui script-gui cm-script-gui streamlit" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=cm,gui,cm-gui,script-gui,cm-script-gui,streamlit[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "cm gui cm-gui script-gui cm-script-gui streamlit [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


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


=== "Docker"
    ##### Run this script via Docker (beta)

    ```bash
    cm docker script "cm gui cm-gui script-gui cm-script-gui streamlit[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * Group "**app**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_chatgpt`
               - ENV variables:
                   - CM_GUI_APP: `chatgpt`
        * `_graph`
               - ENV variables:
                   - CM_GUI_APP: `graph`
        * `_main`
               - ENV variables:
                   - CM_GUI_APP: `app`
        * `_playground`
               - ENV variables:
                   - CM_GUI_APP: `playground`

        </details>

=== "Input Flags"


    #### Input Flags

    * --**script:** script tags
    * --**app:** gui app
=== "Input Flag Mapping"


    #### Script flags mapped to environment

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



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_GUI_EXTRA_CMD: ``
    * CM_GUI_SCRIPT_PREFIX_LINUX: `gnome-terminal --`
    * CM_GUI_APP: `app`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/gui/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/gui/run.bat)
___
#### Script output
```bash
cmr "cm gui cm-gui script-gui cm-script-gui streamlit [variations]" [--input_flags] -j
```