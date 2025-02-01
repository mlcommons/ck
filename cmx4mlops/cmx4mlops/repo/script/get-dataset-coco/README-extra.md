# CM interface to download or detect COCO data sets 

This CM automation recipe helps to download or detect [COCO datasets](https://cocodataset.org)
and register them in the CM cache with various environment variables 
to be reused in CM workflows and other projects.

Supported versions: 
* 2017 val/train
* 2014 val/train 

## Use-cases

* https://github.com/mlcommons/abtf-ssd-pytorch

## Download COCO dataset and register in CM cache

```bash
cmr "get coco dataset"
cmr "get coco dataset _val _2017"
cmr "get coco dataset _train _2017"
```

You can find this data set in the CM cache using the following command:

```bash
cm show cache "get coco dataset"
```

#### Output environment variables

You can check produced environment variables produced by this CM script by adding the `-j` flag:

```bash
cmr "get coco dataset _val _2017" -j
```

```json
  "new_env": {
    "CM_DATASET_COCO_URL_ANNOTATIONS": "http://images.cocodataset.org/annotations",
    "CM_DATASET_COCO_URL_DATA": "http://images.cocodataset.org/zips",
    "CM_DATASET_COCO_VERSION": "2017",
    "CM_DATASET_COCO_TYPE": "val",
    "CM_DATASET_COCO_SIZE": "complete",
    "CM_DATASET_COCO_ANNOTATIONS_DOWNLOAD_PATH": "d:\\Work2\\COCO-2017-val\\annotations_trainval2017.zip",
    "CM_DATASET_COCO_ANNOTATIONS_PATH": "D:\\Work1\\CM\\repos\\local\\cache\\62ad05746b5d4f07\\annotations",
    "CM_DATASET_COCO_DATA_DOWNLOAD_PATH": "d:\\Work2\\COCO-2017-val\\val2017.zip",
    "CM_DATASET_COCO_DATA_PATH": "D:\\Work1\\CM\\repos\\local\\cache\\62ad05746b5d4f07\\val2017",
    "CM_DATASET_COCO_MD5SUM_ANN": "f4bbac642086de4f52a3fdda2de5fa2c",
    "CM_DATASET_COCO_MD5SUM_DATA": "442b8da7639aecaf257c1dceb8ba8c80",
    "CM_DATASET_COCO_PATH": "D:\\Work1\\CM\\repos\\local\\cache\\62ad05746b5d4f07",
    "CM_DATASET_COCO_TYPE_AND_VERSION": "val2017",
    "CM_DATASET_COCO_URL_ANNOTATIONS_FULL": "http://images.cocodataset.org/annotations/annotations_trainval2017.zip",
    "CM_DATASET_COCO_URL_DATA_FULL": "http://images.cocodataset.org/zips/val2017.zip",
    "CM_DATASET_PATH": "D:\\Work1\\CM\\repos\\local\\cache\\62ad05746b5d4f07",
    "CM_DATASET_PATH_ROOT": "D:\\Work1\\CM\\repos\\local\\cache\\62ad05746b5d4f07"
  },
```

#### Input flags and equivalent environment variables

* `--from` - where to find dataset archive files instead of downloading them
* `--to` - where to extract dataset files
* `--path` - where to pick up extracted dataset files
* `--store` - where to keep downloaded files

#### Variations

* Dataset type: `_val` | `_train`
* Dataset year: `2017` | `2014`


## Detect already installed COCO dataset

```bash
cmr "get coco dataset" --path={PATH to the installed dataset}"
```

CM script will attempt to automatically detect the type (val/train) and version (2014/2017) 
of the dataset files.

## Install dataset from already downloaded archives

```bash
cmr "get coco dataset  _val _2017" --from=d:\Work2\COCO-2017-val -j
```

where `--from` points to the COCO dataset zip files already downloaded from the server.
It is useful when all files are already downloaded and saved for common use.


## Download and store dataset files locally

```bash
cmr "get coco dataset _val _2017" --to=d:\Downloads\COCO-2017-val --store=d:\Downloads
```
