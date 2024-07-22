**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ipol-src).**



Automatically generated README for this automation recipe: **get-ipol-src**

Category: **Reproducibility and artifact evaluation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ipol-src,b6fd8213d03d4aa4) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ipol-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ipol,journal,src,ipol-src*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "get ipol journal src ipol-src" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ipol,journal,src,ipol-src`

`cm run script --tags=get,ipol,journal,src,ipol-src [--input_flags]`

*or*

`cmr "get ipol journal src ipol-src"`

`cmr "get ipol journal src ipol-src " [--input_flags]`



#### Input Flags

* --**number**=IPOL publication number
* --**year**=IPOL publication year

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "number":...}
```
#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ipol,journal,src,ipol-src'
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

```cmr "cm gui" --script="get,ipol,journal,src,ipol-src"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ipol,journal,src,ipol-src) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ipol journal src ipol-src" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--number=value`  &rarr;  `CM_IPOL_NUMBER=value`
* `--year=value`  &rarr;  `CM_IPOL_YEAR=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "number":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ipol-src/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ipol-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ipol-src/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ipol-src/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ipol-src/_cm.json)

___
### Script output
`cmr "get ipol journal src ipol-src " [--input_flags] -j`
#### New environment keys (filter)

* `CM_IPOL_*`
#### New environment keys auto-detected from customize

* `CM_IPOL_PATH`