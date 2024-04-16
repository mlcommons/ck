**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/download-and-extract).**



Automatically generated README for this automation recipe: **download-and-extract**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=download-and-extract,c67e81a4ce2649f5) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-and-extract)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *download-and-extract,file*
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

````cmr "download-and-extract file" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=download-and-extract,file`

`cm run script --tags=download-and-extract,file[,variations] [--input_flags]`

*or*

`cmr "download-and-extract file"`

`cmr "download-and-extract file [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'download-and-extract,file'
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

```cmr "cm gui" --script="download-and-extract,file"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=download-and-extract,file) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "download-and-extract file[variations]" [--input_flags]`

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
    * `_rclone`
      - Workflow:
    * `_torrent`
      - Environment variables:
        - *CM_DAE_DOWNLOAD_USING_TORRENT*: `yes`
        - *CM_TORRENT_DOWNLOADED_FILE_NAME*: `<<<CM_DAE_FILENAME>>>`
        - *CM_TORRENT_DOWNLOADED_PATH_ENV_KEY*: `CM_DAE_FILEPATH`
        - *CM_TORRENT_WAIT_UNTIL_COMPLETED*: `yes`
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
* `--from=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
* `--local_path=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
* `--store=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--to=value`  &rarr;  `CM_EXTRACT_PATH=value`
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
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-and-extract/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-and-extract/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-and-extract/_cm.json)***
     * download,file
       * `if (CM_DAE_DOWNLOAD_USING_TORRENT not in ['yes', 'True'])`
       * CM names: `--adr.['download-script']...`
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. ***Run native script if exists***
  1. ***Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-and-extract/_cm.json)***
     * extract,file
       * `if (CM_DAE_EXTRACT_DOWNLOADED in ['yes', 'True'])`
       * CM names: `--adr.['extract-script']...`
       - CM script: [extract-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/extract-file)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-and-extract/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-and-extract/_cm.json)

___
### Script output
`cmr "download-and-extract file [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `<<<CM_DOWNLOAD_FINAL_ENV_NAME>>>`
* `<<<CM_EXTRACT_FINAL_ENV_NAME>>>`
* `CM_DOWNLOAD_DOWNLOADED_PATH*`
* `CM_EXTRACT_EXTRACTED_PATH`
* `CM_GET_DEPENDENT_CACHED_PATH`
#### New environment keys auto-detected from customize

* `CM_GET_DEPENDENT_CACHED_PATH`