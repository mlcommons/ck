# Tutorial: understanding CM scripts

*Note that CM script automation is under development and can still evolve!*

This tutorial demonstrates how to organize your existing scripts and artifacts
as a database of more portable, plug&play, deterministic and reusable components
with zero or little effort using a unified CM CLI, API and extensible meta descriptions.

Such CM scripts can be chained and interconnected into complex automation pipelines and workflows 
with a minimal effort in a native environment and without the need for specialized workflow
frameworks and containers.

This approach provides a simple and practical intermediate step 
to make existing DevOps and MLOps scripts 
more interchangeable, portable, deterministic, reusable and reproducible
before investing into other specialized workflow frameworks, platforms and containers.

*You may be interested to check the following docs to better understand the CM/CK concepts: 
 [CK concepts](https://arxiv.org/abs/2011.01149), 
 [CM (aka CK2) basics](tutorial-concept.md)*.

## Motivation

The development of the CM unification framework (aka CK2) is motivated by our tedious experience trying to
[make ML and systems research more deterministic, reproducible and deployable in production](https://learning.acm.org/techtalks/reproducibility).
When organizing [artifact evaluation at ML and Systems conferences](https://cTuning.org/ae) 
we have noticed that researchers and engineers spent most of the time 
trying to understand numerous technical reports, README files, specifications, dependencies, 
ad-hoc scripts, tools, APIs, models and data sets of all shared projects 
to be able to [validate experimental, benchmarking and optimization results](https://cknowledge.io/?q=%22reproduced-papers%22) 
and adapt ad-hoc projects to the real world with very diverse 
software, hardware, user environments, settings and data.

![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/cm-ad-hoc-scripts.png)

However, we have also noticed that most complex applications and experiments can be decomposed
into relatively simple, small and atomic actions easily reusable across all projects.
Such actions usually update OS environment variables and produce new files while taking
host and target platform parameters into account.

### Portable CM scripts

That is why we started developing the CM automation called 
["script")](https://github.com/mlcommons/ck/tree/master/cm-devops/automation/script)
to wrap existing native user scripts and artifacts for DevOps and MLOps
with a simple and unified Python API and CLI.

Such CM scripts can be shared inside local directories, Git projects 
and containers as a database of components with an extensible JSON/YAML meta description
that provide dependencies on other scripts, pre/post processing Python code
and unification of environment variables and files:

![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/cm-plug-and-play-script-concept.png)

### Pipeline of CM scripts

The CM script automation has a "run" action that takes a unified CM dictionary with the following keys as the input:

* "artifact" (str): CM artifact with CM script from [this list](https://github.com/mlcommons/ck/tree/master/cm-devops/automation/script)
* "tags" (str): instead of using an explicit CM script name, we can use the tags separated by comma to find a given CM script

* "env" (dict): original environment (can be empty)
* "state" (dict): original state (can be empty)

* extra flags to customize the execution of a given CM script

The output of this automation is also a unified CM dictionary:

* "new_env" (dict): update for the original environment (excluding original environment)
* "new_state" (dict): update for the original state (excluding original environment)

![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/cm-plug-and-play-script-details.png)

A CM script simply wraps existing user scripts (run.sh on Unix or run.bat on Windows),
reads meta description, runs other CM script dependencies,
runs "preprocessing" function from "customize.py" (if exists)
to update "env" and the "state" and produce extra files needed for a native script,
runs the script, reads produced files with updated "env" and "state",
and runs "postprocessing" function from "customize.py" (if exists)
to finalize updating "env" and "state".

If meta description of a given CM script contains ```"install": true```, the output files and the updated "env" and "state"
will be cached in the "local" CM database using the "installed" automation.
This is particularly useful when installing packages and tools or 
downloading ML models and data sets needed to build and deploy
complex applications and web services.

Next, you can try to run some [existing CM scripts](https://github.com/octoml/cm-mlops/tree/main/script) 
and create the new ones yourself.



## Installing CM

Install CM as described [here](installation.md). Normally, CM should work on any OS and platform. 
However, if you encounter some issues, please report them [here](https://github.com/mlcommons/ck/issues).


## Installing the CM script automation

Pull repository with CM automations:

```bash
$ cm pull repo mlcommons@ck
```

Check that the CM script automation is available:
```bash
$ cm find automation script
```

Check available automation actions for the CM script automation:
```bash
$ cm help script
```

Check the API of the CM script run action:
```bash
$ cm run script --help
```

## Installing CM repository with CM scripts

CM scripts can be embedded in Git repositories and tar/zip archives as a CM database.
We are prototyping CM scripts needed for collaborative benchmarking, optimization and deployment of ML Systems
in http://github.com/octoml/cm-mlops .
You can install it in CM as follows:

```bash
$ cm pull repo octoml@cm-mlops
```

List available CM scripts:
```bash
$ cm find script
```

## Running "hello world" CM script

You can run a CM script that prints "hello world" using its explicit name (CM alias):

```bash
$ cm run script prototype-print-hello-world

...

CM_ENV_TEST1 = TEST1
CM_ENV_TEST2 = TEST2

HELLO WORLD!
```

or using tags:

```bash
$ cm run script --tags=print,hello-world,script

...

CM_ENV_TEST1 = TEST1
CM_ENV_TEST2 = TEST2

HELLO WORLD!
```

## Understanding the "hello world" CM script

Let's find the CM database entry for the CM script component by CM alias as follows:
```bash
$ cm find script prototype-print-hello-world
```

or using tags from meta description:


```bash
$ cm find script --tags=print,hello-world,script
```

Let's check the content of this directory (see on [GitHub]( https://github.com/octoml/cm-mlops/tree/main/script/prototype-print-hello-world )):
```bash
$ ls `cm find script --tags=print,hello-world,script`
```

* *_cm.json* - meta description of this CM script
* *run.sh* - Linux (Unix) script 
* *run.bat* - Windows script

### Meta description

*_cm.json* describes how to find and run this CM script:

```json
{
  "automation_alias": "ic",               # related CM automation alias
  "automation_uid": "972c28dafb2543fa",   # related CM automation UID

  "alias": "prototype-print-hello-world", # this CM script alias
  "uid": "b9f0acba4aca4baa",              # this CM script UID

  "tags": [          # Tags to find this CM script in CM databases (CM repositories 
                     # pulled from Git or downloaded as Zip/tar archives)
                     # or shared in Docker containers)
    "prototype",     # and differentiate this CM script from other CM script
    "print",
    "hello-world",
    "hello world",
    "hello",
    "world",
    "script"
  ],

  "env": {                      # Set global environment variables
    "CM_ENV_TEST1": "TEST1"
  },

  "new_env": {                  # Set local environment variables
    "CM_ENV_TEST2": "TEST2"     # (for this CM script only)
  },

  "deps": [                     # A chain of dependencies on other CM scripts
    {                           # These CM scripts will be executed before
      "tags": "win,echo-off"    # running a given CM script
    }
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

## Modifying environment variables

CM script automation merges "env" and "new_env" before running this script.

You can modify a given environment variable as follows:
```bash
$ cm run script --tags=print,hello-world,script --env.CM_ENV_TEST1=ABC1 --env.CM_ENV_TEST2=ABC2 

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
$ cm run script @input.json
```


You can use YAML file instead of CLI. Create *input.yaml* (or any other filename):
```yaml
tags: "print,hello-world,script"
env:
  CM_ENV_TEST1: "ABC1"
  CM_ENV_TEST2: "ABC2"
```

and run the CM script with this input file as follows:
```
$ cm run script @input.json
```


## Printing JSON output

You can see the output of the CM script automation in the JSON format as follows:

```bash
$ cm run script --tags=print,hello-world,script --env.CM_ENV_TEST1=ABC1 --env.CM_ENV_TEST2=ABC2 --out=json

CM_ENV_TEST1 = ABC1
CM_ENV_TEST2 = ABC2

HELLO WORLD!
{
  "new_env": {
    "CM_ENV_TEST2": "TEST2"
  },
  "new_state": {
    "script_prefix": [
      "@echo off"
    ]
  },
  "return": 0
}

```

## Running CM scripts from Python

You can run CM script from python or Jupyter notebook as follows:

```python

import cmind as cm

r = cm.access({'action':'run',
               'automation':'script',
               'tags':'print,hello-world,script',
               'env':{
                 'CM_ENV_TEST1':'ABC1',
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

We describe a pipeline of CM script dependencies that must be executed before running a given CM script using *deps* list in the *_cm.json* of this CM script:

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

For example, our "Hello world" CM script example has just one dependency described with tags "win,echo-off".

We can find this component as follows:

```bash
$ cm find script --tags=win,echo-off
```

This is a [very simple CM script]( https://github.com/octoml/cm-mlops/tree/main/script/prototype-set-echo-off-win )
that doesn't have dependencies on other CM script and does not even have native OS scripts.

However, it has a *customize.py* file with the *preprocess* function that is executed
when we run this CM script. 

Note that this function is used to update environment variables and the "state" dictionary
before running the native script or to influence the next CM scripts. For example, it can set up an 
environment variable that will be used in some other CM scripts in the dependency chain to skip their execution
as shown in [this example]( https://github.com/octoml/cm-mlops/blob/main/script/prototype-set-echo-off-win/customize.py#L21 ).

This component detects that the host platform is Windows and adds "@echo off" to all further CM script executions
to minimize output noise. It does nothing on Linux:

```python

    if os_info['platform'] == 'windows':

        script_prefix = new_state.get('script_prefix',[])

        s='@echo off'
        if s not in script_prefix:
            script_prefix.insert(0, s)
        
        new_state['script_prefix'] = script_prefix

```

We can run it independently as follows:

```bash
$ cm run script --tags=win,echo-off --out=json
```

The [CM script automation]( https://github.com/mlcommons/ck/blob/master/cm-devops/automation/script/module.py) 
monitors the "state" and alters the execution of the next CM scripts  
based on specialized keys in the "state" dictionary (such as "script_prefix").

This approach allows the community to gradually extend this automation and CM scripts without breaking 
backwards compatibility!


## Customizing CM script execution

We use *customize.py* to preprocess the execution of a native script (if exists),
i.e. prepare environment, the state dictionary and files needed to run this script.

You can find the automation code that prepares the input for the preprocess function 
[here]( https://github.com/mlcommons/ck/blob/master/cm-devops/automation/script/module.py#L567 ).

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

You can find the automation code that prepares the input for the postprocess function 
[here]( https://github.com/mlcommons/ck/blob/master/cm-devops/automation/script/module.py#L699 ).


## Unifying host OS and CPU detection

In order to make MLOps and DevOps tools more portable and interoperable, we need to unify
the information about host OS and CPU. We are developing the following 2 CM script:

* *detect-os* - See [CM artifact](https://github.com/octoml/cm-mlops/tree/main/script/prototype-detect-os)
* *detect-cpu* - See [CM artifact](https://github.com/octoml/cm-mlops/tree/main/script/prototype-detect-cpu)

These 2 CM script have *customize.py* with preprocess and postprocess functions
and a native run script to detect OS info and update environment variables
and the state dictionary needed by dependent CM scripts. 

You can run them on your platform as follows:

```bash
$ cm run script --tags=detect-os --out=json

...

$ cm run script --tags=detect-cpu --out=json
```

## Detecting, installing and caching system dependencies

We can now use CM scripts to detect or install system dependencies based on the OS and CPU info.
We have implemented such a prototype of the CM script [*prototype-install-sys-utils-cm*](https://github.com/octoml/cm-mlops/tree/main/script/prototype-install-sys-utils-cm)
that either downloads and caches various basic tools (wget, tar, gzip) on Windows
or installs system dependencies via *apt-get* on Linux with *sudo*.

You can test it as follows:
```bash
$ cm run script --tags=install,sys-utils-cm
```

## Detecting, installing and caching tools

One of our goals is to automatically detect all existing dependencies required to run a given tool or application
before installing the fixed ones to be able to automatically adapt tools and applications to a user platform and environment.

We are developing CM scripts *get-{tool or artifact}* to detect installed artifacts, prepare their environment
and cache them in the *local* CM repository using the "installed" automation.

If installed artifact doesn't exist, we either enhance above scripts to include download, install and even build
or we create new CM scripts *install-{tool or artifact}* that download and prepare tools and artifacts (install, build
and preprocess them).

Let's check the CM script *get-python3* (See [CM artifact at GitHub](https://github.com/octoml/cm-mlops/tree/main/script/prototype-get-python3)).
It has *customize.py* with *preprocess* function that implements the search for python3 on Linux
or python.exe on Windows, 2 native scripts *run.sh* and *run.bat* to get the version of the detected python installation,
and *postprocess* function to prepare environment variables *CM_PYTHON_BIN* and *CM_PYTHON_BIN_WITH_PATH*
that can be used by other CM scripts.

Let's run it:
```bash
$ cm run script --tags=get-python --out=json
```

If you run it for the first time and CM script detects multiple versions of python, it will ask you to select one.
IC will then cache the output in the *installed* entry of the CM database. You can see all *installed* CM entries
for other tools and artifacts as follows:
```bash
$ cm list installed
```
or
```bash
$ cm list installed --tags=get-python
```

You can see the cached files as follows:
```bash
$ ls `cm find installed --tags=get-python`
```

If you (or other CM script) run this CM script to get the python tool for the second time, CM script will use the cached data:
```bash
$ cm run script --tags=get,python --out=json
```

Such approach allows us to "probe" the user environment and detect different tools that can be unified
and used by other CM scripts or external workflows.

If a tool or artifact is not detected, we can use installation script.
For example, you can install a prebuilt version of LLVM in a unified way on Windows, Linux and MacOs as follows:
```bash
$ cm run scipt --tags=install,prebuilt-llvm --version=14.0.0
```

## Detecting, installing and caching artifacts

One of the differences of MLOps from DevOps is that MLOps must be able to deal with diverse ML models, data sets 
and continuous experiments to iteratively improve accuracy, performance, energy usage, model/memory size and other
important parameters of the ML and AI-based applications.

That is why our CM script concept is applied not only to scripts and tools but also to any user artifact required
to develop, optimize, deploy and use a complex application

For example, we have developed 2 CM scripts to demonstrate how to install "ResNet-50" model and reduced "ImageNet" dataset with 500 images:
* [*prototype-install-ml-model-resnet50-onnx*]( https://github.com/octoml/cm-mlops/tree/main/script/prototype-install-ml-model-resnet50-onnx )
* [*prototype-install-imagenet-val*]( https://github.com/octoml/cm-mlops/tree/main/script/prototype-install-imagenet-val )

You can run them as follows:
```bash
$ cm run script --tags=install,ml-model,resnet50-onnx
$ cm run script --tags=install,dataset,imagenet
```

or

```bash
$ cm run script --tags=install,ml-model,image-classification
$ cm run script --tags=install,dataset,image-classification
```

When executed for the first time, these CM scripts will download ML artifacts and cache them using CM "installed" automation.

Note that you can find these "installed" CM entries using CM database API and use them in your own projects
without the need for further CM automation. Such approach allows gradual decomposition of complex
applications into CM scripts and gradual (evolutionary) adoption of the CM technology.

### Using variations

It is possible to download a specific version of an artifact using so-called "variations".
For example, the CM script *prototype-install-ml-model-resnet50-onnx* has 2 variations for ONNX Opset 8 and 11
as described in [_cm.json]( https://github.com/octoml/cm-mlops/blob/main/script/prototype-install-ml-model-resnet50-onnx/_cm.json#L20 ).

It is possible to specify a required variation when running a given CM script using tags with "_" prefix.
For example, you can install ResNet-50 model with "1.5-opset-11" variation as follows:
```bash
$ cm run script --tags=install,ml-model,resnet50-onnx,_1.5-opset-11
```

You can also install another variation "1.5-opset-8" of this CM script at the same time:
```bash
$ cm run script --tags=install,ml-model,resnet50-onnx,_1.5-opset-8
```

## Assembling image classification pipeline

We can now use existing CM scripts as basic "LEGO" blocks to quickly assemble more complex automation pipelines and workflows
as new CM scripts with the same API/CLI.


We demonstrate this approach by implementing simple image classification as an CM script 
[*prototype-image-classification-onnx-py*](https://github.com/octoml/cm-mlops/tree/main/script/prototype-image-classification-onnx-py).

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
      "tags": "install,sys-utils-cm"
    },
    {
      "tags": "get,python"
    },
    {
      "tags": "install,dataset,image-classification,original"
    },
    {
      "tags": "install,dataset-aux,image-classification"
    },
    {
      "tags": "install,ml-model-onnx,image-classification"
    }
  ],
```

It also has *run.sh* and *run.bat* to install Python requirements and run a Python script 
that will output classification results. You can run it as follows:

```bash
$ cm run script --tags=app,image-classification,onnx,python --out=json
```

If you run this CM script for the first time, it will run and cache all dependencies.

You can run it with your own image as follows:
```bash
$ cm run script --tags=app,image-classification,onnx,python --input={path to my JPEG image}
```

## Compiling and running image corner detection

We can also create a pipeline from CM scripts to compile and run some program.
We have implemented a sample [image corner detection CM script](https://github.com/octoml/cm-mlops/tree/main/script/prototype-image-corner-detection) 
that compiles C program using a detected or installed compiler via CM (for example LLVM)
and runs it with some image.

First, let's detect installed LLVM:
```bash
$ cm run script --tags=get,llvm
```
or install a prebuilt version on Linux, MacOs or Windows:
```bash
$ cm run script --tags=install,prebuilt-llvm --version=14.0.0
```

We can then run CM script to compile and run image corner detection as follows:
```bash
$ cm run script --tags=app,corner-detection --input={path to my PGM image}
```

Normally, a C program will be compiled, executed and a new image created with
detected corners: *output_image_with_corners.pgm*



## Running CM scripts inside containers

CM scripts can be used both in the native environment and containers.
In fact, CM scripts can be used to automatically connect the same complex automation pipelines and workflows 
with external data and tools via environment variables and files. 

We are developing the concept of modular containers assembled from "CM" scripts
and will update this section soon!


## Adding your own CM script

One of the main goals of CM (aka CK2) is to make it easier to onboard new users 
and add new CM components in comparison with the 1st version (CK2).

You can now add your own working component with some tags and run it as a dummy filter 
with a minimal effort as follows:

```bash
$ cm add script my-cool-component --tags=my,cool-component,prototype
$ cm run script my-cool-component
$ cm run script --tags=my,cool-component
```

You can then find this component and just add there your own script with the name *run.sh* 
on Linux/MacOS or *run.bat* on Windows:
```bash
$ cd `cm find script my-cool-component`

$ cat > run.sh
echo "My cool component"

$ cm run script my-cool-component

...
My cool component
```

You can then extend *_cm.json* and add more tags or dependencies to reuse environment variables and files
in your script prepared by other CM scripts from public or private projects.

Finally, you can add the *customize.py* script with *preprocess* and *postprocess* functions to implement more
complex logic to customize the execution of a given CM script based on previous dependencies, flags, platform and CPU info, etc.


## Extending CM scripts as a collaborative playground

We have developed CM as a collaborative playground to work with the community and gradually unify the APIs of diverse DevOps and MLOps scripts and tools,
and interconnect them to simplify the development, optimization, deployment and usage of complex applications into intelligent "CM" components.

Our next steps:
* agreeing on and unifying tags that describe different CM scripts in a unique way
* agreeing on and unifying scripts, env variables and state of different CM scripts
* adding support for different CM scripts versions and ranges similar to Pypi
* adding support to run CM script scripts for a specific host OS version and CPU
* implementing MLPerf benchmark as a pipeline of CM scripts

Please get in touch if you want to join this collaborative effort to unify DevOps and MLOps 
and make them more portable, interoperable and deterministic.
