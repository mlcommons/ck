# GPU version

```bash
cm run script "python app image-classification onnx _gpu"
cm run script "python app image-classification onnx _gpu" --input=src/computer_mouse.jpg
```

## Tested on Windows 10
* ONNX Runtime 1.13.1 with CUDA
* CUDA 11.6
* cuDNN 8.5.0.96
