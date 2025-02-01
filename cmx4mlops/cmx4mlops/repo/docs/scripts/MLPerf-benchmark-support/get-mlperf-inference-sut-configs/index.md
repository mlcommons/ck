# get-mlperf-inference-sut-configs
Automatically generated README for this automation recipe: **get-mlperf-inference-sut-configs**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-sut-configs/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-sut-configs/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get mlperf inference sut configs sut-configs" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,mlperf,inference,sut,configs,sut-configs [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get mlperf inference sut configs sut-configs " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,mlperf,inference,sut,configs,sut-configs'
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
    cm docker script "get mlperf inference sut configs sut-configs" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--configs_git_url=value`  &rarr;  `CM_GIT_URL=value`
    * `--repo_path=value`  &rarr;  `CM_SUT_CONFIGS_PATH=value`
    * `--run_config=value`  &rarr;  `CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_SUT_CONFIGS_PATH: ``
    * CM_GIT_URL: ``



___
#### Script output
```bash
cmr "get mlperf inference sut configs sut-configs " [--input_flags] -j
```