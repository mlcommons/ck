Examples:

### Check flags

```bash
cm run script --tags=get,raw,dataset,mlcommons-cognata --help
```

### Import already downloaded dataset

Note that this automation will attempt to install aria2 tool via sudo apt on Ubuntu.

```bash
cm run script --tags=get,raw,dataset,mlcommons-cognata --import=${HOME}/datasets/cognata -j
cm run script --tags=get,raw,dataset,mlcommons-cognata --import=${HOME}/datasets/cognata -j --private_url="{ADD PRIVATE URL FOR COGNATA} FOR FULL AUTOMATION"
cm run script --tags=get,raw,dataset,mlcommons-cognata --import=%userprofile%\datasets\cognata -j
cm run script --tags=get,raw,dataset,mlcommons-cognata --import=D:\Work2\cognata -j
```

### Download dataset to CM cache

```bash
cm run script --tags=get,raw,dataset,mlcommons-cognata
```

### Find dataset in CM cache

```bash
cm show cache --tags=dataset,mlcommons-cognata

cm rm cache --tags=dataset,mlcommons-cognata
```

### Download dataset to some local directory

```bash
cm run script --tags=get,raw,dataset,mlcommons-cognata --path=${HOME}/datasets/cognata -j
cm run script --tags=get,raw,dataset,mlcommons-cognata --path=%userprofile%\datasets\cognata -j
cm run script --tags=get,raw,dataset,mlcommons-cognata --path=D:\Work2\cognata-downloaded -j

```

### Download subsets of this dataset

```bash
cm run script --tags=get,raw,dataset,mlcommons-cognata --serial_numbers=10002_Urban_Clear_Morning
cm run script --tags=get,raw,dataset,mlcommons-cognata --serial_numbers=10002_Urban_Clear_Morning --group_names=Cognata_Camera_01_8M
cm run script --tags=get,raw,dataset,mlcommons-cognata --serial_numbers=10002_Urban_Clear_Morning --group_names=Cognata_Camera_01_8M --file_names=Cognata_Camera_01_8M_ann.zip;Cognata_Camera_01_8M_ann_laneline.zip;Cognata_Camera_01_8M.zip
cm run script --tags=get,raw,dataset,mlcommons-cognata --serial_numbers=10002_Urban_Clear_Morning --group_names=Cognata_Camera_01_8M --file_names=Cognata_Camera_01_8M_ann.zip;Cognata_Camera_01_8M_ann_laneline.zip;Cognata_Camera_01_8M.zip
```

Compact way to download the ABTF demo data set to the CM cache:

```bash
cm run script --tags=get,raw,dataset,mlcommons-cognata,_abtf-demo
```

or to specific path
```bash
cm run script --tags=get,raw,dataset,mlcommons-cognata _abtf-demo" --path=./cognata
cm run script --tags=get,raw,dataset,mlcommons-cognata _abtf-demo" --path=.\cognata
```
