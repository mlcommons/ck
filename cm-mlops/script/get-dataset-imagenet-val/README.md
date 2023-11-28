<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *AI/ML datasets.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,val,validation,dataset,imagenet,ILSVRC,image-classification,original*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,val,validation,dataset,imagenet,ILSVRC,image-classification,original[,variations] [--input_flags]`

2. `cmr "get val validation dataset imagenet ILSVRC image-classification original[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,val,validation,dataset,imagenet,ILSVRC,image-classification,original'
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

```cmr "cm gui" --script="get,val,validation,dataset,imagenet,ILSVRC,image-classification,original"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,val,validation,dataset,imagenet,ILSVRC,image-classification,original) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get val validation dataset imagenet ILSVRC image-classification original[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_2012-500`
      - Workflow:
    * `_2012-full`
      - Workflow:

    </details>


  * Group "**count**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_full`
      - Environment variables:
        - *CM_DATASET_SIZE*: `50000`
        - *CM_IMAGENET_FULL*: `yes`
        - *CM_DAE_FILENAME*: `ILSVRC2012_img_val.tar`
        - *CM_DAE_DOWNLOADED_CHECKSUM*: `29b22e2961454d5413ddabcf34fc5622`
      - Workflow:
    * `_size.#`
      - Environment variables:
        - *CM_DATASET_SIZE*: `#`
      - Workflow:
    * **`_size.500`** (default)
      - Environment variables:
        - *CM_DATASET_SIZE*: `500`
        - *CM_DAE_FILENAME*: `ILSVRC2012_img_val_500.tar`
        - *CM_DAE_URL*: `http://cKnowledge.org/ai/data/ILSVRC2012_img_val_500.tar`
      - Workflow:

    </details>


  * Group "**dataset-version**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_2012`** (default)
      - Environment variables:
        - *CM_DATASET_VER*: `2012`
      - Workflow:

    </details>


#### Default variations

`_2012,_size.500`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--imagenet_path=value`  &rarr;  `IMAGENET_PATH=value`
* `--torrent=value`  &rarr;  `CM_DATASET_IMAGENET_VAL_TORRENT_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "imagenet_path":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)***
     * download-and-extract,file,_extract
       * `if (CM_DATASET_IMAGENET_VAL_REQUIRE_DAE in ['yes', 'True'])`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
     * file,extract
       * `if (CM_DAE_ONLY_EXTRACT in ['yes', 'True'])`
       - CM script: [extract-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/extract-file)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/run.bat)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)
</details>

___
### Script output
`cmr "get val validation dataset imagenet ILSVRC image-classification original[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_DATASET_IMAGENET_PATH`
* `CM_DATASET_IMAGENET_VAL_PATH`
* `CM_DATASET_PATH`
* `CM_DATASET_SIZE`
* `CM_DATASET_VER`
#### New environment keys auto-detected from customize

* `CM_DATASET_IMAGENET_PATH`
* `CM_DATASET_IMAGENET_VAL_PATH`
* `CM_DATASET_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)