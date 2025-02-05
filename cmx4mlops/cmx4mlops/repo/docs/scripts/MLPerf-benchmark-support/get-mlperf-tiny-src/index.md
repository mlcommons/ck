# get-mlperf-tiny-src
Automatically generated README for this automation recipe: **get-mlperf-tiny-src**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-tiny-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get src source tiny tiny-src tiny-source tinymlperf tinymlperf-src mlperf mlcommons" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,src,source,tiny,tiny-src,tiny-source,tinymlperf,tinymlperf-src,mlperf,mlcommons 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get src source tiny tiny-src tiny-source tinymlperf tinymlperf-src mlperf mlcommons " 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,src,source,tiny,tiny-src,tiny-source,tinymlperf,tinymlperf-src,mlperf,mlcommons'
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
    cm docker script "get src source tiny tiny-src tiny-source tinymlperf tinymlperf-src mlperf mlcommons" 
    ```
___

=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_GIT_CHECKOUT: `master`
    * CM_GIT_PATCH: `no`
    * CM_GIT_RECURSE_SUBMODULES: ``
    * CM_GIT_URL: `https://github.com/mlcommons/tiny.git`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-tiny-src/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-tiny-src/run.bat)
___
#### Script output
```bash
cmr "get src source tiny tiny-src tiny-source tinymlperf tinymlperf-src mlperf mlcommons "  -j
```