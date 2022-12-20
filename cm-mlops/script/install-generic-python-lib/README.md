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

Python automation.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
install,generic,generic-python-lib

___
### Variations
#### All variations
* apache-tvm
* attrs
* boto3
* colored
* decorator
* jax
* jax_cuda
* mlperf_logging
* numpy
* nvidia-pycocotools
* nvidia-pyindex
* nvidia-tensorrt
* onnx
* onnxruntime
* onnxruntime_gpu
* opencv-python
* pandas
* pillow
* pip
* polygraphy
* protobuf
* psutil
* pycocotools
* pycuda
* scipy
* setuptools
* sklearn
* tensorflow
* tokenization
* torch
* torch_cuda
* torchaudio
* torchaudio_cuda
* torchvision
* torchvision_cuda
* tqdm
* transformers
* typing_extensions
* ujson
* wandb
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
`cm run script --tags="install,generic,generic-python-lib"`

*or*

`cm run script "install generic generic-python-lib"`

*or*

`cm run script f4f502b7b5d545c8`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,generic,generic-python-lib'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)