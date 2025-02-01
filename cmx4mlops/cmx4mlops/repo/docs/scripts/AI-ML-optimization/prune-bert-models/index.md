# prune-bert-models
Automatically generated README for this automation recipe: **prune-bert-models**

Category: **[AI/ML optimization](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/prune-bert-models/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/prune-bert-models/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "prune bert-models bert-prune prune-bert-models" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=prune,bert-models,bert-prune,prune-bert-models[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "prune bert-models bert-prune prune-bert-models [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'prune,bert-models,bert-prune,prune-bert-models'
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
    cm docker script "prune bert-models bert-prune prune-bert-models[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_model.#`
               - ENV variables:
                   - CM_BERT_PRUNE_MODEL_NAME: `#`
                   - CM_MODEL_ZOO_STUB: `#`
        * `_path.#`
               - ENV variables:
                   - CM_BERT_PRUNE_CKPT_PATH: `#`
        * `_task.#`
               - ENV variables:
                   - CM_BERT_PRUNE_TASK: `#`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--constraint=value`  &rarr;  `CM_BERT_PRUNE_CONSTRAINT=value`
    * `--output_dir=value`  &rarr;  `CM_BERT_PRUNE_OUTPUT_DIR=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_BERT_PRUNE_TASK: `squad`
    * CM_BERT_PRUNE_MODEL_NAME: `bert-large-uncased`
    * CM_MODEL_ZOO_STUB: `bert-large-uncased`
    * CM_BERT_PRUNE_CONSTRAINT: `0.5`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/prune-bert-models/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "prune bert-models bert-prune prune-bert-models [variations]" [--input_flags] -j
```