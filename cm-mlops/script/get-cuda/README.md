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

```bash
cm run script "get cuda" --path="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\bin"
```
