# benchmark-program-mlperf
Automatically generated README for this automation recipe: **benchmark-program-mlperf**

Category: **[Modular MLPerf inference benchmark pipeline](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-program-mlperf/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "mlperf benchmark-mlperf" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=mlperf,benchmark-mlperf[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "mlperf benchmark-mlperf [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'mlperf,benchmark-mlperf'
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
    cm docker script "mlperf benchmark-mlperf[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * Group "**power-mode**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_no-power`** (default)
        * `_power`
               - ENV variables:
                   - CM_MLPERF_POWER: `yes`

        </details>


    ##### Default variations

    `_no-power`

___
#### Script output
```bash
cmr "mlperf benchmark-mlperf [variations]"  -j
```