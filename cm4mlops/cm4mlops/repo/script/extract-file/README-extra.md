# CM interface to extract files in a unified way on any system

## Extract files without CM caching

You can use this script to extract `.tar`, `.gz`, `.zip`, `.bz2`, `.tag.gz` and `.tgz` files.

Before using further examples, you can download `coco-2017-val-annotations.zip` using CM:
```bash
cmr "download file" --url=https://cKnowledge.org/test/coco-2017-val-annotations.zip
```

Extract this archive in the current path while keeping the archive file:

```bash
cmr "extract file _keep" --input=coco-2017-val-annotations.zip
```

or

```bash
cmr "extract file _keep _path.coco-2017-val-annotations.zip"
```

You can remove `_keep` to delete archive after extracting files:

```bash
cmr "extract file" --input=coco-2017-val-annotations.zip
```

#### Output environment variables

You can check produced environment variables produced by this CM script by adding the `-j` flag:

```bash
cmr "extract file _keep" --input=coco-2017-val-annotations.zip -j
```

```json
  "new_env": {
    "CM_EXTRACT_EXTRACTED_PATH": "D:\\Work99.3 readme\\xyz",
    "CM_GET_DEPENDENT_CACHED_PATH": "D:\\Work99.3 readme\\xyz"
  },
```

#### Input flags and equivalent environment variables

* `--input` or `--env.CM_EXTRACT_FILEPATH` - input file
* `--extract_path` or `--to` or `--env.CM_EXTRACT_PATH` - where to extract files (--input should have full path then)
* `--extra_folder` or `--env.CM_EXTRACT_TO_FOLDER` - extra directory when extracting file (to avoid messing up current directory)

#### Variations

* `_keep` or `_no-remove-extracted` or `--env.CM_EXTRACT_REMOVE_EXTRACTED=no` - keep archive file (it will be deleted by default)



### Extract to a specific folder

Note that you need to provide a full path to the archive file if you want to extract it to some directory:

```bash
cmr "extract file _keep" --input="$PWD/coco-2017-val-annotations.zip" --extract_path="$HOME/cm-test"
```

### Add extra folder to extracted files

You can add extra folder when extracting files to avoid messing up current directory:

```bash
cmr "extract file _keep" --input=coco-2017-val-annotations.zip --extra_folder=xyz
```




## Extract 1 file and test MD5SUM without CM caching

You can use this script to extract 1 archived file (model, captions, etc) and test MD5SUM.

To test this CM script, download `captions_val2017.json.gz`:
```bash
cmr "download file _url.https://cKnowledge.org/test/captions_val2017.json.gz"
```

Then extract it and test MD5SUM as follows:

```bash
cmr "extract file _keep _path.captions_val2017.json.gz" --env.CM_EXTRACT_EXTRACTED_CHECKSUM=b7bec29ab7bd8971ae4cafc2390a658f -j
```


### Force another filename during extract

Some workflows may need to use a different filename than original. You can change it as follows:
```bash
cmr "extract file _keep _path.captions_val2017.json.gz" --env.CM_EXTRACT_EXTRACTED_FILENAME=new-file.json --env.CM_EXTRACT_EXTRACTED_CHECKSUM=b7bec29ab7bd8971ae4cafc2390a658f
```




## Extract file(s) to CM cache

You can use all above commands with `--force_cache` and `--extra_cache_tags` flags.
In such case, file(s) will be extracted to the CM cache and can be reused by other CM scripts and workflows.
Note that you need to provide full path to the archive file.

```bash
cmr "extract file _keep" --input=$HOME/coco-2017-val-annotations.zip --force_cache --extra_cache_tags=coco,2017,val,annotations
```

You can find it in CM cache using extra cache tags as follows:
```bash
cm show cache "extract file annotations coco 2017 val"
```
