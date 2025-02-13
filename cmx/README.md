# Common Metadata eXchange (CMX)

The [Common Metadata eXchange framework (CMX)](https://github.com/mlcommons/ck/tree/master/cmx)
was developed to support open science and facilitate
collaborative, reproducible, and reusable research, development, 
and experimentation based on [FAIR principles](https://en.wikipedia.org/wiki/FAIR_data).

It helps users non-intrusively convert their software projects,
directories, and Git(Hub) repositories into file-based repositories
of portable and reusable artifacts (code, data, models, scripts) 
with extensible metadata, a unified command-line interface, 
and a simple Python API.

Such artifacts can be easily chained together into portable automation
workflows, enabling users to rerun, reproduce, and reuse complex
experimental setups across diverse and rapidly evolving models, datasets,
software, and hardware.

For example, you can run image classification and the MLPerf inference benchmark on Linux, macOS, 
and Windows using a few CMX commands as follows:

```bash
pip install cmind
cmx pull repo mlcommons@ck --dir=cmx4mlops/cmx4mlops
cmx run script "app image-classification python torch" --quiet
cmx run script "run-mlperf inference _performance-only _short" --model=resnet50 --precision=float32 --backend=onnxruntime --scenario=Offline --device=cpu --env.CM_SUDO_USER=no --quiet
cmx show cache
```

CMX extends the [Collective Knowledge (CK)](https://learning.acm.org/techtalks/reproducibility) 
and [Collective Mind (CM)](https://zenodo.org/records/8105339) concepts,
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

*Under preparation*

* [Installation (Linux, Windows, MacOS)](install.md)
* [Getting Started Guide](getting-started.md)
* [MLOps, DevOps and MLPerf automations](https://access.cknowledge.org/playground/?action=scripts)
* [High-level architecture](architecture-4.0.0.png)
* [Python API](https://cknowledge.org/docs/cmx)
* [Motivation](motivation.md)





## Author

[Grigori Fursin](https://cKnowledge.org/gfursin).

We thank all our [contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTORS.md) 
for their invaluable feedback and support!

## License

[Apache 2.0](https://github.com/mlcommons/ck/blob/master/cm/LICENSE.md)

## Copyright

Copyright (c) 2024-2025 MLCommons

Grigori Fursin and the cTuning foundation donated this project to MLCommons to benefit everyone.

## Concepts

To learn more about the motivation behind this project, please explore the following articles and presentations:

* HPCA'25 article "MLPerf Power: Benchmarking the Energy Efficiency of Machine Learning Systems from Microwatts to Megawatts for Sustainable AI": [ [Arxiv](https://arxiv.org/abs/2410.12032) ], [ [tutorial to reproduce results using CM/CMX](https://github.com/aryatschand/MLPerf-Power-HPCA-2025/blob/main/measurement_tutorial.md) ]
* "Enabling more efficient and cost-effective AI/ML systems with Collective Mind, virtualized MLOps, MLPerf, Collective Knowledge Playground and reproducible optimization tournaments": [ [ArXiv](https://arxiv.org/abs/2406.16791) ]
* ACM REP'23 keynote about the MLCommons CM automation framework: [ [slides](https://doi.org/10.5281/zenodo.8105339) ] 
* ACM TechTalk'21 about Collective Knowledge project: [ [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4) ] [ [slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2021/grigorifursin_techtalk_slides.pdf) ]
* Journal of Royal Society'20: [ [paper](https://royalsocietypublishing.org/doi/10.1098/rsta.2020.0211) ]

## Citation

If you found the CMX automations helpful, kindly reference this article:
[ [ArXiv](https://arxiv.org/abs/2406.16791) ], [ [BibTex](https://github.com/mlcommons/ck/blob/master/citation.bib) ].
