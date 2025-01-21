# get-onnxruntime-prebuilt
Automatically generated README for this automation recipe: **get-onnxruntime-prebuilt**

Category: **[AI/ML frameworks](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-onnxruntime-prebuilt/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install onnxruntime get prebuilt lib lang-c lang-cpp" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "install onnxruntime get prebuilt lib lang-c lang-cpp [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp'
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
    cm docker script "install onnxruntime get prebuilt lib lang-c lang-cpp[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cpu`** (default)
               - ENV variables:
                   - CM_ONNXRUNTIME_DEVICE: ``
        * `_cuda`
               - ENV variables:
                   - CM_ONNXRUNTIME_DEVICE: `gpu`

        </details>


    ##### Default variations

    `_cpu`
#### Versions
Default version: `1.16.3`


#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-onnxruntime-prebuilt/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-onnxruntime-prebuilt/run.bat)
___
#### Script output
```bash
cmr "install onnxruntime get prebuilt lib lang-c lang-cpp [variations]"  -j
```