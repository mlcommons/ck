This script is a CM wrapper to the official [Nvidia submission code](https://github.com/mlcommons/inference_results_v2.1/tree/master/closed/NVIDIA) used for 2.1 MLPerf inference round. 

This script will automatically call the Nvidia script to [add a custom system](https://github.com/mlcommons/inference_results_v2.1/tree/master/closed/NVIDIA#adding-a-new-or-custom-system).

Nvidia working directory is given by `CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH` variable which can be seen by running 
```bash
cm run script --tags=get,nvidia,common-code,_custom --out=json
```


Requirements: You need to have CUDA, cuDNN and TensorRT installed on your system. 

If CUDA is not detected, CM should download and install it automatically when you run the workflow.

For x86 machines, you can download the tar files for cuDNN and TensorRT and install them using the following commands
```bash
cm run script --tags=get,cudnn --input=<PATH_TO_CUDNN_TAR_FILE>
```

```bash
cm run script --tags=get,tensorrt --input=<PATH_TO_TENSORRT_TAR_FILE>
```

On other systems you can do a package manager install and then CM should pick up the installation automatically during the workflow run.

## Managing the configuration files


```
cm run script --tags=build,nvidia,inference,server
```
Once the below command is done, inference server will be build and your system will be automatically detected by Nvidia scripts.

Nividia code location is output by the below command
```
cd `cm find cache --tags=inference,results,mlperf,_custom`
```

Further cd into inference_results_v<>/closed/NVIDIA

Nvidia run configuration values for each model-sceraio for known systems are stored in `__init__.py` files under configs directory. For custom systems (ones which are different from the ones used by Nvidia for submission) these are stored under `custom.py` files. 

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
