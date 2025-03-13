# run-docker-container
Automatically generated README for this automation recipe: **run-docker-container**

Category: **[Docker automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/run-docker-container/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/run-docker-container/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "run docker container" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=run,docker,container [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "run docker container " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,docker,container'
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
    cm docker script "run docker container" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--all_gpus=value`  &rarr;  `CM_DOCKER_ADD_ALL_GPUS=value`
    * `--base=value`  &rarr;  `CM_DOCKER_IMAGE_BASE=value`
    * `--cache=value`  &rarr;  `CM_DOCKER_CACHE=value`
    * `--cm_repo=value`  &rarr;  `CM_MLOPS_REPO=value`
    * `--detached=value`  &rarr;  `CM_DOCKER_DETACHED_MODE=value`
    * `--device=value`  &rarr;  `CM_DOCKER_ADD_DEVICE=value`
    * `--docker_image_base=value`  &rarr;  `CM_DOCKER_IMAGE_BASE=value`
    * `--docker_os=value`  &rarr;  `CM_DOCKER_OS=value`
    * `--docker_os_version=value`  &rarr;  `CM_DOCKER_OS_VERSION=value`
    * `--extra_run_args=value`  &rarr;  `CM_DOCKER_EXTRA_RUN_ARGS=value`
    * `--fake_run_option=value`  &rarr;  `CM_DOCKER_FAKE_RUN_OPTION=value`
    * `--gh_token=value`  &rarr;  `CM_GH_TOKEN=value`
    * `--image_name=value`  &rarr;  `CM_DOCKER_IMAGE_NAME=value`
    * `--image_repo=value`  &rarr;  `CM_DOCKER_IMAGE_REPO=value`
    * `--image_tag=value`  &rarr;  `CM_DOCKER_IMAGE_TAG=value`
    * `--image_tag_extra=value`  &rarr;  `CM_DOCKER_IMAGE_TAG_EXTRA=value`
    * `--interactive=value`  &rarr;  `CM_DOCKER_INTERACTIVE_MODE=value`
    * `--it=value`  &rarr;  `CM_DOCKER_INTERACTIVE=value`
    * `--mounts=value`  &rarr;  `CM_DOCKER_VOLUME_MOUNTS=value`
    * `--num_gpus=value`  &rarr;  `CM_DOCKER_ADD_NUM_GPUS=value`
    * `--pass_user_group=value`  &rarr;  `CM_DOCKER_PASS_USER_GROUP=value`
    * `--port_maps=value`  &rarr;  `CM_DOCKER_PORT_MAPS=value`
    * `--post_run_cmds=value`  &rarr;  `CM_DOCKER_POST_RUN_COMMANDS=value`
    * `--pre_run_cmds=value`  &rarr;  `CM_DOCKER_PRE_RUN_COMMANDS=value`
    * `--real_run=value`  &rarr;  `CM_REAL_RUN=value`
    * `--recreate=value`  &rarr;  `CM_DOCKER_IMAGE_RECREATE=value`
    * `--run_cmd=value`  &rarr;  `CM_DOCKER_RUN_CMD=value`
    * `--run_cmd_extra=value`  &rarr;  `CM_DOCKER_RUN_CMD_EXTRA=value`
    * `--save_script=value`  &rarr;  `CM_DOCKER_SAVE_SCRIPT=value`
    * `--script_tags=value`  &rarr;  `CM_DOCKER_RUN_SCRIPT_TAGS=value`
    * `--shm_size=value`  &rarr;  `CM_DOCKER_SHM_SIZE=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_DOCKER_DETACHED_MODE: `yes`



___
#### Script output
```bash
cmr "run docker container " [--input_flags] -j
```