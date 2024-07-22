[ [Back to index](README.md) ]

## New CM automation capabilities for MLPerf inference benchmarks

This section highlights the new capabilities of the [Collective Mind automation language](https://doi.org/10.5281/zenodo.8105339)
to [modularize MLPerf benchmarks and enable mass-scale submissions by the community](https://github.com/mlcommons/ck/tree/master/docs/mlperf)
added by [the community](https://access.cknowledge.org/playground/?action=contributors), 
[cTuning.org](https://cTuning.org) and [cKnowledge.org](https://www.linkedin.com/company/cknowledge)
via [public MLPerf challenges](https://access.cknowledge.org/playground/?action=challenges).

The latest CM/CK MLPerf automation supports practically any combination of 
* All MLPerf models including GPT-J
* Main MLPerf implementations (all reference, Nvidia, Intel, TFLite, MIL)
* Main frameworks and run-times (DeepSparse, PyTorch, TensorFlow, TFLite, TVM, TensorRT, ONNX, NCNN, Triton)
* Diverse hardware including Coral TPU, Nvidia GPUs (A100,T4,L4,RTX 4090, Jetson Orin), Intel/AMD servers, Graviton, NeoVerse, Apple metal
* All major cloud providers including AWS, GCP and Azure with Ubuntu, RHEL, SLES, Amazon Linux and Windows 11
* Most laptops and servers including Apple, Dell, Toshiba, Asus, HPE, Lenovo

## Highlights of the MLPerf inference v3.1 results from the community and cTuning

The goal of CM and CK technology is to democratize MLPerf and make it accessible to everyone to
showcase, select and co-design the most efficient AI systems (performance, power, accuracy, costs).

Our open-source technology has helped [the community](https://access.cknowledge.org/playground/?action=contributors) 
submit and reproduce >90% of all MLPerf inference v3.1 results, >90% of all the power results and >55% of all the submitted system configurations
via the [cTuning foundation](https://cTuning.org). 

Never before has MLPerf inference benchmark crossed 10,000 results and this time [cTuning foundation and the community](https://cTuning.org) submitted 12,000+ results 
showing that anyone can benchmark AI systems and even set record performance using our CM based MLPerf inference automation.

We thank all [our contributors](https://access.cknowledge.org/playground/?action=contributors), Neural Magic, TTA, One Stop Systems, Nutanix, Collabora, Deelvin, cKnowledge, AMD and Nvidia
for interesting discussions and feedback that helped to improve the open-source MLCommons CM automation workflows
for MLPerf benchmarks and [make them available to everyone](https://github.com/mlcommons/ck/tree/master/docs/mlperf)!



## New CM capabilities to automate experiments, optimizations and design space exploration

The 1st [CM experiment automation](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/experiment/README-extra.md) 
for BERT performance/power/accuracy exploration from NeuralMagic Zoo, Hugging Face Hub and NeurIPS papers
(sparsity, quantization and batch size) across multiple AMD, Intel and
ARM-based systems.

## Upcoming events powered by CM

* [CK playground for MLPerf at AI hardware summit'23](https://aihwedgesummit.com/events/aihwedgesummit)
* [CM automation language to reproduce papers from the ACM MICRO'23 conference](https://ctuning.org/ae/micro2023.html)
* [Tutorial about CM automation language and CK playground for MLPerf at IISWC'23]( https://iiswc.org/iiswc2023/#/program/ )
* [CM automation language and CK playground to run MLPerf at the Student Cluster Competition at SuperComputing'23](https://sc23.supercomputing.org/students/student-cluster-competition)

*More events to come soon!*

