<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *Cloud automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *run,terraform*
* Output cached?: *True*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=run,terraform(,variations from below) (flags from below)`

*or*

`cm run script "run terraform (variations from below)" (flags from below)`

*or*

`cm run script ec344bd44af144d7`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,terraform'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>

#### CM modular Docker container
*TBD*
___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_aws`
      - Environment variables:
        - *CM_TERRAFORM_CONFIG_DIR_NAME*: `aws`
      - Workflow:
    * `_c5.12xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `c5.12xlarge`
      - Workflow:
    * `_c5.4xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `c5.4xlarge`
        - *TF_VAR_DISK_GBS*: `80`
      - Workflow:
    * `_c5d.9xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `c5d.9xlarge`
      - Workflow:
    * `_g4dn.xlarge`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `g4dn.xlarge`
      - Workflow:
    * `_t2.micro`
      - Environment variables:
        - *TF_VAR_INSTANCE_TYPE*: `t2.micro`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**cminit**=value --> **CM_TERRAFORM_CM_INIT**=value
* --**destroy**=value --> **CM_DESTROY_TERRAFORM**=value
* --**disk_size**=value --> **TF_VAR_DISK_GBS**=value
* --**key_file**=value --> **CM_SSH_KEY_FILE**=value
* --**run_cmds**=value --> **CM_TERRAFORM_RUN_COMMANDS**=value
* --**ssh_key_file**=value --> **CM_SSH_KEY_FILE**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "cminit":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* TF_VAR_SECURITY_GROUP_ID: **sg-0783752c97d2e011d**
* TF_VAR_CPU_COUNT: **1**
* TF_VAR_DISK_GBS: **8**

</details>

___
### Script workflow, dependencies and native scripts

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)***
     * get,terraform
       - CM script: [get-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-terraform)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)***
     * destroy,terraform
       * `if (CM_DESTROY_TERRAFORM  == on)`
       * CM names: `--adr.['destroy-cmd']...`
       - CM script: [destroy-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/destroy-terraform)
___
### Script output
#### New environment keys (filter)

* **CM_TERRAFORM_CONFIG_DIR**
* **CM_TERRAFORM_RUN_DIR**
#### New environment keys auto-detected from customize

* **CM_TERRAFORM_CONFIG_DIR**
* **CM_TERRAFORM_RUN_DIR**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)