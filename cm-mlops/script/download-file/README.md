**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/download-file).**



Automatically generated README for this automation recipe: **download-file**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=download-file,9cdc8dc41aae437e) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-file)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *download,file*
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

````cmr "download file" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=download,file`

`cm run script --tags=download,file[,variations] [--input_flags]`

*or*

`cmr "download file"`

`cmr "download file [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'download,file'
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

```cmr "cm gui" --script="download,file"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=download,file) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "download file[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_url.#`
      - Environment variables:
        - *CM_DOWNLOAD_URL*: `#`
      - Workflow:

    </details>


  * Group "**download-tool**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cmutil`** (default)
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `cmutil`
      - Workflow:
    * `_curl`
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `curl`
      - Workflow:
    * `_gdown`
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `gdown`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_package.gdown
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_rclone`
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `rclone`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,rclone
             - CM script: [get-rclone](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-rclone)
    * `_wget`
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `wget`
      - Workflow:

    </details>


#### Default variations

`_cmutil`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--from=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
* `--local_path=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
* `--md5sum=value`  &rarr;  `CM_DOWNLOAD_CHECKSUM=value`
* `--store=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--url=value`  &rarr;  `CM_DOWNLOAD_URL=value`
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

* CM_RCLONE_COPY_USING: `sync`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-file/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-file/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-file/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-file/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-file/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-file/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-file/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-file/_cm.json)

___
### Script output
`cmr "download file [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `<<<CM_DOWNLOAD_FINAL_ENV_NAME>>>`
* `CM_DOWNLOAD_DOWNLOADED_PATH`
* `CM_GET_DEPENDENT_CACHED_PATH`
#### New environment keys auto-detected from customize

* `CM_DOWNLOAD_DOWNLOADED_PATH`
* `CM_GET_DEPENDENT_CACHED_PATH`