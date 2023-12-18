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

#### Summary

* Category: *DevOps automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *dae,file,download-and-extract*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=dae,file,download-and-extract[,variations] [--input_flags]`

2. `cmr "dae file download-and-extract[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'dae,file,download-and-extract'
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

```cmr "cm gui" --script="dae,file,download-and-extract"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=dae,file,download-and-extract) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "dae file download-and-extract[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_extract`
      - Environment variables:
        - *CM_DAE_EXTRACT_DOWNLOADED*: `yes`
      - Workflow:
    * `_keep`
      - Environment variables:
        - *CM_EXTRACT_REMOVE_EXTRACTED*: `no`
      - Workflow:
    * `_no-remove-extracted`
      - Environment variables:
        - *CM_EXTRACT_REMOVE_EXTRACTED*: `no`
      - Workflow:
    * `_url.#`
      - Environment variables:
        - *CM_DAE_URL*: `#`
      - Workflow:

    </details>


  * Group "**download-tool**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cmutil`** (default)
      - Workflow:
    * `_curl`
      - Workflow:
    * `_gdown`
      - Workflow:
    * `_torrent`
      - Environment variables:
        - *CM_DAE_DOWNLOAD_USING_TORRENT*: `yes`
        - *CM_TORRENT_WAIT_UNTIL_COMPLETED*: `yes`
        - *CM_TORRENT_DOWNLOADED_PATH_ENV_KEY*: `CM_DAE_FILEPATH`
        - *CM_TORRENT_DOWNLOADED_FILE_NAME*: `<<<CM_DAE_FILENAME>>>`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * download,torrent
             - CM script: [download-torrent](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-torrent)
    * `_wget`
      - Workflow:

    </details>


#### Default variations

`_cmutil`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--extra_folder=value`  &rarr;  `CM_EXTRACT_TO_FOLDER=value`
* `--extract_path=value`  &rarr;  `CM_EXTRACT_PATH=value`
* `--local_path=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
* `--url=value`  &rarr;  `CM_DAE_URL=value`
* `--verify=value`  &rarr;  `CM_VERIFY_SSL=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "download_path":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract/_cm.json)***
     * download,file
       * `if (CM_DAE_DOWNLOAD_USING_TORRENT not in ['yes', 'True'])`
       * CM names: `--adr.['download-script']...`
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. ***Run native script if exists***
  1. ***Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract/_cm.json)***
     * extract,file
       * `if (CM_DAE_EXTRACT_DOWNLOADED in ['yes', 'True'])`
       * CM names: `--adr.['extract-script']...`
       - CM script: [extract-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/extract-file)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract/_cm.json)
</details>

___
### Script output
`cmr "dae file download-and-extract[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `<<<CM_DOWNLOAD_FINAL_ENV_NAME>>>`
* `<<<CM_EXTRACT_FINAL_ENV_NAME>>>`
* `CM_DOWNLOAD_DOWNLOADED_PATH*`
* `CM_EXTRACT_EXTRACTED_PATH`
* `CM_GET_DEPENDENT_CACHED_PATH`
#### New environment keys auto-detected from customize

* `CM_GET_DEPENDENT_CACHED_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)