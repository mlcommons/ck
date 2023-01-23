**[ [Back to TOC](../README.md) ]**

# Shortcuts

- [Plug in downloaded BraTS 2019](#plug-in-downloaded-brats-2019)

# Notes

[BraTS 2019 dataset](https://www.med.upenn.edu/cbica/brats-2019/)
is not publicly available without registration
and this CK meta-package cannot automatically download it!
If you already have it installed on your machine, you can detect
and register it to work with CK workflows as described further.

The size of the dataset is about 2.8 GB and it is
separated into 5 folds for cross-validation. The MLPerf workflow uses
[fold 1](https://github.com/mlcommons/inference/blob/master/vision/medical_imaging/3d-unet-brats19/folds/fold1_validation.txt).


# Install CK

Please follow [this guide](https://github.com/ctuning/ck#instalation)

# Install CK repos with MLOps components

```bash
ck pull repo:mlcommons@ck-mlops
```

# Plug in downloaded BraTS 2019

*BraTS 2019 dataset is not publicly available.*
If you already have it installed on your machine, you can detect
and register it to work with CK workflows using this command:

```bash
ck detect soft:dataset.brats.2019.train --force_version=2019 \
            --extra_tags=full --search_dir={/path/to/MICCAI_BraTS_2019_Data_Training/}
```

You can download it via [Academic Torrents](https://academictorrents.com/details/82cef583fa17480b0f9a6342591d01dc67abe055)
and then register in the CK using the above command.
