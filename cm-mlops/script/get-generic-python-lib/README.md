<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM GUI](#cm-gui)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *Python automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,install,generic,generic-python-lib*
* Output cached?: *True*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=get,install,generic,generic-python-lib[,variations] `

2. `cm run script "get install generic generic-python-lib[,variations]" `

3. `cm run script 94b62a682bc44791 `

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,install,generic,generic-python-lib'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### CM GUI

```cm run script --tags=gui --script="get,install,generic,generic-python-lib"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,install,generic,generic-python-lib) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_Pillow`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `Pillow`
      - Workflow:
    * `_apache-tvm`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `apache-tvm`
        - *CM_GENERIC_PYTHON_PIP_EXTRA*: ` --pre`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_typing_extensions
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_apex`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `apex`
      - Workflow:
    * `_attr`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `attr`
      - Workflow:
    * `_attrs`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `attrs`
      - Workflow:
    * `_boto3`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `boto3`
      - Workflow:
    * `_cloudpickle`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `cloudpickle`
      - Workflow:
    * `_cmind`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `cmind`
      - Workflow:
    * `_colored`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `colored`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://pypi.ngc.nvidia.com`
      - Workflow:
    * `_datasets`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `datasets`
      - Workflow:
    * `_decorator`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `decorator`
      - Workflow:
    * `_deepsparse`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `deepsparse`
      - Workflow:
    * `_dllogger`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `dllogger`
        - *CM_GENERIC_PYTHON_PIP_URL*: `git+https://github.com/NVIDIA/dllogger#egg=dllogger`
      - Workflow:
    * `_fiftyone`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `fiftyone`
      - Workflow:
    * `_google-api-python-client`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `google_api_python_client`
      - Workflow:
    * `_google-auth-oauthlib`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `google_auth_oauthlib`
      - Workflow:
    * `_huggingface_hub`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `huggingface_hub`
      - Workflow:
    * `_inflect`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `inflect`
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
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
    * `_librosa`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `librosa`
      - Workflow:
    * `_matplotlib`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `matplotlib`
      - Workflow:
    * `_mlperf_logging`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `mlperf_logging`
        - *CM_GENERIC_PYTHON_PIP_URL*: `git+https://github.com/mlperf/logging.git@2.1.0`
      - Workflow:
    * `_mpld3`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `mpld3`
      - Workflow:
    * `_nibabel`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `nibabel`
      - Workflow:
    * `_numpy`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `numpy`
      - Workflow:
    * `_nvidia-apex`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `apex`
        - *CM_GENERIC_PYTHON_PACKAGE_VARIANT*: `nvidia-apex`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torch_cuda
             * CM names: `--adr.['torch']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,git,repo,_repo.https://github.com/NVIDIA/apex
             - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
    * `_nvidia-dali`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `nvidia-dali-cuda110`
        - *CM_GENERIC_PYTHON_PIP_EXTRA*: ` --upgrade`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://developer.download.nvidia.com/compute/redist`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
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
        - *CM_ONNXRUNTIME_VERSION_EXTRA*: `GPU`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
    * `_opencv-python`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `opencv-python`
      - Workflow:
    * `_package.#`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `#`
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
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_colored
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_pre`
      - Environment variables:
        - *CM_GENERIC_PYTHON_DEV_VERSION*: `yes`
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
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
    * `_requests`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `requests`
      - Workflow:
    * `_scikit-learn`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `scikit-learn`
      - Workflow:
    * `_scipy`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `scipy`
      - Workflow:
    * `_scons`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `scons`
      - Workflow:
    * `_setfit`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `setfit`
      - Workflow:
    * `_setuptools`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `setuptools`
      - Workflow:
    * `_six`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `six`
      - Workflow:
    * `_sklearn`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `sklearn`
      - Workflow:
    * `_sox`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `sox`
      - Workflow:
    * `_sparsezoo`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `sparsezoo`
      - Workflow:
    * `_streamlit`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `streamlit`
      - Workflow:
    * `_streamlit_option_menu`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `streamlit_option_menu`
      - Workflow:
    * `_tensorboard`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `tensorboard`
      - Workflow:
    * `_tensorflow`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `tensorflow`
      - Workflow:
    * `_tflite`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `tflite`
      - Workflow:
    * `_tflite-runtime`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `tflite-runtime`
      - Workflow:
    * `_tokenization`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `tokenization`
      - Workflow:
    * `_toml`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `toml`
      - Workflow:
    * `_torch`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torch`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/cpu`
      - Workflow:
    * `_torch,pre`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torch`
        - *CM_GENERIC_PYTHON_PIP_EXTRA*: ` --pre`
        - *CM_GENERIC_PYTHON_PIP_INDEX_URL*: `https://download.pytorch.org/whl/nightly/cpu`
      - Workflow:
    * `_torch_cuda`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torch`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/${CM_TORCH_CUDA}`
        - *CM_TORCH_CUDA*: `cu118`
        - *CM_TORCH_VERSION_EXTRA*: `CUDA`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
    * `_torch_cuda,pre`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torch`
        - *CM_GENERIC_PYTHON_PIP_INDEX_URL*: `https://download.pytorch.org/whl/${CM_TORCH_CUDA}`
        - *CM_GENERIC_PYTHON_PIP_EXTRA*: ` --pre`
        - *CM_TORCH_CUDA*: `cu118`
        - *CM_TORCH_VERSION_EXTRA*: `CUDA`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_torchaudio`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchaudio`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/cpu`
      - Workflow:
    * `_torchaudio_cuda`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchaudio`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/${CM_TORCH_CUDA}`
        - *CM_TORCHAUDIO_VERSION_EXTRA*: `CUDA`
        - *CM_TORCH_CUDA*: `cu118`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
    * `_torchvision`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchvision`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/cpu`
      - Workflow:
    * `_torchvision_cuda`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchvision`
        - *CM_TORCHVISION_VERSION_EXTRA*: `CUDA`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
    * `_tornado`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `tornado`
      - Workflow:
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
    * `_unidecode`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `unidecode`
      - Workflow:
    * `_wandb`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `wandb`
      - Workflow:
    * `_west`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `west`
      - Workflow:
    * `_xgboost`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `xgboost`
      - Workflow:
    * `_xlsxwriter`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `xlsxwriter`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib/_cm.json)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib/_cm.json)
</details>

___
### Script output
#### New environment keys (filter)

* `CM_PYTHONLIB_*`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)