<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
* [Customization](#customization)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *Remote automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh [--input_flags]`

2. `cmr "remote run cmds remote-run remote-run-cmds ssh-run ssh" [--input_flags]`

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "remote run cmds remote-run remote-run-cmds ssh-run ssh" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--client_refresh=value`  &rarr;  `CM_SSH_CLIENT_REFRESH=value`
* `--host=value`  &rarr;  `CM_SSH_HOST=value`
* `--password=value`  &rarr;  `CM_SSH_PASSWORD=value`
* `--port=value`  &rarr;  `CM_SSH_PORT=value`
* `--run_cmds=value`  &rarr;  `CM_SSH_RUN_COMMANDS=value`
* `--skip_host_verify=value`  &rarr;  `CM_SSH_SKIP_HOST_VERIFY=value`
* `--ssh_key_file=value`  &rarr;  `CM_SSH_KEY_FILE=value`
* `--user=value`  &rarr;  `CM_SSH_USER=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "client_refresh":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_SSH_PORT: `22`
* CM_SSH_HOST: `localhost`
* CM_SSH_USER: `$USER`
* CM_SSH_CLIENT_REFRESH: `10`
* CM_SSH_KEY_FILE: `$HOME/.ssh/id_rsa`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/_cm.json)
</details>

___
### Script output
`cmr "remote run cmds remote-run remote-run-cmds ssh-run ssh" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)