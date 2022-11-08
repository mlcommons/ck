# MLPerf automation and reproducibility initiative

One of the goals of the [MLCommons education and reproducibility taskforce](../mlperf-education-workgroup.md) 
is to make it easier to run MLPerf benchmark with any model, data, software and hardware using 
a common workflow automation meta-framework [(Collective Mind aka CM)](https://github.com/mlcommons/ck)
and [reusable CM components](https://github.com/mlcommons/ck/tree/master/cm-mlops/script#readme) for interoperable MLOps and DevOps.

This page contains reproducibility reports from the community testing the MLPerf inference benchmark
across different ML models, datasets, frameworks, run-times and hardware using CM.

Note that the long-term goal of our taskforce is to automate this process of testing all possible combinations
of ML models, datasets, software and hardware and submitting Pareto-optimal configurations to MLPerf.
Feel free to check our [on-going work](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw) 
and help with this community effort!

## Original reference MLPerf benchmark implementations


Reproducibility setup | [Image classification](reproducibility-report--image-classification--ref.md) | [Object detection](reproducibility-report--object-detection--ref.md) | Medical imaging | [Language](reproducibility-report--language--ref.md) | Recommendation | Speech |
--- | --- | --- | --- | --- | --- | --- |
x8664; GCP ?;Ubuntu `[20.04,22.04]`;Python `[3.8,3.9]`; MLPerf inference ?; ONNX 1.11.1; ResNet50 ONNX; ImageNet; [`Offline`] | [&#10003;ResNet50](reproducibility-report--image-classification--ref.md#f28ae623c84049dd) | | | | | |
x8664; ?; Ubuntu 22.04; Python 3.9; MLPerf inference ?; PyTorch ?; ResNet50 PyTorch; ImageNet; [`Offline`] | [&#10060;ResNet50](reproducibility-report--image-classification--ref.md#0ff2cc95fc1a4f19) | | | | | |
x8664; ?; Ubuntu `[20.04,22.04]`; Python `[3.8,3.9]`; MLPerf inference ?; ONNX 1.12.1; RetinaNet ONNX; Open Images; [`Offline`] | | [&#10003;RetinaNet](reproducibility-report--object-detection--ref.md#9af41c1477644ae7) | | | | |
Nvidia GPU ?; Ubuntu `[20.04,22.04]`; Python `[3.8,3.9]`; MLPerf inference ?; CUDA X; RetinaNet ONNX; Open Images; [`Offline`] | | [&#10003;RetinaNet](reproducibility-report--object-detection--ref.md#6c0274555cf64f33) | | | | |
Nvidia GPU ?; Ubuntu `[20.04,22.04]`; Python `[3.8,3.9]`; MLPerf inference ?; CUDA X; BERT-Large; SQUAD; [`Offline`] | | | | [&#10003; BERT-Large](reproducibility-report--language--ref.md#491fe590c3d24bcd) | | |


## C++ universal "plug&play" front-end for MLPerf loadgen

We are developing a new universal C++ front-end for loadgen
with CM automations to make it easier to plug in any models, datasets, frameworks and hardware 
using the same [portable CM components](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
as for the Python FE.

Reproducibility setup | Image classification | Object detection | Medical imaging | Language | Recommendation | Speech |
--- | --- | --- | --- | --- | --- | --- |
x8664; Ubuntu 22.04; LLVM 14.0; MLPerf inference ?; ONNX 1.11.1; ResNet50 ONNX; ImageNet; [Offline] | TBD [ResNet50](reproducibility-report--image-classification--cpp.md#d7e10b7b396a4fd9) | | | | | |
