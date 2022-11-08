[ [Back to index](../README.md) ]

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

## Single Command for Generating a Submission
Say if we want to generate a submission for a System Under Test, we need to create a system description like 
[here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-sut/suts/gcp-n2-standard-80-tf.json) and a run configuration 
like [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-sut-mlc-configs/configs/gcp-n2-standard-80-tf/config.yaml) and then do the following command for generating a submission zip folder for `resnet50` model.
```
cm run script --tags=app,mlperf,inference,reference,python,_resnet50,_tf,_cpu,_submission,_valid \
--output_dir=$HOME/results \
--add_deps_tags.imagenet=_full \
--env.IMAGENET_PATH=$HOME/datasets/imagenet-2012-val \
--env.CM_SUT_NAME=gcp-n2-standard-80-tf
```
Here, `_submission` variation internally calls `_all-scenarios` and `all_modes` variations (all variation tags begin with an '\_') 
and they automatically all the required scenarios and modes needed for the given model under the category given in the input 
system description. Here, we have to give the path of IMAGENET because it is not publicly available and so we must have a local 
copy of it in some system location. More details and run options can be seen [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-vision-reference)

For generating a submission for another model say `retinanet` we just have to replace `_resnet50` with `_retinanet` and 
its dataset OPENIMAGES being publicly available we no longer need to give the path for it. Further retinanet reference implementation
currently does not support `tensorflow` and thus we use `onnxruntime` for it. Thus we get the following submission generation
command for retinanet
```
cm run script --tags=app,mlperf,inference,reference,python,_retinanet,_onnxruntime,_cpu,_submission,_valid \
--output_dir=$HOME/results \
--env.CM_SUT_NAME=gcp-n2-standard-80-onnxruntime
```
