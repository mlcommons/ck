# download-and-extract
Automatically generated README for this automation recipe: **download-and-extract**

Category: **[DevOps automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/download-and-extract/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/download-and-extract/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "download-and-extract file" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=download-and-extract,file[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "download-and-extract file [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'download-and-extract,file'
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
    cm docker script "download-and-extract file[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_extract`
               - ENV variables:
                   - CM_DAE_EXTRACT_DOWNLOADED: `yes`
        * `_keep`
               - ENV variables:
                   - CM_EXTRACT_REMOVE_EXTRACTED: `no`
        * `_no-remove-extracted`
               - ENV variables:
                   - CM_EXTRACT_REMOVE_EXTRACTED: `no`
        * `_url.#`
               - ENV variables:
                   - CM_DAE_URL: `#`

        </details>


      * Group "**download-tool**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cmutil`** (default)
        * `_curl`
        * `_gdown`
        * `_rclone`
        * `_torrent`
               - ENV variables:
                   - CM_DAE_DOWNLOAD_USING_TORRENT: `yes`
                   - CM_TORRENT_DOWNLOADED_FILE_NAME: `<<<CM_DAE_FILENAME>>>`
                   - CM_TORRENT_DOWNLOADED_PATH_ENV_KEY: `CM_DAE_FILEPATH`
                   - CM_TORRENT_WAIT_UNTIL_COMPLETED: `yes`
        * `_wget`

        </details>


    ##### Default variations

    `_cmutil`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
    * `--extra_folder=value`  &rarr;  `CM_EXTRACT_TO_FOLDER=value`
    * `--extract_path=value`  &rarr;  `CM_EXTRACT_PATH=value`
    * `--from=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
    * `--local_path=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
    * `--store=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
    * `--to=value`  &rarr;  `CM_EXTRACT_PATH=value`
    * `--url=value`  &rarr;  `CM_DAE_URL=value`
    * `--verify=value`  &rarr;  `CM_VERIFY_SSL=value`




___
#### Script output
```bash
cmr "download-and-extract file [variations]" [--input_flags] -j
```