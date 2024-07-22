**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/process-mlperf-accuracy).**



Automatically generated README for this automation recipe: **process-mlperf-accuracy**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=process-mlperf-accuracy,6e809013816b42ea) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-mlperf-accuracy)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *run,mlperf,mlcommons,accuracy,mlc,process,process-accuracy*
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

````cmr "run mlperf mlcommons accuracy mlc process process-accuracy" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=run,mlperf,mlcommons,accuracy,mlc,process,process-accuracy`

`cm run script --tags=run,mlperf,mlcommons,accuracy,mlc,process,process-accuracy[,variations] [--input_flags]`

*or*

`cmr "run mlperf mlcommons accuracy mlc process process-accuracy"`

`cmr "run mlperf mlcommons accuracy mlc process process-accuracy [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mlperf,mlcommons,accuracy,mlc,process,process-accuracy'
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

```cmr "cm gui" --script="run,mlperf,mlcommons,accuracy,mlc,process,process-accuracy"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,mlperf,mlcommons,accuracy,mlc,process,process-accuracy) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run mlperf mlcommons accuracy mlc process process-accuracy[variations]" [--input_flags]`

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
    * `_open-orca`
      - Environment variables:
        - *CM_DATASET*: `openorca`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset,openorca,preprocessed
             * CM names: `--adr.['openorca-dataset']...`
             - CM script: [get-preprocessed-dataset-openorca](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openorca)
           * get,ml-model,llama2
             * CM names: `--adr.['llama2-model']...`
             - CM script: [get-ml-model-llama2](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-llama2)
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

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--result_dir=value`  &rarr;  `CM_MLPERF_ACCURACY_RESULTS_DIR=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "result_dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-mlperf-accuracy/_cm.json)***
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src', 'accuracy-check-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-mlperf-accuracy/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-mlperf-accuracy/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-mlperf-accuracy/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-mlperf-accuracy/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-mlperf-accuracy/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-mlperf-accuracy/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-mlperf-accuracy/_cm.json)

___
### Script output
`cmr "run mlperf mlcommons accuracy mlc process process-accuracy [,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
