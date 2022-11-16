[ [Back to index](../README.md) ]

# Tutorial: customizing the MLPerf inference benchmark (part 3)

<details>
<summary>Click here to see the table of contents.</summary>

* [Introduction](#introduction)
  * [Update CM framework and automation repository](#update-cm-framework-and-automation-repository)
  * [MLPerf inference - Python - ResNet50 FP32 - ImageNet - ONNX - CPU - Offline](#mlperf-inference---python---resnet50-fp32---imagenet---onnx---cpu---offline)
  * [MLPerf inference - Python - ResNet50 Int8 - ImageNet - TVM - CPU - Offline](#mlperf-inference---python---resnet50-int8---imagenet---tvm---cpu---offline)
* [The next steps](#the-next-steps)
* [Authors](#authors)
* [Acknowledgments](#acknowledgments)

</details>

# Introduction

We expect that you have completed the [1st part](sc22-scc-mlperf.md) of this tutorial 
and managed to run the MLPerf inference benchmark for object detection
with RetinaNet FP32, Open Images and ONNX runtime on a CPU target.

*Note that this tutorial is under preparation and is gradually extended
 by the [MLCommons taskforce on education and reproducibility](../mlperf-education-workgroup.md).*


## Update CM framework and automation repository

Note that the [CM automation meta-framework](https://github.com/mlcommons/ck) 
and the [repository with automation scripts ](https://github.com/mlcommons/ck/tree/master/cm-mlops)
are being continuously updated by the community to improve the portability and interoperability of 
all reusable components for MLOps and DevOps.

You can get the latest version of the CM framework and automation repository as follows
(though be careful since CM CLI and APIs may change):

```bash
python3 -m pip install cmind -U
cm pull repo mlcommons@ck --checkout=master
```



## MLPerf inference - Python - ResNet50 FP32 - ImageNet - ONNX - CPU - Offline


## MLPerf inference - Python - ResNet50 Int8 - ImageNet - TVM - CPU - Offline

TBD





# The next steps

Please check other parts of this tutorial to learn how to 
customize and optimize MLPerf inference benchmark using MLCommons CM
(under preparation):

* [1st part](sc22-scc-mlperf.md): customize MLPerf inference (Python ref implementation, Open images, ONNX, CPU)
* [2nd part](sc22-scc-mlperf2.md): customize MLPerf inference (C++ implementation, CUDA, PyTorch)
* *To be continued*

You are welcome to join the [open MLCommons taskforce on education and reproducibility](../mlperf-education-workgroup.md)
to contribute to this project and continue optimizing this benchmark and prepare an official submission 
for MLPerf inference v3.0 (March 2023) with the help of the community.

See the development roadmap [here](https://github.com/mlcommons/ck/issues/536).

# Authors

* [Grigori Fursin](https://cKnowledge.io/@gfursin) (OctoML, MLCommons, cTuning foundation)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) (OctoML, MLCommons)


# Acknowledgments

We thank 
[Hai Ah Nam](https://www.nersc.gov/about/nersc-staff/advanced-technologies-group/hai-ah-nam),
[Steve Leak](https://www.linkedin.com/in/steve-leak),
[Vijay Janappa Reddi](https://scholar.harvard.edu/vijay-janapa-reddi/home),
[Tom Jablin](https://scholar.google.com/citations?user=L_1FmIMAAAAJ&hl=en),
[Ramesh N Chukka](https://www.linkedin.com/in/ramesh-chukka-74b5b21),
[Peter Mattson](https://www.linkedin.com/in/peter-mattson-33b8863/),
[David Kanter](https://www.linkedin.com/in/kanterd),
[Pablo Gonzalez Mesa](https://www.linkedin.com/in/pablo-gonzalez-mesa-952ab2207),
[Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189),
[Thomas Schmid](https://www.linkedin.com/in/tschmid)
and [Gaurav Verma](https://www.linkedin.com/in/grverma)
for their suggestions and contributions.
