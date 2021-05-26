**[ [TOC](../README.md) ]**

ImageNet 2012 validation set is no longer publicly available
and this CK meta-package cannot automatically download it!

If you already have it installed on your machine, you can detect
and register it to work with CK workflows as described further.

However, we prepared a CK package with a reduced Imagenet dataset (500 images)
to let you test CK-MLPerf workflows.


Select ImageNet 2012 variation:
* [Reduced dataset with the first 500 images (for tests)](#install-reduced-imagenet-2012-val-dataset-with-the-first-500-images)
* [Full dataset with 50,000 images](#install-detect-full-imagenet-2012-val-dataset-with-50000-images)


# Install CK with ML repository

```bash
python3 -m pip install ck
ck pull repo:octoml@mlops
```

# Install reduced ImageNet 2012 val dataset with the first 500 images

If you do not have the full ImageNet val dataset, you can install its reduced version via CK
with the first 500 images just for a test:

```
ck install package --tags=imagenet,2012,val,min,non-resized
ck install package --tags=imagenet,2012,aux,from.berkeley
```

## Prepare CK for ImageNet preprocessing

### Set up CK environment

```
ck detect platform.os --platform_init_uoa=generic-linux-dummy
ck detect soft:compiler.python
ck detect soft:compiler.gcc --full_path=`which gcc`
```

### Install common CK packages

You will need cmake to build MLPerf&trade; loadgen. First, attempt to detect if you already have it installed:
```
ck detect soft --tags=tool,cmake
```

Note that you need version >= 3.16

CK will register your version if it manages to detect it:
```
ck show env

Env UID:         Target OS: Bits: Name: Version: Tags:

2aa2c857e2be84a4   linux-64    64 cmake 3.16.3   64bits,cmake,host-os-linux-64,target-os-linux-64,tool,v3,v3.16,v3.16.3
`````

If you do not have cmake installed or CK did not manage to detect it, you can use a CK package to build it for your system:
```
ck install package --tags=tool,cmake,src
```

### Install Python dependencies via CK

You can now install other dependencies via CK:

```
ck install package --tags=lib,python-package,absl
ck install package --tags=lib,python-package,numpy
ck install package --tags=lib,python-package,cython
ck install package --tags=lib,python-package,pillow
ck install package --tags=lib,python-package,opencv-python-headless
```

### Preprocess using OpenCV (better accuracy but may fail on some machines)

```
time ck install package --dep_add_tags.dataset-source=min \
          --tags=dataset,imagenet,val,full,preprocessed,using-opencv,side.224 \
          --version=2012
```

### Preprocess using Pillow (slightly worse accuracy but works most of the time)

```
time ck install package --dep_add_tags.dataset-source=min \
          --tags=dataset,imagenet,val,full,preprocessed,using-pillow,side.224 \
          --version=2012
```


# Install (detect) full ImageNet 2012 val dataset with 50000 images

ImageNet 2012 validation set is no longer publicly available.
If you already have it installed on your machine, you can detect
and register it to work with CK workflows using this command:

```
ck detect soft:dataset.imagenet.val --force_version=2012 \
            --extra_tags=full --search_dir={directory where the dataset is installed}
```

You can download it via [Academic Torrents](https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5)
and then register in the CK using the above command.


## Preprocess using OpenCV (better accuracy but may fail on some machines)

```
time ck install package --dep_add_tags.dataset-source=full \
          --tags=dataset,imagenet,val,full,preprocessed,using-opencv,side.224 \
          --version=2012
```

Processing time: ~30 min.

## Preprocessing using pillow (slightly worse accuracy but works most of the time)

```
time ck install package --dep_add_tags.dataset-source=full \
          --tags=dataset,imagenet,val,full,preprocessed,using-pillow,side.224 \
          --version=2012
```

Processing time: ~26 min.


## Preprocess ImageNet for other models with different resolutions

* [CK-ML repo docs](https://github.com/ctuning/ck-ml/blob/main/program/image-classification-tflite-loadgen/README.md)
