# MLPerf Inference Benchmarking on AWS dl2q.24xlarge instance using 8 QAIC Cloud AI 100

`dl2q.24xlarge` instance is available in `us-west-2d` and it has 96 vCPUs and 768 GB of memory. 

[Deep Learning Base Qualcomm AMI (Amazon Linux 2)](https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Images:visibility=public-images;imageId=ami-0287712deef96ecc6) image is recommended OS image as it comes with the QIAC SDKs (both Apps and Platform) preinstalled. 


## System setup
```
yum install -y python3-devel git
python3 -m pip install cmind
cm pull repo mlcommons@ck
```

## ResNet50

Do a performance run for the Offline scenario 

```
cm run script --tags=generate-run-cmds,inference,_performance-only --device=qaic --backend=glow \
--scenario=Offline  --implementation=kilt --model=resnet50 \
--test_query_count=40000 --precision=fp32 --rerun
```

* `--adr.lperf-inference-implementation.device_ids=0` can be used to run the inference only on the first QAIC device
* `--precision=uint8` is the best option to be used but unfortunately, it is not working with the default platform SDK. When we use `--precision=fp32` the float32 inputs are on the fly converted by the QAIC driver to uint8 format. This overhead and 4x memory BW usage reduces the Offline scenario performance by nearly 50%. We got `~9000` QPS for a single device run

*WIP*
