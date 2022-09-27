**[ [TOC](../README.md) ]**

You can use the [virtual CK environment](https://github.com/mlcommons/ck-venv) to avoid mixing up your current Python installation as follows:

```
ck pull repo:mlcommons@ck-venv
ck create venv:test
ck activate venv:test
```

You can create a virtual environment using a template such as MLPerf&trade; inference. 
CK will attempt to automatically install extra CK packages required for MLPerf&trade; inference:
```
ck ls venv.template
ck create venv:mlperf --template=mlperf-inference-dev
ck activate venv:mlperf
```

We suggest you to use generic template with minimal CK setup:
```
ck create venv:test1 --template=generic
ck activate venv:test1
```
