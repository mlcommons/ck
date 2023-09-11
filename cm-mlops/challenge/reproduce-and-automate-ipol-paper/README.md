### Challenge

Reproduce and automate IPOL paper (proof-of-concept): 

#### Organizers

* Jose Hernandez
* Miguel Colom
* Grigori Fursin
* [cTuning foundation](https://cTuning.org)
* [cKnowledge Ltd](https://cKnowledge.org)

### Initial discussion and materials

* https://github.com/mlcommons/ck/issues/617
* http://www.ipol.im/pub/art/2022/439/
* https://access.cknowledge.org/playground/?action=challenges&name=reproduce-and-automate-ipol-paper

### Status

Grigori implemented 2 CM scripts for this challenge:

* [Download IPOL paper sources and cache them in CM](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ipol-src)
* [Run IPOL 2022 439 paper demo using above script and PyTorch](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-ipol-paper-2022-439)

### Validation 

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

4. Run demo (CM will detect or install missing dependencies)
```bash
cm run script "reproduce ipol 2022-439"
```

This script will use these [sample images](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-ipol-reproducibility-2022-439/sample-images)
and should produce *diff.png* in the current directory.

You can use other 2 images by specifying their full path as follows:
```bash
cm run script "reproduce ipol 2022-439" \
       --image1={full path to png image 1} \
       --image2={full path to png image 2}
```

