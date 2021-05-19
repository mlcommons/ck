# MLPerf inference benchmark automation guide

This document is prepared by [OctoML.ai](https://github.com/ctuning/ck) (MLCommons member) 
in collaboration with the [MLCommons&trade; community](https://mlcommons.org)
to make it easier to reproduce MLPerf&trade; benchmark results and automate new submissions.

# News

* **20210519**: make sure that you update CK (```python3 -m pip install ck -U```) and use the version >= 2.1.0 (```ck version```) to support inheritance of CK entries.

# Table of content

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
  * [Standardization of MLPerf&trade; workflows](tbd/standardization.md)
  * [More automation](tbd/automation.md)
  * [Redesigning CK (CKLite)](tbd/ck2.md)

*Please feel free to contribute to this collaborative doc by sending your PR [here]( https://github.com/ctuning/ck/pulls )! Thank you!*

# Feedback

* Feel free to create tickets at [github.com/mlcommons/inference](https://github.com/mlcommons/inference) and [github.com/ctuning/ck](https://github.com/ctuning/ck).
* Contact [Grigori Fursin](https://cKnowledge.io/@gfursin) (VP of MLOps at [OctoML.ai](https://octoml.ai) and creator of the [CK framework](https://github.com/ctuning/ck)).
