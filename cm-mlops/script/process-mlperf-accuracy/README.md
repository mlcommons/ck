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
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

#### Summary

* Category: *MLPerf benchmark support.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *run,mlperf,mlcommons,accuracy,mlc,process-accuracy*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=run,mlperf,mlcommons,accuracy,mlc,process-accuracy[,variations] `

2. `cmr "run mlperf mlcommons accuracy mlc process-accuracy[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mlperf,mlcommons,accuracy,mlc,process-accuracy'
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

```cmr "cm gui" --script="run,mlperf,mlcommons,accuracy,mlc,process-accuracy"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,mlperf,mlcommons,accuracy,mlc,process-accuracy) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run mlperf mlcommons accuracy mlc process-accuracy[ variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_default-pycocotools,openimages`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_pycocotools
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,mlcommons,mlperf,inference,src,-_openimages-nvidia-pycocotools
             * CM names: `--adr.['for-pycocotools', 'accuracy-check-src']...`
             - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
    * `_nvidia-pycocotools,openimages`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_nvidia-pycocotools
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,mlcommons,mlperf,inference,src,_openimages-nvidia-pycocotools
             * CM names: `--adr.['for-pycocotools', 'accuracy-check-src']...`
             - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)

    </details>


  * Group "**coco-evaluation-tool**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_default-pycocotools`** (default)
      - Workflow:
    * `_nvidia-pycocotools`
      - Workflow:

    </details>


  * Group "**dataset**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_cnndm`
      - Environment variables:
        - *CM_DATASET*: `cnndm`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset,cnndm,_validation
             - CM script: [get-dataset-cnndm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-cnndm)
           * get,generic-python-lib,_package.rouge_score
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.nltk
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.evaluate
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.absl-py
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.rouge_score
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_coco2014`
      - Environment variables:
        - *CM_DATASET*: `coco2014`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset,coco2014,original
             * CM names: `--adr.['coco2014-dataset', 'coco2014-original']...`
             - CM script: [get-dataset-coco2014](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco2014)
    * **`_imagenet`** (default)
      - Environment variables:
        - *CM_DATASET*: `imagenet`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset-aux,image-classification,imagenet-aux
             - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_kits19`
      - Environment variables:
        - *CM_DATASET*: `kits19`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset,preprocessed,medical-imaging,kits19
             - CM script: [get-preprocessed-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-kits19)
    * `_librispeech`
      - Environment variables:
        - *CM_DATASET*: `librispeech`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset,preprocessed,speech-recognition,librispeech
             - CM script: [get-preprocessed-dataset-librispeech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-librispeech)
    * `_openimages`
      - Environment variables:
        - *CM_DATASET*: `openimages`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset-aux,openimages,annotations
             * `if (CM_MLPERF_RUN_STYLE  == valid)`
             - CM script: [get-dataset-openimages-annotations](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-annotations)
           * get,dataset,openimages,original
             * `if (CM_MLPERF_RUN_STYLE  != valid)`
             * CM names: `--adr.['openimages-original']...`
             - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
           * get,generic-python-lib,_package.kiwisolver
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_squad`
      - Environment variables:
        - *CM_DATASET*: `squad`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_boto3
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.transformers
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,dataset,squad,language-processing
             * `if (CM_DATASET_SQUAD_VAL_PATH not in [])`
             - CM script: [get-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)
           * get,dataset-aux,squad-vocab
             * `if (CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH  != on)`
             - CM script: [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)
           * get,generic-python-lib,_torch
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_tokenization
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_terabyte`
      - Environment variables:
        - *CM_DATASET*: `squad`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_ujson
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_scikit-learn
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_float16`
      - Environment variables:
        - *CM_ACCURACY_DTYPE*: `float16`
      - Workflow:
    * **`_float32`** (default)
      - Environment variables:
        - *CM_ACCURACY_DTYPE*: `float32`
      - Workflow:
    * `_float64`
      - Environment variables:
        - *CM_ACCURACY_DTYPE*: `float64`
      - Workflow:
    * `_int16`
      - Environment variables:
        - *CM_ACCURACY_DTYPE*: `int16`
      - Workflow:
    * `_int32`
      - Environment variables:
        - *CM_ACCURACY_DTYPE*: `int32`
      - Workflow:
    * `_int64`
      - Environment variables:
        - *CM_ACCURACY_DTYPE*: `int64`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_ACCURACY_DTYPE*: `int8`
      - Workflow:

    </details>


#### Default variations

`_default-pycocotools,_float32,_imagenet`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy/_cm.json)***
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src', 'accuracy-check-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy/_cm.json)
</details>

___
### Script output
`cmr "run mlperf mlcommons accuracy mlc process-accuracy[,variations]"  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)