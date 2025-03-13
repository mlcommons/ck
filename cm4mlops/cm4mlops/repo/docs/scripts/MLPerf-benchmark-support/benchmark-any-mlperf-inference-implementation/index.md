# benchmark-any-mlperf-inference-implementation
Automatically generated README for this automation recipe: **benchmark-any-mlperf-inference-implementation**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-any-mlperf-inference-implementation/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=benchmark,run,natively,all,inference,any,mlperf,mlperf-implementation,implementation,mlperf-models[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'benchmark,run,natively,all,inference,any,mlperf,mlperf-implementation,implementation,mlperf-models'
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
    cm docker script "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * Group "**implementation**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_deepsparse`
               - ENV variables:
                   - DIVISION: `open`
                   - IMPLEMENTATION: `deepsparse`
        * `_intel`
               - ENV variables:
                   - IMPLEMENTATION: `intel`
        * `_mil`
               - ENV variables:
                   - IMPLEMENTATION: `mil`
        * `_nvidia`
               - ENV variables:
                   - IMPLEMENTATION: `nvidia-original`
        * `_qualcomm`
               - ENV variables:
                   - IMPLEMENTATION: `qualcomm`
        * `_reference`
               - ENV variables:
                   - IMPLEMENTATION: `reference`
        * `_tflite-cpp`
               - ENV variables:
                   - IMPLEMENTATION: `tflite_cpp`

        </details>


      * Group "**power**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_performance-only`** (default)
        * `_power`
               - ENV variables:
                   - POWER: `True`

        </details>


      * Group "**sut**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_aws-dl2q.24xlarge`
        * `_macbookpro-m1`
               - ENV variables:
                   - CATEGORY: `edge`
                   - DIVISION: `closed`
        * `_mini`
        * `_orin`
        * `_orin.32g`
               - ENV variables:
                   - CATEGORY: `edge`
                   - DIVISION: `closed`
        * `_phoenix`
               - ENV variables:
                   - CATEGORY: `edge`
                   - DIVISION: `closed`
        * `_rb6`
        * `_rpi4`
        * `_sapphire-rapids.24c`
               - ENV variables:
                   - CATEGORY: `edge`
                   - DIVISION: `closed`

        </details>


    ##### Default variations

    `_performance-only`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--backends=value`  &rarr;  `BACKENDS=value`
    * `--category=value`  &rarr;  `CATEGORY=value`
    * `--devices=value`  &rarr;  `DEVICES=value`
    * `--division=value`  &rarr;  `DIVISION=value`
    * `--extra_args=value`  &rarr;  `EXTRA_ARGS=value`
    * `--models=value`  &rarr;  `MODELS=value`
    * `--power_server=value`  &rarr;  `POWER_SERVER=value`
    * `--power_server_port=value`  &rarr;  `POWER_SERVER_PORT=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * DIVISION: `open`
    * CATEGORY: `edge`



#### Native script being run
=== "Linux/macOS"
     * [run-template.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-any-mlperf-inference-implementation/run-template.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models [variations]" [--input_flags] -j
```