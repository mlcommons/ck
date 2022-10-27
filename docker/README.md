# Modularizing MLPerf benchmarks

*This is work in progress within [MLPerf taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
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
   --build-arg cm_automation_repo="octoml@ck" \
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


#### Test Run (accuracy)

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



#### Test Run (performance)

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


### Preparing end-to-end submission

TBD

