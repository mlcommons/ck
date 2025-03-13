# get-android-sdk
Automatically generated README for this automation recipe: **get-android-sdk**

Category: **[Detection or installation of tools and artifacts](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-android-sdk/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-android-sdk/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get android sdk android-sdk" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,android,sdk,android-sdk [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get android sdk android-sdk " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,android,sdk,android-sdk'
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
    cm docker script "get android sdk android-sdk" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--android_cmake_version=value`  &rarr;  `CM_ANDROID_CMAKE_VERSION=value`
    * `--android_ndk_version=value`  &rarr;  `CM_ANDROID_NDK_VERSION=value`
    * `--android_version=value`  &rarr;  `CM_ANDROID_VERSION=value`
    * `--build_tools_version=value`  &rarr;  `CM_ANDROID_BUILD_TOOLS_VERSION=value`
    * `--cmdline_tools_version=value`  &rarr;  `CM_ANDROID_CMDLINE_TOOLS_VERSION=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_ANDROID_BUILD_TOOLS_VERSION: `29.0.3`
    * CM_ANDROID_CMAKE_VERSION: `3.6.4111459`
    * CM_ANDROID_CMDLINE_TOOLS_URL: `https://dl.google.com/android/repository/commandlinetools-${CM_ANDROID_CMDLINE_TOOLS_OS}-${CM_ANDROID_CMDLINE_TOOLS_VERSION}_latest.zip`
    * CM_ANDROID_CMDLINE_TOOLS_VERSION: `9123335`
    * CM_ANDROID_NDK_VERSION: `21.3.6528147`
    * CM_ANDROID_VERSION: `30`



___
#### Script output
```bash
cmr "get android sdk android-sdk " [--input_flags] -j
```