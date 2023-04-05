## Setup for Google Cloud Instances
```
sudo snap install google-cloud-cli --classic
gcloud auth application-default login
```

The above two commands will install google-cloud-cli and authorizes the user to access it. Once done, you can start creating gcp instance using CM commands like below. To destroy an instance just repeat the same command with `--destroy` option.

```
cm run script --tags=run,terraform,_gcp,_gcp_project.mlperf-inference-tests --cminit
```
Here, `mlperf-inference-tests` is the name of the google project as created in [Google cloud console](https://console.cloud.google.com/apis/dashboard)
