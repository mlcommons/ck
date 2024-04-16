**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/extract-file).**



Automatically generated README for this automation recipe: **extract-file**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=extract-file,3f0b76219d004817) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/extract-file)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *extract,file*
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

````cmr "extract file" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=extract,file`

`cm run script --tags=extract,file[,variations] [--input_flags]`

*or*

`cmr "extract file"`

`cmr "extract file [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'extract,file'
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

```cmr "cm gui" --script="extract,file"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=extract,file) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "extract file[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_keep`
      - Environment variables:
        - *CM_EXTRACT_REMOVE_EXTRACTED*: `no`
      - Workflow:
    * `_no-remove-extracted`
      - Environment variables:
        - *CM_EXTRACT_REMOVE_EXTRACTED*: `no`
      - Workflow:
    * `_path.#`
      - Environment variables:
        - *CM_EXTRACT_FILEPATH*: `#`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--extra_folder=value`  &rarr;  `CM_EXTRACT_TO_FOLDER=value`
* `--extract_path=value`  &rarr;  `CM_EXTRACT_PATH=value`
* `--input=value`  &rarr;  `CM_EXTRACT_FILEPATH=value`
* `--to=value`  &rarr;  `CM_EXTRACT_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "extra_folder":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/extract-file/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/extract-file/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/extract-file/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/extract-file/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/extract-file/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/extract-file/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/extract-file/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/extract-file/_cm.json)

___
### Script output
`cmr "extract file [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `<<<CM_EXTRACT_FINAL_ENV_NAME>>>`
* `CM_EXTRACT_EXTRACTED_PATH`
* `CM_GET_DEPENDENT_CACHED_PATH`
#### New environment keys auto-detected from customize

* `CM_EXTRACT_EXTRACTED_PATH`
* `CM_GET_DEPENDENT_CACHED_PATH`