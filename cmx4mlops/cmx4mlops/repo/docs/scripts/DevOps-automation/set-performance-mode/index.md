# set-performance-mode
Automatically generated README for this automation recipe: **set-performance-mode**

Category: **[DevOps automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/set-performance-mode/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "set system performance power mode" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=set,system,performance,power,mode[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "set system performance power mode [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'set,system,performance,power,mode'
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
    cm docker script "set system performance power mode[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_reproducibility`
               - ENV variables:
                   - CM_SET_OS_PERFORMANCE_REPRODUCIBILITY_MODE: `yes`

        </details>


      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cpu`** (default)
               - ENV variables:
                   - CM_SET_PERFORMANCE_MODE_OF: `cpu`

        </details>


      * Group "**performance-mode**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_performance`** (default)
               - ENV variables:
                   - CM_SET_PERFORMANCE_MODE: `performance`

        </details>


      * Group "**power**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_power`
               - ENV variables:
                   - CM_SET_PERFORMANCE_MODE: `power`

        </details>


    ##### Default variations

    `_cpu,_performance`

#### Native script being run
=== "Linux/macOS"
     * [run-ubuntu.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/set-performance-mode/run-ubuntu.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/set-performance-mode/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/set-performance-mode/run.bat)
___
#### Script output
```bash
cmr "set system performance power mode [variations]"  -j
```