# install-tensorflow-from-src
Automatically generated README for this automation recipe: **install-tensorflow-from-src**

Category: **[AI/ML frameworks](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-tensorflow-from-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get install tensorflow lib source from-source from-src src from.src" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,install,tensorflow,lib,source,from-source,from-src,src,from.src[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get install tensorflow lib source from-source from-src src from.src [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,install,tensorflow,lib,source,from-source,from-src,src,from.src'
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
    cm docker script "get install tensorflow lib source from-source from-src src from.src[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_tflite`
               - ENV variables:
                   - CM_TFLITE: `on`

        </details>

=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_GIT_URL: `https://github.com/tensorflow/tensorflow`
    * CM_GIT_DEPTH: `1`
    * CM_TFLITE: `off`


#### Versions
Default version: `master`

* `master`
* `v1.15.0`
* `v2.0.0`
* `v2.1.0`
* `v2.10.0`
* `v2.11.0`
* `v2.12.0`
* `v2.13.0`
* `v2.14.0`
* `v2.15.0`
* `v2.16.1`
* `v2.2.0`
* `v2.3.0`
* `v2.4.0`
* `v2.5.0`
* `v2.6.0`
* `v2.7.0`
* `v2.8.0`
* `v2.9.0`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-tensorflow-from-src/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get install tensorflow lib source from-source from-src src from.src [variations]"  -j
```