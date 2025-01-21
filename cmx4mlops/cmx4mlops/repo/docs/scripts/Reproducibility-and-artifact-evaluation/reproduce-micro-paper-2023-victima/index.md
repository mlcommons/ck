# reproduce-micro-paper-2023-victima
Automatically generated README for this automation recipe: **reproduce-micro-paper-2023-victima**

Category: **[Reproducibility and artifact evaluation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-micro-paper-2023-victima/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-micro-paper-2023-victima/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "reproduce project paper micro micro-2023 victima" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=reproduce,project,paper,micro,micro-2023,victima[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "reproduce project paper micro micro-2023 victima [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,project,paper,micro,micro-2023,victima'
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
    cm docker script "reproduce project paper micro micro-2023 victima[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_install_deps`
        * `_plot`
        * `_run`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--container=value`  &rarr;  `CM_VICTIMA_CONTAINER=value`
    * `--job_manager=value`  &rarr;  `CM_VICTIMA_JOB_MANAGER=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_VICTIMA_JOB_MANAGER: `native`
    * CM_VICTIMA_CONTAINER: `docker`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-micro-paper-2023-victima/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "reproduce project paper micro micro-2023 victima [variations]" [--input_flags] -j
```