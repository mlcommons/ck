# CM "script" automation

<details>
<summary>Click here to see the table of contents.</summary>

  * [Motivation](#motivation)
  * [Obtaining shared CM scripts](#obtaining-shared-cm-scripts)
  * [Running CM scripts](#running-cm-scripts)
    * [Wrapping native scripts](#wrapping-native-scripts)
    * [Modifying environment variables](#modifying-environment-variables)
    * [Understanding unified output dictionary](#understanding-unified-output-dictionary)
    * [Modifying state dictionary](#modifying-state-dictionary)
    * [Running CM scripts via CM Python API](#running-cm-scripts-via-cm-python-api)
  * [Understanding CM script dependencies](#understanding-cm-script-dependencies)
  * [Customizing CM script execution](#customizing-cm-script-execution)
  * [Unifying host OS and CPU detection](#unifying-host-os-and-cpu-detection)
  * [Detecting, installing and caching system dependencies](#detecting-installing-and-caching-system-dependencies)
  * [Detecting, installing and caching tools](#detecting-installing-and-caching-tools)
  * [Detecting, installing and caching artifacts](#detecting-installing-and-caching-artifacts)
    * [Using variations](#using-variations)
  * [Assembling image classification pipeline](#assembling-image-classification-pipeline)
  * [Compiling and running image corner detection](#compiling-and-running-image-corner-detection)
  * [Running CM scripts inside containers](#running-cm-scripts-inside-containers)
  * [Related](#related)

</details>


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





## Obtaining shared CM scripts

In order to reuse some CM scripts embedded into shared projects, 
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

You can now see all available CM scripts in your system as follows:

```bash
cm find script
cm find script install* | sort

```




## Running CM scripts

CM scripts are treated as standard CM artifacts with the associated CM automation ["script"](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script),
CM action ["run"](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/script/module.py#L73),
and JSON &| YAML meta descriptions. 

CM scripts can be invoked by using their alias, unique ID and human-readable tags (preferred method).

For example, the [CM "Print Hello World" script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world) 
simply wraps 2 native `run.sh` and `run.bat` scripts to print "Hello World" on Linux, MacOs or Windows 
together with a few environment variables:

```bash
ls `cm find script print-hello-world`

README.md  _cm.json  run.bat  run.sh
```

It is described by this [_cm.json meta description file](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/print-hello-world/_cm.json) 
with the following alias, UID and tags:

```json
{
  "automation_alias": "script",
  "automation_uid": "5b4e0237da074764",

  "alias": "print-hello-world",
  "uid": "b9f0acba4aca4baa",

  "default_env": {
    "CM_ENV_TEST1": "TEST1"
  },

  "env": {
    "CM_ENV_TEST2": "TEST2"
  },

  "input_mapping": {
    "test1": "CM_ENV_TEST1"
  },

  "new_env_keys": [
    "CM_ENV_TEST*"
  ],

  "new_state_keys": [
    "hello_test*"
  ],

  "tags": [
    "print",
    "hello-world",
    "hello world",
    "hello",
    "world",
    "native-script",
    "native",
    "script"
  ]
}
```

The `automation_alias` and `automation_uid` tells CM that this artifact can be used with the CM "script" automation.

Therefore, this script can be executed from the command line in any of the following ways:

```bash
cm run script print-hello-world
cm run script b9f0acba4aca4baa
cm run script --tags=print,native-script,hello-world
cm run script "print native-script hello-world"
```

The same script can be also executed using CM Python API as follows:
```python
import cmind

output = cmind.access({'action':'run', 'automation':'script', 'tags':'print,native-script,hello-world'})
if output['return']>0:
    cmind.error(output)

import json
print (json.dumps(output, indent=2))
```

Normally you should see the following output along with some debug information (that will be removed soon):

```bash

...

CM_ENV_TEST1 = TEST1
CM_ENV_TEST2 = TEST2

HELLO WORLD!
...
```

### Wrapping native scripts

*run.bat* and *run.sh* are native scripts that will be executed by this CM script in a unified way on Linux, MacOS and Windows:

```bash
echo ""
echo "CM_ENV_TEST1 = ${CM_ENV_TEST1}"
echo "CM_ENV_TEST2 = ${CM_ENV_TEST2}"

echo ""
echo "HELLO WORLD!"
```

The idea to use native scripts is to make it easier for researchers and engineers to reuse their existing automation scripts
while providing a common CM wrapper with a unified CLI, Python API and extensible meta descriptions.




### Modifying environment variables

CM script automation CLI uses a flag `--env.VAR=VALUE` to set some environment variable and pass it to a native script
as shown in this example:

```bash
cm run script "print native-script hello-world" --env.CM_ENV_TEST1=ABC1 --env.CM_ENV_TEST2=ABC2

...

CM_ENV_TEST1 = ABC1
CM_ENV_TEST2 = TEST2

HELLO WORLD!
```

Note, that *CM_ENV_TEST2* did not change. This happened because dictionary `env` in the *_cm.json* forces *CM_ENV_TEST2* to *TEST2*,
while `default_env` dictionary allows environment variables to be updated externally.

You can still force an environment variable to a given value externally using a `--const` flag as follows:

```bash
cm run script "print native-script hello-world" --env.CM_ENV_TEST1=ABC1 --const.CM_ENV_TEST2=ABC2 

...

CM_ENV_TEST1 = ABC1
CM_ENV_TEST2 = ABC2

HELLO WORLD!

```

You can also use a JSON file instead of flags. Create *input.json* (or any other filename):
```json
{
  "tags":"print,native-script,hello-world",
  "env":{
    "CM_ENV_TEST1":"ABC1"
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
env:
  CM_ENV_TEST1: "ABC1"
```

and run the CM script with this input file as follows:
```
cm run script @input.yaml
```

Finally, you can map any other flag from the script CLI to an environment variable 
using the key `input_mapping` in the `_cm.json` meta description of this script:

```bash
cm run script "print native-script hello-world" --test1=ABC1

...

CM_ENV_TEST1 = ABC1
CM_ENV_TEST2 = TEST2

HELLO WORLD!

```


### Understanding unified output dictionary

You can see the output of a given CM script in the JSON format by adding `--out=json` flag as follows:

```bash
cm run script --tags=print,hello-world,script --env.CM_ENV_TEST1=ABC1 --out=json

...

CM_ENV_TEST1 = ABC1
CM_ENV_TEST2 = ABC2

HELLO WORLD!

{
  "deps": [],
  "env": {
    "CM_ENV_TEST1": "ABC1",
    "CM_ENV_TEST2": "TEST2"
  },
  "new_env": {
    "CM_ENV_TEST1": "ABC1",
    "CM_ENV_TEST2": "TEST2"
  },
  "new_state": {},
  "return": 0,
  "state": {}
}
```

Note that `new_env`shows new environment variables produced and explicitly exposed by this script 
via a `new_env_keys` key in the `_cm.json` meta description of this script.

This is needed to assemble automation pipelines and workflows while avoiding their contamination
with temporal environments. CM script must explicitly expose environment variables that will 
go to the next stage of a pipeline.

In the following example, `CM_ENV_TEST3` will be added to the `new_env` while `CM_XYZ` will not
since it is not included in `"new_env_keys":["CM_ENV_TEST*"]`:

```bash
cm run script --tags=print,hello-world,script --env.CM_ENV_TEST1=ABC1 --out=json --env.CM_ENV_TEST3=ABC3 --env.CM_XYZ=XYZ
```

### Modifying state dictionary

Sometimes, it is needed to use more complex structures than environment variables in scripts and workflows.
We use a dictionary `state` that can be updated and exposed by a given script via `new_state_keys` key
in the `_cm.json` meta description of this script.

In the following example, `hello_world` key will be updated in the `new_state` dictionary,
while `hello` key will not be updated because it is not included in the wildcard `"new_state_key":["hello_world*"]`:

```bash
cm run script --tags=print,hello-world,script --out=json --state.hello=xyz1 --state.hello_world=xyz2

...

{
  "deps": [],
  "env": {
    "CM_ENV_TEST1": "TEST1",
    "CM_ENV_TEST2": "TEST2"
  },
  "new_env": {
    "CM_ENV_TEST1": "TEST1",
    "CM_ENV_TEST2": "TEST2"
  },
  "new_state": {
    "hello_world": "xyz2"
  },
  "return": 0,
  "state": {
    "hello": "xyz1",
    "hello_world": "xyz2"
  }
}
```

### Running CM scripts via CM Python API

You can run a given CM script from python or Jupyter notebooks as follows:

```python

import cmind

r = cmind.access({'action':'run',
                  'automation':'script',
                  'tags':'print,hello-world,script',
                  'const':{
                    'CM_ENV_TEST1':'ABC1',
                  },
                  'env':{
                    'CM_ENV_TEST2':'ABC2'
                  },
                  'state': {
                    'hello':'xyz1',
                    'hello_world':'xyz2'
                  }
                 })

print (r)

```

```bash
...

CM_ENV_TEST1 = ABC1
CM_ENV_TEST2 = ABC2

HELLO WORLD!

{'return': 0, 
 'env': {'CM_ENV_TEST2': 'TEST2', 'CM_ENV_TEST1': 'ABC1'}, 
 'new_env': {'CM_ENV_TEST2': 'TEST2', 'CM_ENV_TEST1': 'ABC1'}, 
 'state': {'hello': 'xyz1', 'hello_world': 'xyz2'}, 
 'new_state': {'hello_world': 'xyz2'}, 
 'deps': []}

```



### Assembling pipelines (workflows) of CM scripts

We've added a simple mechanism to chain reusable CM scripts into complex pipelines
without the need for specialized workflow frameworks.

Simply add the following dictionary "deps" to the `_cm.json` or `_cm.yaml` of your script as follows:

```json

{
  "deps": [
    {                           
      "tags": "a string of tags separated by comma to find and execute the 1st CM script"
    },
    {                           
      "tags": "a string of tags separated by comma to find and execute the 1st CM script" 
    },
    ...
  ]
}

```

This CM script will run all dependendent scripts in above sequence, aggregate environment variable and `state` dictionary,
and will then run native scripts.

You can also turn on specific dependencies based on some values oin specific environment variables in the pipeline as follows:

```json

{
  "deps": [
    {                           
      "tags": "a string of tags separated by comma to find and execute the 1st CM script",
      "enable_if_env": { "USE_CUDA" : ["yes", "YES", "true"] }
    },
    {                           
      "tags": "a string of tags separated by comma to find and execute the 1st CM script" 
      "enable_if_env": { "USE_CPU" : ["yes", "YES", "true"] }
    },
    ...
  ]
}

```

You can also specify dependencies to be invoked after executing native scripts
using a dictionary `"post_deps"` with the same format `"deps"`.









### Customizing CM script execution flow

If a developer adds `customize.py` file inside a given CM script,
it can be used to programmatically update environment variables, prepare input scripts
and even invoke other scripts programmatically using Python.

If a function `preprocess` exists in this file, CM script will call it before
invoking a native script. 

If this function returns `{"skip":True}` in the output,
further execution of this script will be skipped.

After executing the preprocess function, the CM script automation will record the global state dictionary
into *tmp-state.json* and the local state dictionary from this CM script into *tmp-state-new.json*.

The CM script automation will then run a native script (run.sh on Linux/MacOS or run.bat on Windows)
with all merged environment variables from previous scripts.

Note that native scripts can also create 2 files that will be automatically picked up and processed by the CM script automation:
* *tmp-run-env.out* - list of environment variables to update the "new_env" of a given CM script
* *tmp-run-state.json* - the state dictionary to update the "new_state" of a given CM script

If `postprocess` function exists in the *customize.py* file, the CM script will call it
to finalize the postprocessing of files, environment variables, and the state dictionary.







### Getting help about all script automation flags

You can get help about all flags used to customize execution 
of a given CM script from the command line as follows:

```bash
cm run script --help
```

Some flags are useful to make it easier to debug scripts and save output in files.

You can find more info about CM script execution flow in this [document](README-specs.md).








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
