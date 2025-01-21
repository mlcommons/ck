Please execute the following CM command to obtain the platform details of the System Under Test (SUT):

```
cm run script --tags=get,platform-details --platform_details_dir=<DIRECTORY_TO_SAVE_THE_TXT_FILE>
```


The generated details will be saved as a text file in the specified directory. If no directory is specified, the generated text file will be saved in the CM cache

A sample of the generated text file can be found [here](https://github.com/GATEOverflow/mlperf_inference_test_submissions_v5.0/blob/main/open/MLCommons/measurements/gh_action-reference-gpu-pytorch_v2.5.0-cu124/system_info.txt)
