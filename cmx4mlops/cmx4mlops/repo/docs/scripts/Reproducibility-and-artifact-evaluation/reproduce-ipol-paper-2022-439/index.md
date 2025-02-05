# reproduce-ipol-paper-2022-439
Automatically generated README for this automation recipe: **reproduce-ipol-paper-2022-439**

Category: **[Reproducibility and artifact evaluation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-ipol-paper-2022-439/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-ipol-paper-2022-439/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "app python reproduce project paper ipol journal repro reproducibility pytorch 2022-439" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=app,python,reproduce,project,paper,ipol,journal,repro,reproducibility,pytorch,2022-439 [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "app python reproduce project paper ipol journal repro reproducibility pytorch 2022-439 " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,python,reproduce,project,paper,ipol,journal,repro,reproducibility,pytorch,2022-439'
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
    cm docker script "app python reproduce project paper ipol journal repro reproducibility pytorch 2022-439" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--image1=value`  &rarr;  `CM_IMAGE_1=value`
    * `--image2=value`  &rarr;  `CM_IMAGE_2=value`




#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-ipol-paper-2022-439/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-ipol-paper-2022-439/run.bat)
___
#### Script output
```bash
cmr "app python reproduce project paper ipol journal repro reproducibility pytorch 2022-439 " [--input_flags] -j
```