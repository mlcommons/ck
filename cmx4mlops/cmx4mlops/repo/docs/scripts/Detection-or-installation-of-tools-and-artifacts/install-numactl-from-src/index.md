# Build numactl from sources
Automatically generated README for this automation recipe: **install-numactl-from-src**

Category: **[Detection or installation of tools and artifacts](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-numactl-from-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install src from.src numactl src-numactl" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=install,src,from.src,numactl,src-numactl[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "install src from.src numactl src-numactl [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,src,from.src,numactl,src-numactl'
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
    cm docker script "install src from.src numactl src-numactl[variations]" 
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
        * `_sha.#`
               - ENV variables:
                   - CM_GIT_CHECKOUT_SHA: `#`
        * `_tag.#`
               - ENV variables:
                   - CM_GIT_CHECKOUT_TAG: `#`

        </details>


      * Group "**repo**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_repo.#`
               - ENV variables:
                   - CM_GIT_URL: `#`
        * **`_repo.https://github.com/numactl/numactl`** (default)
               - ENV variables:
                   - CM_GIT_URL: `https://github.com/numactl/numactl`

        </details>


    ##### Default variations

    `_repo.https://github.com/numactl/numactl`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-numactl-from-src/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "install src from.src numactl src-numactl [variations]"  -j
```