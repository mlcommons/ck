**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/install-cuda-prebuilt).**



Automatically generated README for this automation recipe: **install-cuda-prebuilt**

Category: **CUDA automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-cuda-prebuilt,14eadcd42ba340c3) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cuda-prebuilt)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda`

`cm run script --tags=install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda[,variations] [--input_flags]`

*or*

`cmr "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda"`

`cmr "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### Run this script via GUI

```cmr "cm gui" --script="install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda[variations]" [--input_flags]`

___
### Customization


#### Variations

  * Group "**install-driver**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_driver`
      - Environment variables:
        - *CM_CUDA_INSTALL_DRIVER*: `yes`
      - Workflow:
    * **`_no-driver`** (default)
      - Environment variables:
        - *CM_CUDA_INSTALL_DRIVER*: `no`
      - Workflow:

    </details>


#### Default variations

`_no-driver`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--local_run_file_path=value`  &rarr;  `CUDA_RUN_FILE_LOCAL_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "local_run_file_path":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_SUDO: `sudo`

</details>

#### Versions
Default version: `11.8.0`

* `11.7.0`
* `11.8.0`
* `12.0.0`
* `12.1.1`
* `12.2.0`
* `12.3.2`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cuda-prebuilt/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cuda-prebuilt/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cuda-prebuilt/_cm.json)***
     * download,file
       * CM names: `--adr.['download-script']...`
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cuda-prebuilt/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cuda-prebuilt/_cm.json)
  1. Run "postrocess" function from customize.py
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cuda-prebuilt/_cm.json)***
     * get,cuda
       * `if (CM_REQUIRE_INSTALL  != yes)`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)

___
### Script output
`cmr "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_CUDA_*`
* `CM_NVCC_*`
#### New environment keys auto-detected from customize

* `CM_CUDA_INSTALLED_PATH`
* `CM_NVCC_BIN_WITH_PATH`