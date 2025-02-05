# get-generic-sys-util
Automatically generated README for this automation recipe: **get-generic-sys-util**

Category: **[Detection or installation of tools and artifacts](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-generic-sys-util/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get sys-util generic generic-sys-util" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,sys-util,generic,generic-sys-util[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get sys-util generic generic-sys-util [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,sys-util,generic,generic-sys-util'
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
    cm docker script "get sys-util generic generic-sys-util[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_g++-12`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `g++12`
        * `_gflags-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `gflags-dev`
        * `_git-lfs`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `git-lfs`
        * `_glog-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `glog-dev`
        * `_libboost-all-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libboost-all-dev`
        * `_libbz2-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libbz2_dev`
        * `_libev-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libev_dev`
        * `_libffi-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libffi_dev`
        * `_libffi7`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libffi7`
        * `_libgdbm-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libgdbm_dev`
        * `_libgmock-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libgmock-dev`
        * `_liblzma-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `liblzma_dev`
        * `_libmpfr-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libmpfr-dev`
        * `_libncurses-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libncurses_dev`
        * `_libnuma-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libnuma-dev`
        * `_libpci-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libpci-dev`
        * `_libre2-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libre2-dev`
        * `_libreadline-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libreadline_dev`
        * `_libsqlite3-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libsqlite3_dev`
        * `_libssl-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libssl_dev`
        * `_libudev-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `libudev-dev`
        * `_ninja-build`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `ninja-build`
        * `_nlohmann-json3-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `nlohmann_json3_dev`
        * `_ntpdate`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `ntpdate`
        * `_numactl`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `numactl`
        * `_nvidia-cuda-toolkit`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `nvidia-cuda-toolkit`
        * `_rapidjson-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `rapidjson-dev`
        * `_rsync`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `rsync`
        * `_screen`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `screen`
        * `_sox`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `sox`
        * `_tk-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `tk_dev`
        * `_transmission`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `transmission`
        * `_wget`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `wget`
        * `_zlib`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `zlib`
        * `_zlib1g-dev`
               - ENV variables:
                   - CM_SYS_UTIL_NAME: `zlib1g_dev`

        </details>

=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_CLEAN_DIRS: `bin`
    * CM_SUDO: `sudo`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-generic-sys-util/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get sys-util generic generic-sys-util [variations]"  -j
```