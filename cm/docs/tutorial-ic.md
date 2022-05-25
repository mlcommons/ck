# Tutorial: understanding intelligent CM components

*Note that IC automation is under development and can still evolve!*

We want to demonstrate that it is possible to organize ad-hoc DevOps, MLOps and other scripts
and artifacts into a database of portable and reusable components.
It is then possible to implement complex automation pipelines with a minimal effort
in a native environment and without the need for specialized workflow 
frameworks and containers.
Our evolutionary approach can be a simple and practical intermediate step 
to automate and simplify the existing ad-hoc development, optimization and deployment flows 
of complex applications before investing into specialized workflow frameworks, platforms and containers.

## Motivation

CM is motivated by our tedious experience trying to
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
Such actions usually update the global OS environment and produce new files while taking
host and target platform parameters into account.

### Intelligent CM component (IC)

That is why we are developing the CM automation 
called [ic ("intelligent component")](https://github.com/mlcommons/ck/tree/master/cm-devops/automation/ic)
to organize and wrap existing ad-hoc DevOps and MLOps scripts and artifacts
with a unified CLI and Python API.

We are also developing intelligent components as CM artifacts with an extensible JSON/YAML meta description
to make benchmarking, optimization and deployment of ML Systems more deterministic, 
portable and reproducible: https://github.com/octoml/cm-mlops/tree/main/ic .

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

You can run an intelligent CM component that prints "hello world" using its explicit name:

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

Let's find the CM database entry for the IC component as follows:
```bash
$ cm find ic prototype-print-hello-world
```
or

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

  "tags": [          # Tags to find this IC and differentiate from others!
    "prototype",
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

  "deps": [                     # Pipeline of dependencies on other IC
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

r=cm.access({'action':'run',
             'automation':'ic',
             'tags':'print,hello-world,script',
             'env':{
               'CM_ENV_TEST1':'ABC1',
               'CM_ENV_TEST2':'ABC2'
             }
            })

print (r)

```

```
...

CM_ENV_TEST1 = ABC1
CM_ENV_TEST2 = ABC2

HELLO WORLD!

{'return': 0, 'new_state': {'script_prefix': ['@echo off']}, 'new_env': {'CM_ENV_TEST2': 'TEST2'}}

```



Deps

detect-os

 customize.py
 pre/post-processing

files
 env
 state

post-processing
why state

get-python
installed
cached

image classification
 ml model
 dataset

Modularize containers

Further work:
 run for OS flavor, etc
