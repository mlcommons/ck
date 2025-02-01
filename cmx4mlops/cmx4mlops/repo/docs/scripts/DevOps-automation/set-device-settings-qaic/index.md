# set-device-settings-qaic
Automatically generated README for this automation recipe: **set-device-settings-qaic**

Category: **[DevOps automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/set-device-settings-qaic/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "set device qaic ai100 cloud performance power setting mode vc ecc" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=set,device,qaic,ai100,cloud,performance,power,setting,mode,vc,ecc[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "set device qaic ai100 cloud performance power setting mode vc ecc [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'set,device,qaic,ai100,cloud,performance,power,setting,mode,vc,ecc'
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
    cm docker script "set device qaic ai100 cloud performance power setting mode vc ecc[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_ecc`
               - ENV variables:
                   - CM_QAIC_ECC: `yes`
        * `_vc.#`
               - ENV variables:
                   - CM_QAIC_VC: `#`

        </details>

=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_QAIC_DEVICES: `0`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/set-device-settings-qaic/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "set device qaic ai100 cloud performance power setting mode vc ecc [variations]"  -j
```