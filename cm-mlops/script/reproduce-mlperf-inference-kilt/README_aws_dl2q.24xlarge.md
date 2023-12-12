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

*WIP*
