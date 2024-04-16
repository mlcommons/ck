**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-using-imagenet-from-model-zoo).**



Automatically generated README for this automation recipe: **get-ml-model-using-imagenet-from-model-zoo**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-using-imagenet-from-model-zoo,153e08828c4e45cc) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ml-model,model-zoo,zoo,imagenet,image-classification*
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

````cmr "get ml-model model-zoo zoo imagenet image-classification" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ml-model,model-zoo,zoo,imagenet,image-classification`

`cm run script --tags=get,ml-model,model-zoo,zoo,imagenet,image-classification[,variations] `

*or*

`cmr "get ml-model model-zoo zoo imagenet image-classification"`

`cmr "get ml-model model-zoo zoo imagenet image-classification [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,model-zoo,zoo,imagenet,image-classification'
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

```cmr "cm gui" --script="get,ml-model,model-zoo,zoo,imagenet,image-classification"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,model-zoo,zoo,imagenet,image-classification) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model model-zoo zoo imagenet image-classification[variations]" `

___
### Customization


#### Variations

  * Group "**model-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_model.#`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,zoo,deepsparse,_model-stub.#
             * CM names: `--adr.['neural-magic-zoo-downloader']...`
             - CM script: [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo)
    * `_model.resnet101-pytorch-base`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,zoo,deepsparse,_model-stub.zoo:cv/classification/resnet_v1-101/pytorch/sparseml/imagenet/base-none
             * CM names: `--adr.['neural-magic-zoo-downloader']...`
             - CM script: [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo)
    * `_model.resnet50-pruned95-uniform-quant`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,zoo,deepsparse,_model-stub.zoo:cv/classification/resnet_v1-50/pytorch/sparseml/imagenet/pruned95_uniform_quant-none
             * CM names: `--adr.['neural-magic-zoo-downloader']...`
             - CM script: [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo)

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo/_cm.json)

___
### Script output
`cmr "get ml-model model-zoo zoo imagenet image-classification [,variations]"  -j`
#### New environment keys (filter)

* `CM_ML_MODEL*`
#### New environment keys auto-detected from customize
