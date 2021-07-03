# MLPerf&trade; inference benchmark automation

This is an *on-going community effort* to introduce portable workflows to make it easier to customize, run and reproduce 
MLPerf&trade; inference benchmarks across continuously changing ML models, frameworks, libraries, compilers, data sets and platform.
We also want to develop an open database for benchmarking results and provenance information 
compatible with [FAIR principles](https://www.go-fair.org/fair-principles).

As a starting point, we will use the open-source and technology-neutral [CK framework](https://github.com/ctuning/ck) 
with a [collection](https://github.com/ctuning/ai) of [reusable automation recipes](https://github.com/ctuning/ai/tree/main/program) 
and [plug&play packages](https://github.com/ctuning/ai/tree/main/package) 
for ML systems. CK framework was already successfully used by several MLCommons members 
to automate their MLPerf inference submissions and we want to build upon their experience. 

We will also reuse a relatively mature ACM methodology to reproduce research results ([ACM TechTalk](https://youtu.be/7zpeIVwICa4) and [Artifact Evaluation](https://cTuning.org/ae)),
open-source tools from the MLCommons&trade; Best Practices WorkGroup ([MLCube&trade;](https://github.com/mlcommons/mlcube)).

A few examples: 
* [MLPerf&trade; object detection workflow](https://github.com/ctuning/ck/blob/master/docs/mlperf-automation/tasks/task-object-detection.md)
* [Docker image for MLPerf&trade; with OpenVINO]( https://github.com/ctuning/ai/tree/main/docker/mlperf-inference-v0.7.openvino )
* [Jupyter notebook for ML DSE](https://nbviewer.jupyter.org/urls/dl.dropbox.com/s/f28u9epifr0nn09/ck-dse-demo-object-detection.ipynb)
* [Webcam test of the MLPerf object detection model with TFLite](https://cknowledge.io/solution/demo-obj-detection-coco-tf-cpu-webcam-linux-azure#test)
* [Public scoreboard with MLPerf DSE](https://cknowledge.io/result/crowd-benchmarking-mlperf-inference-classification-mobilenets-all)

Feel free to contribute to this collaborative doc by sending your PR [here]( https://github.com/ctuning/ck/pulls )
or creating tickets at [github.com/mlcommons/inference](https://github.com/mlcommons/inference) and [github.com/ctuning/ck](https://github.com/ctuning/ck).
Thank you!


# News and updates

* **20210701**: Make sure that your CK version >= 2.5.5 with many enhancements for MLPerf (```ck version```). 
  You can update it via (```python3 -m pip install ck -U```).
* [TBD: Common workflow for MLPerf inference](inference/workflow.md)
* [TBD: Test and update CK automation recipes for MLOps](components/README.md)
* [TBD: Docker containers to run MLPerf inference out of the box](inference/containers.md)

# Table of contents

* [Prepare your platform](platform/README.md)
* [Install CK framework](tools/ck.md)
  * [Install CK virtual environment (optional)](tools/ck-venv.md)
  * [Use adaptive CK container](tools/ck-docker.md)
* [**Prepare and run reference MLPerf&trade; inference benchmark**](tasks/README.md)
  * [Customize MLPerf&trade; inference benchmark](tasks-custom/README.md)
* [Integrate CK workflows with CI platforms](tools/continuous-integration.md)
* [Analyze MLPerf inference results](results/README.md)
  * [Example of CK dashboards for ML Systems DSE](results/ck-dashboard.md)
* [**Reproduce MLPerf&trade; results and DSE**](reproduce/README.md)
* [Use CK with MLCube&trade;](tools/mlcube.md)
* [Test models with a webcam](reproduce/demo-webcam-object-detection-x86-64.md)
* [Explore ML Systems designs (AutoDSE)](dse/README.md)
* [Submit to MLPerf&trade; inference](submit/README.md)
* [Related tools](tools/README.md)
* Further improvements:
  * [Unifying CK components for ML Systems](components/README.md)
  * [Ideas to make it easier to use MLPerf&trade; inference benchmarks](https://docs.google.com/document/d/1xUI4_ArXssMUigsSHTAE2lL7jRZE12XXvzoV3QMoT84)
  * Add MLPerf&trade; power measurements to our automated benchmark toolset
  * [Standardization of MLPerf&trade; workflows](tbd/standardization.md)
  * [More automation](tbd/automation.md)
  * [Redesigning CK (CKLite)](tbd/ck2.md)



# Support

* [OctoML.ai](https://octoml.ai)
* [MLCommons Best Practices WG](https://mlcommons.org)
* [cTuning foundation](https://cTuning.org)
* [ACM](https://acm.org)


# Coordinator

* [Grigori Fursin](https://cKnowledge.io/@gfursin)
