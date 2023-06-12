[ [Back to index](../README.md) ]

# Tutorial: Adding a common interface to reproduce research projects

## Motivation

While helping the community to reproduce and replicate [many research papers](https://learning.acm.org/techtalks/reproducibility) 
during [artifact evaluation](https://cTuning.org/ae), we have seen that reviewers spend most of their time
deciphering numerous ad-hoc READMEs to figure out how to prepare and run shared applications. 

That motivated us to develop a [human readable language (Collective Mind)](../README.md#collective-mind-language-cm) 
to automate and unify the [most commonly used tasks](../list_of_scripts.md) 
to reproduce or replicate shared applications across the same or different software, hardware, models and data.

The goal of our common automation and reproducibility interface is to make it easier for the community 
to reproduce/replicate research results and apply them in the real world.
You can see an example of using CM automation language to reproduce an IPOL journal paper 
in this [tutorial](reproduce-research-paper-ipol.md).



## Installing CM language

CM requires minimal dependencies (Python 3+ and Git) and it should be straightforward to install it
on Linux, MacOS, Windows and any other platform using this [guide](../installation.md).

If you encounter any issue, please don't hesitate to tell us via [Discord server](https://discord.gg/JjWNWXKxwT) 
and/or open a ticket [here](https://github.com/mlcommons/ck/issues).



## Adding CM interface to your research project

### Local directory

To initialize a CM repository/interface in a local project directory,
you need to go there and run the following CM command
while substituting `my-research-project` with a unique name:

```bash
cm init repo my-research-project --path=. --prefix=cmr
```

If this research project is associated with artifact evaluation, we suggest to use
the name of the conference and your paper ID such as `micro-2023-038` for ACM MICRO.

This command will create a `cmr.yaml` file with a description and unique ID of this repository,
and will register it in the CM. Note that all CM automations and artifacts will be located
in the `cmr` sub-directory to avoid contaminating your project. They can be deleted
or moved to another project at any time.

### Git project

If you use Git for your project, we suggest to initialize your repository
as follows:
```bash
cm pull repo my-research-project --url={Git URL}
```

In such case, CM will pull your Git repository, initialize CM interface and register it in the CM.

You can see your registered CM repositories as follows:
```bash
cm list repo
```

You can find the location of your Git repository in CM for further editing as follows:
```bash
cm find repo my-research-project
```


## Adding CM script to prepare and run your experiment







## Participating in discussions and developments

Please join our [Discord server](https://discord.gg/JjWNWXKxwT) from the [MLCommons task force on automation and reproducibility](../taskforce.md)
to get free help to add CM interface to your research projects, reuse and/or extend [shared CM scripts](../../cm-mlops/script), add new automations,
participate in the unification of the CM automation and reproducibility language, and participate in our 
[open optimization and reproducibility challenges](https://access.cknowledge.org/playground/?action=challenges).
