# Modularizing MLPerf benchmarks

*This is work in progress within [MLPerf taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
 to make MLPerf easier to run, customize and reproduce using the [MLCommons CM (CK2) automation meta-framework](https://github.com/mlcommons/ck)*.

## Demo: MLPerf inference - ref - python - object detection - RetinaNet - ONNX - CPU - Ubuntu

This demo shows how to run MLPerf inference benchmark with reference python implementation, object detection, RetinaNet, ONNX run-time, CPU and Ubuntu

* [using modular MLPerf Docker container](#using-docker)
* [using native environment](#using-native-environment)



### Using Docker

#### Build

You can build a self-contained container to customize and run MLPerf inference benchmark with object detection as follows:

```bash
time docker build -f cm-mlperf-inference-retinanet-ubuntu-cpu.Dockerfile \
                  -t mlcommons/cm-mlperf-inference:ubuntu-20.04 .
```

The MLCommons CM automation meta-framework is used inside our [Dockerfile](https://github.com/octoml/ck/blob/master/docker/cm-mlperf-inference-retinanet-ubuntu-cpu.Dockerfile) 
to automatically detect or install all required [dependencies](https://github.com/octoml/ck/tree/master/cm-mlops/script) 
described in this [CM YAML file](https://github.com/octoml/ck/blob/master/cm-mlops/script/app-mlperf-inference-reference/_cm.yaml)
and prepare MLPerf inference for further experimentation.

It takes around 25 minutes on our GCP instance with 16 cores and 64GB of memory. The final Docker image takes ~2.7GB of space.


<details>

You can customize your build to test different versions of different MLPerf dependencies as follows:

```bash
time docker build -f cm-mlperf-inference-retinanet-ubuntu-cpu.Dockerfile \
   -t mlcommons/cm-mlperf-inference:ubuntu-20.04 \
   --build-arg cm_os_name="ubuntu" \
   --build-arg cm_os_version="20.04" \
   --build-arg cm_version="1.0.3" \
   --build-arg cm_automation_repo="ctuning@mlcommons-ck" \
   --build-arg cm_automation_checkout="" \
   --build-arg cm_python_version="3.10.7" \
   --build-arg cm_cmake_version="3.24.2" \
   --build-arg cm_mlperf_inference_loadgen_version="" \
   --build-arg cm_mlperf_inference_src_tags="_octoml" \
   --build-arg cm_mlperf_inference_src_version="" \
   --build-arg cm_ml_engine="onnxruntime" \
   --build-arg cm_ml_engine_version="1.12.1" \
   --build-arg cm_llvm_version="14.0.0" \
   .
```
</details>


#### Test Run (offline; accuracy)

You can now test this benchmark with RetinaNet and a small data set in accuracy mode as follows:
```bash
docker run -it mlcommons/cm-mlperf-inference:ubuntu-20.04 \
           -c "cm run script --tags=app,mlperf,inference,generic,reference,_python,_retinanet,_onnxruntime,_cpu --rerun --scenario=Offline --mode=accuracy --test_query_count=10"
```

After ~5 min you should obtain the following output:
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



#### Test Run (offline; performance)

You can now test this benchmark with RetinaNet and a small data set in performance mode as follows:
```bash
docker run -it mlcommons/cm-mlperf-inference:ubuntu-20.04 \
           -c "cm run script --tags=app,mlperf,inference,generic,reference,_python,_retinanet,_onnxruntime,_cpu --rerun --scenario=Offline --mode=performance --test_query_count=10"
```

You should obtain the following output:
```txt
TestScenario.Offline qps=0.89, mean=8.6960, time=11.180, acc=31.661%, mAP=65.417%, queries=10, tiles=50.0:8.8280,80.0:9.0455,90.0:9.1450,95.0:9.2375,99.0:9.3114,99.9:9.3281
```



### Using native environment

This demo showcases the use of the [MLCommons CM (CK2) automation meta-framework](https://github.com/mlcommons/ck) 
being developed by the [MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md).

The goal of CM is to modularize ML Systems and automate their benchmarking, optimization and co-design across any software and hardware stack.

You can run the above demo with MLPerf inference benchmark natively as follows (without Docker).

First, you need to install the CM framework as desribed [here](https://github.com/mlcommons/ck#installation).

Here is the typical installation on Ubuntu 22.04:

```bash
sudo apt install python3 python3-pip git wget
python3 -m pip install cmind
source .profile
```

Next you need to install a CM repository with [cross-platform automations (portable CM scripts)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) for ML Systems:

```bash
cm pull repo mlcommons@ck
```

Note that you can fork [this repository](https://github.com/mlcommons/ck) and use your own one instead of mlcommons@ck for public or private benchmarking.
For example, we use [cTuning](https://cTuning.org) fork to improve these automations:

```bash
cm pull repo ctuning@mlcommons-ck
```

Now we suggest you to install a virtual python via CM to avoid mixing up your native Python installation:
```bash
cm run script "install python-venv" --name=mlperf --version=3.10.7
```

You can now test MLPerf inference benchmark with RetinaNet and ONNX runtime using just one CM command:
```bash
cm run script "app mlperf inference generic reference _python _retinanet _onnxruntime _cpu" \
    --adr.compiler.tags=gcc -v --rerun \
    --scenario=Offline --mode=accuracy --test_query_count=10
```

The first run can take around 25 minutes on our GCP instance with 16 cores and 64GB of memory because
CM will automatically detect and install all the necessary ML components while adapting to your system.

These dependencies are described in a simple YAML [here](https://github.com/octoml/ck/blob/master/cm-mlops/script/app-mlperf-inference-reference/_cm.yaml).

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

Any other run will automatically pick up all dependencies from the CM cache while setting up all environment variable and files to launch the prepared MLPerf inference benchmark.
For example, you can run these benchmark in performance mode as follows:
```bash
cm run script "app mlperf inference generic reference _python _retinanet _onnxruntime _cpu" \ 
    --adr.compiler.tags=gcc -v --rerun \
    --scenario=Offline --mode=performance --test_query_count=10
```

You should see the following output:
```txt
TestScenario.Offline qps=0.89, mean=8.6960, time=11.180, acc=31.661%, mAP=65.417%, queries=10, tiles=50.0:8.8280,80.0:9.0455,90.0:9.1450,95.0:9.2375,99.0:9.3114,99.9:9.3281
```

Note that before running MLPerf inference benchmark, you can also install any version of any ML component via CM.
They will be cached and automatically picked up when you run MLPerf benchmark via CM.

<details>

Here are examples of CM automations (basic MLOps interoperability blocks) for typical ML components required by MLPerf:

```bash
cm run script "install python-venv" --version=3.9.6 --name=my-test

cm run script "get cmake"
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

</details>



You can see the state of CM cache at any time as follows:
```bash
cm show cache
cm show cache --tags=ml-model
```

You can clean the cache at any time as follows:
```
cm rm cache -f
```



### Preparing end-to-end submission

You can use CM to automate submissions.

Here is an example for ResNet50. 

Since it's not possible to automatically download ImageNet, we assume that you have it installed in /datasets/imagenet-2012-val.
You can run the following CM command to launch a full MLPerf inference run for Offline mode and prepare your submission
(CM will automatically pick up ImageNet and cache its' environment for further use):

```bash
cm run script --tags=run,mlperf,inference,generate-run-cmds,_valid,_submission  --model=resnet50 --backend=onnxruntime --device=cpu --lang=python \
     --verbose --adr.inference-src.tags=_octoml --adr.compiler.tags=gcc \
     --imagenet_path=/datasets/imagenet-2012-val --adr.imagenet-preprocessed.tags=_full  
     --output_dir=~/out/results \
     --submission_dir=~/out/submission'
```

You can use Docker too:
```bash
docker build -f cm-mlperf-inference-ubuntu-cpu.Dockerfile -t mlcommons/cm-mlperf-inference-resnet50:ubuntu-20.04 .
chmod -R 777 ~/out
docker run -it --privileged -v /datasets/imagenet-2012-val:/datasets/imagenet-2012-val -v ~/out:/home/cmuser/out mlcommons/cm-mlperf-inference-resnet50:ubuntu-22.04  \
  'cm run script --tags=run,mlperf,inference,generate-run-cmds,_valid,_submission  --model=resnet50 --backend=onnxruntime --device=cpu --lang=python --verbose --adr.inference-src.tags=_octoml --adr.compiler.tags=gcc --imagenet_path=/datasets/imagenet-2012-val --adr.imagenet-preprocessed.tags=_full  --output_dir=/home/cmuser/out/results --submission_dir=/home/cmuser/out/submission'
```
