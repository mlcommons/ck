**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/push-csv-to-spreadsheet).**



Automatically generated README for this automation recipe: **push-csv-to-spreadsheet**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=push-csv-to-spreadsheet,5ec9e5fa7feb4fff) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-csv-to-spreadsheet)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *push,google-spreadsheet,spreadsheet,push-to-google-spreadsheet*
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

````cmr "push google-spreadsheet spreadsheet push-to-google-spreadsheet" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=push,google-spreadsheet,spreadsheet,push-to-google-spreadsheet`

`cm run script --tags=push,google-spreadsheet,spreadsheet,push-to-google-spreadsheet [--input_flags]`

*or*

`cmr "push google-spreadsheet spreadsheet push-to-google-spreadsheet"`

`cmr "push google-spreadsheet spreadsheet push-to-google-spreadsheet " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'push,google-spreadsheet,spreadsheet,push-to-google-spreadsheet'
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

```cmr "cm gui" --script="push,google-spreadsheet,spreadsheet,push-to-google-spreadsheet"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=push,google-spreadsheet,spreadsheet,push-to-google-spreadsheet) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "push google-spreadsheet spreadsheet push-to-google-spreadsheet" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--csv_file=value`  &rarr;  `CM_CSV_FILE_PATH=value`
* `--sheet_name=value`  &rarr;  `CM_GOOGLE_SHEET_NAME=value`
* `--spreadsheet_id=value`  &rarr;  `CM_GOOGLE_SPREADSHEET_ID=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "csv_file":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GOOGLE_SPREADSHEET_ID: `1gMHjXmFmwZR4-waPPyxy5Pc3VARqX3kKUWxkP97Xa6Y`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-csv-to-spreadsheet/_cm.json)***
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_google-api-python-client
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_google-auth-oauthlib
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-csv-to-spreadsheet/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-csv-to-spreadsheet/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-csv-to-spreadsheet/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-csv-to-spreadsheet/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-csv-to-spreadsheet/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-csv-to-spreadsheet/_cm.json)

___
### Script output
`cmr "push google-spreadsheet spreadsheet push-to-google-spreadsheet " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
