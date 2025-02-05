# get-generic-python-lib
Automatically generated README for this automation recipe: **get-generic-python-lib**

Category: **[Python automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-generic-python-lib/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-generic-python-lib/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get generic-python-lib" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,generic-python-lib[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get generic-python-lib [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


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


=== "Docker"
    ##### Run this script via Docker (beta)

    ```bash
    cm docker script "get generic-python-lib[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_Pillow`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `Pillow`
        * `_anthropic`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `anthropic`
        * `_apache-tvm`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `apache-tvm`
                   - CM_GENERIC_PYTHON_PIP_EXTRA: ` --pre`
        * `_apex`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `apex`
        * `_async_timeout`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `async_timeout`
        * `_attr`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `attr`
        * `_attrs`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `attrs`
        * `_boto3`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `boto3`
        * `_cloudpickle`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `cloudpickle`
        * `_cmind`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `cmind`
        * `_colored`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `colored`
                   - CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL: `https://pypi.ngc.nvidia.com`
        * `_conda.#`
        * `_cupy`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `cupy`
        * `_custom-python`
               - ENV variables:
                   - CM_TMP_USE_CUSTOM_PYTHON: `on`
        * `_datasets`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `datasets`
        * `_decorator`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `decorator`
        * `_deepsparse`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `deepsparse`
        * `_dllogger`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `dllogger`
                   - CM_GENERIC_PYTHON_PIP_URL: `git+https://github.com/NVIDIA/dllogger#egg=dllogger`
        * `_fiftyone`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `fiftyone`
        * `_google-api-python-client`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `google_api_python_client`
        * `_google-auth-oauthlib`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `google_auth_oauthlib`
        * `_huggingface_hub`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `huggingface_hub`
        * `_inflect`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `inflect`
        * `_jax`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `jax`
        * `_jax_cuda`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `jax[cuda]`
                   - CM_GENERIC_PYTHON_PIP_EXTRA: `-f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html`
                   - CM_JAX_VERSION_EXTRA: `CUDA`
        * `_librosa`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `librosa`
        * `_matplotlib`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `matplotlib`
        * `_mlperf_loadgen`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `mlperf_loadgen`
                   - CM_GENERIC_PYTHON_PIP_URL: `git+https://github.com/mlcommons/inference.git#subdirectory=loadgen`
        * `_mlperf_logging`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `mlperf_logging`
                   - CM_GENERIC_PYTHON_PIP_URL: `git+https://github.com/mlperf/logging.git`
        * `_mpld3`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `mpld3`
        * `_nibabel`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `nibabel`
        * `_numpy`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `numpy`
        * `_nvidia-apex`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `apex`
                   - CM_GENERIC_PYTHON_PACKAGE_VARIANT: `nvidia-apex`
                   - CM_GENERIC_PYTHON_PIP_URL: `git+https://github.com/nvidia/apex@0da3ffb92ee6fbe5336602f0e3989db1cd16f880`
        * `_nvidia-apex-from-src`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `apex`
                   - CM_GENERIC_PYTHON_PACKAGE_VARIANT: `nvidia-apex`
        * `_nvidia-dali`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `nvidia-dali-cuda120`
                   - CM_GENERIC_PYTHON_PIP_EXTRA: ` --upgrade --default-timeout=900`
                   - CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL: `https://developer.download.nvidia.com/compute/redist`
        * `_nvidia-pycocotools`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PIP_UNINSTALL_DEPS: `pycocotools`
                   - CM_GENERIC_PYTHON_PIP_URL: `pycocotools@git+https://github.com/NVIDIA/cocoapi#subdirectory=PythonAPI`
        * `_nvidia-pyindex`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `nvidia-pyindex`
        * `_nvidia-tensorrt`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `nvidia-tensorrt`
        * `_onnx`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `onnx`
        * `_onnx-graphsurgeon`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `onnx_graphsurgeon`
        * `_onnxruntime`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `onnxruntime`
        * `_onnxruntime_gpu`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `onnxruntime_gpu`
                   - CM_ONNXRUNTIME_VERSION_EXTRA: `GPU`
        * `_openai`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `openai`
        * `_opencv-python`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `opencv-python`
        * `_package.#`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `#`
                   - CM_GENERIC_PYTHON_PIP_UNINSTALL_DEPS: ``
                   - CM_GENERIC_PYTHON_PIP_URL: ``
        * `_pandas`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `pandas`
        * `_path.#`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PIP_URL: `#`
        * `_pillow`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `Pillow`
        * `_pip`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `pip`
        * `_polygraphy`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `polygraphy`
                   - CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL: `https://pypi.ngc.nvidia.com`
        * `_pre`
               - ENV variables:
                   - CM_GENERIC_PYTHON_DEV_VERSION: `yes`
        * `_protobuf`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `protobuf`
        * `_psutil`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `psutil`
        * `_pycocotools`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `pycocotools`
        * `_pycuda`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `pycuda`
        * `_ray`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `ray[default]`
        * `_requests`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `requests`
        * `_rocm`
        * `_safetensors`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `safetensors`
        * `_scikit-learn`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `scikit-learn`
        * `_scipy`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `scipy`
        * `_scons`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `scons`
        * `_setfit`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `setfit`
        * `_setuptools`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `setuptools`
        * `_six`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `six`
        * `_sklearn`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `sklearn`
        * `_sox`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `sox`
        * `_sparsezoo`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `sparsezoo`
        * `_streamlit`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `streamlit`
        * `_streamlit_option_menu`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `streamlit_option_menu`
        * `_tensorboard`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `tensorboard`
        * `_tensorflow`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `tensorflow`
        * `_tensorrt`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `tensorrt`
                   - CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL: `https://download.pytorch.org/whl/<<<CM_CUDA_VERSION_STRING>>>`
                   - CM_TORCH_VERSION_EXTRA: `CUDA`
        * `_tflite`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `tflite`
        * `_tflite-runtime`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `tflite-runtime`
        * `_tokenization`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `tokenization`
        * `_toml`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `toml`
        * `_torch`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `torch`
                   - CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL: `https://download.pytorch.org/whl/cpu`
        * `_torch_cuda`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `torch`
                   - CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL1: `https://download.pytorch.org/whl/<<<CM_CUDA_VERSION_STRING>>>`
                   - CM_TORCH_VERSION_EXTRA: `CUDA`
        * `_torch_tensorrt`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `torch-tensorrt`
                   - CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL: `https://download.pytorch.org/whl/<<<CM_CUDA_VERSION_STRING>>>`
                   - CM_TORCH_VERSION_EXTRA: `CUDA`
        * `_torchaudio`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `torchaudio`
                   - CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL: `https://download.pytorch.org/whl/cpu`
        * `_torchaudio_cuda`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `torchaudio`
                   - CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL1: `https://download.pytorch.org/whl/<<<CM_CUDA_VERSION_STRING>>>`
                   - CM_TORCHAUDIO_VERSION_EXTRA: `CUDA`
        * `_torchvision`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `torchvision`
                   - CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL: `https://download.pytorch.org/whl/cpu`
        * `_torchvision_cuda`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `torchvision`
                   - CM_TORCHVISION_VERSION_EXTRA: `CUDA`
        * `_tornado`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `tornado`
        * `_tqdm`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `tqdm`
        * `_transformers`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `transformers`
        * `_typing_extensions`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `typing_extensions`
        * `_ujson`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `ujson`
        * `_unidecode`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `unidecode`
        * `_url.#`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PIP_URL: `#`
                   - CM_TMP_PYTHON_PACKAGE_FORCE_INSTALL: `yes`
        * `_wandb`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `wandb`
        * `_west`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `west`
        * `_xgboost`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `xgboost`
        * `_xlsxwriter`
               - ENV variables:
                   - CM_GENERIC_PYTHON_PACKAGE_NAME: `xlsxwriter`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--extra_index_url=value`  &rarr;  `CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL=value`
    * `--force_install=value`  &rarr;  `CM_TMP_PYTHON_PACKAGE_FORCE_INSTALL=value`
    * `--index_url=value`  &rarr;  `CM_GENERIC_PYTHON_PIP_INDEX_URL=value`




#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-generic-python-lib/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-generic-python-lib/run.bat)
___
#### Script output
```bash
cmr "get generic-python-lib [variations]" [--input_flags] -j
```