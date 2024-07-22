**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/set-device-settings-qaic).**



Automatically generated README for this automation recipe: **set-device-settings-qaic**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=set-device-settings-qaic,408a1a1563b44780) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-device-settings-qaic)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *set,device,qaic,ai100,cloud,performance,power,setting,mode,vc,ecc*
* Output cached? *False*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "set device qaic ai100 cloud performance power setting mode vc ecc" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=set,device,qaic,ai100,cloud,performance,power,setting,mode,vc,ecc`

`cm run script --tags=set,device,qaic,ai100,cloud,performance,power,setting,mode,vc,ecc[,variations] `

*or*

`cmr "set device qaic ai100 cloud performance power setting mode vc ecc"`

`cmr "set device qaic ai100 cloud performance power setting mode vc ecc [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'set,device,qaic,ai100,cloud,performance,power,setting,mode,vc,ecc'
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

```cmr "cm gui" --script="set,device,qaic,ai100,cloud,performance,power,setting,mode,vc,ecc"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=set,device,qaic,ai100,cloud,performance,power,setting,mode,vc,ecc) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "set device qaic ai100 cloud performance power setting mode vc ecc[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_ecc`
      - Environment variables:
        - *CM_QAIC_ECC*: `yes`
      - Workflow:
    * `_vc.#`
      - Environment variables:
        - *CM_QAIC_VC*: `#`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_QAIC_DEVICES: `0`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-device-settings-qaic/_cm.json)***
     * detect-os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,qaic,platform,sdk
       - CM script: [get-qaic-platform-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-qaic-platform-sdk)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-device-settings-qaic/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-device-settings-qaic/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-device-settings-qaic/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-device-settings-qaic/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-device-settings-qaic/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-device-settings-qaic/_cm.json)

___
### Script output
`cmr "set device qaic ai100 cloud performance power setting mode vc ecc [,variations]"  -j`
#### New environment keys (filter)

* `CM_QAIC_DEVICE_*`
#### New environment keys auto-detected from customize
