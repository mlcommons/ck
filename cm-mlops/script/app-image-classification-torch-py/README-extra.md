# CPU

## 20240129; Windows 11

```bash
cmr "get generic-python-lib _package.torch" --version=2.1.1
cmr "get generic-python-lib _package.torchvision" --version=0.16.2
```

# CUDA

```bash
cm run script "install python-venv" --name=test
cm run script "python app image-classification pytorch _cuda" --adr.python.name=test
cm run script "python app image-classification pytorch _cuda" --adr.python.name=test --input=src/computer_mouse.jpg
```
