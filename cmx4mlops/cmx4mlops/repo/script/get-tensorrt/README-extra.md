# Get TensorRT

This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) installs TensorRT when the corrsponding [tar file](https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html#installing-tar) is provided as an input.

## How to Use
```
cm run script --tags=get,tensorrt --tar_file=<PATH_TO_DOWNLOADED_FILE>
```

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
