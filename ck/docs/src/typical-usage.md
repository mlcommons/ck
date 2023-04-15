# The most common usage

Here we describe how to create and share new CK program workflows, software detection plugins, and packages
either using new (empty) CK repositories or the existing ones.
Portable CK program workflow is the most commonly used CK automation to compile, run, validate, and compare
different algorithms and benchmarks across different compilers, libraries, models, datasets, and platforms.

We strongly suggest you to check the [CK introduction](introduction.md) 
and [getting started guide](first-steps.md) first.

You can also check the following [real-world use cases](https://cKnowledge.org/partners.html) 
that are based on our portable and customizable CK workflow:
* [MLPerf&trade; benchmark automation](https://github.com/ctuning/ck-mlperf)
* [Reproducible ACM REQUEST tournaments](https://cKnowledge.org/request) to co-design Pareto-efficient AI/ML/SW/HW stacks
* [Reproducible quantum hackathons](https://cKnowledge.org/quantum)
* Student Cluster Competition automation at SuperComputing: [SCC18]( https://github.com/ctuning/ck-scc18 ), [general SCC]( https://github.com/ctuning/ck-scc )
* [reproducible and interactive paper for ML-based compilers]( https://cKnowledge.org/rpi-crowd-tuning )




## Initialize a new CK repository in the current directory (can be existing Git repo)

If you plan to contribute to already [existing CK repositories]( http://cknow.io/repos )
you can skip this subsection. Otherwise, you need to manually create a new CK repository.

You need to choose some user friendly name such as "my-new-repo" 
and initialize CK repository in your current directory
from the command line (Linux, Windows, and MacOS) as follows:

```bash
ck init repo:my-new-repo
```

If the current directory belongs to a Git repo, CK will automatically detect the URL.
Otherwise you need to specify it from CLI too:

```bash
ck init repo:my-new-repo --url={Git URL}
```

You can then find where CK created this dummy CK repository using the following command:

```bash
ck where repo:my-new-repo
```

Note that if you want to share your repository with the community or within workgroups to reuse automations and components,
you must create an empty repository at [GitHub](http://www.github.com), 
[GitLab](http://gitlab.com), [BitBucket](http://bitbucket.org) 
or any other Git-based service. Let's say that you have created *my-new-repo* at *https://github.com/my_name*. 

You can then pull this repository using CK as follows:

```bash
ck pull repo --url=https://github.com/my_name/my-new-repo
```

CK will then create my_name_repo repository locally, add default meta information, and will mark it as shared repository 
(to semi-automatically synchronize content with the associated Git repository):
```bash
ck where repo:my-new-repo
```

For example, you can later commit and push updates for this repository back to Git as follows:
```bash
ck push repo:my-new-repo
```

We then suggest you to make the first commit immediately after you pulled your
dummy repository from GitHub to push automatically *.ckr.json* file
with some internal meta information and Unique ID back to the GitHub.

Note that you can also commit and push all updates using Git commands 
directly from the CK repository directory! Do not forget to commit hidden
CK directories *.cm/**!

You are now ready to use the newly created repository as a database to add, share, and reuse
new components. You can also share this repository with your colleagues or the [Artifact Evaluation Committee](https://cTuning.org/ae)
to test your components and workflows in a unified way:

```bash
ck pull repo --url=https://github.com/my_name/my-new-repo
```




## Add dependency on other repositories to reuse automation actions and components

When you want to reuse existing CK automation actions and components from other
repositories, you need to add a dependency to all these repositories 
in the *.ckr.json* file in your root CK repository:


```json
  ...
  "dict": {
    ...
    "repo_deps": [
      {
        "repo_uoa": "ck-env"
      },
      {
        "repo_uoa": "ck-autotuning"
      },
      {
        "repo_uoa": "ck-mlperf",
        "repo_url": "https://github.com/ctuning/ck-mlperf"
      }
    ] 
  }
```

Whenever someones pull your repository, CK will automatically pull all other required CK repositories with automation actions!






## Add a new program workflow

You are now ready to add a new CK workflow to compile and run some algorithm or a benchmark in a unified way.

Since CK concept is about reusing and extending existing components with a common API similar to Wikipedia,
we suggest you to look at [this index]( https://cknow.io/programs ) of shared CK programs
in case someone have already shared a CK workflows for the same or similar program!

If you found a similar program, for example "image-corner-detection" 
you can create a working copy of this program in your new CK repository
for further editing as follows:

```bash
ck pull repo:ctuning-programs 
ck cp program:image-corner-detection my-new-repo:program:my-copy-of-image-corner-detection
```

You now have a working copy of the CK "image-corner-detection" program entry in your new repository 
that contains sources and the CK meta information about how to compile and run this program:

```bash
ck compile program:my-copy-of-image-corner-detection --speed
ck run program:my-copy-of-image-corner-detection
```

You can find and explore the new CK entry from command line as follows:
```bash
ck find program:my-copy-of-image-corner-detection
```

You will see the following files in this directory:

* *.cm/desc.json* - description of all I/O types in all automation actions (empty by default - we can skip it for now)
* *.cm/info.json* - the provenance for this entry (creation date, author, license, etc)
* *.cm/meta.json* - **main CK meta information about how to compile, run, and validate this program**
* *susan.c'' - source code of this program

Once again, do not forget to add .cm directories when committing to Git since *.cm* files are usually not visible from bash in Linux!

If you did not find a similar program, you can then create a new program using shared program templates as follows:

```bash
ck add my-new-repo:program:my-new-program
```

CK will then ask you to select the most close template:

```
0) C program "Hello world" (--template=template-hello-world-c)
1) C program "Hello world" with compile and run scripts (--template=template-hello-world-c-compile-run-via-scripts)
2) C program "Hello world" with jpeg dataset (--template=template-hello-world-c-jpeg-dataset)
3) C program "Hello world" with output validation (--template=template-hello-world-c-output-validation)
4) C program "Hello world" with xOpenME interface and pre/post processing (--template=template-hello-world-c-openme)
5) C++ TensorFlow classification example (--template=image-classification-tf-cpp)
6) C++ program "Hello world" (--template=template-hello-world-cxx)
7) Fortran program "Hello world" (--template=template-hello-world-fortran)
8) Java program "Hello world" (--template=template-hello-world-java)
9) Python MXNet image classification example (--template=mxnet)
10) Python TensorFlow classification example (--template=image-classification-tf-py)
11) Python program "Hello world" (--template=template-hello-world-python)
12) image-classification-tflite (--template=image-classification-tflite)
13) Empty entry
```

If you select "Python TensorFlow classification example", 
CK will create a working image classification program 
in your new repository with software dependencies 
on TensorFlow AI framework and compatible models.

Since it's a Python program, you do not need to compile it:

```bash
ck run program:my-new-program
```

Note that you can later make your own program a template by adding the following key to the *meta.json* file:
```json
  "template": "yes"
```



### Update program sources

If you found a similar program with all the necessary software dependencies, 
you can now update or change its sources for your own program.

In such case, you must update the following keys in the *meta.json* of this program entry:

* add your source files:
```json
  "source_files": [
    "susan.c"
  ], 
```

* specify a command line to run your program (see *run_cmd_main*):

```json
  "run_cmds": {
    "corners": {
      "dataset_tags": [
        "image", 
        "pgm", 
        "dataset"
      ], 
      "ignore_return_code": "no", 
      "run_time": {
        "run_cmd_main": "$#BIN_FILE#$ $#dataset_path#$$#dataset_filename#$ tmp-output.tmp -c" 
      }
    }, 
    "edges": {
      "dataset_tags": [
        "image", 
        "pgm", 
        "dataset"
      ], 
      "ignore_return_code": "no", 
      "run_time": {
        "run_cmd_main": "$#BIN_FILE#$ $#dataset_path#$$#dataset_filename#$ tmp-output.tmp -e" 
      }
    }, 

```

Note that you can have more than one possible command line to run this program. 
In such case, CK will ask you which one to use when you run this program.
For example, this can be useful to perform ML model training ("train"), validation ("test"),
and classification ("classify").

You can also update meta.json keys to customize program compilation and execution:
```bash
  "build_compiler_vars": {
    "XOPENME": ""
  }, 

  "compiler_env": "CK_CC", 

  "extra_ld_vars": "$<<CK_EXTRA_LIB_M>>$", 

  "run_vars": {
    "CT_REPEAT_MAIN": "1",
    "NEW_VAR":"123"
  }, 
```

Note that you can update environment variables when running a given program 
in a unified way from the command line as follows:
```bash
ck run program:my-new-program --env.OMP_NUM_THREADS=4 --env.ML_MODEL=mobilenet-v3
```

You can also expose different algorithm parameters and optimizations via environment 
to apply customizable CK autotuner as used in this 
[CK ReQuEST workflow](https://github.com/dividiti/ck-request-asplos18-mobilenets-armcl-opencl/blob/master/script/mobilenets-armcl-opencl/benchmark.py#L304)
to automatically explore (co-design) different MobileNets configurations in terms of speed, accuracy, and costs.

Here is the brief description of other important keys in CK program *meta.json*:

```json
  "run_cmds": {                

    "corners": {               # User key describing a given execution command line

      "dataset_tags": [        # dataset tags - will be used to query CK
        "image",               # and automatically find related entries such as images
        "pgm", 
        "dataset"
      ], 

      "run_time": {            # Next is the execution command line format
                               # $#BIN_FILE#$ will be automatically substituted with the compiled binary
                               # $#dataset_path#$$#dataset_filename#$ will be substituted with
                               # the first file from the CK dataset entry (see above example
                               # of adding new datasets to CK).
                               # tmp-output.tmp is and output file of a processed image.
                               # Basically, you can shuffle below words to set your own CMD

        "run_cmd_main": "$#BIN_FILE#$ $#dataset_path#$$#dataset_filename#$ tmp-output.tmp -c", 

        "run_cmd_out1": "tmp-output1.tmp",  # If !='', add redirection of the stdout to this file
        "run_cmd_out2": "tmp-output2.tmp",  # If !='', add redirection of the stderr to this file

        "run_output_files": [               # Lists files that are produced during
                                            # benchmark execution. Useful when program
                                            # is executed on remote device (such as
                                            # Android mobile) to pull necessary
                                            # files to host after execution
          "tmp-output.tmp", 
          "tmp-ck-timer.json"
        ],


        "run_correctness_output_files": [   # List files that should be used to check
                                            # that program executed correctly.
                                            # For example, useful to check benchmark correctness
                                            # during automatic compiler/hardware bug detection
          "tmp-output.tmp", 
          "tmp-output2.tmp"
        ], 

        "fine_grain_timer_file": "tmp-ck-timer.json"  # If XOpenME library is used, it dumps run-time state
                                                      # and various run-time parameters (features) to tmp-ck-timer.json.
                                                      # This key lists JSON files to be added to unified 
                                                      # JSON program workflow output
      },

      "hot_functions": [                 # Specify hot functions of this program
        {                                # to analyze only these functions during profiling
          "name": "susan_corners",       # or during standalone kernel extraction
          "percent": "95"                # with run-time memory state (see "codelets"
                                         #  shared in CK repository from the MILEPOST project
                                         #  and our recent papers for more info)
        }
      ] 

      "ignore_return_code": "no"         # Some programs have return code >0 even during
                                         # successful program execution. We use this return code
                                         # to check if benchmark failed particularly during
                                         # auto-tuning or compiler/hardware bug detection
                                         #  (when randomly or semi-randomly altering code,
                                         #   for example, see Grigori Fursin's PhD thesis with a technique
                                         #   to break assembler instructions to detect 
                                         #   memory performance bugs) 
    }, 
    ...
  }, 
```

You can also check how to use pre and post-processing scripts before and after running your program
in [this example](https://github.com/ctuning/ck-scc18/blob/master/program/seissol-netcdf/.cm/meta.json)
from the Student Cluster Competition'18.





## Update software dependencies

If you new program rely on extra software dependencies (compilers, libraries, models, datasets)
you must first find the ones you need in this [online index](https://cknow.io/soft)
of software detection plugins. You can then specify the tags and versions either using 
*compile_deps* or *run_deps* keys in the *meta.json* of your new program as follows:

```json
  "compile_deps": {
    "compiler": {
      "local": "yes", 
      "name": "C compiler", 
      "sort": 10, 
      "tags": "compiler,lang-c"
    }, 
    "xopenme": {
      "local": "yes", 
      "name": "xOpenME library", 
      "sort": 20, 
      "tags": "lib,xopenme"
    }
  }, 
```

```json
  "run_deps": {
    "lib-tensorflow": {
      "local": "yes",
      "name": "TensorFlow library",
      "sort": 10,
      "tags": "lib,tensorflow",
      "no_tags":"vsrc"
    },
    "tensorflow-model": {
      "local": "yes",
      "name": "TensorFlow model (net and weights)",
      "sort": 20,
      "tags": "tensorflowmodel,native"
    }
  },
```

As a minimum, you just need to add a new sub-key such as "lib-tensorflow",
a user-friendly name such as "TensorFlow library",
one or more tags to specify your software detection plugin from above index
(CK will use these tags to find related CK components),
and an order in which dependencies will be resolved using the *sort* key.

You can also select version ranges with the following keys:
```json
  "version_from": [1,64,0], # inclusive
  "version_to": [1,66,0]    # exclusive
```

Have a look at a [more complex meta.json](https://github.com/dividiti/ck-caffe/blob/master/package/lib-caffe-bvlc-master-cuda-universal/.cm/meta.json) 
of the Caffe CUDA package.

Whenever CK compiles or runs programs, it first automatically resolves all software dependencies.
CK also registers all detected software or installed packages in the CK virtual environment
(see the [getting started guide](first-steps.md)) with automatically generated *env.sh* or *env.bat* batch scripts.
These scripts are then loaded one after another 
based on the above *sort*  key to aggregate all required environment variables 
and pass them either to the compilation or execution scripts.
Your scripts and algorithms can then use all these environment variables to customize compilation and execution
without any need to change paths manually, i.e. we enable portable workflows that can automatically adapt
to a user environment.





## Reuse or add basic datasets

We have developed a simple mechanism in the CK workflow to reuse basic (small) datasets such a individual images. 

You can find already shared datasets using this [online index]( https://cknow.io/c/dataset ).

If you want to reuse them in your program workflow, you can find the related one,
check its tags (see the [meta.json](https://github.com/ctuning/ck-autotuning/blob/master/dataset/image-jpeg-fgg/.cm/meta.json) 
of the image-jpeg-0001 dataset), and add them to your program meta as follows:
```json
  "run_cmds": {
    "corners": {
      "dataset_tags": [
        "image", 
        "pgm", 
        "dataset"
      ], 
      "ignore_return_code": "no", 
      "run_time": {
        "run_cmd_main": "$#BIN_FILE#$ $#dataset_path#$$#dataset_filename#$ tmp-output.tmp -c" 
      }
    }, 

```

CK then search for all dataset entries in all pulled CK repositories using these flags, 
and will ask a user which one to use when multiple entries are found. CK will then
substitute *$#dataset_path#$$#dataset_filename#$* with the full path and a file
of the dataset from the selected entry. 

Such approach allows to get rid of hardwired paths in ad-hoc scripts
while easily sharing and reusing related datasets. 
Whenever you pull a new repository with CK datasets, 
they can be automatically picked up by a given program workflow!

For example you can see all pgm images available in your CK repositories as follows:
```bash
ck pull repo:ctuning-datasets-min
ck search dataset --tags=dataset,image,pgm
```

You can add a new dataset in your new repository as follows:
```bash
ck add my-new-repo:dataset:my-new-dataset
```

You will be asked to enter some tags and to select a file that will be copied into your new CK entry. 

Note that for large and complex datasets such as ImageNet, we use CK packages 
that can download a given dataset and even process it depending on other software dependencies.
For example one may need a different procedure when using TensorFlow or PyTorch or MXNet.




## Add new CK software detection plugins

If CK software plugin doesn't exist for a given code, data, or models, 
you can add a new one either in your own repository or in [already existing ones](https://cknow.io/repos).

We suggest you to find the most close software detection plugin using 
[this online index](http://cknow.io/soft),
pull this repository, and make a copy in your repository as follows:

```bash
ck copy soft:lib.armcl my-new-repo:soft:lib.my-new-lib
```
or
```bash
ck copy soft:dataset.imagenet.train my-new-repo:soft:my-new-data-set
```

Alternatively, you can add a new soft entry and select the most relevant template:
```bash
ck add my-new-repo:soft:my-new-data-set
```

You must then update related keys in the *.cm/meta.json* file of the new CK entry.
You can find it as follows:

```bash
ck find soft:lib.my-new-lib
```

Typical software meta description:
```json
{
  "auto_detect": "yes",
  "customize": {
    "check_that_exists": "yes",
    "ck_version": 10,
    "env_prefix": "CK_ENV_LIB_ARMCL",
    "limit_recursion_dir_search": {
      "linux": 4,
      "win": 4
    },
    "soft_file": {
      "linux": "libarm_compute.a",
      "win": "arm_compute.lib"
    },
    "soft_path_example": {
    }
  },
  "soft_name": "ARM Compute Library",
  "tags": [
    "lib",
    "arm",
    "armcl",
    "arm-compute-library"
  ]
}
```

First, you must update *tags* keys for your new software, 
*soft_name* to provide a user-friendly name for your software,
*env_prefix* to expose different environment variables 
for the detected software in the automatically generated virtual environment script
(*env.sh* or *env.bat*), and *soft_file* keys to tell CK which unique filename inside this soft
to search for when detecting this software automatically on your system.

If the *soft_file* is the same across all platforms (Linux, Windows, MacOS, etc),
you can use the following universal key:
```json
    "soft_file_universal": "libGL$#file_ext_dll#$",
```

CK will then substitute *file_ext_dll* with *dll* key from the *file_extensions* dictionary
in the target OS (see example for the [64-bit Linux](https://github.com/ctuning/ck-env/blob/master/os/linux-64/.cm/meta.json#L39)
and [64-bit Windows](https://github.com/ctuning/ck-env/blob/master/os/windows-64/.cm/meta.json#L34)).

You can also tell CK to detect a given soft for a different target such as Android as follows:
```bash
ck detect soft:compiler.gcc.android.ndk --target_os=android21-arm64
ck detect soft --tags=compiler,android,ndk,llvm --target_os=android21-arm64
```

Next, you may want to update the [customize.py file](https://github.com/ctuning/ck-env/blob/master/soft/lib.armcl/customize.py) in the new entry.
This Python script can have multiple functions to customize the detection of a given software
and update different environment variables in the automatically generated "env.sh" or "env.bat" 
for the virtual CK environment.

For example, *setup* function receives a full path to a found software file specified using the above *soft_name* keys:

```python
    cus=i.get('customize',{})
    fp=cus.get('full_path','')
```

It is then used to prepare different environment variables with different paths (see *env* dictionary)
as well as embedding commands directly to "env.sh" or "env.bat" using "s" string in the returned dictionary:

```python
    return {'return':0, 'bat':s}
```

Here is an example of the automatically generated "env.sh" on a user machine:

```bash
#! /bin/bash
# CK generated script

if [ "$1" != "1" ]; then if [ "$CK_ENV_LIB_ARMCL_SET" == "1" ]; then return; fi; fi

# Soft UOA           = lib.armcl (fc544df6941a5491)  (lib,arm,armcl,arm-compute-library,compiled-by-gcc,compiled-by-gcc-8.1.0,vopencl,vdefault,v18.05,v18,channel-stable,host-os-linux-64,tar
get-os-linux-64,64bits,v18.5,v18.5.0)
# Host OS UOA        = linux-64 (4258b5fe54828a50)
# Target OS UOA      = linux-64 (4258b5fe54828a50)
# Target OS bits     = 64
# Tool version       = 18.05-b3a371b
# Tool split version = [18, 5, 0]

# Dependencies:
. /home/fursin/CK/local/env/fd0d1d044f44c09b/env.sh
. /home/fursin/CK/local/env/72fa25bd445a993f/env.sh

export CK_ENV_LIB_ARMCL_LIB=/home/fursin/CK-TOOLS/lib-armcl-opencl-18.05-gcc-8.1.0-linux-64/install/lib
export CK_ENV_LIB_ARMCL_INCLUDE=/home/fursin/CK-TOOLS/lib-armcl-opencl-18.05-gcc-8.1.0-linux-64/install/include


export LD_LIBRARY_PATH="/home/fursin/CK-TOOLS/lib-armcl-opencl-18.05-gcc-8.1.0-linux-64/install/lib":$LD_LIBRARY_PATH
export LIBRARY_PATH="/home/fursin/CK-TOOLS/lib-armcl-opencl-18.05-gcc-8.1.0-linux-64/install/lib":$LIBRARY_PATH

export CK_ENV_LIB_ARMCL=/home/fursin/CK-TOOLS/lib-armcl-opencl-18.05-gcc-8.1.0-linux-64/install
export CK_ENV_LIB_ARMCL_CL_KERNELS=/home/fursin/CK-TOOLS/lib-armcl-opencl-18.05-gcc-8.1.0-linux-64/src/src/core/CL/cl_kernels/
export CK_ENV_LIB_ARMCL_DYNAMIC_CORE_NAME=libarm_compute_core.so
export CK_ENV_LIB_ARMCL_DYNAMIC_NAME=libarm_compute.so
export CK_ENV_LIB_ARMCL_LFLAG=-larm_compute
export CK_ENV_LIB_ARMCL_LFLAG_CORE=-larm_compute_core
export CK_ENV_LIB_ARMCL_SRC=/home/fursin/CK-TOOLS/lib-armcl-opencl-18.05-gcc-8.1.0-linux-64/src
export CK_ENV_LIB_ARMCL_SRC_INCLUDE=/home/fursin/CK-TOOLS/lib-armcl-opencl-18.05-gcc-8.1.0-linux-64/src/include
export CK_ENV_LIB_ARMCL_STATIC_CORE_NAME=libarm_compute_core.a
export CK_ENV_LIB_ARMCL_STATIC_NAME=libarm_compute.a
export CK_ENV_LIB_ARMCL_TESTS=/home/fursin/CK-TOOLS/lib-armcl-opencl-18.05-gcc-8.1.0-linux-64/src/tests
export CK_ENV_LIB_ARMCL_UTILS=/home/fursin/CK-TOOLS/lib-armcl-opencl-18.05-gcc-8.1.0-linux-64/src/utils

export CK_ENV_LIB_ARMCL_SET=1
```

All these environment variables will be exposed to the CK program compilation and execution workflow
if this software dependency is seleted in a program meta description.
 
You can also look at how this functionality is implemented in the [CK soft module](https://github.com/ctuning/ck-env/blob/master/module/soft/module.py).

There are many options and nuances so we suggest you to have a look 
at existing examples or contact [the CK community](https://cKnowledge.org/contacts.html) for further details.
We regularly explain users how to add new software detection plugins and packages.




## Add new CK packages

Whenever a required software is not found, CK will automatically search
for existing packages with the same tags for a given target 
in all installed CK repositories.

[CK package module]( https://cknow.io/c/module/package ) provides a unified JSON API 
to automatically download, install, and potentially rebuild a given package
(software, datasets, models, etc) in a portable way across Linux, Windows, MacOS, Android,
and other supported platforms. It is also a unified front-end for other
package managers and build tools including make, cmake, scons, Spack, EasyBuild, etc.

If CK packages are not found, CK will print notes from the *install.txt* file
from a related software detection plugin about how to download and install such package manually 
as shown in this [example](https://github.com/ctuning/ck-env/blob/master/soft/compiler.cuda/install.txt)
for CUDA.

In such case, you may be interested to provide a new CK package to be reused either in your workgroup
or by the broad community to automate the installation.

Similar to adding CK software detection plugins, you must first find the most close package 
from this [online index](https://cknow.io/packages), download it,
and make a new copy in your repository unless you want to share it immediately with the community
in already [existing CK repositories]( https://cknow.io/repos ).

For example, let's copy a CK protobuf package that downloads a given protobuf version in a tgz archive 
and uses cmake to build it:

```bash
ck cp package:lib-protobuf-3.5.1-host my-new-repo:package:my-new-lib
```

Note, that all CK packages must be always connected with some software detection plugins
such as "soft:lib.my-new-lib" created in the previous section. 
You just need to find its Unique ID as follows:
```bash
ck info soft:lib.my-new-lib
```
and add it to the *soft_uoa* key in the package *meta.json*.

Next, copy/paste *the same* tags from the *meta.json* of the soft plugin
to the *meta.json* of the package and add extra tags specifying a version. 
See examples of such tags in existing packages 
such as [lib-armcl-opencl-18.05](https://github.com/ctuning/ck-math/blob/master/package/lib-armcl-opencl-18.05/.cm/meta.json)
and [compiler-llvm-10.0.0-universal](https://github.com/ctuning/ck-env/blob/master/package/compiler-llvm-10.0.0-universal/.cm/meta.json).

Alternatively, you can add a new CK package using existing templates
while specifying a related software plugin in the command line as follows:

```bash
ck add my-new-repo:package:my-new-lib --soft=lib.my-new-lib
```

In such case, CK will automatically substitute correct values for *soft_uoa* and *tags* keys!

Next, you need to update the *.cm/meta.json* file in the new CK package entry:
```bash
ck find package:my-new-lib
```

For example, you need to update other keys in the package meta.json
to customize downloading and potentially building (building is not strictly required 
when you download datasets, models, and other binary packages):

```json
   "install_env": {
      "CMAKE_CONFIG": "Release",
      "PACKAGE_AUTOGEN": "NO",
      "PACKAGE_BUILD_TYPE": "cmake",
      "PACKAGE_CONFIGURE_FLAGS": "-Dprotobuf_BUILD_TESTS=OFF",
      "PACKAGE_CONFIGURE_FLAGS_LINUX": "-DCMAKE_INSTALL_LIBDIR=lib",
      "PACKAGE_CONFIGURE_FLAGS_WINDOWS": "-DBUILD_SHARED_LIBS=OFF -Dprotobuf_MSVC_STATIC_RUNTIME=OFF",
      "PACKAGE_FLAGS_LINUX": "-fPIC",
      "PACKAGE_NAME": "v3.5.1.tar.gz",
      "PACKAGE_NAME1": "v3.5.1.tar",
      "PACKAGE_NAME2": "v3.5.1",
      "PACKAGE_RENAME": "YES",
      "PACKAGE_SUB_DIR": "protobuf-3.5.1",
      "PACKAGE_SUB_DIR1": "protobuf-3.5.1/cmake",
      "PACKAGE_UNGZIP": "YES",
      "PACKAGE_UNTAR": "YES",
      "PACKAGE_UNTAR_SKIP_ERROR_WIN": "YES",
      "PACKAGE_URL": "https://github.com/google/protobuf/archive",
      "PACKAGE_WGET": "YES"
    },
    "version": "3.5.1"
```

You can specify extra software dependencies using *deps* dictionary if needed.

You must also describe the file which will be downloaded or created at the end of
the package installation process using *end_full_path* key to let CK validate
that the process was successful:

```json
  "end_full_path": {
    "linux": "install$#sep#$lib$#sep#$libprotobuf.a",
    "win": "install\\lib\\libprotobuf.lib"
```

You can add or update a script to download and build a given package. See examples of such scripts in
CK package *imagenet-2012-aux*: [install.sh](]https://github.com/ctuning/ck-env/blob/master/package/imagenet-2012-aux/install.sh)
and [install.bat](https://github.com/ctuning/ck-env/blob/master/package/imagenet-2012-aux/install.bat)
 to download ImageNet 2012 auxiliary dataset used in the [ACM ReQuEST-ASPLOS tournament](https://cKnowledge.org/request)
and [MLPerf&trade; submissions](https://github.com/ctuning/ck-mlperf).

Note that CK will pass at least 2 environment variables to this script:
* *PACKAGE_DIR* - the path to the CK package entry. This is useful if your script need additional files or subscripts from the CK package entry.
* *INSTALL_DIR* - the path where this package will be installed. Note that *end_full_path* key will be appended to this path.

If you need to know extra CK variables passed to this script, 
you can just export all environment variable to some file 
and check the ones starting from *CK_*.

For example, if your package has software dependencies on a specific Python version,
all environment variables from the resolved software dependencies will be available 
in your installation script. This allows you to use the *${CK_ENV_COMPILER_PYTHON_FILE}*
environment variable instead of calling python directly to be able to automatically 
adapt to different python versions on your machine.

At the end of the package installation, CK will check if this file was created,
and will pass it to the related software detection plugin to register the CK virtual environment,
thus fully automating the process of rebuilding the required environment
for a given workflow!

If you need to create a simple package that downloads an archive, uses *configure* to configure it, 
and builds it using *make*, use this [lib-openmpi-1.10.3-universal CK package](https://github.com/ctuning/ck-env/tree/master/package/lib-openmpi-1.10.3-universal)
as example:

```json
 "PACKAGE_URL": "https://www.open-mpi.org/software/ompi/v1.10/downloads",
 "PACKAGE_NAME": "openmpi-1.10.3.tar.gz",
 "PACKAGE_NAME1": "openmpi-1.10.3.tar",
 "PACKAGE_NAME2": "openmpi-1.10.3",
 "PACKAGE_SUB_DIR": "openmpi-1.10.3",
 "PACKAGE_SUB_DIR1": "openmpi-1.10.3",
 "linux": "install/lib/libmpi.so"
```

Note that we described only a small part of all available functions of
the CK package manager that we have developed in collaboration with our [http://cKnowledge.org/partners.html partners and users].
We continue documenting them and started working on a user-friendly GUI
to add new software and packages via web. You can try it [here](https://cknow.io/add-artifact).




## Pack CK repository

You can pack a given repository as follows:
```bash
ck zip repo:my-new-repo
```

This command will create a *ckr-my-new-repo.zip* file that you can archive or send to your colleagues and [artifact evaluators](https://cTuning.org/ae).

Other colleagues can then download it and install it on their system as follows:

```bash
ck add repo --zip=ckr-my-new-repo.zip
```

They can also unzip entries to an existing repository (local by default) as follows:
```
ck unzip repo --zip=ckr-my-new-repo.zip
```

This enables a simple mechanism to share repositories, automation actions, and components 
including experimental results and reproducible papers with the community.
We also hope it will help to automate the [tedious Artifact Evaluation process](https://cTuning.org/ae).




## Prepare CK repository for Digital Libraries

During the [ACM ReQuEST-ASPLOS'18 tournament]( https://cKnowledge.org/request )
the authors needed to share the snapshots of their implementations of efficient deep learning algorithms 
for the ACM Digital Library.

We have added a new automation to the CK to prepare such snapshots
of a given repository with all dependencies and the latest CK framework in one zip file: 

```bash
ck snapshot artifact --repo=my-new-repo
```

It will create a *ck-artifacts-{date}.zip* archive with all related CK repositories, the CK framework, and two scripts:

* *prepare_virtual_ck.bat*
* *run_virtual_ck.bat*

The first script will unzip all CK repositories and the CK framework inside your current directory.

The second script will set environment variables to point to above CK repositories in such a way 
that it will not influence you existing CK installation! Basically it creates a virtual CK environment 
for a given CK snapshot. At the end, this script will run *bash* on Linux/MacOS or *cmd* on Windows
allowing you to run CK commands to prepare, run, and validate a given CK workflow
while adapting to your platform and environment! 






## Prepare a Docker container with CK workflows

One of the CK goals is to be a plug&play connector between non-portable workflows and containers.

CK can work both in native environments and containers. While portable CK workflows can fail
in the latest environment, they will work fine inside a container with a stable environment.

We have added the CK module [*docker*]( https://cknow.io/c/module/docker ) 
to make it easier to build, share, and run Docker descriptions.
Please follow the Readme in the [ck-docker]( https://github.com/ctuning/ck-docker ) for more details.

Please check examples of the CK Docker entries with CK workflows and components in the following projects:

* https://github.com/ctuning/ck-mlperf/tree/master/docker
* https://github.com/ctuning/ck-request-asplos18-caffe-intel/tree/master/docker
* https://github.com/ctuning/ck-docker/tree/master/docker

You can find many of these containers ready for deployment, usage, and further customization
at the [cTuning Docker hub]( https://hub.docker.com/u/ctuning ).







## Create more complex workflows

Users can create even more complex CK workflows that will automatically compile, run, and validate
multiple applications with different compilers, datasets, and models across different platforms 
while sharing, visualizing, and comparing experimental results via live scoreboards.

See the following examples:
* https://cKnowledge.org/rpi-crowd-tuning
* https://github.com/SamAinsworth/reproduce-cgo2017-paper (see [CK workflow module](https://github.com/SamAinsworth/reproduce-cgo2017-paper/blob/master/module/workflow-from-cgo2017-paper/module.py))
* https://github.com/ctuning/ck-scc18/wiki
* https://github.com/ctuning/ck-scc
* https://github.com/ctuning/ck-request-asplos18-results


Users can create such workflows using two methods:

### Using shell scripts

We have added CK module *script* that allows you to add a CK entry 
where you can store different system scripts. Such scripts can call
different CK modules to install packages, build and run programs, 
prepare interactive graphs, generate papers, etc.

You can see examples of such scripts from the [reproducible CGO'17 paper]( https://github.com/SamAinsworth/reproduce-cgo2017-paper/tree/master/script/reproduce-cgo2017-paper ).
You can also check this [unified Artifact Appendix and reproducibility checklist](https://www.cl.cam.ac.uk/~sa614/papers/Software-Prefetching-CGO2017.pdf) 
at the end of this article describing how to run those scripts.

You can add your own CK script entry as follows:
```bash
 $ ck add my-new-repo:script:my-scripts-to-run-experiments
 $ ck add my-new-repo:script:my-scripts-to-generate-articles
```

You can also write Python scripts calling CK APIs directly.
For example, check [this ReQuEST-ASPLOS'18 benchmark script]( https://github.com/dividiti/ck-request-asplos18-mobilenets-armcl-opencl/blob/master/script/mobilenets-tensorflow/benchmark.py )
to prepare, run, and customize [ACM REQUEST]( https://cKnowledge.org/request ) experiments:

```bash
#! /usr/bin/python

import ck.kernel as ck
import os

...

def do(i, arg):

    # Process arguments.
    if (arg.accuracy):
        experiment_type = 'accuracy'
        num_repetitions = 1
    else:
        experiment_type = 'performance'
        num_repetitions = arg.repetitions

    random_name = arg.random_name
    share_platform = arg.share_platform

    # Detect basic platform info.
    ii={'action':'detect',
        'module_uoa':'platform',
        'out':'con'}
    if share_platform: ii['exchange']='yes'
    r=ck.access(ii)
    if r['return']>0: return r

...
```



### Using CK modules

You can also add and use any new module "workflow.my-new-experiments" as a workflow 
with different functions to prepare, run, and validate experiments. 
This is the preferred method that allows you to use unified CK APIs 
and reuse this module in other projects:

```bash
ck add my-new-repo:module:workflow.my-new-experiments
```

Note, that CK module and entry names are global in the CK. Therefore, we suggest you to find a unique name.

You can then add any function to this workflow. For example, let's add a function "run" to run your workflow:
```bash
ck add_action my-new-repo:module:workflow.my-new-experiments --func=run
```

CK will create a working dummy function in the python code of this CK module that you can test immediately:
```bash
ck run workflow.my-new-experiments
```

You can then find the *module.py* from this CK module and update *run* function to implement your workflow:
```bash
ck find module:workflow.my-new-experiments
cd `ck find module:workflow.my-new-experiments`
ls *.py
```

Don't hesitate to get in touch with the [[Contacts|CK community]] if you have questions or comments.





## Generate reproducible and interactive articles



Unified CK APIs and portable CK workflows can help to automate all experiments as well as 
the generation of papers with all tables and graphs. 

As a proof-of-concept, we collaborated with the [Raspberry Pi foundation]( https://www.raspberrypi.org )
to reproduce results from the [MILEPOST project]( https://en.wikipedia.org/wiki/MILEPOST_GCC )
and develop a Collective Knowledge workflow for collaborative research into multi-objective autotuning 
and machine learning techniques.

We have developed a [MILEPOST GCC workflow](https://github.com/ctuning/reproduce-milepost-project),
shared results in the [CK repository](https://github.com/ctuning/ck-rpi-optimization-results),
created [live CK dashboards to crowdsource autotuning]( https://cKnowledge.org/repo-beta ),
and automatically generated a [live and interactive article](https://cKnowledge.org/rpi-crowd-tuning)
where results can be automatically updated by the community. The stable snapshot of such article
can still be published as a [traditional PDF paper](https://arxiv.org/abs/1801.08024).

However, it is still a complex process. We have started documenting this functionality [here](https://github.com/ctuning/ck/wiki/Interactive-articles)
and plan to gradually improve it. When we have more resources, we plan to add a web-based GUI to the [cknow.io platform](https://cknow.io)
to make it easier to create such live, reproducible, and interactive articles.







## Publish CK repositories, workflows, and components

We are developing an open [cKnowledge.io platform](https://cknow.io) to let users
share and reuse CK repositories, workflows, and components similar to PyPI.
Please follow [this guide]( https://cknow.io/docs ) to know more.




## Contact the CK community

We continue improving the CK technology, components, automation actions, workflows, and this documentation!
If you have questions, encounter problems or have some feedback,
do not hesitate to [contact us](https://cKnowledge.org/contacts.html)!
