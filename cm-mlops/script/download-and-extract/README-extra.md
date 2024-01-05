# CM interface to download and extract files in a unified way on any system

## Download and extract file without CM caching

### Use internal CM download function

This script will use [internal CM download function](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/utils/module.py#L157) 
to download and extract a given file to the current directory:

```bash
cmr "download-and-extract file _extract" --url=https://cKnowledge.org/test/coco-2017-val-annotations.zip
```
or

```bash
cmr "dae file _extract _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip"
```

#### Output environment variables

You can check produced environment variables produced by this CM script by adding the `-j` flag:

```bash
cmr "dae file _extract _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip" -j
```

```json
  "new_env": {
    "CM_DOWNLOAD_DOWNLOADED_PATH": "D:\\Work\\coco-2017-val-annotations.zip",
    "CM_EXTRACT_EXTRACTED_PATH": "D:\\Work",
    "CM_GET_DEPENDENT_CACHED_PATH": "D:\\Work"
  },
```

#### Input flags and equivalent environment variables

* `--url` or `--env.CM_DAE_URL` - URL to download file
* `--verify` or `--env.CM_VERIFY_SSL` - set to `no` to skip SSL certificate verification
* `--download_path` or `--store` or `--env.CM_DOWNLOAD_PATH` - where to download file
* `--local_path` or `--from` or `--env.CM_DOWNLOAD_LOCAL_FILE_PATH` - where to take file from instead of downloading
* `--extract_path` or `--to` or `--env.CM_EXTRACT_PATH` - where to extract files (--input should have full path then)
* `--extra_folder` or `--env.CM_EXTRACT_TO_FOLDER` - extra directory when extracting file (to avoid messing up current directory)


#### Variations

* `_keep` or `_no-remove-extracted` or `--env.CM_EXTRACT_REMOVE_EXTRACTED=no` - keep archive file (it will be deleted by default)



### Use wget without SSL certificate verification

```bash
cmr "dae file _extract _keep _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no
```

### Use curl without SSL certificate verification

```bash
cmr "dae file _extract _keep _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _curl" --verify=no
```

### Check MD5SUM

```bash
cmr "dae file _extract _keep _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no --env.CM_DOWNLOAD_CHECKSUM=bbe2f8874ee9e33cf5d6906338027a56
```

### Save to another file

```bash
cmr "dae file _extract _keep  _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no --env.CM_DOWNLOAD_FILENAME=xyz --env.CM_DOWNLOAD_CHECKSUM=bbe2f8874ee9e33cf5d6906338027a56
```

### Save to another place

```bash
cmr "dae file _extract _keep _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no --download_path=D:\Work --env.CM_DOWNLOAD_CHECKSUM=bbe2f8874ee9e33cf5d6906338027a56
```

### Reuse local file instead of downloading a file

```bash
cmr "dae file _extract _keep _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no --local_path="D:\Work\coco-2017-val-annotations.zip" --env.CM_DOWNLOAD_CHECKSUM=bbe2f8874ee9e33cf5d6906338027a56 -j
```


### Simplified language to download, store and extract file


```bash
cmr "dae file _extract _keep _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no --env.CM_DOWNLOAD_CHECKSUM=bbe2f8874ee9e33cf5d6906338027a56 --store=$HOME/dir1 --to=$HOME/dir2
```



## Download and extract files with CM caching

You can use all above commands with `--force_cache` and `--extra_cache_tags` flags.
In such case, a given file will be downloaded to CM cache and can be reused by other CM scripts and workflows:

```bash
cmr "dae file _extract _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no --env.CM_DOWNLOAD_CHECKSUM=bbe2f8874ee9e33cf5d6906338027a56 --force_cache --extra_cache_tags=coco,2017,val,annotations
```

You can find it in CM cache using extra cache tags as follows:
```bash
cm show cache "dae file annotations coco 2017 val"
```
