# get-ipol-src
Automatically generated README for this automation recipe: **get-ipol-src**

Category: **[Reproducibility and artifact evaluation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ipol-src/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ipol-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ipol journal src ipol-src" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,ipol,journal,src,ipol-src [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get ipol journal src ipol-src " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ipol,journal,src,ipol-src'
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
    cm docker script "get ipol journal src ipol-src" [--input_flags]
    ```
___

=== "Input Flags"


    #### Input Flags

    * --**number:** IPOL publication number
    * --**year:** IPOL publication year
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--number=value`  &rarr;  `CM_IPOL_NUMBER=value`
    * `--year=value`  &rarr;  `CM_IPOL_YEAR=value`




___
#### Script output
```bash
cmr "get ipol journal src ipol-src " [--input_flags] -j
```