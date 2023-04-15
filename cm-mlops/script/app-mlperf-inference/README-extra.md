# Examples

## MLPerf object detection with python, RetinaNet, Open Images, ONNX runtime (CPU), Ubuntu

This example shows how to use this CM script to run the reference python implementation 
of the MLPerf inference benchmark for object detection, RetinaNet, ONNX run-time (CPU) and Ubuntu.

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
cm run script "install python-venv" --name=mlperf
```

If you need a specific python version use this command:
```bash
cm run script "install python-venv" --name=mlperf --version=3.10.7
```

You can now test the MLPerf inference benchmark with RetinaNet and ONNX runtime CPU using just one CM command:

```bash
cm run script "app mlperf inference generic reference _python _retinanet _onnxruntime _cpu" \
    --adr.python.name=mlperf \
    --adr.compiler.tags=gcc \
    --scenario=Offline \
    --mode=accuracy \
    --test_query_count=10 \
    --quiet
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
    --adr.python.name=mlperf \
    --adr.compiler.tags=gcc \
    --scenario=Offline \
    --mode=performance \
    --test_query_count=10 \
    --rerun
```

You should see the following output:
```txt
TestScenario.Offline qps=0.89, mean=8.6960, time=11.180, acc=31.661%, mAP=65.417%, queries=10, tiles=50.0:8.8280,80.0:9.0455,90.0:9.1450,95.0:9.2375,99.0:9.3114,99.9:9.3281
```



### Using Docker

Please check the prototype of Docker containers with the CM automation meta-framework 
for modular MLPerf [here](https://github.com/mlcommons/ck/tree/master/docker) 
(on-going work).

```bash
docker build -f dockerfiles/resnet50/ubuntu_20.04_python_onnxruntime_cpu.Dockerfile -t resnet50_onnxruntime:ubuntu20.04 .
```

```bash
docker run -it --rm resnet50_onnxruntime:ubuntu20.04 -c "cm run script --tags=app,mlperf,inference,reference,python_resnet50,_onnxruntime,_cpu --scenario=Offline --mode=accuracy"
```




# Future work

* See the current coverage of different models, devices and backends [here](README-extra.md#current-coverage).

* See the development roadmap [here](https://github.com/mlcommons/ck/issues/536).

* See extension projects to enable collaborative benchmarking, design space exploration and optimization of ML and AI Systems [here](https://github.com/mlcommons/ck/issues/627).


# Developers

[Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), 
[Grigori Fursin]( https://cKnowledge.org/gfursin ) 
and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
