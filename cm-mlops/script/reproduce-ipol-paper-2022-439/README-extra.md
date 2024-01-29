# CM-based reproducibility demo for IPOL journal

This is a part of the [open challenge](https://access.cknowledge.org/playground/?action=challenges&name=f284c08891c44058) 
to make it easier to reproduce experimental results from research papers 
using the [MLCommons CM scripting language](https://github.com/mlcommons/ck).

Code and sample images are taken from https://ipolcore.ipol.im/demo/clientApp/demo.html?id=439 .

The demo illustrates the method proposed by Daudt et al. (2019) for change detection on satellite images. It takes as input two color images in PNG format. Both images should be satellites images of the same area, and co-registered.
The output image is a change map. For each pixel in the input images, the value of the change map is 1 if a change is detected and 0 otherwise.

Pair of images from the OSCD test set are already provided with the demo. For those images, 
the ground truth is available in the original dataset: https://ieee-dataport.org/open-access/oscd-onera-satellite-change-detection.

## Authors

* [Jose Hernandez](https://www.linkedin.com/in/jose-hernandez-a261182b)
* [Grigori Fursin](https://cKnowledge.org/gfursin)

## Initial discussion and materials

* https://github.com/mlcommons/ck/issues/617
* http://www.ipol.im/pub/art/2022/439/
* https://access.cknowledge.org/playground/?action=challenges&name=reproduce-and-automate-ipol-paper

## Implementation

We implemented 2 CM scripts for this challenge:

* [Download IPOL paper sources and cache them in CM](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ipol-src)
* [Run IPOL 2022 439 paper demo using above script and PyTorch](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-ipol-paper-2022-439)

## Reproducibility

CM scripts are implemented for a demo on Ubuntu and must be tested across different systems:

1. Install MLCommons CM(CK2) automation framework as described [here](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

2. Install MLCommons repository with CM automation scripts:

```bash
cm pull repo mlcommons@ck
```

3. Install src from IPOL 2022 439 paper:
```bash
cm run script "get ipol src" --year=2022 --number=439

cm show cache --tags=ipol,src
```

4. Download sample images and run demo (CM will detect or install missing dependencies)
```bash
cm run script "download file _wget" --url=https://cKnowledge.org/ai/data/ipol-paper-2024-439-sample-image-1.png --verify=no --env.CM_DOWNLOAD_CHECKSUM=850639287ad23194576582680c2ecfc3
cm run script "download file _wget" --url=https://cKnowledge.org/ai/data/ipol-paper-2024-439-sample-image-2.png --verify=no --env.CM_DOWNLOAD_CHECKSUM=31364c03d91873ed2d244cce6d664dd0
cm run script "reproduce ipol 2022-439"
cm run script "reproduce ipol 2022-439" --adr.torch.version=1.13.1 --adr.torchvision.version=0.14.1
```

This script will use 2 sample images from this paper
and should produce *diff.png* in the current directory.

## Usage with different images

You can use other 2 images by specifying their full path as follows:
```bash
cm run script "reproduce ipol 2022-439" \
       --image1={full path to png image 1} \
       --image2={full path to png image 2}
```

## Collaborative development

Join the public [MLCommons Task Force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
to participate in further collaborative developments.
