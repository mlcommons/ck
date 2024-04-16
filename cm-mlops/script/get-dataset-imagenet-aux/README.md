**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-aux).**



Automatically generated README for this automation recipe: **get-dataset-imagenet-aux**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-dataset-imagenet-aux,bb2c6dd8c8c64217) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-aux)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,aux,dataset-aux,image-classification,imagenet-aux*
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

````cmr "get aux dataset-aux image-classification imagenet-aux" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,aux,dataset-aux,image-classification,imagenet-aux`

`cm run script --tags=get,aux,dataset-aux,image-classification,imagenet-aux[,variations] `

*or*

`cmr "get aux dataset-aux image-classification imagenet-aux"`

`cmr "get aux dataset-aux image-classification imagenet-aux [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,aux,dataset-aux,image-classification,imagenet-aux'
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

```cmr "cm gui" --script="get,aux,dataset-aux,image-classification,imagenet-aux"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,aux,dataset-aux,image-classification,imagenet-aux) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get aux dataset-aux image-classification imagenet-aux[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_2012`
      - Environment variables:
        - *CM_DATASET_AUX_VER*: `2012`
      - Workflow:

    </details>


  * Group "**download-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_from.berkeleyvision`
      - Environment variables:
        - *CM_WGET_URL*: `http://dl.caffe.berkeleyvision.org/caffe_ilsvrc12.tar.gz`
      - Workflow:
    * **`_from.dropbox`** (default)
      - Environment variables:
        - *CM_WGET_URL*: `https://www.dropbox.com/s/92n2fyej3lzy3s3/caffe_ilsvrc12.tar.gz`
      - Workflow:

    </details>


#### Default variations

`_from.dropbox`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-aux/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-aux/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)

___
### Script output
`cmr "get aux dataset-aux image-classification imagenet-aux [,variations]"  -j`
#### New environment keys (filter)

* `CM_DATASET_AUX_*`
#### New environment keys auto-detected from customize
