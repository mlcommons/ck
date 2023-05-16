# CM "script" automation

*We suggest you to check [CM introduction](https://github.com/mlcommons/ck/blob/master/docs/introduction-cm.md) 
 and [CM CLI/API](https://github.com/mlcommons/ck/blob/master/docs/interface.md) to understand CM motivation and concepts.
 You can also try [CM tutorials](https://github.com/mlcommons/ck/blob/master/docs/tutorials/README.md) 
 to run some applications and benchmarks on your platform using CM scripts.*

## Motivation

While helping the community reproduce [150+ research papers](https://learning.acm.org/techtalks/reproducibility),
we have noticed that researchers always create their own ad-hoc scripts, environment variable and files
to perform *exactly the same steps (actions) across all papers* to prepare, run and reproduce their experiments 
across different software, hardware, models and data.

![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/cm-ad-hoc-projects.png)

This experience motivated us the create a CM automation called "script" to warp native scripts
from research papers with a common CM CLI (and Pyhton API) to make them more reusable, portable, 
findable and deterministic across different projects. 

These scripts simply unify updating and caching of environment variables and output files.

They can be embedded into existing projects in a non-intrusive way to and can be connected
into powerful and portable workflows to prepare, run and reproduce experiments across continuously changing technology.

![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/cm-unified-projects.png)


## Obtaining CM scripts

In order to (re)use some CM scripts embedded into shared projects, 
you need to install these projects via the CM interface.

For example, to use automation scripts developed by the [MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md)
and shared via GitHub, you just need to pull this repository via CM:

```bash
cm pull repo --url=https://github.com/mlcommons/ck
```

or

```bash
cm pull repo mlcommons@ck
```

You can see all available CM scripts in your system as follows:

```bash
cm find script
cm find script install* | sort

```

## Running CM scripts

CM scripts are treated as standard CM artifacts with the CM automation "script", CM action "run",
and JSON &| YAML meta descriptions. 

The can be invoked by alias, unique ID and human-readable tags (preferred method).

For example, [this CM script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os) unifies detection of operating system parameters 
on any platform. 

It is described by [this _cm.json file](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/detect-os/_cm.json) with the following alias, UID and tags:
```json
{
  "alias": "detect-os",
  "uid": "863735b7db8c44fc",

  "tags": [
    "detect-os",
    "detect",
    "os",
    "info"
  ],

  "automation_alias": "script",
  "automation_uid": "5b4e0237da074764"

}
```

The `automation_alias` and `automation_uid` tells CM that this artifact is compatible with the CM "script" automation.

Therefore, it can be executed from the command line in any of the following ways:

```bash
cm run script detect-os --out=json
cm run script 863735b7db8c44fc  --out=json
cm run script --tags=detect,os  --out=json
cm run script "detect os"  --out=json
```

This script can be also executed using CM Python API as follows:
```python
import cmind

output = cmind.access({'action':'run', 'automation':'script', 'tags':'detect,os'})
if output['return']>0:
    cmind.error(output)

import json
print (json.dumps(output, indent=2))
```



















### CM script pipeline

The CM script automation has a "run" action that takes a unified CM dictionary with the following keys as the input:

* "artifact" (str): CM name from [this list](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
* "tags" (str): instead of using an explicit CM script name, we can use the tags separated by comma to find a given CM script

* "env" (dict): original environment (can be empty)
* "state" (dict): original state (can be empty)

* extra flags to customize the execution of a given CM script

The output of this automation is also a unified CM dictionary:

* "new_env" (dict): update for the original environment (excluding original environment)
* "new_state" (dict): update for the original state (excluding original environment)

![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/cm-plug-and-play-script-details.v2.png)

A CM script simply wraps existing user scripts (run.sh on Linux and MacOS or run.bat on Windows),
reads meta description, runs other CM script dependencies,
runs "preprocessing" function from "customize.py" (if exists)
to update "env" and the "state" and produce extra files needed for a native script,
runs the script, reads produced files with updated "env" and "state",
and runs "postprocessing" function from "customize.py" (if exists)
to finalize updating "env" and "state".

If meta description of a given CM script contains ```"install": true```, the output files and the updated "env" and "state"
will be cached in the "local" CM database using the CM "cache" automation.
This is particularly useful when installing packages and tools or 
downloading ML models and data sets needed to build and deploy
complex applications and web services.

Next, you can try to run some [existing CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) 
and create the new ones yourself.



## Installing CM

Install CM as described [here](installation.md). Normally, CM should work on any OS and platform. 
However, if you encounter some issues, please report them [here](https://github.com/mlcommons/ck/issues)
(prefixed by [CK2/CM]).


## Installing the CM script automation

CM scripts can be embedded in Git repositories and tar/zip archives as a CM database.

We are prototyping CM scripts needed for MLOps and DevOps to unify 
collaborative benchmarking, optimization and deployment of ML Systems
in https://github.com/mlcommons/ck/tree/master/cm-mlops .

You can install it in CM as follows:

```bash
cm pull repo mlcommons@ck
```

Check that the CM script automation is available:
```bash
cm find automation script
```

Check available automation actions for the CM script automation:
```bash
cm help script
```

Check the API of the CM script run action:
```bash
cm run script --help
```

## Installing CM repository with CM scripts

CM scripts can be embedded in Git repositories and tar/zip archives as a CM database.
We are prototyping CM scripts needed for collaborative benchmarking, optimization and deployment of ML Systems
in http://github.com/octoml/cm-mlops .
You can install it in CM as follows:

```bash
cm pull repo octoml@cm-mlops
```

List available CM scripts:
```bash
cm find script
```

## Running "hello world" CM script

You can run a CM script that wraps run.sh and run.bat with echo "hello world" using its explicit name (CM alias):

```bash
cm run script print-hello-world

...

CM_ENV_TEST1 = TEST1
CM_ENV_TEST2 = 

HELLO WORLD!
```

or using tags:

```bash
cm run script --tags=print,hello-world,script

...

CM_ENV_TEST1 = TEST1
CM_ENV_TEST2 = TEST2

HELLO WORLD!
```

## Understanding the "hello world" CM script

Let's find the CM database entry for the CM script component by CM alias as follows:
```bash
cm find script print-hello-world
```

or using tags from meta description:


```bash
cm find script --tags=print,hello-world,script
```

Let's check the content of this directory (see on [GitHub]( https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world )):
```bash
ls `cm find script --tags=print,hello-world,script`
```

* *_cm.json* - meta description of this CM script
* *run.sh* - Linux or MacOS script 
* *run.bat* - Windows script

### Meta description

*_cm.json* describes how to find and run this CM script:

```json
{
  "automation_alias": "script",           # related CM automation alias
  "automation_uid": "5b4e0237da074764",   # related CM automation UID

  "alias": "print-hello-world",           # this CM script alias
  "uid": "b9f0acba4aca4baa",              # this CM script UID

  "tags": [          # Tags to find this CM script in CM databases (CM repositories 
                     # pulled from Git or downloaded as Zip/tar archives)
                     # or shared in Docker containers)
    "print",     # and differentiate this CM script from other CM script
    "hello-world",
    "hello world",
    "hello",
    "world",
    "script"
  ],

  "env": {                      # Set global environment variables
    "CM_ENV_TEST1": "TEST1"
  },

  "deps": [                     # A chain of dependencies on other CM scripts
    {                           # These CM scripts will be executed before
      "tags": "win,echo-off"    # running a given CM script
    }                           # and update global env variables
  ]
                                
  ...                           # Extra keys will be gradually added by the community
                                # while enhancing the CM script automation
                                # and keeping backwards compatibility
}
```

### Scripts

*_run.bat* and *_run.sh* are native scripts that will be executed by this CM script on Linux and Windows-based system:

```bash
echo ""
echo "CM_ENV_TEST1 = ${CM_ENV_TEST1}"
echo "CM_ENV_TEST2 = ${CM_ENV_TEST2}"

echo ""
echo "HELLO WORLD!"
```

The idea to use native scripts is to make it easier for researchers and engineers to reuse their existing automation scripts
while providing a common wrapper with a unified CLI, JSON API, extensible meta descriptions and portability layer in *customize.py*.


## Modifying environment variables

CM script automation merges "env" and "new_env" before running this script.

You can modify a given environment variable as follows:
```bash
cm run script --tags=print,hello-world,script --env.CM_ENV_TEST1=ABC1 --env.CM_ENV_TEST2=ABC2 

...

CM_ENV_TEST1 = TEST1
CM_ENV_TEST2 = ABC2

HELLO WORLD!
```

Note, that *CM_ENV_TEST1* did not change. This happened because *_cm.json* forces *CM_ENV_TEST1* to *TEST1*.
To update such variables, one should use --const instead of --env:
```bash
cm run script --tags=print,hello-world,script --const.CM_ENV_TEST1=ABC1 --env.CM_ENV_TEST2=ABC2 

...

CM_ENV_TEST1 = ABC1
CM_ENV_TEST2 = ABC2

HELLO WORLD!

```

You can use JSON file instead of CLI. Create *input.json* (or any other filename):
```json
{
  "tags":"print,hello-world,script",
  "env":{
    "CM_ENV_TEST1":"ABC1",
    "CM_ENV_TEST2":"ABC2"
  }
}
```

and run the CM script with this input file as follows:
```
cm run script @input.json
```


You can use YAML file instead of CLI. Create *input.yaml* (or any other filename):
```yaml
tags: "print,hello-world,script"
const:
  CM_ENV_TEST1: "ABC1"
env:
  CM_ENV_TEST2: "ABC2"
```

and run the CM script with this input file as follows:
```
cm run script @input.yaml
```


## Printing JSON output

You can see the output of the CM script automation in the JSON format as follows:

```bash
cm run script --tags=print,hello-world,script --const.CM_ENV_TEST1=ABC1 --env.CM_ENV_TEST2=ABC2 --out=json

CM_ENV_TEST1 = ABC1
CM_ENV_TEST2 = ABC2

HELLO WORLD!

{
  "env": {
    "CM_ENV_TEST1": "ABC1",
    "CM_ENV_TEST2": "ABC2",
    "CM_TMP_CURRENT_PATH": "D:\\",
    "CM_TMP_CURRENT_SCRIPT_PATH": "D:\\Work1\\CK\\ck\\cm-mlops\\script\\print-hello-world",
    "CM_TMP_PIP_VERSION_STRING": "",
    "CM_WINDOWS": "yes"
  },
  "new_env": {
    "CM_ENV_TEST1": "ABC1",
    "CM_WINDOWS": "yes"
  },
  "new_state": {
    "script_prefix": [
      "@echo off"
    ]
  },
  "return": 0,
  "state": {
    "script_prefix": [
      "@echo off"
    ]
  }
}
```

## Running CM scripts from Python

You can run CM script from python or Jupyter notebook as follows:

```python

import cmind as cm

r = cm.access({'action':'run',
               'automation':'script',
               'tags':'print,hello-world,script',
               'const':{
                 'CM_ENV_TEST1':'ABC1',
               },
               'env':{
                 'CM_ENV_TEST2':'ABC2'
               }
              })

print (r)

```

```bash
...

CM_ENV_TEST1 = ABC1
CM_ENV_TEST2 = ABC2

HELLO WORLD!

{'return': 0, 'new_state': {'script_prefix': ['@echo off']}, 'new_env': {'CM_ENV_TEST2': 'TEST2'}}

```

## Understanding CM script dependencies

CM meta descriptions enable a very simple mechanism to inter-connect native scripts and enable pipelines and workflows 
(also implemented as CM scripts) without the need for specialized workflow frameworks.

Our idea is to let any CM script automatically run additional CM scripts to prepare required environment variables,
"state" and files for a given platform and user requirements required for other CM scripts in a pipeline or workflow.

We describe a pipeline of CM script dependencies that must be executed before running a native script using *deps* list in the *_cm.json* of this CM script:

```json

{
  "deps": [
    {                           
      "tags":  # a string of tags separated by comma to find and execute the 1st CM script
    },
    {                           
      "tags":  # 2nd CM script
    },
    ...
  ]
}

```

We can also specify dependencies executing after the native script inside CM automation as follows:
```json
{
   "post_deps": [
    {                           
      "tags":  # a string of tags separated by comma to find and execute the 1st CM script
    },
    ...
   ]
}
```

For example, our "Hello world" CM script example has just one dependency described with tags "win,echo-off".

We can find this component as follows:

```bash
cm find script --tags=win,echo-off
```

This is a [very simple CM script]( https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-echo-off-win )
that doesn't have dependencies on other CM script and does not even have native OS scripts.

However, it has a *customize.py* file with the *preprocess* function that is executed
when we run this CM script. 

Note that this function is used to update environment variables and the "state" dictionary
before running the native script or to influence the next CM scripts. For example, it can set up an 
environment variable that will be used in some other CM scripts in the dependency chain to skip their execution
as shown in [this example]( https://github.com/mlcommons/ck/blob/master/cm-mlops/script/set-echo-off-win/customize.py#L21 ).

This component detects that the host platform is Windows and adds "@echo off" to all further CM script executions
to minimize output noise. It does nothing on Linux:

```python

    if os_info['platform'] == 'windows':

        script_prefix = state.get('script_prefix',[])

        s='@echo off'
        if s not in script_prefix:
            script_prefix.insert(0, s)

        state['script_prefix'] = script_prefix

```

We can run it independently as follows:

```bash
cm run script --tags=win,echo-off --out=json
```

The [CM script automation]( https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/script/module.py#L145 ) 
monitors the "state" and alters the execution of the next CM scripts  
based on specialized keys in the "state" dictionary (such as "script_prefix").

This approach allows the community to gradually extend this automation and CM scripts without breaking 
backwards compatibility!


## Customizing CM script execution

We use *customize.py* to preprocess the execution of a native script (if exists),
i.e. prepare environment, the state dictionary and files needed to run this script.

You can find the automation code that prepares the input for the preprocess function 
[here]( https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/script/module.py#L927 ).

We can also use this function to skip the execution of this CM script based on environment, state and files
if it returns *{"skip":True}*.


After executing the preprocess function, the CM script automation will record the global state dictionary
into *tmp-state.json* and the local state dictionary from this CM script into *tmp-state-new.json*.

The CM script automation will then run a native script with the global environment updated by 
and will call a native script (run.sh on Linux/MacOS or run.bat on Windows).

The native script will call some MLOps or DevOps tools based on environment variables
and files prepared by previous CM scripts or already preset in the native environment or container.

The native script can also create 2 files that will be automatically picked up and processed by the CM script automation:
* *tmp-run-env.out* - list of environment variables to update the "new_env" of a given CM script
* *tmp-run-state.json* - the state dictionary to update the "new_state" of a given CM script

If the *customize.py* script exists with a *postprocess* function, the CM script will call it
to finalize the postprocessing of files, environment variables and the state dictionary.


## Unifying host OS and CPU detection

In order to make MLOps and DevOps tools more portable and interoperable, we need to unify
the information about host OS and CPU. We are developing the following 2 CM script:

* *detect-os* - See [CM script on GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
* *detect-cpu* - See [CM script on GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)

These 2 CM script have *customize.py* with preprocess and postprocess functions
and a native run script to detect OS info and update environment variables
and the state dictionary needed by dependent CM scripts. 

You can run them on your platform as follows:

```bash
cm run script --tags=detect-os --out=json

...

cm run script --tags=detect-cpu --out=json
```

## Detecting, installing and caching system dependencies

We can now use CM scripts to detect or install system dependencies based on the OS and CPU info.

We have implemented such a prototype of the CM script [*get-sys-utils-cm*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
that either downloads and caches various basic tools (wget, tar, gzip) on Windows
or installs system dependencies via *apt-get* on Linux with *sudo*.

You can test it as follows:
```bash
cm run script --tags=get,sys-utils-cm
```

## Detecting, installing and caching tools

One of our goals is to automatically detect all existing dependencies required to run a given tool or application
before installing the fixed ones to be able to automatically adapt tools and applications to a user platform and environment.

We are developing CM scripts *get-{tool or artifact}* to detect installed artifacts, prepare their environment
and cache them in the *local* CM repository using the "installed" automation.

If installed artifact doesn't exist, we either enhance above scripts to include download, install and even build
or we create new CM scripts *install-{tool or artifact}* that download and prepare tools and artifacts (install, build
and preprocess them).

Let's check the CM script *get-python3* (See [CM script on GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)).
It has *customize.py* with *preprocess* function that implements the search for python3 on Linux
or python.exe on Windows, 2 native scripts *run.sh* and *run.bat* to get the version of the detected python installation,
and *postprocess* function to prepare environment variables *CM_PYTHON_BIN* and *CM_PYTHON_BIN_WITH_PATH*
that can be used by other CM scripts.

Let's run it:
```bash
cm run script --tags=get-python --out=json
```

If you run it for the first time and CM script detects multiple versions of python, it will ask you to select one.
IC will then cache the output in the *cache* entry of the CM database. You can see all *cache* CM entries
for other tools and artifacts as follows:
```bash
cm show cache
```
or
```bash
cm show cache --tags=get-python
```

You can see the cached files as follows:
```bash
ls `cm find cache --tags=get-python`
```

If you (or other CM script) run this CM script to get the python tool for the second time, CM script will use the cached data:
```bash
cm run script --tags=get,python --out=json
```

Such approach allows us to "probe" the user environment and detect different tools that can be unified
and used by other CM scripts or external workflows.

If a tool or artifact is not detected, we can use installation script.
For example, you can install a prebuilt version of LLVM in a unified way on Windows, Linux and MacOs as follows:
```bash
cm run script --tags=install,prebuilt-llvm --version=14.0.0
```

## Detecting, installing and caching artifacts

One of the differences of MLOps from DevOps is that MLOps must be able to deal with diverse ML models, data sets 
and continuous experiments to iteratively improve accuracy, performance, energy usage, model/memory size and other
important parameters of the ML and AI-based applications.

That is why our CM script concept is applied not only to scripts and tools but also to any user artifact required
to develop, optimize, deploy and use a complex application

For example, we have developed 2 CM scripts to demonstrate how to install "ResNet-50" model and reduced "ImageNet" dataset with 500 images:
* [*get-ml-model-resnet50-onnx*]( https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-onnx )
* [*get-imagenet-val*]( https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-imagenet-val )

You can run them as follows:
```bash
cm run script --tags=get,ml-model-onnx,resnet50
cm run script --tags=get,dataset,imagenet

cm show cache
```

or

```bash
cm run script --tags=get,ml-model-onnx,image-classification
cm run script --tags=get,dataset,image-classification
```

When executed for the first time, these CM scripts will download ML artifacts and cache them using CM "cache" automation.

Note that you can find these "cache" CM entries using CM database API and use the *tmp-env.sh* or *tmp-env.bat* directly
in your own projects without the need for further CM automation. Such approach allows gradual decomposition of complex
applications into CM scripts and gradual (evolutionary) adoption of the CM technology.

### Using variations

It is possible to download a specific version of an artifact using so-called "variations".
For example, the CM script *get-ml-model-resnet50-onnx* has 2 variations for ONNX Opset 8 and 11
as described in [_cm.json]( https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-ml-model-resnet50-onnx/_cm.json#L20 ).

It is possible to specify a required variation when running a given CM script using tags with "_" prefix.
For example, you can install ResNet-50 model with "1.5-opset-11" variation as follows:
```bash
cm run script --tags=get,ml-model,resnet50-onnx,_1.5-opset-11
```

You can also install another variation "1.5-opset-8" of this CM script at the same time:
```bash
cm run script --tags=get,ml-model,resnet50-onnx,_1.5-opset-8
```

## Assembling image classification pipeline

We can now use existing CM scripts as basic "LEGO" blocks to quickly assemble more complex automation pipelines and workflows
as new CM scripts with the same API/CLI.


We demonstrate this approach by implementing simple image classification as an CM script 
[*app-image-classification-onnx-py*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py).

It has a dependency on the above CM scripts including OS unification, python detection, ResNet-50 model and the ImageNet dataset 
as described in its [*_cm.json*](prototype-image-classification-onnx-py):

```json
"deps": [
    {
      "tags": "set,echo-off,win"
    },
    {
      "tags": "detect,os,info"
    },
    {
      "tags": "get,sys-utils-cm"
    },
    {
      "tags": "get,python"
    },
    {
      "tags": "get,dataset,imagenet,image-classification,original"
    },
    {
      "tags": "get,dataset-aux,imagenet-aux,image-classification"
    },
    {
      "tags": "get,ml-model-onnx,resnet50,image-classification"
    },
    {
      "tags": "get,onnxruntime,python-lib"
    }
  ],
```

It also has *run.sh* and *run.bat* to install Python requirements and run a Python script 
that will output classification results. You can run it as follows:

```bash
cm run script --tags=app,image-classification,onnx,python
cm run script --tags=app,image-classification,onnx,python --out=json

```

If you run this CM script for the first time, it will run and cache all dependencies.

You can run it with your own image as follows:
```bash
cm run script --tags=app,image-classification,onnx,python --input={path to my JPEG image}
```

## Compiling and running image corner detection

We can also create a pipeline from CM scripts to compile and run some program.
We have implemented a sample [image corner detection CM script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-corner-detection) 
that compiles C program using a detected or installed compiler via CM (for example LLVM)
and runs it with some image.

First, let's detect installed LLVM:
```bash
cm run script --tags=get,llvm
```
or install a prebuilt version on Linux, MacOs or Windows:
```bash
cm run script --tags=install,prebuilt-llvm --version=14.0.0
```

We can then run CM script to compile and run image corner detection as follows:
```bash
cm run script --tags=app,corner-detection --input={path to my PGM image}
```

Normally, a C program will be compiled, executed and a new image created with
detected corners: *output_image_with_corners.pgm*



## Running CM scripts inside containers

CM scripts can be used both in the native environment and containers.
In fact, CM scripts can be used to automatically connect the same complex automation pipelines and workflows 
with external data and tools via environment variables and files. 

We are developing the concept of modular containers assembled from "CM" scripts
and will update this section soon!

Related CM scripts under development:
* https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile
* https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image
* https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-image-classification-onnx-py
* https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-mlperf-vision-reference








                           


## Related

* [CM "script" automation specification](README-specs.md)
* [List of portable and reusable CM scripts from MLCommons](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md)
* [CM "cache" automation](../cache/README-extra.md)
