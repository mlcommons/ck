*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

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

Tests.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-py)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
print,hello world,hello-world,hello,world,python

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
`cm run script --tags="print,hello world,hello-world,hello,world,python"`

*or*

`cm run script "print hello world hello-world hello world python"`

*or*

`cm run script d83274c7eb754d90`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'print,hello world,hello-world,hello,world,python'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)