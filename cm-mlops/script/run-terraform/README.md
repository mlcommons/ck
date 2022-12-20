*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Variations](#variations)
  * [ All variations](#all-variations)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
  * [ Script input flags mapped to environment](#script-input-flags-mapped-to-environment)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Cloud automation.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
run,terraform

___
### Variations
#### All variations
* aws
  - *ENV CM_TERRAFORM_CONFIG_DIR_NAME: aws*
* c5.12xlarge
  - *ENV TF_VAR_INSTANCE_TYPE: c5.12xlarge*
* c5.4xlarge
  - *ENV TF_VAR_INSTANCE_TYPE: c5.4xlarge*
  - *ENV TF_VAR_DISK_GBS: 80*
* c5d.9xlarge
  - *ENV TF_VAR_INSTANCE_TYPE: c5d.9xlarge*
* g4dn.xlarge
  - *ENV TF_VAR_INSTANCE_TYPE: g4dn.xlarge*
* t2.micro
  - *ENV TF_VAR_INSTANCE_TYPE: t2.micro*
___
### Default environment

* TF_VAR_SECURITY_GROUP_ID: **sg-0783752c97d2e011d**
* TF_VAR_CPU_COUNT: **1**
* TF_VAR_DISK_GBS: **8**
___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)***
     * get,terraform
       - CM script [get-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-terraform)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)***
     * destroy,terraform
       - CM script [destroy-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/destroy-terraform)
___
### New environment export

* **CM_TERRAFORM_CONFIG_DIR**
* **CM_TERRAFORM_RUN_DIR**
___
### New environment detected from customize

___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="run,terraform"`

*or*

`cm run script "run terraform"`

*or*

`cm run script ec344bd44af144d7`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,terraform'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* destroy --> **CM_DESTROY_TERRAFORM**
* cminit --> **CM_TERRAFORM_CM_INIT**
* key_file --> **CM_SSH_KEY_FILE**
* disk_size --> **TF_VAR_DISK_GBS**
* run_cmds --> **CM_TERRAFORM_RUN_COMMANDS**
* ssh_key_file --> **CM_SSH_KEY_FILE**

Examples:

```bash
cm run script "run terraform" --destroy=...
```
```python
r=cm.access({... , "destroy":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)