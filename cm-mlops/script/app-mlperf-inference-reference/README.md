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

Modular MLPerf benchmarks.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.yaml](_cm.yaml)

___
### Tags
app,vision,language,mlcommons,mlperf,inference,reference,ref

___
### Variations
#### All variations
* bert
* bert-99
* bert-99.9
* **cpu** (default)
* cuda
* fast
* **onnxruntime** (default)
* **python** (default)
* pytorch
* quantized
* r2.1_default
* **resnet50** (default)
* retinanet
* tensorflow
* **test** (default)
* tf
* tvm-onnx
* tvm-pytorch
* valid

#### Variations by groups

  * device,
    * **cpu** (default)
    * cuda

  * execution-mode,
    * fast
    * **test** (default)
    * valid

  * framework,
    * **onnxruntime** (default)
    * pytorch
    * tf
    * tvm-onnx
    * tvm-pytorch

  * implementation,
    * **python** (default)

  * models,
    * bert-99
    * bert-99.9
    * **resnet50** (default)
    * retinanet
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
`cm run script --tags="app,vision,language,mlcommons,mlperf,inference,reference,ref"`

*or*

`cm run script "app vision language mlcommons mlperf inference reference ref"`

*or*

`cm run script ff149e9781fc4b65`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,vision,language,mlcommons,mlperf,inference,reference,ref'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)