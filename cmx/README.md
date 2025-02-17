# Collective Mind eXtension aka Common Metadata eXchange (CMX)

We are developing the extension to the MLCommons Collective Mind automation framework 
called [Common Metadata eXchange (CMX)](https://github.com/mlcommons/ck/tree/master/cmx)
to support open science and facilitate
collaborative, reproducible, and reusable research, development, 
and experimentation based on [FAIR principles](https://en.wikipedia.org/wiki/FAIR_data)
and the [Collective Knowledge concept](https://learning.acm.org/techtalks/reproducibility).

It helps users non-intrusively convert their software projects 
into file-based repositories of portable and reusable artifacts 
(code, data, models, scripts) with extensible metadata, 
a unified command-line interface, and a simple Python API.

Such artifacts can be easily chained together into portable and technology-agnostic automation workflows,
enabling users to  rerun, reproduce, and reuse complex experimental setups across diverse and rapidly 
evolving models, datasets, software, and hardware.

Such workflows, in turn, can be easily integrated with CI/CD pipelines and GitHub Actions 
and used to create powerful, portable, modular and GUI-based applications.

For example, you can run image classification and the MLPerf inference benchmark on Linux, macOS, 
and Windows using a few CMX commands as follows:

```bash
pip install cmind
cmx pull repo mlcommons@ck --dir=cmx4mlops/cmx4mlops
cmx run script "app image-classification python torch" --quiet
cmx run script "run-mlperf inference _performance-only _short" --model=resnet50 --precision=float32 --backend=onnxruntime --scenario=Offline --device=cpu --env.CM_SUDO_USER=no --quiet
cmx show cache
```

CMX extends the [Collective Mind (CM) framework](https://zenodo.org/records/8105339),
which have been successfully validated to 
[modularize, automate, and modernize MLPerf benchmarks](https://arxiv.org/abs/2406.16791).

CMX is written in Python, requires minimal dependencies, and has been
tested on various flavors of Linux, macOS, Windows, and other operating
systems to automate benchmarking, building, running, and optimizing AI,
ML, and other emerging workloads and systems.

CMX encourages community collaboration to share, reuse, and improve artifacts, automations, 
and experimental setups through public and private Git repositories, 
rather than redeveloping them from scratch.

CMX is available alongside the legacy CM framework via the cmind PyPI package.
Please follow [this guide](https://access.cknowledge.org/playground/?action=install) 
to install and start using it.

If you encounter any issues or have suggestions, please don't hesitate 
to [open a GitHub ticket](https://github.com/mlcommons/ck)
or contact the [CMX author](mailto:gfursin@mlcommons.org).

## News

### 202502: CMX V4.0.0 release

We have released a new version 4.0.0 of CMX as a drop-in, backward-compatible
replacement for the earlier Collective Mind framework (CM) and other
MLCommons automations. Designed with user feedback in mind, CMX
offers a simpler, more robust interface. It is available alongside
Collective Mind (CM) in the Python cmind package:
[sources](https://github.com/mlcommons/ck/tree/master/cm), 
[pypi](https://pypi.org/project/cmind).

## Documentation

* [MLCommons website](https://docs.mlcommons.org/ck/cmx)
* [GitHub](https://github.com/mlcommons/ck/edit/master/cmx/TOC.md)

## License

[Apache 2.0](https://github.com/mlcommons/ck/blob/master/cm/LICENSE.md)

## Author

[Grigori Fursin](https://cKnowledge.org/gfursin).

We thank all our [contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTORS.md) 
for their invaluable feedback and support!

## Copyright

Copyright (c) 2024-2025 MLCommons

Grigori Fursin and the cTuning foundation donated this project to MLCommons to benefit everyone.

## Citation

If you found the CM/CMX automations for MLOps, DevOps and MLPerf helpful, kindly reference this article:
[ [ArXiv](https://arxiv.org/abs/2406.16791) ], [ [BibTex](https://github.com/mlcommons/ck/blob/master/citation.bib) ].

You are welcome to contact the [author](https://cKnowledge.org/gfursin) to discuss long-term plans and potential collaboration.
