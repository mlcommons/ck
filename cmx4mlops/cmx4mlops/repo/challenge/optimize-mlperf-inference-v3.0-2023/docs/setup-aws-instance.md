The below instructions are for creating an AWS instance from the CLI. You can also create an instance via web and setup CM on it.

## Prerequisites

1. AWS Key, secret and token
2. `*.pem` ssh key file to be used to create the instance (public key from here will be copied to the `$HOME/.ssh/authorized_keys` file in the created instance)

## Run Commands

We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset and register in CM.

### Update Access Details

```
cd $HOME/CM/repos/mlcommon@ck/cm-mlops/script/run-terraform/aws/
cp credentials.example credentials.sh
```
Update `credentials.sh` with your AWS Key, Secret and Token

### Create an AWS Instance


```
cm run script --tags=run,terraform,_m7g.xlarge,_storage_size.500,_ubuntu.2204,_us-west-2 \
--cminit --key_file=$HOME/cmuser.pem
```

The above command will output the IP of the created instance which will be having CM setup already done. 

`_m7g.xlarge,_storage_size.500,_ubuntu.2204` variations can be changed to launch a different instance. Below are the variation combinations we used for MLPerf inference 3.0 submissions.

* `_g4dn.xlarge`
* `_a1.2xlarge,_storage_size.130,_ubuntu.2204`
* `_c5.4xlarge,_storage_size.130,_ubuntu.2204`
* `_m7g.2xlarge,_storage_size.500,_ubuntu.2204`
* `_inf1.2xlarge,_storage_size.500,_amazon-linux-2-kernel.510`
* `_t2.medium,_storage_size.200,_rhel.9`

### Copy the needed files from the local machine

Copy the imagenet dataset to the created instance. For example,

```
rsync -avz -e 'ssh -i $HOME/cmuser.pem' $HOME/imagenet-2012-val/ ubuntu@54.189.93.134:
```
For using [nvidia-original implementation](https://github.com/mlcommons/ck/tree/main/cm-mlops/script/reproduce-mlperf-inference-nvidia) tar files for cuDNN and TensorRT are needed to be downloaded locally from Nvidia website and copied to the AWS instance similar to the above command.

Once all the required files are copied over, login to the instance and follow the individual benchmark instructions from the README files given [here](./)
