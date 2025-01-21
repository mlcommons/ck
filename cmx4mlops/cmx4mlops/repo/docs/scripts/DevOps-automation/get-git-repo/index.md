# get-git-repo
Automatically generated README for this automation recipe: **get-git-repo**

Category: **[DevOps automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-git-repo/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-git-repo/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get git repo repository clone" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,git,repo,repository,clone[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get git repo repository clone [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,git,repo,repository,clone'
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
    cm docker script "get git repo repository clone[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_lfs`
               - ENV variables:
                   - CM_GIT_REPO_NEEDS_LFS: `yes`
        * `_no-recurse-submodules`
               - ENV variables:
                   - CM_GIT_RECURSE_SUBMODULES: ``
        * `_patch`
               - ENV variables:
                   - CM_GIT_PATCH: `yes`
        * `_submodules.#`
               - ENV variables:
                   - CM_GIT_SUBMODULES: `#`

        </details>


      * Group "**checkout**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_branch.#`
               - ENV variables:
                   - CM_GIT_BRANCH: `#`
        * `_sha.#`
               - ENV variables:
                   - CM_GIT_SHA: `#`
        * `_tag.#`
               - ENV variables:
                   - CM_GIT_CHECKOUT_TAG: `#`

        </details>


      * Group "**git-history**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_full-history`
               - ENV variables:
                   - CM_GIT_DEPTH: ``
        * **`_short-history`** (default)
               - ENV variables:
                   - CM_GIT_DEPTH: `--depth 5`

        </details>


      * Group "**repo**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_repo.#`
               - ENV variables:
                   - CM_GIT_URL: `#`

        </details>


    ##### Default variations

    `_short-history`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--branch=value`  &rarr;  `CM_GIT_CHECKOUT=value`
    * `--depth=value`  &rarr;  `CM_GIT_DEPTH=value`
    * `--env_key=value`  &rarr;  `CM_GIT_ENV_KEY=value`
    * `--folder=value`  &rarr;  `CM_GIT_CHECKOUT_FOLDER=value`
    * `--patch=value`  &rarr;  `CM_GIT_PATCH=value`
    * `--pull=value`  &rarr;  `CM_GIT_REPO_PULL=value`
    * `--submodules=value`  &rarr;  `CM_GIT_RECURSE_SUBMODULES=value`
    * `--update=value`  &rarr;  `CM_GIT_REPO_PULL=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_GIT_DEPTH: `--depth 4`
    * CM_GIT_CHECKOUT_FOLDER: `repo`
    * CM_GIT_PATCH: `no`
    * CM_GIT_RECURSE_SUBMODULES: ` --recurse-submodules`
    * CM_GIT_URL: `https://github.com/mlcommons/ck.git`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-git-repo/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-git-repo/run.bat)
___
#### Script output
```bash
cmr "get git repo repository clone [variations]" [--input_flags] -j
```