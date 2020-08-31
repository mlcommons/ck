# CK commands and APIs

Most of the CK functionality is implemented using [CK modules](https://cKnowledge.io/modules) 
with [automation actions]( https://cKnowledge.io/actions ) and associated 
[CK entries (components)]( https://cKnowledge.io/browse ).

Here we describe the main CK functionality to manage repositories, modules, and actions.
Remember that you can see all flags for a given automation action from the command line as follows:
```
ck {action} {CK module} --help
```



## Managing CK repositories

* Automation actions are implemented using the internal CK module [*repo*]( https://cknowledge.io/c/module/repo ).
* See the list of all automation actions and their API at [cKnowledge.io platform]( https://cknowledge.io/c/module/repo/#api ).


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







## Managing CK entries

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

You can search CK entries by the occurance of a given string in values of keys in JSON meta descriptions

```bash
ck search {CK module} --search_string={string with wildcards}
```

Note that CK supports transparent indexing of all CK JSON meta descriptions by [ElasticSearch](https://www.elastic.co) 
to enable fast search and powerful queries. This mode is used in our [cKnowledge.io platform](https://cKnowledge.io).
Please check these pages to know how to configure your CK installation with ES:
* https://github.com/ctuning/ck/wiki/Customization
* https://github.com/ctuning/ck/wiki/Indexing-entries
* https://github.com/ctuning/ck/wiki/Searching-entries




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






## Managing CK actions






## CK Python API




## More resources

* [CK wiki](https://github.com/ctuning/ck/wiki)
