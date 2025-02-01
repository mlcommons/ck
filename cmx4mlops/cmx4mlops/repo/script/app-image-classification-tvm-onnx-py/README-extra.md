Example:

```bash
cm run script "get llvm" --version=14.0.0
cm run script "get tvm _llvm" --version=0.10.0
cm run script "python app image-classification tvm-onnx"
```

Example 2:

```bash
cm run script "install python-venv" --name=test --version=3.10.7
cm run script "get generic-python-lib _apache-tvm"
cm run script "python app image-classification tvm-onnx _tvm-pip-install"
cm run script "python app image-classification tvm-onnx _tvm-pip-install" --input=`cm find script --tags=python,app,image-classification,tvm-onnx`/img/computer_mouse.jpg
```