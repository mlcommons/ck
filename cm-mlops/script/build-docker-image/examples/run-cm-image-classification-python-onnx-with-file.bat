docker run -v %CD%:/tmp/host -it --rm ckrepo/cm-image-classification-python-onnx:ubuntu-22.04 -c "time cm run script --tags=python,app,image-classification,onnx --input=/tmp/host/%1"
