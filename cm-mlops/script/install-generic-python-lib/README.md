*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Variations](#variations)
  * [ All variations](#all-variations)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
  * [ Script input flags mapped to environment](#script-input-flags-mapped-to-environment)
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
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `apache-tvm`
* attrs
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `attrs`
* boto3
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `boto3`
* colored
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `colored`
  - *ENV CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://pypi.ngc.nvidia.com`
* decorator
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `decorator`
* jax
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `jax`
* jax_cuda
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `jax[cuda]`
  - *ENV CM_GENERIC_PYTHON_PIP_EXTRA*: `-f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html`
  - *ENV CM_JAX_VERSION_EXTRA*: `CUDA`
* mlperf_logging
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `mlperf_logging`
  - *ENV CM_GENERIC_PYTHON_PIP_URL*: `git+https://github.com/mlperf/logging.git@2.1.0`
* numpy
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `numpy`
* nvidia-pycocotools
  - *ENV CM_GENERIC_PYTHON_PIP_URL*: `pycocotools@git+https://github.com/NVIDIA/cocoapi#subdirectory=PythonAPI`
* nvidia-pyindex
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `nvidia-pyindex`
* nvidia-tensorrt
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `nvidia-tensorrt`
* onnx
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `onnx`
* onnxruntime
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `onnxruntime`
* onnxruntime_gpu
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `onnxruntime_gpu`
* opencv-python
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `opencv-python`
* pandas
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `pandas`
* pillow
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `Pillow`
* pip
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `pip`
* polygraphy
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `polygraphy`
  - *ENV CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://pypi.ngc.nvidia.com`
* protobuf
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `protobuf`
* psutil
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `psutil`
* pycocotools
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `pycocotools`
* pycuda
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `pycuda`
* scipy
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `scipy`
* setuptools
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `setuptools`
* sklearn
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `sklearn`
* tensorflow
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `tensorflow`
* tokenization
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `tokenization`
* torch
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `torch`
  - *ENV CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/cpu`
* torch_cuda
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `torch`
  - *ENV CM_TORCH_CUDA*: `cu116`
  - *ENV CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/${CM_TORCH_CUDA}`
  - *ENV CM_TORCH_VERSION_EXTRA*: `CUDA`
* torchaudio
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchaudio`
  - *ENV CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/cpu`
* torchaudio_cuda
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchaudio`
  - *ENV CM_TORCH_CUDA*: `cu116`
  - *ENV CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/${CM_TORCH_CUDA}`
  - *ENV CM_TORCH_VERSION_EXTRA*: `CUDA`
* torchvision
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchvision`
  - *ENV CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/cpu`
* torchvision_cuda
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchvision`
  - *ENV CM_TORCH_CUDA*: `cu116`
  - *ENV CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/${CM_TORCH_CUDA}`
  - *ENV CM_TORCH_VERSION_EXTRA*: `CUDA`
* tqdm
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `tqdm`
* transformers
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `transformers`
* typing_extensions
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `typing_extensions`
* ujson
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `ujson`
* wandb
  - *ENV CM_GENERIC_PYTHON_PACKAGE_NAME*: `wandb`
___
### Default environment

___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib/_cm.json)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib/_cm.json)
  1. Run "postrocess" function from customize.py
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib/_cm.json)***
     * get,generic-python-lib
       * `if (CM_REQUIRE_INSTALL  != yes)`
       * CM names: `--adr.['get-python-lib']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
___
### New environment export

___
### New environment detected from customize

* **CM_GENERIC_PYTHON_PIP_EXTRA**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
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
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* update --> **CM_GENERIC_PYTHON_PIP_UPDATE**

Examples:

```bash
cm run script "install generic generic-python-lib" --update=...
```
```python
r=cm.access({... , "update":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)