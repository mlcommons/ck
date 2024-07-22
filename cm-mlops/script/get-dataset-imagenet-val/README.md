**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-val).**



Automatically generated README for this automation recipe: **get-dataset-imagenet-val**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-dataset-imagenet-val,7afd58d287fe4f11) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-val)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,val,validation,dataset,imagenet,ILSVRC,image-classification,original*
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

````cmr "get val validation dataset imagenet ILSVRC image-classification original" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,val,validation,dataset,imagenet,ILSVRC,image-classification,original`

`cm run script --tags=get,val,validation,dataset,imagenet,ILSVRC,image-classification,original[,variations] [--input_flags]`

*or*

`cmr "get val validation dataset imagenet ILSVRC image-classification original"`

`cmr "get val validation dataset imagenet ILSVRC image-classification original [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

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

`cm docker script "get val validation dataset imagenet ILSVRC image-classification original[variations]" [--input_flags]`

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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-val/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-val/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-val/_cm.json)***
     * download-and-extract,file,_extract
       * `if (CM_DATASET_IMAGENET_VAL_REQUIRE_DAE in ['yes', 'True'])`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
     * file,extract,_no-remove-extracted
       * `if (CM_DAE_ONLY_EXTRACT in ['yes', 'True'])`
       - CM script: [extract-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/extract-file)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-val/run.bat)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-val/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-val/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-val/_cm.json)

___
### Script output
`cmr "get val validation dataset imagenet ILSVRC image-classification original [,variations]" [--input_flags] -j`
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