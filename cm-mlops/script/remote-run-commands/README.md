**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/remote-run-commands).**



Automatically generated README for this automation recipe: **remote-run-commands**

Category: **Remote automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=remote-run-commands,b71e24b03c9d49cd) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/remote-run-commands)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh*
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

````cmr "remote run cmds remote-run remote-run-cmds ssh-run ssh" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh`

`cm run script --tags=remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh [--input_flags]`

*or*

`cmr "remote run cmds remote-run remote-run-cmds ssh-run ssh"`

`cmr "remote run cmds remote-run remote-run-cmds ssh-run ssh " [--input_flags]`


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
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/remote-run-commands/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/remote-run-commands/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/remote-run-commands/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/remote-run-commands/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/remote-run-commands/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/remote-run-commands/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/remote-run-commands/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/remote-run-commands/_cm.json)

___
### Script output
`cmr "remote run cmds remote-run remote-run-cmds ssh-run ssh " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
