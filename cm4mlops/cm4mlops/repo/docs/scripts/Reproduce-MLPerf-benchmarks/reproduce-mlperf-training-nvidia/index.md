# reproduce-mlperf-training-nvidia
Automatically generated README for this automation recipe: **reproduce-mlperf-training-nvidia**

Category: **[Reproduce MLPerf benchmarks](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-training-nvidia/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "reproduce mlcommons mlperf train training nvidia-training nvidia" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "reproduce mlcommons mlperf train training nvidia-training nvidia [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia'
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
    cm docker script "reproduce mlcommons mlperf train training nvidia-training nvidia[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * Group "**benchmark**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_resnet`
               - ENV variables:
                   - CM_MLPERF_TRAINING_BENCHMARK: `resnet`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--results_dir=value`  &rarr;  `CM_MLPERF_RESULTS_DIR=value`
    * `--system_conf_name=value`  &rarr;  `CM_MLPERF_NVIDIA_TRAINING_SYSTEM_CONF_NAME=value`



#### Versions
* `r2.1`
* `r3.0`

#### Native script being run
=== "Linux/macOS"
     * [run-resnet.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-training-nvidia/run-resnet.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-training-nvidia/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "reproduce mlcommons mlperf train training nvidia-training nvidia [variations]" [--input_flags] -j
```