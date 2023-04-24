# Trying CK

## How CK enables portable and customizable workflows

We originally developed CK to help our [partners and collaborators](https://cKnowledge.org/partners.html)
implement modular, portable, customizable, and reusable workflows.
We needed such workflows to enable collaborative and reproducible ML&systems R&D 
while focusing on [deep learning benchmarking and ML/SW/HW co-design](https://cKnowledge.org/request).
We also wanted to automate and reuse tedious tasks that are repeated across nearly all ML&systems projects
as described in our [FOSDEM presentation](https://zenodo.org/record/2556147#.XMViWKRS9PY).

In this section, we demonstrate how to use CK with portable and non-virtualized program workflows
that can automatically adapt to any platform and user environment, i.e. automatically detect 
target platform properties and software dependencies and then compile and run a given program 
with any compatible dataset and model in a unified way. 

Note that such approach also supports our [reproducibility initiatives at ML&systems conferences](https://cTuning.org/ae)
to share portable workflows along with [published papers](https://cknow.io/reproduced-papers).
Our goal is to make it easier for the community to reproduce research techniques, compare them, 
build upon them, and adopt them in production.

## CK installation

Follow this [guide](installation.md) to install CK on Linux, MacOS, or Windows. 
Don't hesitate to [contact us](https://cKnowledge.org/contacts.html) 
if you encounter any problem or have questions.


## Pull CK repositories with the universal program workflow


Now you can pull CK repo with automation recipes for collaborative, reproducible and cross-platform benchmarking

```bash
ck pull repo:mlcommons@ck-mlops
ck pull repo:ctuning-datasets-min
```

CK will automatically pull all required CK repositories with different automation actions, benchmarks, and datasets in the CK format.
You can see them as follows:

```bash
ck ls repo
```

By default, CK stores all CK repositories in the user space in *$HOME/CK-REPOS*. However, you can change it using the environment variable *CK_REPOS*.

## Manage CK entries


You can now see all shared program workflows in the CK format:

```bash
ck ls program
```

You can find and investigate the CK format for a given program (such as *image-corner-detection*) as follows:

```bash
ck search program --tags=demo,image,corner-detection
```

You can see the CK meta description of this program from the command line as follows:
```bash
ck load program:image-corner-detection
ck load program:image-corner-detection --min
```

It may be more convenient to check the structure of this entry at [GitHub](https://github.com/mlcommons/ck-mlops/tree/master/program/image-corner-detection) with all the sources and meta-descriptions.

You can also see the CK JSON meta description for this CK program entry [here](https://github.com/mlcommons/ck-mlops/blob/master/program/image-corner-detection/.cm/meta.json).
When you invoke automation actions in the CK module *program*, the automation code will read this meta description and perform actions for different programs accordingly.

## Invoke CK automation actions

You can now try to compile this program on your platform:

```bash
ck compile program:image-corner-detection --speed
```

CK will invoke the function "compile" in the module "program" (you can see it at [GitHub](https://github.com/mlcommons/ck/blob/master/ck/repo/module/program/module.py#L3594)
or you can find the source code of this CK module locally using "ck find module:program"),
read the JSON meta of *image-corner-detection*, and perform a given action.

Note, that you can obtain all flags for a given action as follows:
```bash
ck compile program --help
```

You can update any above key from the command line by adding "--" to it. If you omit the value, CK will use "yes" by default.

When compiling program, CK will first attempt to automatically detect the properties of the platform
and all required software dependencies such as compilers and libraries that are already installed on this platform. 
CK uses [multiple plugins](https://cknow.io/soft) describing how to detect different software, models, and datasets.

Users can add their own plugins either in their own CK repositories or in already existing ones.

You can also perform software detection manually from the command line. For example you can detect all installed GCC or LLVM versions:
```bash
ck detect soft:compiler.gcc
ck detect soft:compiler.llvm
```

Detected software is registered in the local CK repository together 
with the automatically generated environment script (*env.sh* or *env.bat*) 
specifying different environment variables for this software
(paths, versions, etc).

You can list registered software as follows:

```bash
ck show env
ck show env --tags=compiler
```

You can use CK as a virtual environment similar to venv and Conda:
```bash
ck virtual env --tags=compiler,gcc
```

Such approach allows us to separate CK workflows from hardwired dependencies and automatically plug in the requied ones.

You can now run this program as follows:
```bash
ck run program:image-corner-detection
```

While running the program, CK will collect and unify various characteristics (execution time, code size, etc).
This enables unified benchmarking reused across different programs, datasets, models, and platform.
Furthermore, we can continue improving this universal program workflow to monitor CPU/GPU frequencies, 
performing statistical analysis of collected characteristics, validating outputs, etc:

```bash
ck benchmark program:image-corner-detection --repetitions=4 --record --record_uoa=ck_entry_to_record_my_experiment
ck replay experiment:ck_entry_to_record_my_experiment
```

Note that CK programs can automatically plug different datasets from CK entries 
that can be shared by different users in different repos (for example, when publishing a new paper):

```bash
ck search dataset
ck search dataset --tags=jpeg
```

Our goal is to help researchers reuse this universal CK program workflow
instead of rewriting complex infrastructure from scratch in each research project.

## Install missing packages

Note, that if a given software dependency is not resolved, 
CK will attempt to automatically install it using CK meta packages
(see the list of shared CK packages at [cKnowledge.io](https://cknow.io/packages)).
Such meta packages contain JSON meta information and scripts
to install and potentially rebuild a given package 
for a given target platform while reusing existing
build tools and native package managers if possible 
(make, cmake, [scons](https://scons.org), 
[spack](https://spack.io), 
[python-poetry](https://python-poetry.org), etc).
Furthermore, CK package manager can also install 
non-software packages including ML models and datasets
while ensuring compatibility between all components
for portable workflows!

You can list CK packages available on your system (CK will search for them in all CK repositories installed on your system):
```bash
ck search package --all
```

You can then try to install a given LLVM on your system as follows:
```bash
ck install package --tags=llvm,v10.0.0
```

If this package is successfully installed, CK will also create an associated CK environment:
```bash
ck show env --tags=llvm,v10.0.0

```

By default, all packages are installed in the user space (*$HOME/CK-TOOLS*).
You can change this path using the CK environment variable *CK_TOOLS*.
You can also ask CK to install packages inside CK virtual environment entries directly as follows:
```bash
ck set kernel var.install_to_env=yes
```

Note that you can now detect or install multiple versions of the same tool on your system
that can be picked up and used by portable CK workflows!

You can run a CK virtual environment to use a given version as follows:

```bash
ck virtual env --tags=llvm,v10.0.0

```

You can also run multiple virtual environments at once to combine different versions of different tools together:
```bash
ck show env
ck virtual env {UID1 from above list} {UID2 from above list} ...
```

Another important goal of CK is invoke all automation actions and portable workflows
across all operating systems and environments
including Linnux, Windows, MacOS, Android (you can retarget your workflow for Andoird by adding *--target_os=android23-arm64* flag
to all above commands when installing packages or compiling and running your programs).
The idea is to have a unified interface for all research techniques and artifacts
shared along with research papers to make the onboarding easier for the community!


## Participate in crowd-tuning

You can even participate in [crowd-tuning](https://cKnowledge.org/rpi-crowd-tuning) 
of multiple programs and data sets across diverse platforms:.

```
ck crowdtune program:image-corner-detection
ck crowdtune program
```

You can see the live scoreboard with optimizations [here](https://cKnowledge.org/repo-beta).

## Use CK python API

You can also run CK automation actions directly from any Python (2.7+ or 3.3+) using one *ck.access* function:


```python
import ck.kernel as ck

# Equivalent of "ck compile program:image-corner-detection --speed"
r=ck.access({'action':'compile', 'module_uoa':'program', 'data_uoa':'image-corner-detection', 
             'speed':'yes'})
if r['return']>0: return r # unified error handling 

print (r)

# Equivalent of "ck run program:image-corner-detection --env.OMP_NUM_THREADS=4
r=ck.access({'action':'run', 'module_uoa':'program', 'data_uoa':'image-corner-detection', 
             'env':{'OMP_NUM_THREADS':4}})
if r['return']>0: return r # unified error handling 

print (r)

```


## Try the CK MLPerf&trade; workflow

Feel free to try more complex CK MLPerf workflows to benchmark ML Systems 
across different models, data sets, frameworks and hardware
as described [here](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/README.md).


## Further information

As you may notice, CK helps to convert ad-hoc research projects into a unified database
of reusable components with common automation actions and unified meta descriptions.
The goal is to promote artifact sharing and reuse while gradually substituting and unifying 
all tedious and repetitive research tasks!


Please check this [guide](how-to-contribute.md) to learn how to add your own repositories, workflows, and components!


## Contact the CK community

If you encounter problems or have suggestions, do not hesitate to [contact us](https://cKnowledge.org/contacts.html)!
