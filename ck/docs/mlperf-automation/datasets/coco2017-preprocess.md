**[ [TOC](../README.md) ]**

## Install COCO 2017 val dataset (5000 images)

```bash
ck install package --ask --tags=dataset,coco,2017,val,full
```

## Locate installed dataset

```bash
ck locate env --tags=dataset,coco,2017,val,full
```





## Convert COCO to 300x300

```bash
ck install package --tags=dataset,object-detection,preprocessed,full,side.300,using-pillow
```

### Install models compatible with processed COCO 300x300

#### TF SSD Mobilenet-v1 non-quantized

Install the non-quantized model directly
```bash
ck install package --tags=model,tflite,object-detection,ssd-mobilenet,non-quantized
```

Note that opencv provides faster conversion and can give better accuracy than pillow but may fail on some platforms.

## Convert COCO to 1200x1200

```bash
ck install package --tags=dataset,object-detection,preprocessed,full,side.1200
```

You can add flag --ask to select the path where to install this dataset to be able to reuse it later:
```bash
ck install package --tags=dataset,object-detection,preprocessed,full,side.1200 --ask
```
