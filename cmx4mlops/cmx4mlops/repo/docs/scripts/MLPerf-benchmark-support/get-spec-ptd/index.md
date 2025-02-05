# get-spec-ptd
Automatically generated README for this automation recipe: **get-spec-ptd**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-spec-ptd/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-spec-ptd/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get spec ptd ptdaemon power daemon power-daemon mlperf mlcommons" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,spec,ptd,ptdaemon,power,daemon,power-daemon,mlperf,mlcommons [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get spec ptd ptdaemon power daemon power-daemon mlperf mlcommons " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,spec,ptd,ptdaemon,power,daemon,power-daemon,mlperf,mlcommons'
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
    cm docker script "get spec ptd ptdaemon power daemon power-daemon mlperf mlcommons" [--input_flags]
    ```
___

=== "Input Flags"


    #### Input Flags

    * --**input:** Path to SPEC PTDaemon (Optional)
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--input=value`  &rarr;  `CM_INPUT=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_GIT_CHECKOUT: `main`
    * CM_GIT_DEPTH: `--depth 1`
    * CM_GIT_PATCH: `no`
    * CM_GIT_RECURSE_SUBMODULES: ` `
    * CM_GIT_URL: `https://github.com/mlcommons/power.git`


#### Versions
Default version: `main`

* `custom`
* `main`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-spec-ptd/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get spec ptd ptdaemon power daemon power-daemon mlperf mlcommons " [--input_flags] -j
```