# Tutorial: modularizing ML(Perf) benchmark

This tutorial demonstrates how to use CK2(CM) to modularize MLPerf benchmark
and enable automated design space exploration of ML/AI Systems across diverse
and continuously changing ML models, datasets, engines, libraries and platforms.

MLPerf Inference benchmarks suite include the following models as 
of [Release 2.1](https://github.com/mlcommons/inference/tree/r2.1). 
1. resnet50 (Image Classification and uses Imagenet-2012 Dataset
2. retinanet (Object Detection and uses OpenImages Dataset)
3. bert (Language Processing and uses SQUAD-1.1 Dataset)
4. dlrm (Recommendation and uses Criteo Terabyte Dataset)
5. 3d-unet (Medical Imaging and uses KiTS19 Dataset)
6. rnnt (Speech Recognition and OpenSLR LibriSpeech Corpus Dataset)

bert, 3d-unet and dlrm have two flavors - where one has to reach minimum 99% accuracy 
of the reference implementation and another needs 99.9% accuracy. 

We will be using resnet50 as an example in this tutorial.

For a general ML workload a benchmark run usually have the following steps
1. Raw Dataset -> Preprocessed Dataset (say change the layout to make it compatible with the model)
2. Original model -> Processed Model (in case some changes are needed)
3. Framework to support the backend (Tensorflow, Pytorch etc)
4. Benchmark Application code (usually in Python or C++)
5. Any other dependencies (Protobuf, AOCL etc)

In CK2(CM) each of these component is decomposed in to a separate script with its own pre 
as well as post dependencies which makes them reusable as plug and play components. Further 
CK2(CM) provides an easy way to specify any variation. For resnet50 model and Tensorflow (Tf)
backend we used the following scripts as dependecies to the [Reference App Script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-vision-reference) for MLPerf 2.1 submission

1. [Install System Dependencies](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
2. [MLPerf Loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-mlc-inference-loadgen)
3. [Imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-imagenet-val)
4. [TF Model](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tf)
5. [Tensorflow](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorflow)
6. [Get Run Configurations](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sut-mlc-configs)

Here, the `Install System Dependencies` script will install the OS dependent packages needed for 
the benchmark run. The `Get Run Configurations` script will provide the required runtime parameters to loadgen 
based on the System Under Test details provided by the user in a YAML file like [this](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sut-mlc-configs/configs/default). After running the reference implementation postprocess function is 
automatically called where the required files are copied to/created in the run directory as required by MLPerf submission checker.
Once we have run all the required scenarios (all using the same OUTPUT_DIR), we then call the [script to 
generate a valid submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlc-inference-submission)
which moves the result directory to a format needed by MLPerf submission checker. This submission generator script takes in 
the results folder as input (can have results of multiple models and multiple SUTs but only the models under a single
SUT will be processed at a time) and it has [GET SUT](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sut) 
script as a dependency which provides details of the system under test as required by MLPerf. This script also calls two 
scripts as post dependecies

1. [Accuracy Truncater](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlc-accuracy-truncation)
2. [Submission Checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlc-submission-checker)

After the run to Submission Checker is completed we'll have a valid submission folder provided all the runs completed as 
expected. 

## Single Command for Reproducing

## Detailed Steps
