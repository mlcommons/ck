## Run Commands

### Default tflite
```
cm run script --tags=run,mobilenet-models,_find-performance
```
```
cm run script --tags=run,mobilenet-models,_submission
```

### Using ARMNN
```
cm run script --tags=run,mobilenet-models,_armnn,_find-performance
```
```
cm run script --tags=run,mobilenet-models,_armnn,_submission
```
### Using ARMNN with NEON
```
cm run script --tags=run,mobilenet-models,_armnn,_neon,_find-performance
```
```
cm run script --tags=run,mobilenet-models,_armnn,_neon,_submission
```

### Using ARMNN with OpenCL
```
cm run script --tags=run,mobilenet-models,_armnn,_opencl,_find-performance
```
```
cm run script --tags=run,mobilenet-models,_armnn,_opencl,_submission
```
