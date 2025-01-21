# build-mlperf-inference-server-nvidia
Automatically generated README for this automation recipe: **build-mlperf-inference-server-nvidia**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/build-mlperf-inference-server-nvidia/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/build-mlperf-inference-server-nvidia/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "build mlcommons mlperf inference inference-server server nvidia-harness nvidia" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "build mlcommons mlperf inference inference-server server nvidia-harness nvidia [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia'
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
    cm docker script "build mlcommons mlperf inference inference-server server nvidia-harness nvidia[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * Group "**code**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_ctuning`** (default)
        * `_custom`
        * `_go`
        * `_mlcommons`
        * `_nvidia-only`

        </details>


      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_cpu`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `cpu`
        * **`_cuda`** (default)
               - ENV variables:
                   - CM_MLPERF_DEVICE: `cuda`
                   - CM_MLPERF_DEVICE_LIB_NAMESPEC: `cudart`
        * `_inferentia`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `inferentia`

        </details>


      * Group "**version**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_r4.0`

        </details>


    ##### Default variations

    `_ctuning,_cuda`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--clean=value`  &rarr;  `CM_MAKE_CLEAN=value`
    * `--custom_system=value`  &rarr;  `CM_CUSTOM_SYSTEM_NVIDIA=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_MAKE_BUILD_COMMAND: `build`
    * CM_MAKE_CLEAN: `no`
    * CM_CUSTOM_SYSTEM_NVIDIA: `yes`


#### Versions
Default version: `r3.1`

* `r2.1`
* `r3.0`
* `r3.1`
* `r4.0`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/build-mlperf-inference-server-nvidia/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "build mlcommons mlperf inference inference-server server nvidia-harness nvidia [variations]" [--input_flags] -j
```