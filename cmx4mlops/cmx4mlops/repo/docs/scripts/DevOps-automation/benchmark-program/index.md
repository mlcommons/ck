# benchmark-program
Automatically generated README for this automation recipe: **benchmark-program**

Category: **[DevOps automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-program/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-program/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "benchmark program" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=benchmark,program[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "benchmark program [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'benchmark,program'
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
    cm docker script "benchmark program[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_numactl`
        * `_numactl-interleave`
        * `_profile`

        </details>

=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_ENABLE_NUMACTL: `0`
    * CM_ENABLE_PROFILING: `0`



#### Native script being run
=== "Linux/macOS"
     * [run-ubuntu.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-program/run-ubuntu.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-program/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-program/run.bat)
___
#### Script output
```bash
cmr "benchmark program [variations]"  -j
```