**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/print-hello-world-javac).**



Automatically generated README for this automation recipe: **print-hello-world-javac**

Category: **Tests**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=print-hello-world-javac,040fafd538104819) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-javac)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *print,hello world,hello-world,hello,world,javac*
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

````cmr "print hello world hello-world hello world javac" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=print,hello world,hello-world,hello,world,javac`

`cm run script --tags=print,hello world,hello-world,hello,world,javac `

*or*

`cmr "print hello world hello-world hello world javac"`

`cmr "print hello world hello-world hello world javac " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'print,hello world,hello-world,hello,world,javac'
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

```cmr "cm gui" --script="print,hello world,hello-world,hello,world,javac"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=print,hello world,hello-world,hello,world,javac) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "print hello world hello-world hello world javac" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-javac/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,javac
       * CM names: `--adr.['javac']...`
       - CM script: [get-javac](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-javac/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-javac/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-javac/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-javac/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-javac/_cm.json)

___
### Script output
`cmr "print hello world hello-world hello world javac "  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
