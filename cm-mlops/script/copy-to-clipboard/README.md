**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/copy-to-clipboard).**



Automatically generated README for this automation recipe: **copy-to-clipboard**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=copy-to-clipboard,8b3aaa97ce58474d) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/copy-to-clipboard)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *copy,to,clipboard,copy-to-clipboard*
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

````cmr "copy to clipboard copy-to-clipboard" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=copy,to,clipboard,copy-to-clipboard`

`cm run script --tags=copy,to,clipboard,copy-to-clipboard [--input_flags]`

*or*

`cmr "copy to clipboard copy-to-clipboard"`

`cmr "copy to clipboard copy-to-clipboard " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'copy,to,clipboard,copy-to-clipboard'
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

```cmr "cm gui" --script="copy,to,clipboard,copy-to-clipboard"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=copy,to,clipboard,copy-to-clipboard) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "copy to clipboard copy-to-clipboard" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--add_quotes=value`  &rarr;  `CM_COPY_TO_CLIPBOARD_TEXT_ADD_QUOTES=value`
* `--q=value`  &rarr;  `CM_COPY_TO_CLIPBOARD_TEXT_ADD_QUOTES=value`
* `--t=value`  &rarr;  `CM_COPY_TO_CLIPBOARD_TEXT=value`
* `--text=value`  &rarr;  `CM_COPY_TO_CLIPBOARD_TEXT=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "add_quotes":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/copy-to-clipboard/_cm.yaml)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_package.pyperclip
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/copy-to-clipboard/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/copy-to-clipboard/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/copy-to-clipboard/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/copy-to-clipboard/_cm.yaml)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/copy-to-clipboard/_cm.yaml)

___
### Script output
`cmr "copy to clipboard copy-to-clipboard " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
