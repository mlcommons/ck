[ [Back to index](README.md) ]


# CUDA installation using CM

Here we describe how to install CUDA drivers and typical dependencies (cuDNN, TensorRT)
in a native environment via [CM automation language](https://doi.org/10.5281/zenodo.8105339) 
to reproduce CUDA-based research projects and MLPerf benchmarks.

We expect you to have CM already installed as described [here](installation.md).

You should also install or update 
the MLCommons repository with [reusable automation recipes (CM scripts)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
that are being developed and shared by the community under Apache 2.0 license 
to enable portable, modular, and technology-agnostic benchmarks and applications 
that can automatically run with any software, hardware, models and data sets:

```bash
cm pull repo mlcommons@cm4mlops --checkout=dev
```


## Ubuntu, Debian, Red Hat

### Install CUDA drivers

If you use a "clean" system without CUDA drivers (particularly when you install a new AWS, GCP or Azure instance with minimal OS)
you can install CUDA drivers via CM as follows:

```bash
cmr "install cuda prebuilt _driver"
```

By default, it will download and install CUDA driver `11.8.0`. You can change this version 
to the [supported one](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/install-cuda-prebuilt/_cm.json#L56)
as follows:
```bash
cmr "install cuda prebuilt _driver" --version={any CUDA version}
```

You may need to restart your system to load drivers. You can then test them via CM as follows:
```bash
cmr "get cuda-devices"
```

### Detect CUDA drivers

If your system already has CUDA installed, you can detect and plug it into CM as follows:
```bash
cmr "get cuda"
```

### Detect/install cuDNN

If cuDNN is already installed on your system, you can detect and plug it into CM as follows:
    
```bash
cmr "get cudnn"
```

Otherwise, download cuDNN tar file from [Nvidia website](https://developer.nvidia.com/cudnn)
and install it via CM as follows:

```bash
cmr "get cudnn" --tar_file=<PATH_TO_CUDNN_TAR_FILE>
```


### Detect/install TensorRT

If TensorRT is already installed on your system, you can detect and plug it into CM as follows:
    
```bash
cmr "get tensorrt"
```

However, we suggest you to install a development version (with Python integration, etc) as follows:

1. Download TensorRT tar file from [Nvidia website](https://developer.nvidia.com/tensorrt).

2. Install using CM as follows:

```bash
cmr "get tensorrt _dev" --tar_file=<PATH_TO_TENSORRT_TAR_FILE>
```

### Show/clean CM cache with all installations

You can list and find all cached installation in CM as follows:
```bash
cm show cache
```

Note, that you can clean CM cache and start from scratch as follows:
```bash
cm rm cache -f
```

Even more radical, you can delete the whole `$HOME/CM` directory
and start from scratch as follows:
```bash
(sudo) rm -rf $HOME/CM
cm pull repo mlcommons@cm4mlops --checkout=dev
```


## Windows

### Drivers

The community did not yet share the script to automatically download and install CUDA drivers on Windows.
However, you can do it manually and then use CM to detect it and plug into other CM automations:

First, download [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist).

Then, install all system dependencies as described [here](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html).

If Visual Studio and CUDA updated your PATH variable, you should just run the following:
```bash
cmr "get cuda"
```

However, if the PATH variable was not updated, you need to provide path to the cl.exe and nvcc.exe to help CM detect them:

```bash
cmr "get cl" --path="C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64"
cmr "get cuda _compiler" --path="C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\bin"
```
