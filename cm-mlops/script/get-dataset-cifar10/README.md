**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-cifar10).**



Automatically generated README for this automation recipe: **get-dataset-cifar10**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-dataset-cifar10,2f0c0bb3663b4ed7) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cifar10)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,dataset,cifar10,image-classification,validation,training*
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

````cmr "get dataset cifar10 image-classification validation training" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,dataset,cifar10,image-classification,validation,training`

`cm run script --tags=get,dataset,cifar10,image-classification,validation,training[,variations] `

*or*

`cmr "get dataset cifar10 image-classification validation training"`

`cmr "get dataset cifar10 image-classification validation training [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,cifar10,image-classification,validation,training'
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

```cmr "cm gui" --script="get,dataset,cifar10,image-classification,validation,training"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,cifar10,image-classification,validation,training) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset cifar10 image-classification validation training[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_tiny`
      - Environment variables:
        - *CM_DATASET_CONVERT_TO_TINYMLPERF*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,python3
             * CM names: `--adr.['python', 'python3']...`
             - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
           * get,tinymlperf,src
             - CM script: [get-mlperf-tiny-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-src)
           * get,src,eembc,energy-runner
             - CM script: [get-mlperf-tiny-eembc-energy-runner-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src)

    </details>


  * Group "**data_format**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_python`** (default)
      - Environment variables:
        - *CM_DATASET*: `CIFAR10`
        - *CM_DATASET_FILENAME*: `cifar-10-python.tar.gz`
        - *CM_DATASET_FILENAME1*: `cifar-10-python.tar`
        - *CM_DATASET_CIFAR10*: `https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz`
      - Workflow:

    </details>


#### Default variations

`_python`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cifar10/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cifar10/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cifar10/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cifar10/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cifar10/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cifar10/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cifar10/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cifar10/_cm.json)

___
### Script output
`cmr "get dataset cifar10 image-classification validation training [,variations]"  -j`
#### New environment keys (filter)

* `CM_DATASET_*`
#### New environment keys auto-detected from customize
