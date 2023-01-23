This script is a CM wrapper to the official [Nvidia submission code](https://github.com/mlcommons/inference_results_v2.1/tree/master/closed/NVIDIA) used for 2.1 MLPerf inference round. 

This script will automatically call the Nvidia script to [add a custom system](https://github.com/mlcommons/inference_results_v2.1/tree/master/closed/NVIDIA#adding-a-new-or-custom-system).

Nvidia working directory is given by `CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH` variable which can be seen by running 
```bash
cm run script --tags=get,nvidia,common-code,_custom --out=json
```

<details>
```bash
   
arjun@phoenix:~/CM/repos/local/cache/84cc898e307e466d/inference_results_v2.1/closed/NVIDIA$ tree configs
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
