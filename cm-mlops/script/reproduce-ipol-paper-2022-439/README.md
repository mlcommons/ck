**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-ipol-paper-2022-439).**



Automatically generated README for this automation recipe: **reproduce-ipol-paper-2022-439**

Category: **Reproducibility and artifact evaluation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=reproduce-ipol-paper-2022-439,f9b9e5bd65e34e4f) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-ipol-paper-2022-439)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *app,python,reproduce,project,paper,ipol,journal,repro,reproducibility,pytorch,2022-439*
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

````cmr "app python reproduce project paper ipol journal repro reproducibility pytorch 2022-439" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=app,python,reproduce,project,paper,ipol,journal,repro,reproducibility,pytorch,2022-439`

`cm run script --tags=app,python,reproduce,project,paper,ipol,journal,repro,reproducibility,pytorch,2022-439 [--input_flags]`

*or*

`cmr "app python reproduce project paper ipol journal repro reproducibility pytorch 2022-439"`

`cmr "app python reproduce project paper ipol journal repro reproducibility pytorch 2022-439 " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,python,reproduce,project,paper,ipol,journal,repro,reproducibility,pytorch,2022-439'
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

```cmr "cm gui" --script="app,python,reproduce,project,paper,ipol,journal,repro,reproducibility,pytorch,2022-439"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=app,python,reproduce,project,paper,ipol,journal,repro,reproducibility,pytorch,2022-439) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "app python reproduce project paper ipol journal repro reproducibility pytorch 2022-439" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--image1=value`  &rarr;  `CM_IMAGE_1=value`
* `--image2=value`  &rarr;  `CM_IMAGE_2=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "image1":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-ipol-paper-2022-439/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,ipol,src
       * CM names: `--adr.['ipol-src']...`
       - CM script: [get-ipol-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ipol-src)
     * get,generic-python-lib,_torch
       * CM names: `--adr.['torch']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torchvision
       * CM names: `--adr.['torchvision']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-ipol-paper-2022-439/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-ipol-paper-2022-439/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-ipol-paper-2022-439/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-ipol-paper-2022-439/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-ipol-paper-2022-439/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-ipol-paper-2022-439/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-ipol-paper-2022-439/_cm.yaml)

___
### Script output
`cmr "app python reproduce project paper ipol journal repro reproducibility pytorch 2022-439 " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
