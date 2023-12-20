This CM automation recipe helps to download or detect [COCO datasets](https://cocodataset.org)
and register them in the CM cache with various environment variables 
to be reused in CM workflows and other projects.

## Use-cases

* https://github.com/mlcommons/abtf-ssd-pytorch

## Examples

### Download and install COCO dataset:

```bash
cmr "get coco dataset"
cmr "get coco dataset _val _2017"
cmr "get coco dataset _train _2017"
```

### Detect already installed COCO dataset

```bash
cmr "get coco dataset" --path={PATH to installed dataset"
```

cmr "get coco dataset" --path="D:\Work2\COCO 2017 val"


cmr "get coco dataset" ^ 
  --adr.get-dataset-coco-data.local_path="D:\Work2\COCO-2017-val\val2017.zip" ^
  --adr.get-dataset-coco-annotations.local_path="D:\Work2\COCO-2017-val\annotations_trainval2017.zip" 

cmr "get coco dataset" ^ 
  --adr.get-dataset-coco-data.local_path="D:\Work2\COCO-2017-val\val2017.zip" ^
  --adr.get-dataset-coco-data.env.CM_EXTRACT_TO_FOLDER="D:\Work22" ^
  --adr.get-dataset-coco-annotations.local_path="D:\Work2\COCO-2017-val\annotations_trainval2017.zip" ^
  --adr.get-dataset-coco-annotations.extract_to... env.CM_EXTRACT_TO_FOLDER="D:\Work22"

cmr "get coco dataset" --adr.get-dataset-coco-data.env.CM_DOWNLOAD_LOCAL_FILE_PATH="D:\Work1\!!Work\COCO 2017 val\val2017.zip"
cmr "get coco dataset" --adr.746e5dad5e784ad6.local_path="D:\Work1\!!Work\COCO 2017 val\val2017.zip"


To extract somewhere, we should use CM_EXTRACT_PATH -> extract_to
    "download_path": "CM_DOWNLOAD_PATH",

CM_EXTRACT_TO_FOLDER <- add to current directory to avoid messing up current directory if lots of files

