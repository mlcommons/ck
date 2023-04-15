# CK CLI and API

Most of the CK functionality is implemented using [CK modules](https://cknow.io/modules) 
with [automation actions]( https://cknow.io/actions ) and associated 
[CK entries (components)]( https://cknow.io/browse ).

Here we describe the main CK functionality to manage repositories, modules, and actions.
Remember that you can see all flags for a given automation action from the command line as follows:
```bash
ck {action} {CK module} --help
```

You can set the *value* of any *key* for the automation action as follows:
```bash
ck {action} ... key=value
ck {action} ... -key=value
ck {action} ... --key=value
ck {action} ... --key=value
```
If the value is omitted, CK will use "yes" string.

You can also use JSON or YAML files as inputs to a given action:
```bash
ck {action} ... @input.json
ck {action} ... @input.yaml
```


## CLI to manage CK repositories

* Automation actions are implemented using the internal CK module [*repo*]( https://cknow.io/c/module/repo ).
* See the list of all automation actions and their API at [cKnowledge.io platform]( https://cknow.io/c/module/repo/#api ).

### Init new CK repository in the current path
```bash
ck init repo
```

CK will ask user for a repo name and will also attempt to detect Git URL from .git/config.

Extra options:

```bash
ck init repo:{CK repo name}
ck init repo --url={Git URL with the CK repository}
ck init repo --url={Git URL with the CK repository} --deps={list of CK repos}
```

Example:

```
ck init repo:asplos21-artifact123 --url=https://github.com/ctuning/ck-asplos21-artifact123 --deps=ck-autotuning
ck init repo:mlperf-submission --url=https://github.com/ctuning/ck-mlperf-submission321 --deps=ck-mlperf

```

### Pull existing repository using Git URL

```bash
ck pull repo --url={Git URL with the CK repository}
```

### Pull existing repository from cTuning GitHub

```bash
ck pull repo:{CK repo name}
```

In this case, CK will use *https://github.com/ctuning/{CK repo name}*

### Download a repository as a zip file

```bash
ck add repo --zip={URL to the zip file with the CK repository}
```

### Update all local CK repositories from Git

```bash
ck pull all
```

### Create a dummy CK repository locally

Quick mode with minimal questions:

```bash
ck add repo:{user-friendly name} --quiet
```

Advanced mode with many questions to configure repository:
```bash
ck add repo:{user-friendly name}
```

### Import existing local repository from current directory
```bash
ck import repo --quiet
```

### Import existing local repository from some local directory
```bash
ck import repo --path={full path to the local CK repository} --quiet 
```

### List local CK repositories
```bash
ck ls repo
```
 or
```bash
ck list repo
```

### Delete a given CK repository 

Unregister CK repository but do not delete the content (you can later import it again to reuse automation actions and components):
```bash
ck rm repo:{CK repo name from above list}
```
 or
```bash
ck remove repo:{CK repo name from above list}
```
 or
```bash
ck delete repo:{CK repo name from above list}
```

Delete CK repository completely with the content:
```bash
ck rm repo:{CK repo name from above list} --all
```

### Find a path to a given CK repository

```bash
ck where repo:{CK repo name}
```
or
```bash
ck find repo:{CK repo name}
```

### Pack a given CK repository to a zip file
```bash
ck zip repo:{CK repo name}
```

### Add CK entries from a zip file to an existing CK repository

To a local repository:

```bash
ck unzip repo:{CK repo name} --zip={path to a zip file with the CK repo}
```
To a given repository:

```bash
ck unzip repo:{CK repo name} --zip={path to a zip file with the CK repo}
```







## CLI to manage CK entries

CK repository is basically a database of CK modules and entries.
You can see internal CK commands to manage CK entries as follows:
```bash
ck help
```

*CID* is the Collective Identifier of the following formats:
* {CK module name or UID}:{CK entry name or UID}
* {CK repo name or UID}:{CK module name or UID}:{CK entry name or UID}

Note that wildcards are allowed in CID when appropriate!


Here are the most commonly used commands to manage CK modules and entries.

### List CK modules from all local CK repositories

```bash
ck ls module
```
or
```bash
ck list module
```


Show full CID (repository:module:entry):
```bash
ck ls module --all
```

### List some CK modules with a wildcard from all local CK repositories

```bash
ck ls module:{wildcard}
```

Example:

```bash
ck ls module:re* --all

 default:module:repo
 ck-analytics:module:report
 ...
```

### List CK entries for a given CK module in a given repository


```bash
ck ls {CK repo}:{CK module}:
```

or
```bash
ck ls {CK repo}:{CK module}:*

With a wildcard:
```bash
ck ls {CK repo}:{CK module}:{wildcard for CK entries}
```

Example:
```bash
ck ls ctuning-datasets-min:dataset:*jpeg*dnn*

  ctuning-datasets-min:dataset:image-jpeg-dnn-cat
  ctuning-datasets-min:dataset:image-jpeg-dnn-cat-gray
  ctuning-datasets-min:dataset:image-jpeg-dnn-computer-mouse
  ctuning-datasets-min:dataset:image-jpeg-dnn-cropped-panda
  ctuning-datasets-min:dataset:image-jpeg-dnn-fish-bike
  ctuning-datasets-min:dataset:image-jpeg-dnn-snake-224
  ctuning-datasets-min:dataset:image-jpeg-dnn-surfers
```

### Search for CK entries by tags

```bash
ck search {CK module} --tags={list of tags separated by comma}
```
or
```bash
ck search {CK module}:{wildcard for CK entries} --tags={list of tags separated by comma}
```
or
```bash
ck search {CK repo}:{CK module}:{wildcard for CK entries} --tags={list of tags separated by comma}
```

Example:
```bash
ck search dataset --tags=jpeg
ck search dataset:*dnn* --tags=jpeg
```



### Search for CK entries by a string

You can search CK entries by the occurrence of a given string in values of keys in JSON meta descriptions

```bash
ck search {CK module} --search_string={string with wildcards}
```

Note that CK supports transparent indexing of all CK JSON meta descriptions by [ElasticSearch](https://www.elastic.co) 
to enable fast search and powerful queries. This mode is used in our [cKnowledge.io platform](https://cknow.io).
Please check these pages to know how to configure your CK installation with ES:
* https://github.com/mlcommons/ck/wiki/Customization
* https://github.com/mlcommons/ck/wiki/Indexing-entries
* https://github.com/mlcommons/ck/wiki/Searching-entries




### Find a path to a given CK entry

```bash
ck find {CK module}:{CK entry}
```
or 
```bash
ck find {CK repo}:{CK module}:{CK entry}
```

Example:
```bash
ck find module:repo
ck find dataset:image-jpeg-dnn-snake-224
ck find ctuning-datasets-min:dataset:image-jpeg-dnn-snake-224
```





### Show JSON meta description of a given entry

```bash
ck load {CK module}:{CK entry} --min
```
or
```bash
ck load {CK repo}:{CK module}:{CK entry} --min
```




### Delete a given CK entry

```bash
ck rm {CK module}:{CK entry (can be with wildcard)}
```
or
```bash
ck rm {CK repo}:{CK module}:{CK entry can be with wildcard}
```
or
```bash
ck remove {CK repo}:{CK module}:{CK entry can be with wildcard}
```
or
```bash
ck delete {CK repo}:{CK module}:{CK entry can be with wildcard}
```

Example:
```bash
ck rm ctuning-datasets-min:dataset:image-jpeg-dnn-snake-224
ck rm dataset:*dnn*
```




### Create an empty CK entry

Create a CK entry in a *local* repository (CK scratch-pad):

```bash
ck add {CK module}:{CK entry name}
```

Create CK entry in a given repository:
```bash
ck add {CK repo}:{CK module}:{CK entry name}

If CK entry name is omitted, CK will create an entry with a UID:
```bash
ck add {CK module}
```

Example:
```
ck add tmp

  Entry  (2eab7af343d399d1, /home/fursin/CK-REPOS/local/tmp/2eab7af343d399d1) added successfully!

ck add tmp:xyz

  Entry xyz (44812ba5445a0a52, /home/fursin/CK-REPOS/local/tmp/xyz) added successfully!
```

Note that CK always generate Unique IDs for all entries!




### Rename a given CK entry

```bash
ck ren {CK module}:{CK entry} :{new CK entry name}
```
or
```bash
ck ren {CK repo}:{CK module}:{CK entry} :{new CK entry name}
```
or
```bash
ck rename {CK repo}:{CK module}:{CK entry} :{new CK entry name}
```

Note that CK keeps the same global UID for a renamed entry to be able to always find it!

Example:
```bash
ck ren ctuning-datasets-min:dataset:image-jpeg-dnn-snake-224 :image-jpeg-dnn-snake
```




### Move a given CK entry to another CK repository


```bash
ck mv {CK repo}:{CK module}:{CK entry name} {CK new repo}::
```
or
```bash
ck move {CK repo}:{CK module}:{CK entry name} {CK new repo}::
```

Example:
```
ck mv ctuning-datasets-min:dataset:image-jpeg-dnn-computer-mouse local::
```




### Copy a given CK entry


With a new name within the same repository:
```bash
ck cp {CK repo}:{CK module}:{CK entry name} ::{CK new entry name}
```

With a new name in a new repository:


```bash
ck cp {CK repo}:{CK module}:{CK entry name} {CK new repo}::{CK new entry name}
```

Example:
```
ck cp ctuning-datasets-min:dataset:image-jpeg-dnn-computer-mouse local::new-image
```






## CLI to manage CK actions

All the functionality in CK is implemented as automation actions in CK modules.

All CK modules inherit default automation actions from the previous section to manage associated CK entries.

A new action can be added to a given CK module as follows:

```bash
ck add_action {module name} --func={action name}
```

CK will ask you a few questions and will create a dummy function in the given CK module.
You can immediately test it as follows:
```bash
ck {action name} {module name}
```

It will just print the input as JSON to let you play with the command line 
and help you understand how CK converts the command line parameters
into the dictionary input for this function.

Next, you can find this module and start modifying this function:
```bash
ck find module:{module name}
```

For example, you can add the following Python code inside
this function to load some meta description of the entry ''my data''
when you call the following action:

```bash
ck {action name} {module name}:{my data}
```

```Python
    def {action name}(i):

    action=i['action']     # CK will substitute 'action' with {action name}
    module=i['module_uoa'] # CK will substitute 'module_uoa' with {module name}
    data=i['data_uoa']     # CK will substitute 'data_uoa' with {my data}

    # Call CK API to load meta description of a given entry
    # Equivalent to the command line: "ck load {module name}:{data name}"
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'], # Load the UID of a given module
                 'data_uoa':data})
    if r['return']>0: return r # Universal error handler in the CK

    meta=r['dict']      # meta of a given entry
    info=r['info']      # provenance info of this entry
    path=r['path']      # local path to this entry
    uoa=r['data_uoa']   # Name of the CK entry if exists. Otherwise UID.
    uid=r['data_uid']   # Only UID of the entry
```

Note that *uoa* means that this variable accepts Unique ID or Alias (user-friendly name).

Here *ck* is a CK kernel with various productivity functions
and one unified *access* function to all CK modules and actions
with unified dictionary (JSON) I/O.

You can find JSON API for all internal CK actions from the previous section that manage CK entries
from the command line as follows:
```bash
 ck get_api --func={internal action}
```

For example, you can check the API of the "load" action as follows:
```bash
 ck get_api --func=load
```

For non-internal actions, you can check their API as follows:
```bash
 ck {action name} {module name} --help
```

You can also check them at the [cKnowledge.io platform](https://cknow.io/modules).

When executing the following command

```bash
 ck my_action my_module --param1=value1 --param2 -param3=value3 param4 @input.json ...
```
CK will convert the above command line parameters to the following Python dictionary ''i'' 
for a given action:

```Python
 i={
     "action":"my_action",
     "module_uoa":"my_module",
     "param1":"value1",
     "param2":"yes",
     "param3":"value3"

     #extra keys merged from the input.json

     ...
 }
```

Note that when adding a new action to a given module, CK will also create a description
of this action inside the *meta.json* of this module. You can see an example
of such descriptions for the internal CK module "repo" [here](https://github.com/mlcommons/ck/blob/master/ck/repo/module/repo/.cm/meta.json).
When CK calls an action, it is not invoked directly from the given Python module 
but CK first checks the description, tests inputs, and then passes the control to the given Python module.

Also note that we suggest not to use aliases (user-friendly names) inside CK modules
but CK UIDs. The reason is that CK names may change while CK UIDs stay persistent.
We specify dependencies on other CK modules in the *meta.json* of a given module
using the *module_deps* key. See an example in the CK module *program*:
* [program meta.json](https://github.com/ctuning/ck-autotuning/blob/master/module/program/.cm/meta.json#L118)
* [how it is used in the CK module program](https://github.com/ctuning/ck-autotuning/blob/master/module/program/module.py#L479)

Such approach also allows us to visualize the growing knowledge graph:
[interactive graph]( https://cknow.io/kg1 ), 
[video](https://youtu.be/nabXHyot5is).

Finally, a given CK module has an access to the 3 dictionaries:
* *cfg* - this dictionary is loaded from the *meta.json* file from the CK module
* *work* - this dictionary has some run-time information:

  * self_module_uid: UID of the module
  * self_module_uoa: Alias (user-friendly name of the module) or UID
  * self_module_alias: Alias (user-friendly name of the module) or empty
  * path: path to the CK module
* *ck.cfg* - CK global [cfg dictionary](https://github.com/mlcommons/ck/blob/master/ck/kernel.py#L48) 
  that is updated at run-time with the meta description of the "kernel:default" entry.
  This dictionary is used to customize the local CK installation.



## CK Python API

One of the goals of the CK framework was to make it very simple for any user to access any automation action.
That is why we have developed just one [unified Python "access" function](https://ck.readthedocs.io/en/latest/src/ck.html#ck.kernel.access) 
that allows one to access all automation actions with a simple I/O (dictionary as input and dictionary as output).

You can call this function from any Python script or from CK modules as follows:

```Python
import ck.kernel as ck

i={'action': # specify action
   'module_uoa': # specify CK module UID or alias

   check keys from a given automation action for a given CK module (ck action module --help)
  }

r=ck.access(i)

if r['return']>0: return r # if used inside CK modules to propagate to all CK callers
#if r['return']>0: ck.err(r) # if used inside Python scripts to print an error and exit

#r dictionary will contain keys from the given automation action.
# See API of this automation action (ck action module --help)
```

Such approach allows users to continue extending different automation actions by adding new keys
while keeping backward compatibility. That's how we managed to develop 50+ modules with the community
without breaking portable CK workflows for our ML&systems R&D.

At the same time, we have implemented a number of "productivity" functions
in the CK kernel that are commonly used by many researchers and engineers.
For example, you can load JSON files, list files in directories, copy strings to clipboards.
At the same time, we made sure that these functions work in the same way across
different Python versions (2.7+ and 3+) and different operating systems 
thus removing this burden from developers.

You can see the list of such productivity functions [here](https://ck.readthedocs.io/en/latest/src/ck.html).
For example, you can [load a json file](https://ck.readthedocs.io/en/latest/src/ck.html#ck.kernel.load_json_file) 
in your script or CK module in a unified way as follows:

```Python
import ck.kernel as ck

r=ck.load_json_file({'json_file':'some_file.json'})
if r['return']>0: ck.err(r)

d=r['dict']

d['modify_some_key']='new value'

r=ck.save_json_to_file({'json_file':'new_file.json', 'dict':d, 'sort_keys':'yes'})
if r['return']>0: ck.err(r)

```



## More resources

* [CK wiki](https://github.com/mlcommons/ck/wiki)
