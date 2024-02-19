[ [Back to MLPerf inference benchmarks index](../README.md) ]

# MLPerf inference benchmark

## Language processing with BERT

### Notes

Bert has two variants - `bert-99` and `bert-99.9` where the `99` and `99.9` specifies the required accuracy constraint 
with respect to the reference floating point model. `bert-99.9` model is applicable only on a datacenter system.

In the edge category, bert-99 has Offline and SingleStream scenarios and in the datacenter category, 
both `bert-99` and `bert-99.9` have Offline and Server scenarios.

Please check [MLPerf inference GitHub](https://github.com/mlcommons/inference) for more details.
 
### Run using the [MLCommons CM framework](https://github.com/mlcommons/ck)

*From Feb 2024, we suggest you to use [this GUI](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725)
 to configure MLPerf inference benchmark, generate CM commands to run it across different implementations, models, data sets, software
 and hardware, and prepare your submissions.*

### A few ready-to-use CM commands

Install MLCommons CM automation framework with automation recipes for MLPerf as described [here](../../../installation.md).

The following guides explain how to run different implementations of this benchmark via CM:

* [MLCommons reference implementation in Python (CPU & GPU)](README_reference.md)
* [NVIDIA optimized implementation (GPU)](README_nvidia.md)
* [Intel optimized implementation (CPU)](README_intel.md)
* [Qualcomm optimized implementation (QAIC)](README_qualcomm.md)
* [DeepSparse implementation (CPU: x64, Arm64)](README_deepsparse.md)

### Tutorials

* [2023: Tutorial to run MLPerf inference benchmark with reference and deepsparse implementation and prepare submission](tutorial.md)

### A few example scripts

* [Run custom ONNX models with MLPerf reference implementation](run_custom_onnx_models.sh)
* [Run multiple DeepSparse Zoo models via MLPerf](run_sparse_models.sh)

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
