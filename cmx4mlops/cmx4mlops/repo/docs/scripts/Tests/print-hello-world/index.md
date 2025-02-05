# print-hello-world
Automatically generated README for this automation recipe: **print-hello-world**

Category: **[Tests](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/print-hello-world/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "print hello-world hello world hello world native-script native script" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=print,hello-world,hello world,hello,world,native-script,native,script[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "print hello-world hello world hello world native-script native script [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'print,hello-world,hello world,hello,world,native-script,native,script'
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
    cm docker script "print hello-world hello world hello world native-script native script[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_skip_print_env`
               - ENV variables:
                   - CM_PRINT_HELLO_WORLD_SKIP_PRINT_ENV: `yes`
        * `_text.#`
               - ENV variables:
                   - CM_PRINT_HELLO_WORLD_TEXT: `#`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--test1=value`  &rarr;  `CM_ENV_TEST1=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_ENV_TEST1: `TEST1`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/print-hello-world/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/print-hello-world/run.bat)
___
#### Script output
```bash
cmr "print hello-world hello world hello world native-script native script [variations]" [--input_flags] -j
```