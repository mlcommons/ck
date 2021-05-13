# MLCube project

* GitHub: https://github.com/mlcommons/mlcube

## Notes 
* [Single Stage Detection with MLCube(tm)](https://github.com/mlcommons/training/pull/465)
   
### Download SSD dataset (~20 GB, ~40 GB space required)
```
mlcube run --task download_data --platform docker
```

### Download ResNet34 feature extractor
```
mlcube run --task download_model --platform docker
```

### Run benchmark
```
mlcube run --task train --platform docker
```

