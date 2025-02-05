# get-java
Automatically generated README for this automation recipe: **get-java**

Category: **[Detection or installation of tools and artifacts](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-java/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-java/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get java" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,java[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get java [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,java'
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
    cm docker script "get java[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_install`
               - ENV variables:
                   - CM_JAVA_PREBUILT_INSTALL: `on`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--install=value`  &rarr;  `CM_JAVA_PREBUILT_INSTALL=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_JAVA_PREBUILT_VERSION: `19`
    * CM_JAVA_PREBUILT_BUILD: `36`
    * CM_JAVA_PREBUILT_URL: `https://download.java.net/openjdk/jdk${CM_JAVA_PREBUILT_VERSION}/ri/`
    * CM_JAVA_PREBUILT_FILENAME: `openjdk-${CM_JAVA_PREBUILT_VERSION}+${CM_JAVA_PREBUILT_BUILD}_${CM_JAVA_PREBUILT_HOST_OS}-x64_bin`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-java/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-java/run.bat)
___
#### Script output
```bash
cmr "get java [variations]" [--input_flags] -j
```