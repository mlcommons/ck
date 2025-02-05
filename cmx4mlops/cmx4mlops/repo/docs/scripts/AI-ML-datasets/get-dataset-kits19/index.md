# get-dataset-kits19
Automatically generated README for this automation recipe: **get-dataset-kits19**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-kits19/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset medical-imaging kits original kits19" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,dataset,medical-imaging,kits,original,kits19[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get dataset medical-imaging kits original kits19 [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,medical-imaging,kits,original,kits19'
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
    cm docker script "get dataset medical-imaging kits original kits19[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_calibration`
               - ENV variables:
                   - CM_DATASET_CALIBRATION: `yes`
        * `_default`
               - ENV variables:
                   - CM_GIT_PATCH: `no`
        * `_full-history`
               - ENV variables:
                   - CM_GIT_DEPTH: ``
        * `_no-recurse-submodules`
               - ENV variables:
                   - CM_GIT_RECURSE_SUBMODULES: ``
        * `_patch`
               - ENV variables:
                   - CM_GIT_PATCH: `yes`
        * `_short-history`
               - ENV variables:
                   - CM_GIT_DEPTH: `--depth 5`
        * `_validation`
               - ENV variables:
                   - CM_DATASET_VALIDATION: `yes`

        </details>

=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_GIT_CHECKOUT: `master`
    * CM_GIT_DEPTH: `--depth 2`
    * CM_GIT_PATCH: `no`
    * CM_GIT_RECURSE_SUBMODULES: ``
    * CM_GIT_URL: `https://github.com/neheller/kits19`


#### Versions
Default version: `master`

* `custom`
* `master`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-kits19/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get dataset medical-imaging kits original kits19 [variations]"  -j
```