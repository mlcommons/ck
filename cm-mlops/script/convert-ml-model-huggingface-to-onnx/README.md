**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/convert-ml-model-huggingface-to-onnx).**



Automatically generated README for this automation recipe: **convert-ml-model-huggingface-to-onnx**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=convert-ml-model-huggingface-to-onnx,eacb01655d7e49ac) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-ml-model-huggingface-to-onnx)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *ml-model,model,huggingface-to-onnx,onnx,huggingface,convert*
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

````cmr "ml-model model huggingface-to-onnx onnx huggingface convert" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=ml-model,model,huggingface-to-onnx,onnx,huggingface,convert`

`cm run script --tags=ml-model,model,huggingface-to-onnx,onnx,huggingface,convert[,variations] `

*or*

`cmr "ml-model model huggingface-to-onnx onnx huggingface convert"`

`cmr "ml-model model huggingface-to-onnx onnx huggingface convert [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'ml-model,model,huggingface-to-onnx,onnx,huggingface,convert'
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

```cmr "cm gui" --script="ml-model,model,huggingface-to-onnx,onnx,huggingface,convert"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=ml-model,model,huggingface-to-onnx,onnx,huggingface,convert) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "ml-model model huggingface-to-onnx onnx huggingface convert[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_model-path.#`
      - Environment variables:
        - *CM_MODEL_HUGG_PATH*: `#`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-ml-model-huggingface-to-onnx/_cm.json)***
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_transformers
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnxruntime
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-ml-model-huggingface-to-onnx/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-ml-model-huggingface-to-onnx/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-ml-model-huggingface-to-onnx/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-ml-model-huggingface-to-onnx/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-ml-model-huggingface-to-onnx/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-ml-model-huggingface-to-onnx/_cm.json)

___
### Script output
`cmr "ml-model model huggingface-to-onnx onnx huggingface convert [,variations]"  -j`
#### New environment keys (filter)

* `CM_ML_MODEL*`
* `CM_MODEL_HUGG_PATH`
* `HUGGINGFACE_ONNX_FILE_PATH`
#### New environment keys auto-detected from customize
