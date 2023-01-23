# Get Preprocessed Criteo Dataset
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) preprocesses the Criteo dataset.

## How To
```bash
cm run script --tags=get,criteo,preprocessed --threads=[NUM_THREADS]
```
where, 
* `[DIRECTORY]:` is the folder to store the preprocessed dataset. Default is current work directory
* `[NUM_THREADS:]` is the number of threads to do preprocessing. Default is number of host cpus. 


## Exported Variables
* `[CM_DATASET_PREPROCESSED_PATH]:` Directory where the preprocessed images are stored


