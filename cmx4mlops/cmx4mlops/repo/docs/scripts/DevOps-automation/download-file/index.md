# download-file
Automatically generated README for this automation recipe: **download-file**

Category: **[DevOps automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/download-file/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/download-file/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "download file" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=download,file[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "download file [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'download,file'
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
    cm docker script "download file[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_url.#`
               - ENV variables:
                   - CM_DOWNLOAD_URL: `#`

        </details>


      * Group "**download-tool**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cmutil`** (default)
               - ENV variables:
                   - CM_DOWNLOAD_TOOL: `cmutil`
        * `_curl`
               - ENV variables:
                   - CM_DOWNLOAD_TOOL: `curl`
        * `_gdown`
               - ENV variables:
                   - CM_DOWNLOAD_TOOL: `gdown`
        * `_rclone`
               - ENV variables:
                   - CM_DOWNLOAD_TOOL: `rclone`
        * `_wget`
               - ENV variables:
                   - CM_DOWNLOAD_TOOL: `wget`

        </details>


    ##### Default variations

    `_cmutil`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
    * `--from=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
    * `--local_path=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
    * `--md5sum=value`  &rarr;  `CM_DOWNLOAD_CHECKSUM=value`
    * `--output_file=value`  &rarr;  `CM_DOWNLOAD_FILENAME=value`
    * `--store=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
    * `--url=value`  &rarr;  `CM_DOWNLOAD_URL=value`
    * `--verify=value`  &rarr;  `CM_VERIFY_SSL=value`
    * `--verify_ssl=value`  &rarr;  `CM_VERIFY_SSL=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_RCLONE_COPY_USING: `sync`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/download-file/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/download-file/run.bat)
___
#### Script output
```bash
cmr "download file [variations]" [--input_flags] -j
```