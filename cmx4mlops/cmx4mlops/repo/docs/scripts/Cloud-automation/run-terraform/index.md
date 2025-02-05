# run-terraform
Automatically generated README for this automation recipe: **run-terraform**

Category: **[Cloud automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/run-terraform/README-extra.md)


---

## Setup for Google Cloud Instances
```
sudo snap install google-cloud-cli --classic
gcloud auth application-default login
```

The above two commands will install google-cloud-cli and authorizes the user to access it. Once done, you can start creating gcp instance using CM commands like below. To destroy an instance just repeat the same command with `--destroy` option.

```
cm run script --tags=run,terraform,_gcp,_gcp_project.mlperf-inference-tests --cminit
```
Here, `mlperf-inference-tests` is the name of the google project as created in [Google cloud console](https://console.cloud.google.com/apis/dashboard)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/run-terraform/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "run terraform" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=run,terraform[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "run terraform [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,terraform'
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
    cm docker script "run terraform[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_amazon-linux-2-kernel.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE_OS: `amazon-linux-2-kernel.#`
        * `_graviton`
               - ENV variables:
                   - CM_TERRAFORM_AWS_GRAVITON_INSTANCE: `yes`
        * `_inferentia`
               - ENV variables:
                   - CM_TERRAFORM_AWS_INFERENTIA_INSTANCE: `yes`
        * `_rhel.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE_OS: `rhel.#`
        * `_ubuntu.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE_OS: `ubuntu.#`

        </details>


      * Group "**aws-instance-image**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_amazon-linux-2-kernel.510,arm64,us-west-2`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE: `ami-0f1a5f5ada0e7da53`
        * `_aws_instance_image.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE: `#`
        * `_aws_instance_image.ami-0735c191cf914754d`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE: `ami-0735c191cf914754d`
        * `_aws_instance_image.ami-0a0d8589b597d65b3`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE: `ami-0a0d8589b597d65b3`
        * `_rhel.9,x86,us-west-2`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE: `ami-0dda7e535b65b6469`
        * `_ubuntu.2204,arm64,us-west-2`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE: `ami-079f51a7bcca65b92`
        * `_ubuntu.2204,x86,us-west-2`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE: `ami-0735c191cf914754d`

        </details>


      * Group "**aws-instance-type**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_a1.2xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `a1.2xlarge`
        * `_a1.metal`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `a1.metal`
        * `_a1.xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `a1.xlarge`
        * `_aws_instance_type.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `#`
        * `_c5.12xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `c5.12xlarge`
        * `_c5.4xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `c5.4xlarge`
        * `_c5d.9xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `c5d.9xlarge`
        * `_g4dn.xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `g4dn.xlarge`
        * `_inf1.2xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `inf1.2xlarge`
        * `_inf1.xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `inf1.xlarge`
        * `_inf2.8xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `inf2.8xlarge`
        * `_inf2.xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `inf2.xlarge`
        * `_m7g.2xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `m7g.2xlarge`
        * `_m7g.xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `m7g.xlarge`
        * `_t2.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `t2.#`
        * `_t2.2xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `t2.2xlarge`
        * `_t2.large`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `t2.large`
        * `_t2.medium`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `t2.medium`
        * `_t2.micro`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `t2.micro`
        * `_t2.nano`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `t2.nano`
        * `_t2.small`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `t2.small`
        * `_t2.xlarge`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `t2.xlarge`

        </details>


      * Group "**cloud-provider**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_aws`** (default)
               - ENV variables:
                   - CM_TERRAFORM_CONFIG_DIR_NAME: `aws`
        * `_gcp`
               - ENV variables:
                   - CM_TERRAFORM_CONFIG_DIR_NAME: `gcp`

        </details>


      * Group "**gcp-instance-image**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_debian-cloud/debian-11`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE: `debian-cloud/debian-11`
        * `_gcp_instance_image.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE: `#`
        * `_ubuntu-2204-jammy-v20230114`
               - ENV variables:
                   - TF_VAR_INSTANCE_IMAGE: `ubuntu-2204-jammy-v20230114`

        </details>


      * Group "**gcp-instance-type**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_f1-micro`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `f1-micro`
        * `_gcp_instance_type.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `#`
        * `_n1-highmem.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `n1-highmem-#`
        * `_n1-standard.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_TYPE: `n1-highmem-#`

        </details>


      * Group "**gcp-project**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_gcp_project.#`
               - ENV variables:
                   - TF_VAR_GCP_PROJECT: `#`

        </details>


      * Group "**instance-name**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_instance_name.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_NAME: `#`

        </details>


      * Group "**platform**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_arm64`
               - ENV variables:
                   - CM_INSTANCE_PLATFORM: `arm64`
        * **`_x86`** (default)
               - ENV variables:
                   - CM_INSTANCE_PLATFORM: `x86`

        </details>


      * Group "**region**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_region.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_REGION: `#`
        * `_us-west-2`
               - ENV variables:
                   - TF_VAR_INSTANCE_REGION: `us-west-2`

        </details>


      * Group "**storage-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_storage_size.#`
               - ENV variables:
                   - TF_VAR_DISK_GBS: `#`
        * `_storage_size.8`
               - ENV variables:
                   - TF_VAR_DISK_GBS: `8`

        </details>


      * Group "**zone**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_zone.#`
               - ENV variables:
                   - TF_VAR_INSTANCE_ZONE: `#`

        </details>


    ##### Default variations

    `_aws,_x86`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--cminit=value`  &rarr;  `CM_TERRAFORM_CM_INIT=value`
    * `--destroy=value`  &rarr;  `CM_DESTROY_TERRAFORM=value`
    * `--gcp_credentials_json_file=value`  &rarr;  `CM_GCP_CREDENTIALS_JSON_PATH=value`
    * `--key_file=value`  &rarr;  `CM_SSH_KEY_FILE=value`
    * `--run_cmds=value`  &rarr;  `CM_TERRAFORM_RUN_COMMANDS=value`
    * `--ssh_key_file=value`  &rarr;  `CM_SSH_KEY_FILE=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * TF_VAR_SECURITY_GROUP_ID: `sg-0783752c97d2e011d`
    * TF_VAR_CPU_COUNT: `1`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/run-terraform/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "run terraform [variations]" [--input_flags] -j
```