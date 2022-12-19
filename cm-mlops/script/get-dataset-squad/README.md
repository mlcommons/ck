# Downloads SQUAD Dataset
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) downloads the SQUAD dataset.

## Usage

```
cm run script --tags=get,dataset,squad --version=[VERSION]
```
where [VERSION] is one of 
* `1.1`
* `2.0`

## Exported Variables
* `CM_DATASET_SQUAD_PATH:` Directory path to SQUAD dataset
* `CM_DATASET_SQUAD_TRAIN_PATH:` JSON file path to SQUAD training dataset
* `CM_DATASET_SQUAD_VAL_PATH:` JSON file path to SQUAD validation dataset

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9
