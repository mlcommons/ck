# print-any-text
Automatically generated README for this automation recipe: **print-any-text**

Category: **[Tests](..)**

License: **Apache 2.0**

Developers: Grigori Fursin

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/print-any-text/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "print any-text" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=print,any-text[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "print any-text [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'print,any-text'
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
    cm docker script "print any-text[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_cm_env.#`
               - ENV variables:
                   - CM_PRINT_ANY_CM_ENV_KEYS: `#`
        * `_os_env.#`
               - ENV variables:
                   - CM_PRINT_ANY_OS_ENV_KEYS: `#`
        * `_text.#`
               - ENV variables:
                   - CM_PRINT_ANY_TEXT: `#`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--cm_env_keys=value`  &rarr;  `CM_PRINT_ANY_CM_ENV_KEYS=value`
    * `--os_env_keys=value`  &rarr;  `CM_PRINT_ANY_OS_ENV_KEYS=value`
    * `--text=value`  &rarr;  `CM_PRINT_ANY_TEXT=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_PRINT_ANY_TEXT: ``



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/print-any-text/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/print-any-text/run.bat)
___
#### Script output
```bash
cmr "print any-text [variations]" [--input_flags] -j
```