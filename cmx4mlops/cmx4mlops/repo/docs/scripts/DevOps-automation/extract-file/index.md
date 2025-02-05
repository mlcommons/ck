# extract-file
Automatically generated README for this automation recipe: **extract-file**

Category: **[DevOps automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/extract-file/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/extract-file/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "extract file" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=extract,file[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "extract file [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'extract,file'
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
    cm docker script "extract file[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_keep`
               - ENV variables:
                   - CM_EXTRACT_REMOVE_EXTRACTED: `no`
        * `_no-remove-extracted`
               - ENV variables:
                   - CM_EXTRACT_REMOVE_EXTRACTED: `no`
        * `_path.#`
               - ENV variables:
                   - CM_EXTRACT_FILEPATH: `#`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--extra_folder=value`  &rarr;  `CM_EXTRACT_TO_FOLDER=value`
    * `--extract_path=value`  &rarr;  `CM_EXTRACT_PATH=value`
    * `--input=value`  &rarr;  `CM_EXTRACT_FILEPATH=value`
    * `--to=value`  &rarr;  `CM_EXTRACT_PATH=value`




#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/extract-file/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/extract-file/run.bat)
___
#### Script output
```bash
cmr "extract file [variations]" [--input_flags] -j
```