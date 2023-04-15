**[ [TOC](../README.md) ]**


# CK workflows for the MLPerf inference benchmark


# CK workflows for the MLPerf inference benchmark

MLPerf tasks         | PyTorch | TensorFlow | TVM | ONNX | TFLite | OpenVINO | TensorRT |
--- | --- | --- | --- | --- | --- | --- | --- |
Image classification | [CK &#10003;](tasks/task-image-classification-pytorch.md) | [CK &#10003;](tasks/task-image-classification-tf.md) | [CK &#10003;](tasks/task-image-classification-tvm.md) | [CK &#10003;](tasks/task-image-classification-onnx.md) | [CK &#177;](tasks/task-image-classification-tflite.md) | [CK &#177;](tasks/task-image-classification-openvino.md) |  | 
Object detection     |  |  | [CK &#177;](tasks/task-object-detection-tvm.md) | [CK &#10003;](tasks/task-object-detection-onnx.md) | [CK &#177;](tasks/task-object-detection-tflite.md) |  | [CK &#177;](tasks/task-image-classification-tensorrt.md) | 
Medical imaging      |  |  |  |  |  |  |  | 
Language             |  |  |  | [CK &#10003;](tasks/task-language-onnx.md) |  |  |  | 
Recommendation       |  |  |  |  |  |  |  | 
Speech               | [CK &#177;](tasks/task-speech-pytorch.md) |  |  |  |  |  |  | 




# New MLPerf backends

* [MLPerf with TVM and ONNX](tvm/README.md)

# Unsorted notes

* [Image classification](task-image-classification.md)
* [Object detection](task-object-detection.md)
* [Medical imaging ](task-medical-imaging.md)
* [NLP](task-nlp.md)
* [Recommendation](task-recommendation.md)
* [Speech recognition](task-speech-recognition.md)

* [Notes about datasets](../datasets/README.md)
* [Notes about models (issues, quantization, etc)](../models/notes.md)

* DLRM: [notes](dlrm.md), [CK packages](https://cknow.io/?q=module_uoa%3A%22program%22+AND+dlrm), [CK workflows](https://cknow.io/?q=module_uoa%3A%22program%22+AND+dlrm)
* [Search for CK program workflows with "mlperf"](https://cknow.io/?q=module_uoa%3A%22program%22+AND+mlperf)
* [Search for CK program workflows with "loadgen"](https://cknow.io/?q=module_uoa%3A%22program%22+AND+loadgen)

# Feedback
* Contact: grigori@octoml.ai
