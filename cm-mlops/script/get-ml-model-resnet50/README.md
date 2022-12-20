*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Variations](#variations)
* [ All variations](#-all-variations)
* [ Variations by groups](#-variations-by-groups)
* [Script workflow](#script-workflow)
* [Usage](#usage)
* [ CM installation](#-cm-installation)
* [ CM script help](#-cm-script-help)
* [ CM CLI](#-cm-cli)
* [ CM Python API](#-cm-python-api)
* [ CM modular Docker container](#-cm-modular-docker-container)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

ML/AI models.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,raw,ml-model,resnet50,ml-model-resnet50,image-classification

___
### Variations
#### All variations
* **fp32** (default)
* int8
* **onnx** (default)
* onnx,opset-11
* onnx,opset-8
* onnxruntime
* opset-11
* opset-8
* pytorch
* pytorch,fp32
* pytorch,int8
* tensorflow
* tf
* tflite
* uint8

#### Variations by groups

  * framework
    * **onnx** (default)
    * pytorch
    * tensorflow

  * opset-version
    * opset-11
    * opset-8

  * precision
    * **fp32** (default)
    * int8
    * uint8
___
### Script workflow

  #### Meta: "deps" key

  #### customize.py: "preprocess" function

  #### Meta: "prehook_deps" key

  #### Native script (run.sh or run.bat)

  #### Meta: "posthook_deps" key

  #### customize.py: "postprocess" function

  #### Meta: "post_deps" key

___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,raw,ml-model,resnet50,ml-model-resnet50,image-classification"`

*or*

`cm run script "get raw ml-model resnet50 ml-model-resnet50 image-classification"`

*or*

`cm run script 56203e4e998b4bc0`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,raw,ml-model,resnet50,ml-model-resnet50,image-classification'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)