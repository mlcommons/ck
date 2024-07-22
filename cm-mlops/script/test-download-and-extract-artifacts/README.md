**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/test-download-and-extract-artifacts).**



Automatically generated README for this automation recipe: **test-download-and-extract-artifacts**

Category: **Tests**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=test-download-and-extract-artifacts,51dde7580b404b27) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-download-and-extract-artifacts)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *test,download-and-extract-artifacts*
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

````cmr "test download-and-extract-artifacts" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=test,download-and-extract-artifacts`

`cm run script --tags=test,download-and-extract-artifacts `

*or*

`cmr "test download-and-extract-artifacts"`

`cmr "test download-and-extract-artifacts " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'test,download-and-extract-artifacts'
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

```cmr "cm gui" --script="test,download-and-extract-artifacts"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=test,download-and-extract-artifacts) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "test download-and-extract-artifacts" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-download-and-extract-artifacts/_cm.yaml)***
     * download,file,_url.https://zenodo.org/record/4735647/files/resnet50_v1.onnx
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
     * download-and-extract,_extract,_url.https://zenodo.org/record/5597155/files/3dunet_kits19_128x128x128.tf.zip?download=1
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-download-and-extract-artifacts/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-download-and-extract-artifacts/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-download-and-extract-artifacts/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-download-and-extract-artifacts/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-download-and-extract-artifacts/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-download-and-extract-artifacts/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-download-and-extract-artifacts/_cm.yaml)

___
### Script output
`cmr "test download-and-extract-artifacts "  -j`
#### New environment keys (filter)

* `CM_REPRODUCE_PAPER_XYZ*`
#### New environment keys auto-detected from customize
