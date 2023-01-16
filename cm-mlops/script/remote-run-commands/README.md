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
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys](#new-environment-keys)
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *Remote automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh(,variations from below) (flags from below)`

*or*

`cm run script "remote run cmds remote-run remote-run-cmds ssh-run ssh (variations from below)" (flags from below)`

*or*

`cm run script b71e24b03c9d49cd`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh'
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


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**host**=value --> **CM_SSH_HOST**=value
* --**port**=value --> **CM_SSH_PORT**=value
* --**skip_host_verify**=value --> **CM_SSH_SKIP_HOST_VERIFY**=value
* --**client_refresh**=value --> **CM_SSH_CLIENT_REFRESH**=value
* --**run_cmds**=value --> **CM_SSH_RUN_COMMANDS**=value
* --**user**=value --> **CM_SSH_USER**=value
* --**password**=value --> **CM_SSH_PASSWORD**=value
* --**ssh_key_file**=value --> **CM_SSH_KEY_FILE**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "host":"..."}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_SSH_PORT: **22**
* CM_SSH_HOST: **localhost**
* CM_SSH_USER: **$USER**
* CM_SSH_CLIENT_REFRESH: **10**
* CM_SSH_KEY_FILE: **$HOME/.ssh/id_rsa**

</details>

___
### Script workflow, dependencies and native scripts

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/_cm.json)
___
### Script output
#### New environment keys

#### New environment keys auto-detected from customize

* **CM_SSH_CMD**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)