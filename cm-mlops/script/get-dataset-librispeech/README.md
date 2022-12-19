# Downloads LibriSpeech Dataset
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) downloads the LibriSpeech dataset.

## Usage

```
cm run script --tags=get,dataset,librispeech --version=[VERSION]
```
where [VERSION] is one of 
* `dev-clean`
* `dev-other`
* `train-clean`
* `train-other`
* `train-clean-100`
* `train-clean-360`
* `train-other-500`

## Exported Variables
* `CM_DATASET_ARCHIVE:`
* `CM_DATASET_LIBRISPEECH_PATH:`
* `CM_DATASET_MD5:`
* `CM_DATASET_NAME:`

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9
