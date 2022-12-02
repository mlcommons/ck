# CUDA version

```bash
cm run script "install python-venv" --name=test
cm run script "python app image-classification pytorch _cuda"
cm run script "python app image-classification pytorch _cuda" --input=src/computer_mouse.jpg
```

## Tested on Windows 10
* ONNX Runtime 1.13.1 with CUDA
* CUDA 11.6
* cuDNN 8.5.0.96
