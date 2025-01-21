# get-cuda
Automatically generated README for this automation recipe: **get-cuda**

Category: **[CUDA automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cuda/README-extra.md)


---

# System dependencies

* Download [CUDA toolkit](https://developer.nvidia.com/cuda-toolkit).
* Download [cuDNN](https://developer.nvidia.com/rdp/cudnn-download).
* Download [TensorRT](https://developer.nvidia.com/nvidia-tensorrt-8x-download).


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cuda/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda 46d133d9ef92422d" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda,46d133d9ef92422d[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda 46d133d9ef92422d [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda,46d133d9ef92422d'
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
    cm docker script "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda 46d133d9ef92422d[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_cudnn`
               - ENV variables:
                   - CM_CUDA_NEEDS_CUDNN: `yes`
        * `_package-manager`
               - ENV variables:
                   - CM_CUDA_PACKAGE_MANAGER_INSTALL: `yes`

        </details>


      * Group "**installation-mode**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_lib-only`
               - ENV variables:
                   - CM_CUDA_FULL_TOOLKIT_INSTALL: `no`
                   - CM_TMP_FILE_TO_CHECK_UNIX: `libcudart.so`
                   - CM_TMP_FILE_TO_CHECK_WINDOWS: `libcudart.dll`
        * **`_toolkit`** (default)
               - ENV variables:
                   - CM_CUDA_FULL_TOOLKIT_INSTALL: `yes`
                   - CM_TMP_FILE_TO_CHECK_UNIX: `nvcc`
                   - CM_TMP_FILE_TO_CHECK_WINDOWS: `nvcc.exe`

        </details>


    ##### Default variations

    `_toolkit`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--cudnn_tar_file=value`  &rarr;  `CM_CUDNN_TAR_FILE_PATH=value`
    * `--cudnn_tar_path=value`  &rarr;  `CM_CUDNN_TAR_FILE_PATH=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_CUDA_PATH_LIB_CUDNN_EXISTS: `no`
    * CM_REQUIRE_INSTALL: `no`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cuda/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cuda/run.bat)
___
#### Script output
```bash
cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda 46d133d9ef92422d [variations]" [--input_flags] -j
```