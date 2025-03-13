# get-mlperf-inference-nvidia-common-code
Automatically generated README for this automation recipe: **get-mlperf-inference-nvidia-common-code**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-nvidia-common-code/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-nvidia-common-code/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get nvidia mlperf inference common-code" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,nvidia,mlperf,inference,common-code[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get nvidia mlperf inference common-code [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,nvidia,mlperf,inference,common-code'
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
    cm docker script "get nvidia mlperf inference common-code[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * Group "**repo-owner**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_ctuning`
        * `_custom`
        * `_go`
        * `_mlcommons`
        * `_nvidia-only`

        </details>

#### Versions
Default version: `r3.1`

* `r2.1`
* `r3.0`
* `r3.1`
* `r4.0`

___
#### Script output
```bash
cmr "get nvidia mlperf inference common-code [variations]"  -j
```