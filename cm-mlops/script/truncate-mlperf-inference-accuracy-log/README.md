*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Script workflow](#script-workflow)
* [Usage](#usage)
* [ CM installation](#-cm-installation)
* [ CM script help](#-cm-script-help)
* [ CM CLI](#-cm-cli)
* [ CM Python API](#-cm-python-api)
* [ CM modular Docker container](#-cm-modular-docker-container)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Modular MLPerf benchmarks.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
run,mlc,mlcommons,mlperf,inference,mlperf-inference,truncation,truncator,truncate,accuracy,accuracy-log,accuracy-log-trancation,accuracy-log-truncator,mlc-accuracy-log-trancation,mlc-accuracy-log-truncator

___
### Script workflow

  #### Meta: "deps" key

  #### customize.py: "preprocess" function

  #### Meta: "prehook_deps" key

  #### Native script (run.sh or run.bat)

  #### Meta: "posthook_deps" key

  #### customize.py: "postprocess" function

  #### Meta: "post_deps" key

___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script help
```cm run script --help```

#### CM CLI
`cm run script --tags="run,mlc,mlcommons,mlperf,inference,mlperf-inference,truncation,truncator,truncate,accuracy,accuracy-log,accuracy-log-trancation,accuracy-log-truncator,mlc-accuracy-log-trancation,mlc-accuracy-log-truncator"`

*or*

`cm run script "run mlc mlcommons mlperf inference mlperf-inference truncation truncator truncate accuracy accuracy-log accuracy-log-trancation accuracy-log-truncator mlc-accuracy-log-trancation mlc-accuracy-log-truncator"`

*or*

`cm run script 9d5ec20434084d14`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mlc,mlcommons,mlperf,inference,mlperf-inference,truncation,truncator,truncate,accuracy,accuracy-log,accuracy-log-trancation,accuracy-log-truncator,mlc-accuracy-log-trancation,mlc-accuracy-log-truncator'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)