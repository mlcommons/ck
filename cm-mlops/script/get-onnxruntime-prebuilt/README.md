**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-onnxruntime-prebuilt).**



Automatically generated README for this automation recipe: **get-onnxruntime-prebuilt**

Category: **AI/ML frameworks**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-onnxruntime-prebuilt,be02c84ff57c4244) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-onnxruntime-prebuilt)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp*
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

````cmr "install onnxruntime get prebuilt lib lang-c lang-cpp" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp`

`cm run script --tags=install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp[,variations] `

*or*

`cmr "install onnxruntime get prebuilt lib lang-c lang-cpp"`

`cmr "install onnxruntime get prebuilt lib lang-c lang-cpp [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp'
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

```cmr "cm gui" --script="install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install onnxruntime get prebuilt lib lang-c lang-cpp[variations]" `

___
### Customization


#### Variations

  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_ONNXRUNTIME_DEVICE*: ``
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_ONNXRUNTIME_DEVICE*: `gpu`
      - Workflow:

    </details>


#### Default variations

`_cpu`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `1.16.3`

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-onnxruntime-prebuilt/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-onnxruntime-prebuilt/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-onnxruntime-prebuilt/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-onnxruntime-prebuilt/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-onnxruntime-prebuilt/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-onnxruntime-prebuilt/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-onnxruntime-prebuilt/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-onnxruntime-prebuilt/_cm.json)

___
### Script output
`cmr "install onnxruntime get prebuilt lib lang-c lang-cpp [,variations]"  -j`
#### New environment keys (filter)

* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+DYLD_FALLBACK_LIBRARY_PATH`
* `+LD_LIBRARY_PATH`
* `+PATH`
* `CM_ONNXRUNTIME_INCLUDE_PATH`
* `CM_ONNXRUNTIME_LIB_PATH`
#### New environment keys auto-detected from customize

* `CM_ONNXRUNTIME_INCLUDE_PATH`
* `CM_ONNXRUNTIME_LIB_PATH`