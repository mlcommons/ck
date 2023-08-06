docker run -v $PWD:/tmp/host -it --rm cknowledge/cm-image-classification-onnx:ubuntu-23.04-20230806 -c "time cmr 'python app image-classification onnx' --adr.python.name=cm --input=/tmp/host/$1"
