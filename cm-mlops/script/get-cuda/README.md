# Get CUDA
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/tutorial-scripts.md) detects the installed CUDA on the system and if not found calls the [install script for CUDA](../script/install-cuda-prebuilt).

## Exported Variables
* `CM_CUDA_INSTALLED_PATH`
* `CM_CUDA_VERSION`
* `CM_NVCC_BIN_WITH_PATH`

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. Windows

## Examples

### Detect CUDA on Windows

Example (depends on your own installation of VC and CUDA SDK":

```bash
cm run script "get cl" --path="C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64"
cm run script "get cuda" --path="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\bin"
```
