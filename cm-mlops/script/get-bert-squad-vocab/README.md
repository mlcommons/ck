**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-bert-squad-vocab).**



Automatically generated README for this automation recipe: **get-bert-squad-vocab**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-bert-squad-vocab,2f99a545ce734157) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-bert-squad-vocab)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,bert,squad,bert-large,bert-squad,vocab*
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

````cmr "get bert squad bert-large bert-squad vocab" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,bert,squad,bert-large,bert-squad,vocab`

`cm run script --tags=get,bert,squad,bert-large,bert-squad,vocab `

*or*

`cmr "get bert squad bert-large bert-squad vocab"`

`cmr "get bert squad bert-large bert-squad vocab " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,bert,squad,bert-large,bert-squad,vocab'
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

```cmr "cm gui" --script="get,bert,squad,bert-large,bert-squad,vocab"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,bert,squad,bert-large,bert-squad,vocab) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get bert squad bert-large bert-squad vocab" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-bert-squad-vocab/_cm.json)
  1. Run "preprocess" function from customize.py
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-bert-squad-vocab/_cm.json)***
     * download,file
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-bert-squad-vocab/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-bert-squad-vocab/_cm.json)

___
### Script output
`cmr "get bert squad bert-large bert-squad vocab "  -j`
#### New environment keys (filter)

* `CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH`
#### New environment keys auto-detected from customize
