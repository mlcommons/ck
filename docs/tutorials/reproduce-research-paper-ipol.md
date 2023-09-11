[ [Back to index](../README.md) ]

# Tutorial: Reproduce research paper (IPOL'22 example)

This tutorial was prepared during a [public Collective Knowledge challenge](https://access.cknowledge.org/playground/?action=challenges&name=f284c08891c44058)
to reproduce results from the [IPOL'22 439 journal article](http://www.ipol.im/pub/art/2022/439) using the MLCommons CM automation language.

*Please check the [CM introduction](../introduction-cm.md) to understand CM motivation and concepts.*


## Organizers

* Jose Hernandez
* Miguel Colom
* [Grigori Fursin](https://cKnowledge.org/gfursin)
* [cTuning foundation](https://cTuning.org)
* [cKnowledge Ltd](https://cKnowledge.org)

## Initial discussion and materials

* https://github.com/mlcommons/ck/issues/617
* https://access.cknowledge.org/playground/?action=challenges&name=reproduce-and-automate-ipol-paper

## Implementation

We have implemented two portable CM scripts to automate reproducibility on any platform:

* [Download IPOL paper sources and cache them in CM](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ipol-src)
* [Run IPOL 2022 439 paper demo using above script and PyTorch](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-ipol-paper-2022-439)

## Reproducibility study 

1. Install MLCommons CM(CK2) automation framework as described [here](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

2. Install the latest MLCommons repository with reusable CM scripts:

```bash
cm pull repo mlcommons@ck
```

3. Install author sources from IPOL 2022 439 paper using CM:

```bash
cm run script "get ipol src" --year=2022 --number=439

cm show cache --tags=ipol,src
```

4. Run script to install dependencies and reproduce results
```bash
cm run script "reproduce ipol 2022-439"
```

This script will use these [sample images](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-ipol-reproducibility-2022-439/sample-images)
and should produce a *diff.png* file in the current directory.

## Using other data

You can use any other 2 images by specifying their full path as follows:
```bash
cm run script "reproduce ipol 2022-439" \
       --image1={full path to png image 1} \
       --image2={full path to png image 2}
```
