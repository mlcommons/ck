## Run Commands

We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset and register in CM.

## Create an AWS Graviton Instance

```
cd $HOME/CM/repos/mlcommon@ck/cm-mlops/script/run-terraform/aws/
cp credentials.example credentials.sh
```
Update `credentials.sh` with your AWS Key, Secret and Token

```
cm run script --tags=run,terraform,_m7g.xlarge,_storage_size.500,_ubuntu.2204,_us-west-2 \
--cminit --key_file=$HOME/cmuser.pem
```

The above command will output the IP of the created instance which will be having CM setup already done

Copy the imagenet dataset to the created instance. For example,

```
rsync -avz -e 'ssh -i $HOME/cmuser.pem' $HOME/imagenet-2012-val/ ubuntu@54.189.93.134:
```

