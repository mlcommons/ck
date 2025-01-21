# get-qaic-software-kit
Automatically generated README for this automation recipe: **get-qaic-software-kit**

Category: **[AI/ML frameworks](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-qaic-software-kit/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get qaic software kit qaic-software-kit" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,qaic,software,kit,qaic-software-kit[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get qaic software kit qaic-software-kit [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,qaic,software,kit,qaic-software-kit'
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
    cm docker script "get qaic software kit qaic-software-kit[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_branch.#`
               - ENV variables:
                   - CM_GIT_CHECKOUT: `#`

        </details>


      * Group "**repo-source**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_repo.#`
               - ENV variables:
                   - CM_GIT_URL: `#`
        * **`_repo.quic`** (default)
               - ENV variables:
                   - CM_GIT_URL: `https://github.com/quic/software-kit-for-qualcomm-cloud-ai-100`

        </details>


    ##### Default variations

    `_repo.quic`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-qaic-software-kit/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get qaic software kit qaic-software-kit [variations]"  -j
```