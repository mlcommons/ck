**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-generic-python-lib).**



Automatically generated README for this automation recipe: **get-generic-python-lib**

Category: **Python automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-generic-python-lib,94b62a682bc44791) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-python-lib)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,generic-python-lib*
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

````cmr "get generic-python-lib" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,generic-python-lib`

`cm run script --tags=get,generic-python-lib[,variations] [--input_flags]`

*or*

`cmr "get generic-python-lib"`

`cmr "get generic-python-lib [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,generic-python-lib'
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

```cmr "cm gui" --script="get,generic-python-lib"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,generic-python-lib) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get generic-python-lib[variations]" [--input_flags]`

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
    * `_async_timeout`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `async_timeout`
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
    * `_conda.#`
      - Workflow:
    * `_cupy`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `cupy`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
    * `_custom-python`
      - Environment variables:
        - *CM_TMP_USE_CUSTOM_PYTHON*: `on`
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
    * `_mlperf_loadgen`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `mlperf_loadgen`
        - *CM_GENERIC_PYTHON_PIP_URL*: `git+https://github.com/mlcommons/inference.git#subdirectory=loadgen`
      - Workflow:
    * `_mlperf_logging`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `mlperf_logging`
        - *CM_GENERIC_PYTHON_PIP_URL*: `git+https://github.com/mlperf/logging.git`
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
        - *CM_GENERIC_PYTHON_PIP_URL*: `git+https://github.com/nvidia/apex@0da3ffb92ee6fbe5336602f0e3989db1cd16f880`
      - Workflow:
    * `_nvidia-apex-from-src`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `apex`
        - *CM_GENERIC_PYTHON_PACKAGE_VARIANT*: `nvidia-apex`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
           * get,generic-python-lib,_torch_cuda
             * CM names: `--adr.['torch']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,git,repo,_repo.https://github.com/NVIDIA/apex,_tag.23.05
             - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
    * `_nvidia-dali`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `nvidia-dali-cuda120`
        - *CM_GENERIC_PYTHON_PIP_EXTRA*: ` --upgrade --default-timeout=900`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://developer.download.nvidia.com/compute/redist`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
    * `_nvidia-pycocotools`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PIP_UNINSTALL_DEPS*: `pycocotools`
        - *CM_GENERIC_PYTHON_PIP_URL*: `pycocotools@git+https://github.com/NVIDIA/cocoapi#subdirectory=PythonAPI`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_package.cython
             * CM names: `--adr.['cython']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.numpy
             * CM names: `--adr.['numpy']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
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
    * `_onnx-graphsurgeon`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `onnx_graphsurgeon`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_package.nvidia-pyindex
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_onnxruntime`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `onnxruntime`
      - Workflow:
    * `_onnxruntime,rocm`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `onnxruntime-training`
        - *CM_GENERIC_PYTHON_PIP_URL*: `https://download.onnxruntime.ai/onnxruntime_training-1.16.0%2Brocm56-cp3<<<CM_PYTHON_MINOR_VERSION>>>-cp3<<<CM_PYTHON_MINOR_VERSION>>>-manylinux_2_17_x86_64.manylinux2014_x86_64.whl`
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
        - *CM_GENERIC_PYTHON_PIP_UNINSTALL_DEPS*: ``
        - *CM_GENERIC_PYTHON_PIP_URL*: ``
      - Workflow:
    * `_pandas`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `pandas`
      - Workflow:
    * `_path.#`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PIP_URL*: `#`
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
    * `_ray`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `ray[default]`
      - Workflow:
    * `_requests`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `requests`
      - Workflow:
    * `_rocm`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,rocm
             * CM names: `--adr.['rocm']...`
             - CM script: [get-rocm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-rocm)
    * `_safetensors`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `safetensors`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,rust-compiler
             * `if (CM_HOST_PLATFORM_FLAVOR  != x86_64)`
             - CM script: [get-compiler-rust](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-compiler-rust)
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
    * `_tensorflow,rocm`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `tensorflow-rocm`
      - Workflow:
    * `_tensorrt`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `tensorrt`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/<<<CM_CUDA_VERSION_STRING>>>`
        - *CM_TORCH_VERSION_EXTRA*: `CUDA`
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
    * `_torch,rocm`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torch`
        - *CM_GENERIC_PYTHON_PIP_INDEX_URL*: `https://download.pytorch.org/whl/rocm5.6`
        - *CM_GENERIC_PYTHON_PIP_UNINSTALL_DEPS*: `torch`
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * get,generic-python-lib,_torchvision,_rocm
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torchaudio,_rocm
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_torch_cuda`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torch`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL1*: `https://download.pytorch.org/whl/<<<CM_CUDA_VERSION_STRING>>>`
        - *CM_TORCH_VERSION_EXTRA*: `CUDA`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
    * `_torch_cuda,pre`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torch`
        - *CM_GENERIC_PYTHON_PIP_EXTRA*: ` --pre`
        - *CM_GENERIC_PYTHON_PIP_INDEX_URL*: `https://download.pytorch.org/whl/<<<CM_CUDA_VERSION_STRING>>>`
        - *CM_TORCH_VERSION_EXTRA*: `CUDA`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_torch_tensorrt`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torch-tensorrt`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/<<<CM_CUDA_VERSION_STRING>>>`
        - *CM_TORCH_VERSION_EXTRA*: `CUDA`
      - Workflow:
    * `_torchaudio`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchaudio`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL*: `https://download.pytorch.org/whl/cpu`
      - Workflow:
    * `_torchaudio,rocm`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchaudio`
        - *CM_GENERIC_PYTHON_PIP_INDEX_URL*: `https://download.pytorch.org/whl/rocm5.6`
        - *CM_GENERIC_PYTHON_PIP_UNINSTALL_DEPS*: `torchaudio`
      - Workflow:
    * `_torchaudio_cuda`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchaudio`
        - *CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL1*: `https://download.pytorch.org/whl/<<<CM_CUDA_VERSION_STRING>>>`
        - *CM_TORCHAUDIO_VERSION_EXTRA*: `CUDA`
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
    * `_torchvision,rocm`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PACKAGE_NAME*: `torchvision`
        - *CM_GENERIC_PYTHON_PIP_INDEX_URL*: `https://download.pytorch.org/whl/rocm5.6`
        - *CM_GENERIC_PYTHON_PIP_UNINSTALL_DEPS*: `torchvision`
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
    * `_url.#`
      - Environment variables:
        - *CM_GENERIC_PYTHON_PIP_URL*: `#`
        - *CM_TMP_PYTHON_PACKAGE_FORCE_INSTALL*: `yes`
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


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--extra_index_url=value`  &rarr;  `CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL=value`
* `--force_install=value`  &rarr;  `CM_TMP_PYTHON_PACKAGE_FORCE_INSTALL=value`
* `--index_url=value`  &rarr;  `CM_GENERIC_PYTHON_PIP_INDEX_URL=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "extra_index_url":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-python-lib/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python3
       * `if (CM_TMP_USE_CUSTOM_PYTHON  != on)`
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_pip
       * `if (CM_GENERIC_PYTHON_PACKAGE_NAME  != pip)`
       * CM names: `--adr.['python-pip', 'pip']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-python-lib/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-python-lib/_cm.json)***
     * install,onnxruntime,from.src,_cuda
       * `if (CM_INSTALL_ONNXRUNTIME_GPU_FROM_SRC  == yes)`
       - CM script: [install-onnxruntime-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-onnxruntime-from-src)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-python-lib/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-python-lib/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-python-lib/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-python-lib/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-python-lib/_cm.json)

___
### Script output
`cmr "get generic-python-lib [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_PYTHONLIB_*`
#### New environment keys auto-detected from customize
