*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
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

Remote automation.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh

___
### Default environment

* CM_SSH_PORT: **22**
* CM_SSH_HOST: **localhost**
* CM_SSH_USER: **$USER**
* CM_SSH_CLIENT_REFRESH: **10**
* CM_SSH_KEY_FILE: **$HOME/.ssh/id_rsa**
___
### CM script workflow

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
### New environment export

___
### New environment detected from customize

* **CM_SSH_CMD**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh"`

*or*

`cm run script "remote run cmds remote-run remote-run-cmds ssh-run ssh"`

*or*

`cm run script b71e24b03c9d49cd`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* host --> **CM_SSH_HOST**
* port --> **CM_SSH_PORT**
* skip_host_verify --> **CM_SSH_SKIP_HOST_VERIFY**
* client_refresh --> **CM_SSH_CLIENT_REFRESH**
* run_cmds --> **CM_SSH_RUN_COMMANDS**
* user --> **CM_SSH_USER**
* password --> **CM_SSH_PASSWORD**
* ssh_key_file --> **CM_SSH_KEY_FILE**

Examples:

```bash
cm run script "remote run cmds remote-run remote-run-cmds ssh-run ssh" --host=...
```
```python
r=cm.access({... , "host":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)