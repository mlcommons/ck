# MLPerf&trade; inference benchmark automation

This is a community effort to make it easier to use MLPerf&trade; inference benchmarks (prepare, run, reproduce, submit) 
using the ACM methodology and automated workflows to reproduce results from research papers 
([ACM TechTalk intro](https://youtu.be/7zpeIVwICa4) and [Artifact Evaluation](https://cTuning.org/ae)) 
and open-source tools from the MLCommons&trade; Best Practices WorkGroup ([MLCube&trade;](https://github.com/mlcommons/mlcube)).

Feel free to contribute to this collaborative doc by sending your PR [here]( https://github.com/ctuning/ck/pulls )
or creating tickets at [github.com/mlcommons/inference](https://github.com/mlcommons/inference) and [github.com/ctuning/ck](https://github.com/ctuning/ck).
Thank you!


# News

* **20210524**: make sure that your CK version >= 2.4.0 with many enhancements for MLPerf (```ck version```). You can update it via (```python3 -m pip install ck -U```).

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
  * [Ideas to make it easier to use MLPerf&trade; inference benchmarks](https://docs.google.com/document/d/1xUI4_ArXssMUigsSHTAE2lL7jRZE12XXvzoV3QMoT84)
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
