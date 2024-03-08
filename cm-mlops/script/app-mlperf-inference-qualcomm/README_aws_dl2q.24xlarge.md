# MLPerf Inference Benchmarking on AWS dl2q.24xlarge instance using 8 QAIC Cloud AI 100

`dl2q.24xlarge` instance is available in `us-west-2d` and it has 96 vCPUs and 768 GB of memory. 

[Deep Learning Base Qualcomm AMI (Amazon Linux 2) 20240110, ami-0799a42a111b1b87a](https://us-west-2.console.aws.amazon.com/ec2/home?region=us-west-2#LaunchInstances:ami=ami-0799a42a111b1b87a)
image from the Community AMIs is the recommended OS image as it comes with the QIAC SDKs (both Apps and Platform) preinstalled.

* Recommended to take 300 GB root disk


## System setup
```
sudo yum install -y python38-devel git
python3.8 -m pip install cmind
cm pull repo mlcommons@ck
cm run script --tags=get,python --version_min=3.8.1
```

## Bert-99

### Quick performance run
```
cm run script --tags=generate-run-cmds,inference,_performance-only --device=qaic \
--backend=glow --scenario=Offline  --implementation=kilt --model=bert-99 \
--test_query_count=40000 --precision=uint8 --rerun --quiet \
--adr.mlperf-inference-implementation.tags=_loadgen-batch-size.4096,_dl2q.24xlarge \
--quiet --adr.compiler.tags=gcc --execution-mode=test
```

### Full valid run
```
cm run script --tags=generate-run-cmds,inference,_submission --device=qaic \
--backend=glow --scenario=Offline --implementation=kilt --model=bert-99 --precision=uint8 \
--adr.mlperf-inference-implementation.tags=_loadgen-batch-size.4096,_dl2q.24xlarge \
--rerun --quiet --execution-mode=valid
```

The expected performance is ~5700 QPS
The expected accuracy is ~90
* Use `--scenario=Server --server_target_qps=5200` to run the server scenario


## ResNet50

(Optional)
If you have Imagenet 2012 validation dataset downloaded, you can register it in CM as follows. This step is optional and can avoid the download from the public URL which can be slow at times.
```
cm run script --tags=get,dataset,imagenet,original,_full --env.IMAGENET_PATH=`pwd`/imagenet-2012-val
```

### Quick performance run

```
cm run script --tags=generate-run-cmds,inference,_performance-only --device=qaic --backend=glow \
--scenario=Offline  --implementation=kilt --model=resnet50 \
--test_query_count=400000 --precision=uint8 --rerun --adr.compiler.tags=gcc \
--adr.mlperf-inference-implementation.tags=_bs.8,_dl2q.24xlarge --execution-mode=test --quiet
```

### Full valid run

```
cm run script --tags=generate-run-cmds,inference,_submission --device=qaic --backend=glow \
--scenario=Offline  --implementation=kilt --model=resnet50 \
--precision=uint8 --rerun --adr.compiler.tags=gcc \
--adr.mlperf-inference-implementation.tags=_bs.8,_dl2q.24xlarge --execution-mode=valid --quiet
```
Expected performance is ~157500
Expected accuracy is 75.936%

* Use `--scenario=Server --server_target_qps=152000` to run the server scenario


## RetinaNet

### Quick performance run

```
cm run script --tags=generate-run-cmds,inference,_performance-only --device=qaic --backend=glow \
--scenario=Offline  --implementation=kilt --model=retinanet --test_query_count=40000 --precision=uint8 \
--rerun --quiet --adr.mlperf-inference-implementation.tags=_loadgen-batch-size.1,_dl2q.24xlarge,_bs.1 \
--adr.compiler.tags=gcc --execution-mode=test 
```

### Full valid run

```
cm run script --tags=generate-run-cmds,inference,_submission --device=qaic --backend=glow \
--scenario=Offline  --implementation=kilt --model=retinanet \
--precision=uint8 --rerun --adr.compiler.tags=gcc --adr.dataset-preprocessed.tags=_custom-annotations \
--adr.mlperf-inference-implementation.tags=_bs.1,_dl2q.24xlarge --execution-mode=valid --quiet
```
Expected performance is ~2200
The expected accuracy is 37.234

* Use `--scenario=Server --server_target_qps=2050` to run the server scenario

