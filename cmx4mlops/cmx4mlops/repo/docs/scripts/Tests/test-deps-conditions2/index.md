# test-deps-conditions2
Automatically generated README for this automation recipe: **test-deps-conditions2**

Category: **[Tests](..)**

License: **Apache 2.0**

Developers: Grigori Fursin
* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/test-deps-conditions2/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/test-deps-conditions2/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "test deps conditions2" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=test,deps,conditions2 [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "test deps conditions2 " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'test,deps,conditions2'
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
    cm docker script "test deps conditions2" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--test=value`  &rarr;  `TEST=value`




___
#### Script output
```bash
cmr "test deps conditions2 " [--input_flags] -j
```