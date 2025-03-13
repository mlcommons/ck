# push-mlperf-inference-results-to-github
Automatically generated README for this automation recipe: **push-mlperf-inference-results-to-github**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/push-mlperf-inference-results-to-github/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "push mlperf mlperf-inference-results publish-results inference submission github" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=push,mlperf,mlperf-inference-results,publish-results,inference,submission,github [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "push mlperf mlperf-inference-results publish-results inference submission github " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'push,mlperf,mlperf-inference-results,publish-results,inference,submission,github'
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
    cm docker script "push mlperf mlperf-inference-results publish-results inference submission github" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--branch=value`  &rarr;  `CM_GIT_BRANCH=value`
    * `--commit_message=value`  &rarr;  `CM_MLPERF_RESULTS_REPO_COMMIT_MESSAGE=value`
    * `--repo_branch=value`  &rarr;  `CM_GIT_BRANCH=value`
    * `--repo_url=value`  &rarr;  `CM_MLPERF_RESULTS_GIT_REPO_URL=value`
    * `--submission_dir=value`  &rarr;  `CM_MLPERF_INFERENCE_SUBMISSION_DIR=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_MLPERF_RESULTS_GIT_REPO_URL: `https://github.com/ctuning/mlperf_inference_submissions_v4.0`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/push-mlperf-inference-results-to-github/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "push mlperf mlperf-inference-results publish-results inference submission github " [--input_flags] -j
```