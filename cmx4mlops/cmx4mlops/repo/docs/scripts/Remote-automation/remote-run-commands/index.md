# remote-run-commands
Automatically generated README for this automation recipe: **remote-run-commands**

Category: **[Remote automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/remote-run-commands/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/remote-run-commands/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "remote run cmds remote-run remote-run-cmds ssh-run ssh" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "remote run cmds remote-run remote-run-cmds ssh-run ssh " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


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


=== "Docker"
    ##### Run this script via Docker (beta)

    ```bash
    cm docker script "remote run cmds remote-run remote-run-cmds ssh-run ssh" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--client_refresh=value`  &rarr;  `CM_SSH_CLIENT_REFRESH=value`
    * `--host=value`  &rarr;  `CM_SSH_HOST=value`
    * `--password=value`  &rarr;  `CM_SSH_PASSWORD=value`
    * `--port=value`  &rarr;  `CM_SSH_PORT=value`
    * `--run_cmds=value`  &rarr;  `CM_SSH_RUN_COMMANDS=value`
    * `--skip_host_verify=value`  &rarr;  `CM_SSH_SKIP_HOST_VERIFY=value`
    * `--ssh_key_file=value`  &rarr;  `CM_SSH_KEY_FILE=value`
    * `--user=value`  &rarr;  `CM_SSH_USER=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_SSH_PORT: `22`
    * CM_SSH_HOST: `localhost`
    * CM_SSH_USER: `$USER`
    * CM_SSH_CLIENT_REFRESH: `10`
    * CM_SSH_KEY_FILE: `$HOME/.ssh/id_rsa`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/remote-run-commands/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/remote-run-commands/run.bat)
___
#### Script output
```bash
cmr "remote run cmds remote-run remote-run-cmds ssh-run ssh " [--input_flags] -j
```