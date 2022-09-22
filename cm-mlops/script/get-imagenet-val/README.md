# Portable CM script

Detecting and registering ImageNet validation datasets.

## Supported platforms

* Linux, MacOS
* Windows (only 500 images)

## Supported versions and variations

### 2012, 500 images

Use the following CM command to automatically download and register a reduced ImageNet with 500 images:
```bash
cm run script "get imagenet original _2012-500"
```

Alternative CMD:
```bash
cm run script --tags=get,imagenet,original,_2012-500
```

Check that it is correctly registered in CM:
```bash
cm show cache --tags=dataset,imagenet
```

### 2012, 50000 images (full set)

Note that ImageNet 2012 validation set is no longer available for download.

However, you can still download it via Academic Torrents 
[here](https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5)
and register in the CM using the following command:

```bash
cm run script "get imagenet original _2012-full" \
     --env.IMAGENET_PATH={PATH to a directory with ILSVRC2012_val_00000001.JPEG} 
```

For example, 
```bash
cm run script "get imagenet original _2012-full" --env.IMAGENET_PATH=/mnt/extra-disk/imagenet-2012-val
```

## Examples

After CM cached the dataset, you can get the environment with the paths to your IMAGENET and extra meta information as follows:
```bash
cm run script "get imagenet original _2012-full" --out=json
```

See this [CM workflow](https://github.com/mlcommons/ck/blob/master/cm/docs/example-modular-image-classification.md) to classify images.

