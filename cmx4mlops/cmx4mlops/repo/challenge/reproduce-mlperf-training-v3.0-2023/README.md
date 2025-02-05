### Challenge

Prepare, optimize and reproduce MLPerf training v3.0 benchmarks 
using the [MLCommons CM (CK2) automation framework](https://github.com/mlcommons/ck)

### Status

We could not do a successful submission mainly because the training scripts were not converging on a single GPU. We tried resnet and bert training. The below CM scripts are added to do MLPerf training for BERT using the reference and NVIDIA implementations.

1. [BERT Training using Nvidia code](https://github.com/ctuning/mlcommons-ck/tree/master/cm-mlops/script/app-mlperf-training-nvidia)
2. [BERT Training using MLPerf Reference code](https://github.com/ctuning/mlcommons-ck/tree/master/cm-mlops/script/app-mlperf-training-reference)

### Organizers

* [MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce)
* [cTuning foundation](https://cTuning.org)
* [cKnowledge](https://cKnowledge.org)
