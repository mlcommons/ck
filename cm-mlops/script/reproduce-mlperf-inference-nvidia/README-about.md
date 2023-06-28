This script is a CM wrapper to the official [Nvidia submission code](https://github.com/mlcommons/inference_results_v3.0/tree/master/closed/NVIDIA) used for MLPerf inference submissions. 

This script will automatically call the Nvidia script to [add a custom system](https://github.com/mlcommons/inference_results_v3.0/tree/master/closed/NVIDIA#adding-a-new-or-custom-system).

Nvidia working directory is given by `CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH` variable which can be seen by running 
```bash
cm run script --tags=get,nvidia,common-code,_nvidia-only --out=json
```


## Requirements
You need to have CUDA, cuDNN and TensorRT installed on your system. 
### Install CUDA
If CUDA is not detected, CM should download and install it automatically when you run the workflow. If you already have cuda drivers **ensure that you uncheck cuda drivers** while installing cuda.

### Install cuDNN
For x86 machines, you can download the tar files for cuDNN (for cuda 11) and TensorRT and install them using the following commands
```bash
cm run script --tags=get,cudnn --input=<PATH_TO_CUDNN_TAR_FILE>
```

### Install TensorRT
```bash
cm run script --tags=get,tensorrt,_dev --input=<PATH_TO_TENSORRT_TAR_FILE>
```

On other systems, you can do a package manager install and then CM should pick up the installation automatically during the workflow run.

## Managing the configuration files


```
cm run script --tags=build,nvidia,inference,server
```
Once the below command is done, the inference server will be built and your system will be automatically detected by Nvidia scripts.

Nividia code location is output by the below command
```
cd `cm find cache --tags=inference,results,mlperf,_nvidia-only`
```

Further cd into inference_results_v<>/closed/NVIDIA

Nvidia runs configuration values for each model-scenario for known systems are stored in the `__init__.py` files under the configs directory. For custom systems (ones that are different from the ones used by Nvidia for submission) these are stored under `custom.py` files. 

**Important** When custom config files are generated they override the default config values with empty ones (not desirable). So, you'll probably need to open the custom config file and comment out the overrides. Typically `gpu_batch_size` and `offline_expected_qps` are enough for an offline scenario run on a typical single GPU system.

<details>

```bash
arjun@phoenix:~/CM/repos/local/cache/84cc898e307e466d/inference_results_v2.1/closed/NVIDIA$ tree configs
```

```
configs
├── 3d-unet
│   ├── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   └── __init__.py
│   └── SingleStream
│       ├── custom.py
│       └── __init__.py
├── bert
│   ├── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── custom.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── __pycache__
│   │   └── __init__.cpython-310.pyc
│   ├── Server
│   │   ├── custom.py
│   │   └── __init__.py
│   └── SingleStream
│       ├── custom.py
│       └── __init__.py
├── configuration.py
├── dlrm
│   ├── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   └── __init__.py
│   └── Server
│       ├── custom.py
│       └── __init__.py
├── error.py
├── __pycache__
│   ├── configuration.cpython-310.pyc
│   └── error.cpython-310.pyc
├── resnet50
│   ├── __init__.py
│   ├── MultiStream
│   │   ├── custom.py
│   │   └── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── custom.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── __pycache__
│   │   └── __init__.cpython-310.pyc
│   ├── Server
│   │   ├── custom.py
│   │   └── __init__.py
│   └── SingleStream
│       ├── custom.py
│       ├── __init__.py
│       └── __pycache__
│           ├── custom.cpython-310.pyc
│           └── __init__.cpython-310.pyc
├── retinanet
│   ├── __init__.py
│   ├── MultiStream
│   │   ├── custom.py
│   │   └── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── custom.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── __pycache__
│   │   └── __init__.cpython-310.pyc
│   ├── Server
│   │   ├── custom.py
│   │   └── __init__.py
│   └── SingleStream
│       ├── custom.py
│       └── __init__.py
├── rnnt
│   ├── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   └── __init__.py
│   ├── Server
│   │   ├── custom.py
│   │   └── __init__.py
│   └── SingleStream
│       ├── custom.py
│       └── __init__.py
├── ssd-mobilenet
│   ├── __init__.py
│   ├── MultiStream
│   │   ├── custom.py
│   │   └── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   └── __init__.py
│   └── SingleStream
│       ├── custom.py
│       └── __init__.py
└── ssd-resnet34
    ├── __init__.py
    ├── MultiStream
    │   ├── custom.py
    │   └── __init__.py
    ├── Offline
    │   ├── custom.py
    │   └── __init__.py
    ├── Server
    │   ├── custom.py
    │   └── __init__.py
    └── SingleStream
        ├── custom.py
        └── __init__.py

    
```
</details>
