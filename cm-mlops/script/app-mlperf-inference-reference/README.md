# Description

This portable CM script is being developed by the [MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
to modularize the *python reference implementations* of the [MLPerf inference benchmark](https://github.com/mlcommons/inference) 
using the [MLCommons CM automation meta-framework](https://github.com/mlcommons/ck).
The goal is to make it easier to run, optimize and reproduce MLPerf benchmarks 
across diverse platforms with continuously changing software and hardware.

[![License](https://img.shields.io/badge/License-Apache%202.0-green)](https://github.com/mlcommons/ck/tree/master/cm)
[![CM repository](https://img.shields.io/badge/Collective%20Mind-compatible-blue)](https://github.com/mlcommons/ck)

&copy; 2021-2022 [MLCommons](https://mlcommons.org)<br>

# Authors

[Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), 
[Grigori Fursin]( https://cKnowledge.io/@gfursin ) 
and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).

# Command line interface

* [All commands and options](README.commands.md)

# Examples

## MLPerf object detection with python, RetinaNet, Open Images, ONNX runtime (CPU), Ubuntu

This example shows how to use this CM script to run the reference python implementation 
of the MLPerf inference benchmark for object detection, RetinaNet, ONNX run-time (CPU) and Ubuntu.

### Using native environment

Install the MLCommons CM automation meta-framework as described [here]( https://github.com/mlcommons/ck/blob/master/cm/docs/installation.md ).

Here is the typical installation on Ubuntu 20.04:

```bash
sudo apt install python3 python3-pip git wget
python3 -m pip install cmind
source .profile
```

Next you need to install a CM repository with [cross-platform CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) for ML Systems:

```bash
cm pull repo mlcommons@ck
```

Note that you can fork [this repository](https://github.com/mlcommons/ck) and use it instead of mlcommons@ck 
to add CM scripts for your own public and private ML models, data sets, software and hardware.
In such case, just change mlcommons@ck to your own fork in the above command.

You can find the location of this repository on your system as follows:
```bash
cm find repo mlcommons@ck
```

Now we suggest you to set up a virtual python via CM to avoid mixing up your native Python installation:
```bash
cm run script "install python-venv" --name=demo
```

If you need a specific python version use this command:
```bash
cm run script "install python-venv" --name=demo --version=3.10.7
```

You can now test the MLPerf inference benchmark with RetinaNet and ONNX runtime CPU using just one CM command:

```bash
cm run script "app mlperf inference generic reference _python _retinanet _onnxruntime _cpu" \
    --adr.compiler.tags=gcc --scenario=Offline --mode=accuracy --test_query_count=10 --quiet
```

The first run of this CM script takes around 25 minutes on a GCP instance with 16 cores and 64GB of memory because
CM will automatically detect, install and cache all the necessary ML components 
while adapting them to your system using [portable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script).

These dependencies are described using [this simple YAML file](https://github.com/octoml/ck/blob/master/cm-mlops/script/app-mlperf-inference-reference/_cm.yaml#L57)
and can be turned on or off using different environment variables passed to this CM script using `--env.KEY=VALUE`.

You should see the following output in the end:
```txt
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.654
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.827
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.654
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.657
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.566
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.705
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.735
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.738

mAP=65.417%

```

Any other run will automatically pick up all dependencies from the CM cache while setting up all environment variables and files 
to launch the prepared MLPerf inference benchmark. For example, you can run these benchmark in performance mode as follows:

```bash
cm run script "app mlperf inference generic reference _python _retinanet _onnxruntime _cpu" \ 
    --adr.compiler.tags=gcc --scenario=Offline --mode=performance --test_query_count=10 --rerun
```

You should see the following output:
```txt
TestScenario.Offline qps=0.89, mean=8.6960, time=11.180, acc=31.661%, mAP=65.417%, queries=10, tiles=50.0:8.8280,80.0:9.0455,90.0:9.1450,95.0:9.2375,99.0:9.3114,99.9:9.3281
```

Note that before running MLPerf inference benchmark, you can also install specific versions of ML components via CM.
They will be cached and automatically picked up when you run MLPerf benchmark via CM..

Here are examples of CM automations (to ensure universal MLOps interoperability) for typical ML components required by MLPerf:

```bash
cm run script "install python-venv" --version=3.9.6 --name=my-test

cm run script "get cmake" --version=
cm run script "get llvm prebuilt" --version=14.0.0

cm run script "get generic-python-lib _onnxruntime" --version=1.12.1
cm run script "get generic-python-lib _pytorch"
cm run script "get generic-python-lib _transformers"
cm run script "get generic-python-lib _tf"
cm run script "get tvm _llvm" --version=0.9.0

cm run script "get mlperf loadgen" --adr.compiler.tags=gcc

cm run script "get mlperf inference src _octoml"

cm run script "get ml-model object-detection resnext50 fp32 _onnx"

cm run script "get dataset object-detection open-images original"

```


You can see the state of CM cache at any time as follows:
```bash
cm show cache
cm show cache --tags=ml-model
```

You can clean the cache at any time as follows:
```
cm rm cache -f
```



### Using Docker

Please check the prototype of Docker containers with the CM automation meta-framework 
for modular MLPerf [here](https://github.com/mlcommons/ck/tree/master/docker) 
(on-going work).



# TBD

* Specify versions of all deps from command line
* Test CPP+Python for CPU+CUDA
  * Resnet + RetinaNet
* Add your own optimized model
* Run iterative experiments
  * Unify JSON output (ENV + state)
  * Reproduce experiments
  * Visualize experiments
* Prepare end-to-end submissions from the best experiments
* Add Docker examples
