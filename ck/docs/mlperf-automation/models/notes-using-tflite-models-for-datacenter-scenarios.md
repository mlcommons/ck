**[ [TOC](../README.md) ]**

Crefeda Rodrigues <crefeda.rodrigues@arm.com>

Hi,

I wanted to clarify whether we can use tflite models for datacenter scenarios?
My understanding is that we start from the reference model TF model provided and convert it to TFlite.

Thanks,
Crefeda Rodrigues




As long you start with a reference model and can show how you get to your model you should be ok.

Not sure how well tflite models work for datacenter since many times they
are burned in to batchsize 1 and the interpreper api does not allow
multiple requests into the same session (aka you’d need to fiddle with the
app to load the model multiple times).

Guenther. 




Examples:

* ResNet50: https://github.com/arm-software/armnn-mlperf
* SSD-ResNet34, however, was rather tricky to convert: https://github.com/mlcommons/inference/issues/229
