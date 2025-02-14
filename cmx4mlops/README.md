# Aggregated CM and CMX automations for MLOps and MLPerf

[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Powered by CM/CMX](https://img.shields.io/badge/Powered_by-MLCommons%20CM-blue)](https://pypi.org/project/cmind).

This repository is powered by the [CM and/or CMX framework](https://github.com/mlcommons/ck/tree/master/cm).

Two key automations developed using CM are **script** and **cache**, which streamline machine learning (ML) workflows, 
including managing Docker runs. Both Script and Cache automations are part of the **cmx4mlops** repository.

The [CM scripts](https://access.cknowledge.org/playground/?action=scripts), 
also housed in this repository, consist of hundreds of modular Python-wrapped scripts accompanied 
by `yaml` metadata, enabling the creation of robust and flexible ML workflows.

## License

[Apache 2.0](LICENSE.md)

## Copyright

© 2022-2025 MLCommons. All Rights Reserved.

Grigori Fursin, the cTuning foundation and OctoML donated the CK and CM projects to MLCommons to benefit everyone and encourage collaborative development.

## Maintainers

* CM, CM4MLOps and MLPerf automations: MLCommons
* CMX (the next generation of CM): Grigori Fursin

## Author

[Grigori Fursin](https://cKnowledge.org/gfursin)

We sincerely appreciate all [contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTORS.md) 
for their invaluable feedback and support!

## Concepts

Check our [ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339) and the [white paper](https://arxiv.org/abs/2406.16791).

## Test image classification and MLPerf R-GAT inference benchmark via CMX PYPI package

```bash
pip install cmind
pip install cmx4mlops
cmx reindex repo
cmx run script "python app image-classification onnx" --quiet
cmx run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_short --submitter="MLCommons" --adr.inference-src.tags=_branch.dev --pull_changes=yes --pull_inference_changes=yes  --submitter="MLCommons" --hw_name=ubuntu-latest_x86 --model=rgat --implementation=python --backend=pytorch --device=cpu --scenario=Offline --test_query_count=500 --adr.compiler.tags=gcc --category=datacenter --quiet  --v --target_qps=1
```

## Test image classification and MLPerf R-GAT inference benchmark via CMX GitHub repo

```bash
pip uninstall cmx4mlops
pip install cmind
cmx pull repo mlcommons@ck --dir=cmx4mlops/cmx4mlops
cmx run script "python app image-classification onnx" --quiet
cmx run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_short --submitter="MLCommons" --adr.inference-src.tags=_branch.dev --pull_changes=yes --pull_inference_changes=yes  --submitter="MLCommons" --hw_name=ubuntu-latest_x86 --model=rgat --implementation=python --backend=pytorch --device=cpu --scenario=Offline --test_query_count=500 --adr.compiler.tags=gcc --category=datacenter --quiet  --v --target_qps=1
```

## Parent project

Visit the [parent Collective Knowledge project](https://github.com/mlcommons/ck) for further details.

## Citing this project

If you found the CM and CMX automations helpful, kindly reference this article:
[ [ArXiv](https://arxiv.org/abs/2406.16791) ]
