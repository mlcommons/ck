# build-docker-image
Automatically generated README for this automation recipe: **build-docker-image**

Category: **[Docker automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/build-docker-image/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/build-docker-image/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "build docker image docker-image dockerimage" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=build,docker,image,docker-image,dockerimage [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "build docker image docker-image dockerimage " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'build,docker,image,docker-image,dockerimage'
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
    cm docker script "build docker image docker-image dockerimage" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--cache=value`  &rarr;  `CM_DOCKER_CACHE=value`
    * `--cm_repo=value`  &rarr;  `CM_MLOPS_REPO=value`
    * `--docker_os=value`  &rarr;  `CM_DOCKER_OS=value`
    * `--docker_os_version=value`  &rarr;  `CM_DOCKER_OS_VERSION=value`
    * `--dockerfile=value`  &rarr;  `CM_DOCKERFILE_WITH_PATH=value`
    * `--gh_token=value`  &rarr;  `CM_GH_TOKEN=value`
    * `--image_name=value`  &rarr;  `CM_DOCKER_IMAGE_NAME=value`
    * `--image_repo=value`  &rarr;  `CM_DOCKER_IMAGE_REPO=value`
    * `--image_tag=value`  &rarr;  `CM_DOCKER_IMAGE_TAG=value`
    * `--post_run_cmds=value`  &rarr;  `CM_DOCKER_POST_RUN_COMMANDS=value`
    * `--pre_run_cmds=value`  &rarr;  `CM_DOCKER_PRE_RUN_COMMANDS=value`
    * `--push_image=value`  &rarr;  `CM_DOCKER_PUSH_IMAGE=value`
    * `--real_run=value`  &rarr;  `CM_REAL_RUN=value`
    * `--script_tags=value`  &rarr;  `CM_DOCKER_RUN_SCRIPT_TAGS=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_DOCKER_IMAGE_REPO: `local`
    * CM_DOCKER_IMAGE_TAG: `latest`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/build-docker-image/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/build-docker-image/run.bat)
___
#### Script output
```bash
cmr "build docker image docker-image dockerimage " [--input_flags] -j
```