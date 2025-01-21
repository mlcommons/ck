# run-mlperf-power-server
Automatically generated README for this automation recipe: **run-mlperf-power-server**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-power-server/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-power-server/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "run mlc mlcommons mlperf power server power-server" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=run,mlc,mlcommons,mlperf,power,server,power-server [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "run mlc mlcommons mlperf power server power-server " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mlc,mlcommons,mlperf,power,server,power-server'
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
    cm docker script "run mlc mlcommons mlperf power server power-server" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--device_port=value`  &rarr;  `CM_MLPERF_POWER_DEVICE_PORT=value`
    * `--device_type=value`  &rarr;  `CM_MLPERF_POWER_DEVICE_TYPE=value`
    * `--interface_flag=value`  &rarr;  `CM_MLPERF_POWER_INTERFACE_FLAG=value`
    * `--ntp_server=value`  &rarr;  `CM_MLPERF_POWER_NTP_SERVER=value`
    * `--screen=value`  &rarr;  `CM_MLPERF_POWER_SERVER_USE_SCREEN=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_MLPERF_POWER_NTP_SERVER: `time.google.com`
    * CM_MLPERF_POWER_INTERFACE_FLAG: ``
    * CM_MLPERF_POWER_DEVICE_TYPE: `49`
    * CM_MLPERF_POWER_SERVER_ADDRESS: `0.0.0.0`
    * CM_MLPERF_POWER_SERVER_PORT: `4950`
    * CM_MLPERF_POWER_DEVICE_PORT: `/dev/usbtmc0`
    * CM_MLPERF_POWER_SERVER_USE_SCREEN: `no`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-power-server/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-power-server/run.bat)
___
#### Script output
```bash
cmr "run mlc mlcommons mlperf power server power-server " [--input_flags] -j
```