# MLPerf&trade; inference benchmark automation

This is an *on-going community effort* to introduce portable workflows to make it easier to customize, run and reproduce 
MLPerf&trade; inference benchmarks across continuously changing ML models, frameworks, libraries, compilers, data sets and platform.
We also want to develop an open database for benchmarking results and provenance information 
compatible with [FAIR principles](https://www.go-fair.org/fair-principles).

As a starting point, we will use the open-source and technology-neutral [CK framework](https://github.com/ctuning/ck) 
with a [collection](https://github.com/ctuning/ck-mlops) of [reusable automation recipes](https://github.com/ctuning/ck-mlops/tree/main/program), 
[plug&play packages](https://github.com/ctuning/ck-mlops/tree/main/package) and adaptive containers with a common API
([cTuning](https://github.com/ctuning/ck-mlops/tree/main/docker) 
and [OctoML](https://github.com/octoml/mlops/tree/main/docker))
for ML systems. CK framework was already successfully used by several MLCommons members 
to automate their MLPerf inference submissions and we want to build upon their experience. 

We reuse a relatively mature ACM methodology to reproduce research results ([ACM TechTalk](https://youtu.be/7zpeIVwICa4) and [Artifact Evaluation](https://cTuning.org/ae))
and open-source tools from the MLCommons&trade; Best Practices WorkGroup ([MLCube&trade;](https://github.com/mlcommons/mlcube)).

# Standardized CK components for MLPerf

We are working with MLCommons and OctoML to gradually convert all [CK packages](https://github.com/ctuning/ck-mlops/tree/main/package)
[benchmark workflows](https://github.com/ctuning/ck-mlops/tree/main/programs), 
[automation scripts](https://github.com/ctuning/ck-mlops/tree/main/scripts) and 
[Docker containers](https://github.com/ctuning/ck-mlops/tree/main/docker)
for diverse ML tasks, models, datasets and frameworks from the community to support
our new [MLPerf inference submission workflow](https://github.com/octoml/mlops/tree/main/module/bench.mlperf.inference).

## CK workflows for the MLPerf inference benchmark

MLPerf tasks         | PyTorch | TensorFlow | TVM | ONNX | TFLite | OpenVINO | TensorRT |
--- | --- | --- | --- | --- | --- | --- | --- |
Image classification | [CK &#10003;](tasks/task-image-classification-pytorch.md) | [CK &#10003;](tasks/task-image-classification-tf.md) | [CK &#10003;](tasks/task-image-classification-tvm.md) | [CK &#10003;](tasks/task-image-classification-onnx.md) | [CK &#177;](tasks/task-image-classification-tflite.md) | [CK &#177;](tasks/task-image-classification-openvino.md) |  | 
Object detection     |  |  | [CK &#177;](tasks/task-object-detection-tvm.md) | [CK &#10003;](tasks/task-object-detection-onnx.md) | [CK &#177;](tasks/task-object-detection-tflite.md) |  |  | 
Medical imaging      |  |  |  |  |  |  |  | 
Language             |  |  |  | [CK &#177;](tasks/task-language-onnx.md) |  |  |  | 
Recommendation       |  |  |  |  |  |  |  | 
Speech recognition   |  |  |  |  |  |  |  | 

## CK packages with MLPerf datasets

* [COCO 2017](datasets/coco2017.md)
* [ImageNet 2012](datasets/imagenet2012.md)
* [SQuAD](datasets/squad.md)

## CK packages with the reference MLPerf models

* ResNet50: [ONNX](https://github.com/octoml/mlops/tree/main/package/ml-model-mlperf-resnet50-onnx) [PyTorch](https://github.com/octoml/mlops/tree/main/package/ml-model-mlperf-resnet50-pytorch) [TensorFlow](https://github.com/octoml/mlops/tree/master/package/ml-model-mlperf-resnet50-tf)
* SSD MobileNet 300: [ONNX](https://github.com/octoml/mlops/tree/main/package/ml-model-mlperf-ssd-mobilenet-300-onnx)
* SSD ResNet34 1200: [ONNX](https://github.com/octoml/mlops/tree/main/package/ml-model-mlperf-ssd-resnet34-1200-onnx)
* BERT Large: [ONNX](https://github.com/octoml/mlops/tree/main/package/ml-model-mlperf-bert-large-squad-onnx) 

# News and updates

* **20210808**: Make sure that your CK version >= 2.5.8 with many enhancements for MLPerf (```ck version```). 
  You can update it via (```python3 -m pip install ck -U```).

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

* [MLPerf&trade; object detection workflow](https://github.com/ctuning/ck/blob/master/docs/mlperf-automation/tasks/task-object-detection.md)
* [Docker image for MLPerf&trade; with OpenVINO]( https://github.com/ctuning/ck-mlops/tree/main/docker/mlperf-inference-v0.7.openvino)
* [Jupyter notebook for ML DSE](https://nbviewer.jupyter.org/urls/dl.dropbox.com/s/f28u9epifr0nn09/ck-dse-demo-object-detection.ipynb)
* [Webcam test of the MLPerf object detection model with TFLite](https://cknowledge.io/solution/demo-obj-detection-coco-tf-cpu-webcam-linux-azure#test)
* [Public scoreboard with MLPerf DSE](https://cknowledge.io/result/crowd-benchmarking-mlperf-inference-classification-mobilenets-all)


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
* [Redesigning CK (CKLite)](tbd/ck2.md)


# Contributions

Feel free to contribute to this collaborative doc by sending your PR [here]( https://github.com/ctuning/ck/pulls )
or creating tickets at [github.com/mlcommons/inference](https://github.com/mlcommons/inference) 
and [github.com/ctuning/ck](https://github.com/ctuning/ck). 
Thank you!


# Support

* [MLCommons](https://mlcommons.org)
* [OctoML.ai](https://octoml.ai)
* [cTuning foundation](https://cTuning.org)
* [ACM](https://acm.org)


# Coordinators

* [Grigori Fursin](https://cKnowledge.io/@gfursin)
