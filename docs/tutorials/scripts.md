[ [Back to index](../README.md) ]

# Tutorial: adding new CM scripts and automation workflows/pipelines

One of the goals behind the Collective Mind scripting language is to make it as easy as possible 
for new users to add their own CM scripts and automation workflows based on the existing ones 
similar to the Wikipedia concept.

We suggest users to read about [CM scripts](../../cm-mlops/automation/script/README-extra.md) 
and study [existing CM scripts from MLCommons](https://github.com/mlcommons/ck/tree/master/cm-mlops/script),
find the most close one for their required functionality, and either extend it via meta descriptions,
native scripts and customize.py Python gluing or add the next one.

## Adding new CM script with a template

If you found a similar script with some alias, such as `get-ml-model-retinanet`, 
you can copy it to a new one such as `get-ml-model-new` using the CM CLI as follows:

```bash
cm cp script get-ml-model-retinanet get-ml-model-new
```

You can immediately specify new tags via CLI as follows:

```bash
cm cp script get-ml-model-retinanet get-ml-model-new --new_tags=new-model,...
```

You can also edit tags and other information in the _cm.json or _cm.yaml of the newly create script:
```bash
cm find script get-ml-model-new
```

Note that the new script will be created in the same CM repository as the original one.
If you want to create a new script in another repository (for example, in your private CM repository called `my-private-repo`),
you can do it as follows:
```bash
cm cp script get-ml-model-retinanet my-private-repo:get-ml-model-new
```

You can immediately run a new script (with the same automation as the original one) using the new alias:
```bash
cm run script get-ml-model-new
```
or a mix of original and new tags (recommended):
```bash
cm run script "get ml-model new-model"
```

## Adding new dummy CM script

You can also create a dummy CM script with some tags `new-tag1,new-tag2`:

```bash
cm add script new-script --new_tags=new-tag1,new-tag2
```

By default, CM will create it in the `local` CM repository:
```bash
cm find script new-script
```

And you can run it as follows:
```bash
cm run script "new-tag1 new-tag2"
```

You can add flag --yaml if you prefer to use YAML meta description for a new script
instead of JSON:
```bash
cm add script new-script2 --new_tags=new-tag1,new-tag2 --yaml
```


## Customizing new CM script

As soon as you created a new script, you can easily customize it
via meta description files `_cm.json` |& `_cm.yaml`,
`run.sh` |& `run.bat` and customize.py.

For example, you can extend *_cm.json* to add dependencies on other scripts, 
reuse environment variables and files in your new script prepared by other CM scripts 
from public or private projects, and add or update the *customize.py* script 
with *preprocess* and *postprocess* functions to implement more
complex logic to customize the execution of your script 
based on previous dependencies, flags, environment variables, platform and CPU features, etc.

Please, follow this [document](../../cm-mlops/automation/script/README-extra.md) 
to learn more about CM script customization.

Feel free to study these two CM scripts:
* [CM script to reproduce results from IPOL'22 journal paper with PyTorch and 2 images](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-ipol-paper-2022-439)
* [CM script to run image classification with RESNET50 ONNX model](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py)



## Collaborating with the community to unify API and meta of reusable scripts

We have developed CM language to help the community reuse and improve common automations instead of reinventing the wheel.
Feel free to join our [Discord server](https://discord.gg/JjWNWXKxwT) and the [MLCommons task force on automation and reproducibility](../taskforce.md)
to participate in the unification of shared scripts, APIs and meta information for diverse DevOps and MLOps scripts and tools,
and development of automation pipelines and workflows to co-design, benchmark, optimize and deploy efficient computing systems
for AI, ML and other emerging workloads.

