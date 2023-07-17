## Setup

Please follow [this guide](../README.md) to install CM and setup your hardware.

## Notes

Bert has two variants - `bert-99` and `bert-99.9` where the `99` and `99.9` specifies the required accuracy constraint with respect to the reference floating point model. `bert-99.9` model is applicable only on a datacenter system.

In the edge category, bert-99 has Offline and SingleStream scenarios and in the datacenter category, both `bert-99` and `bert-99.9` have Offline and Server scenarios.

## Run MLPerf benchmarks via CM

Please follow the below readmes to run the command specific to a given implementation:

* [MLCommons reference implementation in Python (CPU & GPU)](README_reference.md)
* [NVIDIA optimized implementation (GPU)](README_nvidia.md)
