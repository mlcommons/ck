**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/convert-csv-to-md).**



Automatically generated README for this automation recipe: **convert-csv-to-md**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=convert-csv-to-md,200a95b80bee4a25) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-csv-to-md)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *csv-to-md,convert,to-md,from-csv*
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

````cmr "csv-to-md convert to-md from-csv" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=csv-to-md,convert,to-md,from-csv`

`cm run script --tags=csv-to-md,convert,to-md,from-csv [--input_flags]`

*or*

`cmr "csv-to-md convert to-md from-csv"`

`cmr "csv-to-md convert to-md from-csv " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'csv-to-md,convert,to-md,from-csv'
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

```cmr "cm gui" --script="csv-to-md,convert,to-md,from-csv"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=csv-to-md,convert,to-md,from-csv) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "csv-to-md convert to-md from-csv" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--csv_file=value`  &rarr;  `CM_CSV_FILE=value`
* `--md_file=value`  &rarr;  `CM_MD_FILE=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "csv_file":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-csv-to-md/_cm.json)***
     * get,python3
       * CM names: `--adr.['python, python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_pandas
       * CM names: `--adr.['pandas']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.tabulate
       * CM names: `--adr.['tabulate']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-csv-to-md/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-csv-to-md/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-csv-to-md/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-csv-to-md/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-csv-to-md/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-csv-to-md/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-csv-to-md/_cm.json)

___
### Script output
`cmr "csv-to-md convert to-md from-csv " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
