**[ [Back to TOC](../README.md) ]**

# Shortcuts

- [Install reduced dataset with the first 500 images (for tests)](#install-reduced-imagenet-2012-val-dataset-with-the-first-500-images)
- [Plug in full dataset with 50,000 images](#plug-in-full-imagenet-2012-val-dataset-with-50000-images)
- [Pre-process installed datasets if needed](#preprocess-installed-dataset)

# Notes

ImageNet 2012 validation set is no longer publicly available
and this CK meta-package cannot automatically download it!
If you already have it installed on your machine, you can detect
and register it to work with CK workflows as described further.
However, we prepared a CK package with a reduced Imagenet dataset (500 images)
to let you test CK-MLPerf workflows.


# Install CK

Please follow [this guide](https://github.com/mlcommons/ck#instalation)

# Install CK repos with MLOps components

```bash
ck pull repo:mlcommons@ck-mlops
```

# Install ImageNet 2012 aux package

```bash
ck install package --tags=imagenet,2012,aux,from.berkeley
```

If berkeleyvision website is unavailable, you can use the DropBox substitute as follows:
```bash
ck install package --tags=imagenet,2012,aux,from.dividiti
```

You can locate the place where CK installed this package as follows:
```bash
ck locate env --tags=imagenet,2012,aux
```


# Install reduced ImageNet 2012 val dataset with the first 500 images

If you do not have the full ImageNet val dataset, you can install its reduced version via CK
with the first 500 images just for a test:

```bash
ck install package --tags=imagenet,2012,val,min,non-resized
```

You can locate the place where CK installed this package as follows:
```bash
ck locate env --tags=imagenet,2012,val
```

If you are using MLPerf benchmark scripts without CK workflows, 
you must copy the labels next to the images:
```bash
cp `ck locate env --tags=imagenet,2012,aux`/val.txt `ck locate env --tags=imagenet,2012,val`/val_map.txt
```

*Note that CK workflows will copy labels next to images automatically.*


# Plug in full ImageNet 2012 val dataset with 50000 images

*ImageNet 2012 validation set is no longer publicly available.*
If you already have it installed on your machine, you can detect
and register it to work with CK workflows using this command:

```bash
ck detect soft:dataset.imagenet.val --force_version=2012 \
            --extra_tags=full --search_dir={directory where the dataset is installed}
```

You can download it via [Academic Torrents](https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5)
and then register in the CK using the above command.

# Preprocess installed dataset

If you need a preprocessed dataset or you use CK workflows that require a preprocessed ImageNet, 
the community provided different CK packages to automate ImageNet preprocessing 
as described [here](imagenet2012-preprocess.md).
