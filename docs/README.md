# CM documentation

**We plan to rewrite and simplify the CM documentation and tutorials based on user feedback in Q3 2024 - please stay tuned for more details**.

Collective Mind (CM) is a lightweight, non-intrusive and technology-agnostic workflow automation framework 
being developed by the [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
based on the feedback from the [the community, MLCommons members and individual contributors](../CONTRIBUTING.md).

The goal is to provide a common, simple and human-readable interface to help users encode their knowledge
about how to build, run and customize diverse AI/ML apps, benchmarks and research projects across 
continuously changing models, datasets, software and hardware from different vendors in a unified and automated way.

You can find on-going development tasks [here](https://github.com/mlcommons/ck/blob/dev/docs/taskforce.md#current-tasks).

* [Getting Started Guide and FAQ](getting-started.md)
* [Introduction](introduction-cm.md)
* [CM installation and customization](installation.md)
* [Unified CLI and Python API](interface.md)
  * [CM framework core API](https://cknowledge.org/docs/cm)
  * [CM "script" automation](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/script/README-extra.md)
  * [CM "cache" automation](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/cache/README-extra.md)
  * [CM "experiment" automation](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/experiment/README-extra.md)
  * [List of all unified CM automations from MLCommons](list_of_automations.md)
  * [List of all portable and reusable CM scripts from MLCommons](https://access.cknowledge.org/playground/?action=scripts)
    * The most commonly used CM scripts (basic blocks needed for most portable and tech-agnostic automation workflows)
      * [detect OS](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
      * [detect CPU](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
      * [install system deps for CM](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
        * [install min system deps for Windows](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min)
      * [download file](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/download-file/README-extra.md)
      * [extract file](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/extract-file/README-extra.md)
      * [download and extract file](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/download-and-extract-file/README-extra.md)
      * [detect or install python](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
      * [install/manage multiple python venv](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-venv)
      * [detect conda manager](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-conda)
      * [detect/download COCO dataset](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco/README-extra.md)
* [Debugging](debugging.md)
* [Real-world use cases](use-cases.md)
* [Tutorials](tutorials/README.md)
* [Specifications](specs/README.md)
* [Source code](https://github.com/mlcommons/ck/tree/master/cm/cmind)
* [FAQ](faq.md)
* [CM and CK history](history.md)
