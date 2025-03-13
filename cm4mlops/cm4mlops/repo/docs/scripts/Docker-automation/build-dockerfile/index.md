# build-dockerfile
Automatically generated README for this automation recipe: **build-dockerfile**

Category: **[Docker automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/build-dockerfile/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/build-dockerfile/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "build dockerfile" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=build,dockerfile[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "build dockerfile [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'build,dockerfile'
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
    cm docker script "build dockerfile[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_slim`
               - ENV variables:
                   - CM_DOCKER_BUILD_SLIM: `yes`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--build=value`  &rarr;  `CM_BUILD_DOCKER_IMAGE=value`
    * `--cache=value`  &rarr;  `CM_DOCKER_CACHE=value`
    * `--cm_repo=value`  &rarr;  `CM_MLOPS_REPO=value`
    * `--cm_repo_flags=value`  &rarr;  `CM_DOCKER_ADD_FLAG_TO_CM_MLOPS_REPO=value`
    * `--cm_repos=value`  &rarr;  `CM_DOCKER_EXTRA_CM_REPOS=value`
    * `--comments=value`  &rarr;  `CM_DOCKER_RUN_COMMENTS=value`
    * `--copy_files=value`  &rarr;  `CM_DOCKER_COPY_FILES=value`
    * `--docker_base_image=value`  &rarr;  `CM_DOCKER_IMAGE_BASE=value`
    * `--docker_os=value`  &rarr;  `CM_DOCKER_OS=value`
    * `--docker_os_version=value`  &rarr;  `CM_DOCKER_OS_VERSION=value`
    * `--extra_sys_deps=value`  &rarr;  `CM_DOCKER_EXTRA_SYS_DEPS=value`
    * `--fake_docker_deps=value`  &rarr;  `CM_DOCKER_FAKE_DEPS=value`
    * `--fake_run_option=value`  &rarr;  `CM_DOCKER_FAKE_RUN_OPTION=value`
    * `--file_path=value`  &rarr;  `CM_DOCKERFILE_WITH_PATH=value`
    * `--gh_token=value`  &rarr;  `CM_GH_TOKEN=value`
    * `--image_repo=value`  &rarr;  `CM_DOCKER_IMAGE_REPO=value`
    * `--image_tag=value`  &rarr;  `CM_DOCKER_IMAGE_TAG=value`
    * `--package_manager_update_cmd=value`  &rarr;  `CM_PACKAGE_MANAGER_UPDATE_CMD=value`
    * `--pip_extra_flags=value`  &rarr;  `CM_DOCKER_PIP_INSTALL_EXTRA_FLAGS=value`
    * `--post_file=value`  &rarr;  `DOCKER_IMAGE_POST_FILE=value`
    * `--post_run_cmds=value`  &rarr;  `CM_DOCKER_POST_RUN_COMMANDS=value`
    * `--pre_run_cmds=value`  &rarr;  `CM_DOCKER_PRE_RUN_COMMANDS=value`
    * `--push_image=value`  &rarr;  `CM_DOCKER_PUSH_IMAGE=value`
    * `--real_run=value`  &rarr;  `CM_REAL_RUN=value`
    * `--run_cmd=value`  &rarr;  `CM_DOCKER_RUN_CMD=value`
    * `--run_cmd_extra=value`  &rarr;  `CM_DOCKER_RUN_CMD_EXTRA=value`
    * `--script_tags=value`  &rarr;  `CM_DOCKER_RUN_SCRIPT_TAGS=value`
    * `--skip_cm_sys_upgrade=value`  &rarr;  `CM_DOCKER_SKIP_CM_SYS_UPGRADE=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_DOCKER_BUILD_SLIM: `no`
    * CM_DOCKER_IMAGE_EOL: `
`
    * CM_DOCKER_OS: `ubuntu`



___
#### Script output
```bash
cmr "build dockerfile [variations]" [--input_flags] -j
```