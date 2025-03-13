# generate-mlperf-tiny-submission
Automatically generated README for this automation recipe: **generate-mlperf-tiny-submission**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-mlperf-tiny-submission/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-mlperf-tiny-submission/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "generate submission mlperf mlperf-tiny tiny mlcommons tiny-submission mlperf-tiny-submission mlcommons-tiny-submission" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=generate,submission,mlperf,mlperf-tiny,tiny,mlcommons,tiny-submission,mlperf-tiny-submission,mlcommons-tiny-submission 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "generate submission mlperf mlperf-tiny tiny mlcommons tiny-submission mlperf-tiny-submission mlcommons-tiny-submission " 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'generate,submission,mlperf,mlperf-tiny,tiny,mlcommons,tiny-submission,mlperf-tiny-submission,mlcommons-tiny-submission'
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
    cm docker script "generate submission mlperf mlperf-tiny tiny mlcommons tiny-submission mlperf-tiny-submission mlcommons-tiny-submission" 
    ```
___


___
#### Script output
```bash
cmr "generate submission mlperf mlperf-tiny tiny mlcommons tiny-submission mlperf-tiny-submission mlcommons-tiny-submission "  -j
```