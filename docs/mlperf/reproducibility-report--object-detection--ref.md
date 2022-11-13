# MLPerf Image classification (Python reference implementation)

[*Back to MLPerf reproducibility studies*](reproducibility.md)

## TBD

* Report time to run individual CM components (model/dataset download, pre-processing, compilation, execution (particularly for accuracy))

## Setup

* [System dependencies](../../cm/docs/installation.md#ubuntu--debian)
* [CM workflow automation meta-framework](../../cm/docs/installation.md#cm-installation)

* We are in the process of enabling CUDA support within CM. Until then please setup cuDNN as described [here](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)

## CM automation workflow

* [README](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference#retinanet)

## Reusable CM components

* [Python](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
* [Retinanet model (ONNX)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
* [Openimages validation set](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
* [ONNX run-time](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime)
* [MLPerf inference benchmark workflow with Python FE](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)

* [Other reusable CM components](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)*

# Reproducibility reports by the community

If you encounter issues, please open a [GitHub issue](https://github.com/mlcommons/ck/issues)
and/or feel free to join our [weekly conf-calls](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md) 
to discuss your issues and provide feedback!

## 9af41c1477644ae7

20221011 @ successfully tested the following setups:

*x8664; ?; Ubuntu `[20.04,22.04]`; Python `[3.8,3.9]`; MLPerf inference ?; ONNX 1.12.1; RetinaNet ONNX; Open Images*

```bash
python3 -m pip install cmind==1.0.3

cm pull repo mlcommons@ck --git ...

cm run script "install python venv" --version=3.9
cm run script "get onnxruntime" --version=1.12.1

cm run script --tags=app,mlperf,inference,reference,python,_retinanet,_onnxruntime,_cpu \
     --mode=accuracy \
     --scenario=Offline

cm run script --tags=app,mlperf,inference,reference,python,_retinanet,_onnxruntime,_cpu \
     --mode=performance \
     --scenario=Offline

```



## 6c0274555cf64f33

20221011 @ successfully tested the following setups:

*Nvidia GPU ?; Ubuntu `[20.04,22.04]`; Python `[3.8,3.9]`; MLPerf inference ?; CUDA X; RetinaNet ONNX; Open Images*

```bash
python3 -m pip install cmind==1.0.3

cm pull repo mlcommons@ck --git ...

cm run script "install python venv" --version=3.9
cm run script "get onnxruntime" --version=1.12.1
```

