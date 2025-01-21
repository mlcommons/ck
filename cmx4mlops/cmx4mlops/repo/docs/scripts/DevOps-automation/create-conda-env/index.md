# create-conda-env
Automatically generated README for this automation recipe: **create-conda-env**

Category: **[DevOps automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/create-conda-env/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "create get env conda-env conda-environment create-conda-environment" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=create,get,env,conda-env,conda-environment,create-conda-environment[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "create get env conda-env conda-environment create-conda-environment [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'create,get,env,conda-env,conda-environment,create-conda-environment'
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
    cm docker script "create get env conda-env conda-environment create-conda-environment[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_name.#`
               - ENV variables:
                   - CM_CONDA_ENV_NAME: `#`

        </details>


#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/create-conda-env/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "create get env conda-env conda-environment create-conda-environment [variations]"  -j
```