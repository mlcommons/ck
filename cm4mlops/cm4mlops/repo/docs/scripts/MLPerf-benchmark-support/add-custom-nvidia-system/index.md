# add-custom-nvidia-system
Automatically generated README for this automation recipe: **add-custom-nvidia-system**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/add-custom-nvidia-system/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/add-custom-nvidia-system/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "add custom system nvidia" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=add,custom,system,nvidia[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "add custom system nvidia [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'add,custom,system,nvidia'
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
    cm docker script "add custom system nvidia[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * Group "**code**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_ctuning`
        * `_custom`
        * `_go`
        * `_mlcommons`
        * `_nvidia-only`

        </details>

#### Versions
* `r2.1`
* `r3.0`
* `r3.1`
* `r4.0`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/add-custom-nvidia-system/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "add custom system nvidia [variations]"  -j
```