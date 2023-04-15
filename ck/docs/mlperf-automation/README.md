<br>
<br>
<br>

**Note, that this CK-MLPerf documentation is discontinued after the [open MLCommons taskforce](../../../docs/taskforce.md)
  has released the [2nd generaton of the CK framework (CK2 or CM)](https://github.com/mlcommons/ck/tree/master/cm)
  to decompose MLPerf benchmark into a [database of reusable, portable, customizable and deterministic scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) 
  with a unified CLI, Python API and extensible JSON/YAML meta descriptions.**

<br>
<br>
<br>

# MLPerf&trade; inference benchmark automation

This is a community project to make it easier to customize, run and reproduce MLPerf&trade; inference benchmarks 
across continuously changing ML models, frameworks, libraries, compilers, data sets and platform.
We are also developing an open database for benchmarking results and provenance information 
compatible with [FAIR principles](https://www.go-fair.org/fair-principles).

As a starting point, we will use the open-source and technology-neutral [MLCommons CK framework](https://github.com/mlcommons/ck) 
with a [collection](https://github.com/mlcommons/ck-mlops) of [reusable automation recipes](https://github.com/mlcommons/ck-mlops/tree/main/program), 
[plug&play packages](https://github.com/mlcommons/ck-mlops/tree/main/package) and 
[adaptive containers](https://github.com/mlcommons/ck-mlops/tree/main/docker) 
with a common API for ML systems. CK framework was already successfully used by several MLCommons members 
to automate their MLPerf inference submissions and we want to build upon their experience. 




We reuse a relatively mature methodology to reproduce research results from ML and Systems papers ([ACM TechTalk](https://youtu.be/7zpeIVwICa4) and [Artifact Evaluation](https://cTuning.org/ae))
and open-source tools from the MLCommons&trade; including [MLCube&trade;](https://github.com/mlcommons/mlcube).

# News


* 202208: We've pre-released a set of reusable, portable, customizable and deterministic scripts for MLOps and DevOps:
   [GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script).
* 202205: We've started prototyping the new [CK2 toolkit](https://github.com/mlcommons/ck/tree/master/cm) 
   based on your feedback and combined with our practical experience 
   [reproducing 150+ ML and Systems papers and validating them in the real world](https://www.youtube.com/watch?v=7zpeIVwICa4).
   Please [get in touch](https://github.com/mlcommons/ck/tree/master/cm#contacts) for more details.
* 20210914: [Reproducibility studies for the MLPerf inference benchmark](reproduce/README.md)
* 20210911: cTuning foundation and OctoML donated the CK framework and workflows to MLCommons:
  * https://github.com/mlcommons/ck
  * https://github.com/mlcommons/ck-venv
  * https://github.com/mlcommons/ck-mlops

# Standardization of the CK components for MLPerf

We are gradually converting all CK [packages](https://github.com/mlcommons/ck-mlops/tree/main/package),
[benchmark workflows](https://github.com/mlcommons/ck-mlops/tree/main/programs), 
[automation scripts](https://github.com/mlcommons/ck-mlops/tree/main/scripts) and 
[Docker containers](https://github.com/mlcommons/ck-mlops/tree/main/docker)
for diverse ML tasks, models, datasets and frameworks from the community to support
the new [MLPerf inference submission workflow](https://github.com/mlcommons/ck-mlops/tree/main/module/bench.mlperf.inference).

## CK workflows for the MLPerf inference benchmark


&#10003; - supports the new [MLPerf inference submission workflow](https://github.com/mlcommons/ck-mlops/tree/main/module/bench.mlperf.inference)<br>
&#177; - works fine but uses old format


MLPerf tasks         | PyTorch | TensorFlow | TVM | ONNX | TFLite | OpenVINO | TensorRT |
--- | --- | --- | --- | --- | --- | --- | --- |
Image classification | [CK &#10003;](tasks/task-image-classification-pytorch.md) | [CK &#10003;](tasks/task-image-classification-tf.md) | [CK &#10003;](tasks/task-image-classification-tvm.md) | [CK &#10003;](tasks/task-image-classification-onnx.md) | [CK &#177;](tasks/task-image-classification-tflite.md) | [CK &#177;](tasks/task-image-classification-openvino.md) |  | 
Object detection     |  |  | [CK &#177;](tasks/task-object-detection-tvm.md) | [CK &#10003;](tasks/task-object-detection-onnx.md) | [CK &#177;](tasks/task-object-detection-tflite.md) |  | [CK &#177;](tasks/task-image-classification-tensorrt.md) | 
Medical imaging      | [CK &#10003;](tasks/task-medical-imaging-pytorch.md) |  |  | [CK &#10003;](tasks/task-medical-imaging-onnx.md) |  |  |  | 
Language             |  |  |  | [CK &#10003;](tasks/task-language-onnx.md) |  |  |  | 
Recommendation       |  |  |  |  |  |  |  | 
Speech               | [CK &#177;](tasks/task-speech-pytorch.md) |  |  |  |  |  |  | 

## CK packages with MLPerf datasets

* Object detection: [COCO 2017](datasets/coco2017.md)
* Image classification: [ImageNet 2012](datasets/imagenet2012.md)
* Language: [SQuAD](datasets/squad.md)
* Speech: [LibriSpeech](datasets/librispeech.md)

See other CK packages with open source datasets shared by the community 
(to be standardized and connected with the new submission system):
[View](https://cknow.io/?q=%22package%3Adataset-*%22)

## CK packages with ML models used for MLPerf submissions

* ResNet50: [ONNX](https://github.com/mlcommons/ck-mlops/tree/main/package/ml-model-mlperf-resnet50-onnx) [PyTorch](https://github.com/mlcommons/ck-mlops/tree/main/package/ml-model-mlperf-resnet50-pytorch) [TensorFlow](https://github.com/mlcommons/ck-mlops/tree/master/package/ml-model-mlperf-resnet50-tf) [TFLite](https://github.com/mlcommons/ck-mlops/tree/main/package/model-tflite-mlperf-resnet/.cm/meta.json)
* EfficientNet (quantized/non-quantized): [TensorFlow and TFLite](https://github.com/mlcommons/ck-mlops/tree/main/package/model-tflite-mlperf-efficientnet-lite/.cm/meta.json)
* MobileNet-v3 (quantized/non-quantized): [TensorFlow and TFLite](https://github.com/mlcommons/ck-mlops/tree/main/package/model-tf-and-tflite-mlperf-mobilenet-v3/.cm/meta.json)
* MobileNet-v2 (quantized): [TensorFlow and TFLite](https://github.com/mlcommons/ck-mlops/tree/main/package/model-tf-and-tflite-mlperf-mobilenet-v2-quant/.cm/meta.json)
* MobileNet-v2 (non-quantized): [TensorFlow and TFLite](https://github.com/mlcommons/ck-mlops/tree/main/package/model-tf-and-tflite-mlperf-mobilenet-v2/.cm/meta.json)
* MobileNet-v1 (quantized/non-quantized): [TensorFlow and TFLite](https://github.com/mlcommons/ck-mlops/tree/main/package/model-tf-and-tflite-mlperf-mobilenet-v1-20180802/.cm/meta.json)
* SSD MobileNet 300: [ONNX](https://github.com/mlcommons/ck-mlops/tree/main/package/ml-model-mlperf-ssd-mobilenet-300-onnx)
* SSD ResNet34 1200: [ONNX](https://github.com/mlcommons/ck-mlops/tree/main/package/ml-model-mlperf-ssd-resnet34-1200-onnx)
* BERT Large: [ONNX](https://github.com/mlcommons/ck-mlops/tree/main/package/ml-model-mlperf-bert-large-squad-onnx) 

## Customizable dashboards

* [All aggregated MLPerf inference benchmark results](https://cknow.io/?q=%22mlperf-inference-all%22)

# Table of contents

* [Prepare your platform](platform/README.md)
* [Install CK framework](tools/ck.md)
  * [Install CK virtual environment (optional)](tools/ck-venv.md)
  * [Use adaptive CK container](tools/ck-docker.md)
* [**Prepare and run reference MLPerf&trade; inference benchmark**](tasks/README.md)
  * [Customize MLPerf&trade; inference benchmark](tasks-custom/README.md)
* [Submit to MLPerf&trade; inference](submit/README.md)
* [Integrate CK workflows with CI platforms](tools/continuous-integration.md)
* [Analyze MLPerf inference results](results/README.md)
  * [Example of CK dashboards for ML Systems DSE](results/ck-dashboard.md)
* [**Reproduce MLPerf&trade; results**](reproduce/README.md)
* [Use CK with MLCube&trade;](tools/mlcube.md)
* [Test models with a webcam](reproduce/demo-webcam-object-detection-x86-64.md)
* [Explore ML Systems designs (AutoDSE)](dse/README.md)
* [Related tools](tools/README.md)


# Examples

* [MLPerf&trade; object detection workflow](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/tasks/task-object-detection.md)
* [Docker image for MLPerf&trade; with OpenVINO]( https://github.com/mlcommons/ck-mlops/tree/main/docker/mlperf-inference-v0.7.openvino)
* [Jupyter notebook for ML DSE](https://nbviewer.jupyter.org/urls/dl.dropbox.com/s/f28u9epifr0nn09/ck-dse-demo-object-detection.ipynb)
* [Webcam test of the MLPerf object detection model with TFLite](https://cknow.io/solution/demo-obj-detection-coco-tf-cpu-webcam-linux-azure#test)
* [Public scoreboard with MLPerf DSE](https://cknow.io/result/crowd-benchmarking-mlperf-inference-classification-mobilenets-all)


# Further improvements

* [Common workflow for MLPerf inference (prototype available)](inference/workflow.md)
* [Test and update CK automation recipes for MLOps](components/README.md)
* [Docker containers to run MLPerf inference out of the box](inference/containers.md)
* [MLPerf tutorials](tutorials/README.md)
* [Unifying CK components for ML Systems](components/README.md)
* [Ideas to make it easier to use MLPerf&trade; inference benchmarks](https://docs.google.com/document/d/1xUI4_ArXssMUigsSHTAE2lL7jRZE12XXvzoV3QMoT84)
* Add MLPerf&trade; power measurements to our automated benchmark toolset
* [Standardization of MLPerf&trade; workflows](tbd/standardization.md)
* [More automation](tbd/automation.md)


# Contributions

Feel free to contribute to this collaborative doc by sending your PR [here]( https://github.com/mlcommons/ck/pulls )
or creating tickets at [github.com/mlcommons/inference](https://github.com/mlcommons/inference) 
and [github.com/mlcommons/ck](https://github.com/mlcommons/ck). 
Thank you!


# Support

* [MLCommons](https://mlcommons.org)
* [OctoML.ai](https://octoml.ai)
* [cTuning foundation](https://cTuning.org)
* [ACM](https://acm.org)


# Coordinators

* [Grigori Fursin](https://cKnowledge.org/gfursin)
