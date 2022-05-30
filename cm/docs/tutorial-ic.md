# Tutorial: understanding intelligent CM components

*Note that IC automation is under development and can still evolve!*

This tutorial demonstrates how to organize ad-hoc DevOps and MLOps scripts
and related artifacts into a database of portable and reusable components.
Such components can be chained into complex automation pipelines with a minimal effort
in a native environment and without the need for specialized workflow
frameworks and containers.
This approach provides a simple and practical intermediate step 
to make existing development, optimization and deployment scripts
for complex applications more interchangeable, portable, deterministic, reusable and reproducible
before investing into other specialized workflow frameworks, platforms and containers.

*We suggest you to read the following docs to better understand the CM/CK concepts 
 before this tutorial: [CK concepts](https://arxiv.org/abs/2011.01149), 
 [CM (aka CK2) basics](tutorial-concept.md)*.

## Motivation

The development of the CM unification framework is motivated by our tedious experience trying to
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

### Intelligent CM component (IC)

That is why we started developing the CM automation called 
[ic ("intelligent component")](https://github.com/mlcommons/ck/tree/master/cm-devops/automation/ic)
to wrap existing ad-hoc DevOps and MLOps scripts and artifacts
with a simple and unified Python API and CLI.

Such components can be shared inside local directories, Git projects 
and containers as a database of artifacts with an extensible JSON/YAML meta description:
https://github.com/octoml/cm-mlops/tree/main/ic .

![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/cm-ic-concept.png)

### IC pipeline

The ic automation has a "run" action that takes a unified CM dictionary with the following keys as the input:

* "artifact" (str): CM IC artifact from [this list](https://github.com/mlcommons/ck/tree/master/cm-devops/automation/ic)
* "tags" (str): instead of using an explicit IC name, we can use the tags separated by comma to find a given IC

* "env" (dict): original environment (can be empty)
* "state" (dict): original state (can be empty)

* extra flags to customize the execution of a given IC

The output of this automation is also a unified CM dictionary:

* "new_env" (dict): update for the original environment (excluding original environment)
* "new_state" (dict): update for the original state (excluding original environment)

![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/cm-ic-details.png)

An intelligent CM component simply wraps existing ad-hoc script (run.sh on Unix or run.bat on Windows),
reads meta description, runs other IC dependencies,
runs "preprocessing" function from "customize.py" (if exists)
to update "env" and the "state" and produce extra files needed for an ad-hoc script,
runs the script, reads produced files with updated "env" and "state",
and runs "postprocessing" function from "customize.py" (if exists)
to finalize updating "env" and "state".

If meta description of a given IC contains ```"install": true```, the output files and the updated "env" and "state"
will be cached in the "local" CM database using the "installed" automation.
This is particularly useful when installing packages and tools or 
downloading ML models and data sets needed to build and deploy
complex applications and web services.

Next, you can try to run [existing ICs](https://github.com/octoml/cm-mlops/tree/main/ic) 
and create the new ones yourself.



## Installing CM

Install CM as described [here](installation.md). Normally, CM should work on any OS and platform. 
However, if you encounter some issues, please report them [here](https://github.com/mlcommons/ck/issues).


## Installing the IC automation

Pull repository with CM automations:

```bash
$ cm pull repo mlcommons@ck
```

Check that the IC automation is available:
```bash
$ cm find automation ic
```

Check available automation actions for the IC:
```bash
$ cm help ic
```

Check the API of the IC run action:
```bash
$ cm run ic --help
```

## Installing CM repository with ICs

Intelligent CM components can be embedded in Git repositories and tar/zip archives.
We are prototyping ICs needed for collaborative benchmarking, optimization and deployment of ML Systems
in http://github.com/octoml/cm-mlops .
You can install it in CM as follows:

```bash
$ cm pull repo octoml@cm-mlops
```

List available intelligent components:
```bash
$ cm find ic
```

## Running "hello world" IC

You can run an intelligent CM component that prints "hello world" using its explicit name (CM alias):

```bash
$ cm run ic prototype-print-hello-world

...

CM_ENV_TEST1 = TEST1
CM_ENV_TEST2 = TEST2

HELLO WORLD!
```

or using tags:

```bash
$ cm run ic --tags=print,hello-world,script

...

CM_ENV_TEST1 = TEST1
CM_ENV_TEST2 = TEST2

HELLO WORLD!
```

## Understanding "hello world" IC

Let's find the CM database entry for the IC component by CM alias as follows:
```bash
$ cm find ic prototype-print-hello-world
```

or using tags from meta description:


```bash
$ cm find ic --tags=print,hello-world,script
```

Let's check the content of this directory (see on [GitHub](https://github.com/octoml/cm-mlops/tree/main/ic/prototype-echo-hello-world)):
```bash
$ ls `cm find ic --tags=print,hello-world,script`
```

* *_cm.json* - meta description of this IC
* *run.sh* - Linux (Unix) script 
* *run.bat* - Windows script

### Meta description

*_cm.json* describes how to find and run this IC:

```json
{
  "automation_alias": "ic",               # related CM automation alias
  "automation_uid": "972c28dafb2543fa",   # related CM automation UID

  "alias": "prototype-print-hello-world", # this IC alias
  "uid": "b9f0acba4aca4baa",              # this IC UID

  "tags": [          # Tags to find this IC in CM databases (CM repositories 
                     # pulled from Git or downloaded as Zip/tar archives)
                     # or shared in Docker containers)
    "prototype",     # and differentiate this IC from other IC
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
    "CM_ENV_TEST2": "TEST2"     # (for this IC only)
  },

  "deps": [                     # A chain of dependencies on other IC
    {                           # These IC will be executed before
      "tags": "win,echo-off"    # running a given IC
    }
  ]
                                
  ...                           # Extra keys will be gradually added by the community
                                # while enhancing the IC automation
                                # and keeping backwards compatibility
}
```

### Scripts

*_run.bat* and *_run.sh* are native scripts that will be executed by this IC components on Linux and Windows-based system:

```bash
echo ""
echo "CM_ENV_TEST1 = ${CM_ENV_TEST1}"
echo "CM_ENV_TEST2 = ${CM_ENV_TEST2}"

echo ""
echo "HELLO WORLD!"
```

## Modifying environment variables

IC merges "env" and "new_env" before running this script.

You can modify a given environment variable as follows:
```bash
$ cm run ic --tags=print,hello-world,script --env.CM_ENV_TEST1=ABC1 --env.CM_ENV_TEST2=ABC2 

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

and run the IC with this input file as follows:
```
$ cm run ic @input.json
```


You can use YAML file instead of CLI. Create *input.yaml* (or any other filename):
```yaml
tags: "print,hello-world,script"
env:
  CM_ENV_TEST1: "ABC1"
  CM_ENV_TEST2: "ABC2"
```

and run the IC with this input file as follows:
```
$ cm run ic @input.json
```


## Printing JSON output

You can see the output of the IC automation in JSON as follows:

```bash
$ cm run ic --tags=print,hello-world,script --env.CM_ENV_TEST1=ABC1 --env.CM_ENV_TEST2=ABC2 --out=json

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

## Running IC from Python

You can run IC from python or Jupyter notebook as follows:

```python

import cmind as cm

r = cm.access({'action':'run',
               'automation':'ic',
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

## Understanding IC dependencies

We want to provide a very simple mechanism to decompose development, benchmarking, optimization and deployment of complex applications
into our intelligent CM components that wrap existing DevOps and MLOps tools while making
them more interoperable, deterministic and portable.

Our idea is to let any IC automatically run additional ICs to prepare required environment variables,
"state" and files for a given platform and user requirements required for other IC in a pipeline.

We describe a pipeline of IC dependencies that must be executed before running a given IC using *deps* list in the *_cm.json* of this IC:

```json

{
  "deps": [
    {                           
      "tags":  # a string of tags separated by comma to find and execute the 1st intelligent component
    },
    {                           
      "tags":  # 2nd IC
    },
    ...
  ]
}

```

For example, our "Hello world" IC example has just one dependency described with tags "win,echo-off".

We can find this component as follows:

```bash
$ cm find ic --tags=win,echo-off
```

This is a [very simple IC](https://github.com/octoml/cm-mlops/tree/main/ic/prototype-echo-off-win)
that doesn't have dependencies on other IC and does not even have native OS scripts.

However, it has a *customize.py* file with the *preprocess* function that is executed
when we run this IC. 

Note that this function is used to update environment variables and the "state" dictionary
before running the native script or to influence the next ICs. For example, it can set up an 
environment variable that will be used in some other ICs in the dependency chain to skip their execution
as shown in [this example](https://github.com/octoml/cm-mlops/blob/main/ic/prototype-echo-off-win/customize.py#L21).

This component detects that the host platform is Windows and adds "@echo off" to all further IC executions
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
$ cm run ic --tags=win,echo-off --out=json
```

The [IC automation](https://github.com/mlcommons/ck/blob/master/cm-devops/automation/ic/module.py#L90) 
monitors the "state" and alters the execution of the next ICs  
based on specialized keys in the "state" dictionary (such as "script_prefix").

This approach allows the community to gradually extend this automation and ICs without breaking 
backwards compatibility!


## Customizing IC execution

We use *customize.py* to preprocess the execution of a native script (if exists),
i.e. prepare environment, the state dictionary and files needed to run this script.

You can find the automation code that prepares the input for the preprocess function 
[here]( https://github.com/mlcommons/ck/blob/master/cm-devops/automation/ic/module.py#L370 ).

We can also use this function to skip the execution of this IC based on environment, state and files
if it returns *{"skip":True}*.


After executing the preprocess function, the IC automation will record the global state dictionary
into *tmp-state.json* and the local state dictionary from this IC into *tmp-state-new.json*.

The IC automation will then run a native script with the global environment updated by 
and will call a native script (run.sh on Linux/MacOS or run.bat on Windows).

The native script will call some MLOps or DevOps tools based on environment variables
and files prepared by previous ICs or already preset in the native environment or container.

The native script can also create 2 files that will be automatically picked up and processed by the IC automation:
* *tmp-run-env.out* - list of environment variables to update the "new_env" of a given IC
* *tmp-run-state.json* - the state dictionary to update the "new_state" of a given IC

If the *customize.py* script exists with a *postprocess* function, the IC will call it
to finalize the postprocessing of files, environment variables and the state dictionary.

You can find the automation code that prepares the input for the postprocess function 
[here]( https://github.com/mlcommons/ck/blob/master/cm-devops/automation/ic/module.py#L482 ).


## Unifying host OS and CPU detection

In order to make MLOps and DevOps tools more portable and interoperable, we need to unify
the information about host OS and CPU. We are developing the following 2 IC:

* *detect-os* - See [CM artifact](https://github.com/octoml/cm-mlops/tree/main/ic/prototype-detect-os)
* *get-cpu-info* - See [CM artifact](https://github.com/octoml/cm-mlops/tree/main/ic/prototype-get-cpu-info)

These 2 IC have *customize.py* with preprocess and postprocess functions
and a native run script to detect OS info and update environment variables
and the state dictionary needed by dependent ICs. 

You can run them on your platform as follows:

```bash
$ cm run ic --tags=detect-os --out=json

...

$ cm run ic --tags=get,cpu-info --out=json
```

## Detecting, installing and caching system dependencies

We can now use ICs to detect or install system dependencies based on the OS and CPU info.
We have implemented such a prototype of the IC [*prototype-get-sys-utils-cm*](https://github.com/octoml/cm-mlops/tree/main/ic/prototype-get-sys-utils-cm)
that either downloads and caches various basic tools (wget, tar, gzip) on Windows
or installs system dependencies via *apt-get* on Linux with *sudo*.

You can test it as follows:
```bash
$ cm run ic --tags=get,sys-utils-cm
```

## Detecting, installing and caching tools

One of our goals is to automatically detect all existing dependencies required to run a given tool or application
before installing the fixed ones to be able to automatically adapt tools and applications to a user platform and environment.

We are developing IC *get-{tool}* to detect existing tools, install and even build them if a required version doesn't exist
and cache them in the *local* CM repository using the "installed" automation.

Let's check the IC *get-python* (See [CM artifact at GitHub](https://github.com/octoml/cm-mlops/tree/main/ic/prototype-get-python)).
It has *customize.py* with *preprocess* function that implements the search for python3 on Linux
or python.exe on Windows, 2 native scripts *run.sh* and *run.bat* to get the version of the detected python installation,
and *postprocess* function to prepare environment variables *CM_PYTHON_BIN* and *CM_PYTHON_BIN_WITH_PATH*
that can be used by other ICs.

Let's run it:
```bash
$ cm run ic --tags=get-python --out=json
```

If you run it for the first time and IC detects multiple versions of python, it will ask you to select one.
IC will then cache the output in the *installed* entry of the CM database. You can see all *installed* CM entries
for other tools and artifacts as follows:
```bash
$ cm list installed
```
or
``bash
$ cm list installed --tags=get-python
```

You can see the cached files as follows:
```bash
$ ls `cm find installed --tags=get-python`
```

If you (or other IC) run this IC to get the python tool for the second time, IC will use the cached data:
```bash
$ cm run ic --tags=get,python --out=json
```

Such approach allows us to "probe" the user environment and detect different tools that can be unified
and used by other ICs or external workflows.


## Detecting, installing and caching artifacts

One of the differences of MLOps from DevOps is that MLOps must be able to deal with diverse ML models, data sets 
and continuous experiments to iteratively improve accuracy, performance, energy usage, model/memory size and other
important parameters of the ML and AI-based applications.

That is why our IC concept is applied not only to scripts and tools but also to any user artifact required
to develop, optimize, deploy and use a complex application

For example, we have developed 2 ICs to demonstrate how to install "ResNet-50" model and reduced "ImageNet" dataset with 500 images:
* [*prototype-get-ml-model-resnet50-onnx*](https://github.com/octoml/cm-mlops/tree/main/ic/prototype-get-ml-model-resnet50-onnx)
* [*prototype-get-imagenet-val*](https://github.com/octoml/cm-mlops/tree/main/ic/prototype-get-imagenet-val)

You can run them as follows:
```bash
$ cm run ic --tags=get,ml-model,resnet50-onnx
$ cm run ic --tags=get,dataset,imagenet
```

or

```bash
$ cm run ic --tags=get,ml-model,image-classification
$ cm run ic --tags=get,dataset,image-classification
```

When executed for the first time, these IC will download ML artifacts and cache them using CM "installed" automation.

Note that you can find these "installed" CM entries using CM database API and use them in your own projects
without the need for further CM automation. Such approach allows gradual decomposition of complex
applications into intelligent components and gradual (evolutionary) adoption of the CM technology.

### Using variations

It is possible to download a specific version of an artifact using so-called "variations".
For example, the IC *prototype-get-ml-model-resnet50-onnx* has 2 variations for ONNX Opset 8 and 11
as described in [_cm.json](https://github.com/octoml/cm-mlops/blob/main/ic/prototype-get-ml-model-resnet50-onnx/_cm.json#L19).

It is possible to specify a required variation when running a given IC using tags with "_" prefix.
For example, you can install ResNet-50 model with "1.5-opset-11" variation as follows:
```bash
$ cm run ic --tags=get,ml-model,resnet50-onnx,_1.5-opset-11
```

You can also install another variation "1.5-opset-8" of this IC at the same time:
```bash
$ cm run ic --tags=get,ml-model,resnet50-onnx,_1.5-opset-8
```

## Assembling image classification pipeline

We can now use existing ICs as basic "LEGO" blocks to quickly assemble more complex automation pipelines and workflows
as new ICs with the same API/CLI.


We demonstrate this approach by implementing simple image classification as an IC 
[*prototype-image-classification-onnx-py*](https://github.com/octoml/cm-mlops/tree/main/ic/prototype-image-classification-onnx-py).

It has a dependency on the above ICs including OS unification, python detection, ResNet-50 model and the ImageNet dataset 
as described in its [*_cm.json*](prototype-image-classification-onnx-py):

```json
"deps": [
    {
      "tags": "detect,os"
    },
    {
      "tags": "get,sys-utils-cm"
    },
    {
      "tags": "echo-off"
    },
    {
      "tags": "get,python"
    },
    {
      "tags": "get,dataset,image-classification,original"
    },
    {
      "tags": "get,dataset-aux,image-classification"
    },
    {
      "tags": "get,ml-model,image-classification,onnx"
    }
  ]
```

It also has *run.sh* and *run.bat* to install Python requirements and run a Python script 
that will output classification results. You can run it as follows:

```bash
$ cm run ic --tags=image-classification,onnx,python --out=json
```

If you run this IC for the first time, it will run and cache all dependencies.

You can run it with your own image as follows:
```bash
$ cm run ic --tags=image-classification,onnx,python --env.CM_IMAGE={full path to my JPEG image}
```

## Running IC inside containers

The CM framework with intelligent components can be used both in the native environment and containers.
In fact, ICs can be used to automatically connect the same complex automation pipelines and workflows 
with external data and tools via environment variables and files. 

We are developing the concept of modular containers assembled from intelligent "CM" components
and will update this section soon!


## Adding new IC

One of the main goals of CM (aka CK2) is to make it way easier to onboard new users and add new components
in comparison with the 1st version (CK2).

You can add your own working component with some tags and run it as a dummy filter as follows:

```bash
$ cm add ic my-cool-component --tags=my,cool-component,prototype
$ cm run ic my-cool-component
$ cm run ic --tags=my,cool-component
```

You can then find this component and just add there your own script with the name *run.sh* 
on Linux/MacOS or *run.bat* on Windows:
```bash
$ cd `cm find ic my-cool-component`

$ cat > run.sh
echo "My cool component"

$ cm run ic my-cool-component

...
My cool component
```

You can then extend *_cm.json* and add more tags or dependencies to reuse environment variables and files
in your script prepared by other ICs from public or private projects.

Finally, you can add the *customize.py* script with *preprocess* and *postprocess* functions to implement more
complex logic to customize the execution of a given IC based on previous dependencies, flags, platform and CPU info, etc.


## Extending ICs as a collaborative playground

We have developed CM as a collaborative playground to work with the community and gradually unify diverse DevOps and MLOps scripts and tools
and decompose development, optimization, deployment and usage of complex applications into intelligent "CM" components.

Our next steps:
* agreeing on and unifying tags that describe different ICs in a unique way
* agreeing on and unifying scripts, env variables and state of different ICs
* adding support for different IC versions and ranges similar to Pypi
* adding support to run IC scripts for a specific host OS version and CPU
* implementing MLPerf benchmark as a pipeline of ICs

Please get in touch if you want to join this collaborative effort to unify DevOps and MLOps 
and make them more portable, interoperable and deterministic.
