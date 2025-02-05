# run-mlperf-power-client
Automatically generated README for this automation recipe: **run-mlperf-power-client**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-power-client/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-power-client/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "run mlc mlcommons mlperf power client power-client" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=run,mlc,mlcommons,mlperf,power,client,power-client [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "run mlc mlcommons mlperf power client power-client " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mlc,mlcommons,mlperf,power,client,power-client'
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
    cm docker script "run mlc mlcommons mlperf power client power-client" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--loadgen_logs_dir=value`  &rarr;  `CM_MLPERF_LOADGEN_LOGS_DIR=value`
    * `--log_dir=value`  &rarr;  `CM_MLPERF_POWER_LOG_DIR=value`
    * `--max_amps=value`  &rarr;  `CM_MLPERF_POWER_MAX_AMPS=value`
    * `--max_volts=value`  &rarr;  `CM_MLPERF_POWER_MAX_VOLTS=value`
    * `--ntp_server=value`  &rarr;  `CM_MLPERF_POWER_NTP_SERVER=value`
    * `--port=value`  &rarr;  `CM_MLPERF_POWER_SERVER_PORT=value`
    * `--power_server=value`  &rarr;  `CM_MLPERF_POWER_SERVER_ADDRESS=value`
    * `--run_cmd=value`  &rarr;  `CM_MLPERF_RUN_CMD=value`
    * `--server=value`  &rarr;  `CM_MLPERF_POWER_SERVER_ADDRESS=value`
    * `--server_port=value`  &rarr;  `CM_MLPERF_POWER_SERVER_PORT=value`
    * `--timestamp=value`  &rarr;  `CM_MLPERF_POWER_TIMESTAMP=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_MLPERF_POWER_LOG_DIR: `logs`
    * CM_MLPERF_RUN_CMD: ``
    * CM_MLPERF_POWER_SERVER_ADDRESS: `localhost`
    * CM_MLPERF_POWER_NTP_SERVER: `time.google.com`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-power-client/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "run mlc mlcommons mlperf power client power-client " [--input_flags] -j
```