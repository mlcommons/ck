[ [Back to index](README.md) ]

This section highlights the new CM capabilities 
to [modularize and automate MLPerf inference benchmarks](https://github.com/mlcommons/ck/tree/master/docs/mlperf)
added by [the community](https://access.cknowledge.org/playground/?action=contributors), 
[cTuning foundation](https://cTuning.org) and [cKnowledge](https://www.linkedin.com/company/cknowledge)
via our [public MLPerf challenges](https://access.cknowledge.org/playground/?action=challenges).

We thank Neural Magic, TTA, One Stop Systems, Nutanix, Collabora, Deelvin, cKnowledge, AMD and Nvidia
for interesting discussions and feedback that helped us improve the open-source MLCommons CM automation workflows
for MLPerf benchmarks and beyond.

## New CM automation capabilities for MLPerf inference benchmarks

CM/CK MLPerf automation for practically any combination of 
* All MLPerf models including GPT-J
* Main MLPerf implementations (all reference, Nvidia, Intel, TFLite, MIL)
* Main frameworks and run-times (DeepSparse, PyTorch, TensorFlow, TFLite, TVM, TensorRT, ONNX, NCNN, Triton)
* Diverse hardware including Coral TPU, Nvidia GPUs (A100,T4,L4,RTX 4090, Jetson Orin), Intel/AMD servers, Graviton, NeoVerse, Apple metal
* All major cloud providers including AWS, GCP and Azure with Ubuntu, RHEL, SLES, Amazon Linux and Windows 11
* Most laptops and servers including Apple, Dell, Toshiba, Asus, HPE, Lenovo

## New CM capabilities to automate experiments, optimizations and design space exploration

The 1st [CM experiment automation](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/experiment/README-extra.md) 
for BERT performance/power/accuracy exploration from NeuralMagic Zoo, Hugging Face Hub and NeurIPS papers
(sparsity, quantization and batch size) across multiple AMD, Intel and
ARM-based systems.

## Highlights of the MLPerf inference v3.1 results from the community and cTuning

*These information will become public at the [MLCommons CK playground](https://access.cKnowledge.org)
 with various derived metrics, reproducibility reports and comparison tables
 after the official release of the MLPerf inference v3.1 results.*
