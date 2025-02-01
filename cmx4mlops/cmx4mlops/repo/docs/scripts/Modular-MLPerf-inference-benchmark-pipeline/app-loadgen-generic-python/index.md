# app-loadgen-generic-python
Automatically generated README for this automation recipe: **app-loadgen-generic-python**

Category: **[Modular MLPerf inference benchmark pipeline](..)**

License: **Apache 2.0**

Developers: [Gaz Iqbal](https://www.linkedin.com/in/gaziqbal), [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), [Grigori Fursin](https://cKnowledge.org/gfursin)
* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/app-loadgen-generic-python/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/app-loadgen-generic-python/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "python app generic loadgen" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=python,app,generic,loadgen[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "python app generic loadgen [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'python,app,generic,loadgen'
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
    cm docker script "python app generic loadgen[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_cmc`
               - ENV variables:
                   - CM_CUSTOM_MODEL_CMC: `True`
        * `_huggingface`
               - ENV variables:
                   - CM_CUSTOM_MODEL_SOURCE: `huggingface`
        * `_model-stub.#`
               - ENV variables:
                   - CM_ML_MODEL_STUB: `#`

        </details>


      * Group "**backend**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_onnxruntime`** (default)
               - ENV variables:
                   - CM_MLPERF_BACKEND: `onnxruntime`
        * `_pytorch`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `pytorch`

        </details>


      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cpu`** (default)
               - ENV variables:
                   - CM_MLPERF_DEVICE: `cpu`
                   - CM_MLPERF_EXECUTION_PROVIDER: `CPUExecutionProvider`
        * `_cuda`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `gpu`
                   - CM_MLPERF_EXECUTION_PROVIDER: `CUDAExecutionProvider`

        </details>


      * Group "**models**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_custom`
               - ENV variables:
                   - CM_MODEL: `custom`
        * `_resnet50`
               - ENV variables:
                   - CM_MODEL: `resnet50`
        * `_retinanet`
               - ENV variables:
                   - CM_MODEL: `retinanet`

        </details>


    ##### Default variations

    `_cpu,_onnxruntime`
=== "Input Flags"


    #### Input Flags

    * --**modelpath:** Full path to file with model weights
    * --**modelcodepath:** (for PyTorch models) Full path to file with model code and cmc.py
    * --**modelcfgpath:** (for PyTorch models) Full path to JSON file with model cfg
    * --**modelsamplepath:** (for PyTorch models) Full path to file with model sample in pickle format
    * --**ep:** ONNX Execution provider
    * --**scenario:** MLPerf LoadGen scenario
    * --**samples:** Number of samples (*2*)
    * --**runner:** MLPerf runner
    * --**execmode:** MLPerf exec mode
    * --**output_dir:** MLPerf output directory
    * --**concurrency:** MLPerf concurrency
    * --**intraop:** MLPerf intra op threads
    * --**interop:** MLPerf inter op threads
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--concurrency=value`  &rarr;  `CM_MLPERF_CONCURRENCY=value`
    * `--ep=value`  &rarr;  `CM_MLPERF_EXECUTION_PROVIDER=value`
    * `--execmode=value`  &rarr;  `CM_MLPERF_EXEC_MODE=value`
    * `--interop=value`  &rarr;  `CM_MLPERF_INTEROP=value`
    * `--intraop=value`  &rarr;  `CM_MLPERF_INTRAOP=value`
    * `--loadgen_duration_sec=value`  &rarr;  `CM_MLPERF_LOADGEN_DURATION_SEC=value`
    * `--loadgen_expected_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_EXPECTED_QPS=value`
    * `--modelcfg=value`  &rarr;  `CM_ML_MODEL_CFG=value`
    * `--modelcfgpath=value`  &rarr;  `CM_ML_MODEL_CFG_WITH_PATH=value`
    * `--modelcodepath=value`  &rarr;  `CM_ML_MODEL_CODE_WITH_PATH=value`
    * `--modelpath=value`  &rarr;  `CM_ML_MODEL_FILE_WITH_PATH=value`
    * `--modelsamplepath=value`  &rarr;  `CM_ML_MODEL_SAMPLE_WITH_PATH=value`
    * `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`
    * `--runner=value`  &rarr;  `CM_MLPERF_RUNNER=value`
    * `--samples=value`  &rarr;  `CM_MLPERF_LOADGEN_SAMPLES=value`
    * `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_MLPERF_EXECUTION_MODE: `parallel`
    * CM_MLPERF_BACKEND: `onnxruntime`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-loadgen-generic-python/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/app-loadgen-generic-python/run.bat)
___
#### Script output
```bash
cmr "python app generic loadgen [variations]" [--input_flags] -j
```