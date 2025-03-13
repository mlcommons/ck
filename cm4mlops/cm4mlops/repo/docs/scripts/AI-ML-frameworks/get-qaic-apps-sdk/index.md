# get-qaic-apps-sdk
Automatically generated README for this automation recipe: **get-qaic-apps-sdk**

Category: **[AI/ML frameworks](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-qaic-apps-sdk/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get detect qaic apps sdk apps-sdk qaic-apps-sdk" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,detect,qaic,apps,sdk,apps-sdk,qaic-apps-sdk 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get detect qaic apps sdk apps-sdk qaic-apps-sdk " 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,detect,qaic,apps,sdk,apps-sdk,qaic-apps-sdk'
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
    cm docker script "get detect qaic apps sdk apps-sdk qaic-apps-sdk" 
    ```
___


___
#### Script output
```bash
cmr "get detect qaic apps sdk apps-sdk qaic-apps-sdk "  -j
```