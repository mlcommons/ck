*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

### About

*TBD*

### Category

Modular MLPerf benchmarks.

### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md).

### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*


### Meta description
[_cm.yaml](_cm.yaml)


### Tags
* All CM script tags: *app,vision,language,mlcommons,mlperf,inference,reference,ref*
* CM CLI: *`cm run script --tags="app,vision,language,mlcommons,mlperf,inference,reference,ref"`*
* CM CLI alternative: *`cm run script "app vision language mlcommons mlperf inference reference ref"`*


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