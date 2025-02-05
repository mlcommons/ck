# get-ml-model-huggingface-zoo
Automatically generated README for this automation recipe: **get-ml-model-huggingface-zoo**

Category: **[AI/ML models](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-huggingface-zoo/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-huggingface-zoo/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model huggingface zoo" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,ml-model,huggingface,zoo[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get ml-model huggingface zoo [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,huggingface,zoo'
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
    cm docker script "get ml-model huggingface zoo[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_model-stub.#`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `#`
        * `_onnx-subfolder`
               - ENV variables:
                   - CM_HF_SUBFOLDER: `onnx`
        * `_pierreguillou_bert_base_cased_squad_v1.1_portuguese`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `pierreguillou/bert-base-cased-squad-v1.1-portuguese`
        * `_prune`
               - ENV variables:
                   - CM_MODEL_TASK: `prune`

        </details>


      * Group "**download-type**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_clone-repo`
               - ENV variables:
                   - CM_GIT_CLONE_REPO: `yes`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
    * `--env_key=value`  &rarr;  `CM_MODEL_ZOO_ENV_KEY=value`
    * `--full_subfolder=value`  &rarr;  `CM_HF_FULL_SUBFOLDER=value`
    * `--model_filename=value`  &rarr;  `CM_MODEL_ZOO_FILENAME=value`
    * `--revision=value`  &rarr;  `CM_HF_REVISION=value`
    * `--subfolder=value`  &rarr;  `CM_HF_SUBFOLDER=value`




#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-huggingface-zoo/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-huggingface-zoo/run.bat)
___
#### Script output
```bash
cmr "get ml-model huggingface zoo [variations]" [--input_flags] -j
```