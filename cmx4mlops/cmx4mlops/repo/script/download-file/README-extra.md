# CM interface to download files in a unified way on any system

## Download file without CM caching

### Use internal CM download function

This script will use [internal CM download function](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/utils/module.py#L157) 
to download a given file to the current directory:

```bash
cmr "download file" --url=https://cKnowledge.org/test/coco-2017-val-annotations.zip
```
or

```bash
cmr "download file _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip"
```

#### Output environment variables

You can check produced environment variables produced by this CM script by adding the `-j` flag:

```bash
cmr "download file" _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip -j
```

```json
  "new_env": {
    "CM_DOWNLOAD_DOWNLOADED_PATH": "D:\\Downloads\\coco-2017-val-annotations.zip",
    "CM_GET_DEPENDENT_CACHED_PATH": "D:\\Downloads\\coco-2017-val-annotations.zip"
  },
```

#### Input flags and equivalent environment variables

* `--url` or `--env.CM_DAE_URL` - URL to download file
* `--download_path` or `--to` or `--env.CM_DOWNLOAD_PATH` - where to download file
* `--local_path` or `--from` or `--env.CM_DOWNLOAD_LOCAL_FILE_PATH` - where to take file from instead of downloading
* `--verify` or `--env.CM_VERIFY_SSL` - set to `no` to skip SSL certificate verification


### Use wget without SSL certificate verification

```bash
cmr "download file _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no
```

### Use curl without SSL certificate verification

```bash
cmr "download file _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _curl" --verify=no
```

### Check MD5SUM

```bash
cmr "download file _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no --env.CM_DOWNLOAD_CHECKSUM=bbe2f8874ee9e33cf5d6906338027a56
```

### Save to another file

```bash
cmr "download file _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no --env.CM_DOWNLOAD_FILENAME=xyz --env.CM_DOWNLOAD_CHECKSUM=bbe2f8874ee9e33cf5d6906338027a56
```

### Save to another place

```bash
cmr "download file _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no --download_path=D:\Work --env.CM_DOWNLOAD_CHECKSUM=bbe2f8874ee9e33cf5d6906338027a56
```

### Reuse local file instead of downloading a file

```bash
cmr "download file _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no --local_path="D:\Work\coco-2017-val-annotations.zip" --env.CM_DOWNLOAD_CHECKSUM=bbe2f8874ee9e33cf5d6906338027a56 -j
```

Output environment variables produced by this CM script:
```json
  "new_env": {
    "CM_DOWNLOAD_DOWNLOADED_PATH": "D:\\Work\\coco-2017-val-annotations.zip",
    "CM_GET_DEPENDENT_CACHED_PATH": "D:\\Work\\coco-2017-val-annotations.zip"
  }
```

## Download file with CM caching

You can use all above commands with `--force_cache` and `--extra_cache_tags` flags.
In such case, a given file will be downloaded to CM cache and can be reused by other CM scripts and workflows:

```bash
cmr "download file _url.https://cKnowledge.org/test/coco-2017-val-annotations.zip _wget" --verify=no --env.CM_DOWNLOAD_CHECKSUM=bbe2f8874ee9e33cf5d6906338027a56 --force_cache --extra_cache_tags=coco,2017,val,annotations
```

You can find it in CM cache using extra cache tags as follows:
```bash
cm show cache "download file annotations coco 2017 val"
```
