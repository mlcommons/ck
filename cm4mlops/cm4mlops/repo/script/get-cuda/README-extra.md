# Get CUDA

This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) detects the installed CUDA on the system 
and if not found calls the [install script for CUDA](../script/install-cuda-prebuilt).

## Exported Variables
* `CM_CUDA_INSTALLED_PATH`
* `CM_CUDA_VERSION`
* `CM_NVCC_BIN_WITH_PATH`
* `CUDA_HOME`
* `CUDA_PATH`

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. Windows

# Examples

## Detect CUDA on Windows

You may want to install all system dependencies as described [here](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html).

If Visual Studio and CUDA updated your PATH variable, you should just run the following:
```bash
cm run script "get cuda"
```

However, if the PATH variable was not updated, you need to provide path to the cl.exe and nvcc.exe to help CM detect them:

```bash
cm run script "get cl" --path="C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64"
cm run script "get cuda _compiler" --path="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\bin"
```

# System dependencies

* Download [CUDA toolkit](https://developer.nvidia.com/cuda-toolkit).
* Download [cuDNN](https://developer.nvidia.com/rdp/cudnn-download).
* (Download [TensorRT](https://developer.nvidia.com/nvidia-tensorrt-8x-download)).

## Windows

* ? Download [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)
* Check [Nvidia installation guide](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)
