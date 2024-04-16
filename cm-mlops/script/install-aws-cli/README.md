**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/install-aws-cli).**



Automatically generated README for this automation recipe: **install-aws-cli**

Category: **Cloud automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-aws-cli,4d3efd333c3f4d36) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-aws-cli)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,script,aws-cli,aws,cli*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "install script aws-cli aws cli" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,script,aws-cli,aws,cli`

`cm run script --tags=install,script,aws-cli,aws,cli `

*or*

`cmr "install script aws-cli aws cli"`

`cmr "install script aws-cli aws cli " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,script,aws-cli,aws,cli'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### Run this script via GUI

```cmr "cm gui" --script="install,script,aws-cli,aws,cli"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,script,aws-cli,aws,cli) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install script aws-cli aws cli" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-aws-cli/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-aws-cli/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-aws-cli/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-aws-cli/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-aws-cli/_cm.json)
  1. Run "postrocess" function from customize.py
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-aws-cli/_cm.json)***
     * get,aws-cli
       * `if (CM_REQUIRE_INSTALL  != yes)`
       - CM script: [get-aws-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-aws-cli)

___
### Script output
`cmr "install script aws-cli aws cli "  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
