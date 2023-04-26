The below instructions are for creating a Google Cloud instance from the CLI. You can also create an instance via web and setup CM on it.

## Prerequisites

Please follow the authentication instructions given [here](https://github.com/ctuning/mlcommons-ck/blob/master/cm-mlops/script/run-terraform/README-about.md).


## Run Commands

We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset and register in CM.


### Create a GCP Instance


```
cm run script --tags=run,terraform,_gcp,_n1-highmem.4,_gcp_project.mlperf-inference-tests --cminit
```

The above command will output the IP of the created instance which will be having CM setup already done. 

`_n1-highmem.4` variation can be changed to launch a different instance. Below are the variation combinations we used for MLPerf inference 3.0 submissions.

* `_n1-standard.4`

### Copy the needed files

Copy the imagenet dataset to the created instance. For example,

```
rsync -avz -e 'ssh -i $HOME/cmuser.pem' $HOME/imagenet-2012-val/ ubuntu@54.189.93.134:
```
For using [nvidia-original implementation](https://github.com/mlcommons/ck/tree/main/cm-mlops/script/reproduce-mlperf-inference-nvidia) tar files for cuDNN and TensorRT are needed to be downloaded locally from Nvidia website and copied to the AWS instance similar to the above command.

Once all the required files are copied over, login to the instance and follow the individual benchmark instructions from the README files given [here](./)
