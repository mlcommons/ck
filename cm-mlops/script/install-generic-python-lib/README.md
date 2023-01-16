<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
  * [ Variations](#variations)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys](#new-environment-keys)
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *Python automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *install,generic,generic-python-lib*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=install,generic,generic-python-lib(,variations from below) (flags from below)`

*or*

`cm run script "install generic generic-python-lib (variations from below)" (flags from below)`

*or*

`cm run script f4f502b7b5d545c8`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

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

</details>

#### CM modular Docker container
*TBD*
___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**update**=value --> **CM_GENERIC_PYTHON_PIP_UPDATE**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "update":"..."}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.


</details>


#### Variations

  * *No group (any variation can be selected)*
<details>
<summary>Click here to expand this section.</summary>

    * `_apache-tvm`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `apache-tvm`
      - Workflow:
    * `_attrs`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `attrs`
      - Workflow:
    * `_boto3`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `boto3`
      - Workflow:
    * `_colored`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `colored`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://pypi.ngc.nvidia.com`
      - Workflow:
    * `_decorator`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `decorator`
      - Workflow:
    * `_jax`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `jax`
      - Workflow:
    * `_jax_cuda`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `jax[cuda]`
        - *CM_GENERIC_PYTHON_PIP_EXTRA*: `-f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html`
        - *CM_JAX_VERSION_EXTRA*: `CUDA`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib)
             - CM script: [get-cuda-toolkit](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-toolkit)
    * `_mlperf_logging`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `mlperf_logging`
        - *CM_GENERIC_PYTHON_PIP_URL*: `git+https://github.com/mlperf/logging.git@2.1.0`
      - Workflow:
    * `_numpy`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `numpy`
      - Workflow:
    * `_nvidia-pycocotools`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PIP_URL*: `pycocotools@git+https://github.com/NVIDIA/cocoapi#subdirectory=PythonAPI`
      - Workflow:
    * `_nvidia-pyindex`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `nvidia-pyindex`
      - Workflow:
    * `_nvidia-tensorrt`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `nvidia-tensorrt`
      - Workflow:
    * `_onnx`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `onnx`
      - Workflow:
    * `_onnxruntime`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `onnxruntime`
      - Workflow:
    * `_onnxruntime_gpu`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `onnxruntime_gpu`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib)
             - CM script: [get-cuda-toolkit](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-toolkit)
    * `_opencv-python`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `opencv-python`
      - Workflow:
    * `_pandas`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `pandas`
      - Workflow:
    * `_pillow`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `Pillow`
      - Workflow:
    * `_pip`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `pip`
      - Workflow:
    * `_polygraphy`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `polygraphy`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://pypi.ngc.nvidia.com`
      - Workflow:
    * `_protobuf`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `protobuf`
      - Workflow:
    * `_psutil`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `psutil`
      - Workflow:
    * `_pycocotools`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `pycocotools`
      - Workflow:
    * `_pycuda`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `pycuda`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib)
             - CM script: [get-cuda-toolkit](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-toolkit)
    * `_scipy`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `scipy`
      - Workflow:
    * `_setuptools`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `setuptools`
      - Workflow:
    * `_sklearn`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `sklearn`
      - Workflow:
    * `_tensorflow`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `tensorflow`
      - Workflow:
    * `_tokenization`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `tokenization`
      - Workflow:
    * `_torch`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torch`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/cpu`
      - Workflow:
    * `_torch_cuda`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torch`
        - *CM_TORCH_CUDA*: `cu116`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/${CM_TORCH_CUDA}`
        - *CM_TORCH_VERSION_EXTRA*: `CUDA`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib)
             - CM script: [get-cuda-toolkit](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-toolkit)
    * `_torchaudio`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchaudio`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/cpu`
      - Workflow:
    * `_torchaudio_cuda`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchaudio`
        - *CM_TORCH_CUDA*: `cu116`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/${CM_TORCH_CUDA}`
        - *CM_TORCH_VERSION_EXTRA*: `CUDA`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib)
             - CM script: [get-cuda-toolkit](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-toolkit)
    * `_torchvision`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchvision`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/cpu`
      - Workflow:
    * `_torchvision_cuda`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchvision`
        - *CM_TORCH_CUDA*: `cu116`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/${CM_TORCH_CUDA}`
        - *CM_TORCH_VERSION_EXTRA*: `CUDA`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib)
             - CM script: [get-cuda-toolkit](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-toolkit)
    * `_tqdm`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `tqdm`
      - Workflow:
    * `_transformers`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `transformers`
      - Workflow:
    * `_typing_extensions`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `typing_extensions`
      - Workflow:
    * `_ujson`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `ujson`
      - Workflow:
    * `_wandb`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `wandb`
      - Workflow:

</details>

___
### Script workflow, dependencies and native scripts

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
### Script output
#### New environment keys

#### New environment keys auto-detected from customize

* **CM_GENERIC_PYTHON_PIP_EXTRA**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)