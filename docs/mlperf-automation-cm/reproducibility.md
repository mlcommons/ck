# MLPerf automation and reproducibility initiative

One of the goals of the [CM workflow automation meta-framework](https://github.com/mlcommons/ck) 
is to make it easier for the community to reproduce official benchmarking results from MLPerf, 
and run MLPerf with any model, data, software and hardware using 
[portable CM components](https://github.com/mlcommons/ck/tree/master/cm-mlops/script).

Here we keep track of CM automation and reproducibility for all reference MLPerf benchmark implementations:

## Original Python front-end for loadgen


Reproducibility setup | Image classification | Object detection | Medical imaging | Language | Recommendation | Speech |
--- | --- | --- | --- | --- | --- | --- |
x8664; Ubuntu `[20.04,22.04]`, Python `[3.8,3.9]`, ONNX 1.11.1 | &#10003; [report](reproducibility-report--image-classification--f28ae623c84049dd.md) | | | | | |
x8664; Ubuntu 22.04, Python 3.9, PyTorch | &#10060; [report](reproducibility-report--image-classification--0ff2cc95fc1a4f19.md) | | | | | |



## New and universal C++ front-end for loadgen

We are developing a new [universal C++ front-end for loadgen](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation-cm/reproducibility.md#original-python-front-end-for-loadgen) 
with CM automations to make it easier to plug in any models, data sets, frameworks and hardware 
using the same [portable CM components](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
as for the Python FE.

Reproducibility setup | Image classification | Object detection | Medical imaging | Language | Recommendation | Speech |
--- | --- | --- | --- | --- | --- | --- |
x8664; Ubuntu 22.04, LLVM 14.0, ONNX 1.11.1 | &#10003; [report](reproducibility-report--image-classification--78ac1dc6120f4421.md) | | | | | |

