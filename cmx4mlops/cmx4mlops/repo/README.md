## Unified and cross-platform CM interface for DevOps, MLOps and MLPerf

[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![Powered by CM](https://img.shields.io/badge/Powered_by-MLCommons%20CM-blue)](https://pypi.org/project/cmind).
[![Downloads](https://static.pepy.tech/badge/cm4mlops)](https://pepy.tech/project/cm4mlops)

[![CM script automation features test](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-script-features.yml)
[![MLPerf inference bert (deepsparse, tf, onnxruntime, pytorch)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-bert-deepsparse-tf-onnxruntime-pytorch.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-bert-deepsparse-tf-onnxruntime-pytorch.yml)
[![MLPerf inference MLCommons C++ ResNet50](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-mlcommons-cpp-resnet50.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-mlcommons-cpp-resnet50.yml)
[![MLPerf inference ABTF POC Test](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-abtf-poc.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-abtf-poc.yml)
[![Test Compilation of QAIC Compute SDK (build LLVM from src)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-qaic-compute-sdk-build.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-qaic-compute-sdk-build.yml)
[![Test QAIC Software kit Compilation](https://github.com/mlcommons/cm4mlops/actions/workflows/test-qaic-software-kit.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-qaic-software-kit.yml)


# CM4MLOps repository

**CM4MLOps** repository is powered by the [Collective Mind automation framework](https://github.com/mlcommons/ck/tree/master/cm), 
a [Python package](https://pypi.org/project/cmind/) with a CLI and API designed for creating and managing automations. 

Two key automations developed using CM are **Script** and **Cache**, which streamline machine learning (ML) workflows, 
including managing Docker runs. Both Script and Cache automations are part of the **cm4mlops** repository.

The CM scripts, also housed in this repository, consist of hundreds of modular Python-wrapped scripts accompanied 
by `yaml` metadata, enabling the creation of robust and flexible ML workflows.

- **CM Scripts Documentation**: [https://docs.mlcommons.org/cm4mlops/](https://docs.mlcommons.org/cm4mlops/)
- **CM CLI Documentation**: [https://docs.mlcommons.org/ck/specs/cm-cli/](https://docs.mlcommons.org/ck/specs/cm-cli/)  

The `mlperf-branch` of the **cm4mlops** repository is dedicated to developments specific to MLPerf Inference. 
Please submit any pull requests (PRs) to this branch. For more information about using CM for MLPerf Inference, 
refer to the [MLPerf Inference Documentation](https://docs.mlcommons.org/inference/).

## License

[Apache 2.0](LICENSE.md)

## Copyright

© 2022-2025 MLCommons. All Rights Reserved.

Grigori Fursin, the cTuning foundation and OctoML donated the CK and CM projects to MLCommons to benefit everyone and encourage collaborative development.

## Maintainer(s)

* MLCommons

## CM author

[Grigori Fursin](https://cKnowledge.org/gfursin)

## CM concepts

Check our [ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339) and the [white paper](https://arxiv.org/abs/2406.16791).

## CM script developers

Arjun Suresh, Anandhu Sooraj, Grigori Fursin

## Parent project

Visit the [parent Collective Knowledge project](https://github.com/mlcommons/ck) for further details.

## Citing this project

If you found the CM automations helpful, kindly reference this article:
[ [ArXiv](https://arxiv.org/abs/2406.16791) ]
