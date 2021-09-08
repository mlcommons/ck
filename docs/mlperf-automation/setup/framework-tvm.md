**[ [TOC](../README.md) ]**

## Pull MLOps automation repo

```bash
ck pull repo:mlcommons@ck-mlops
```

## Detect already installed tools

If you have already installed cmake, LLVM and TVM that you would like to use with MLPerf,
you can automatically plug them into CK as follows:
```bash
ck detect soft:tool.cmake
ck detect soft:compiler.llvm
ck detect soft:compiler.tvm
```

CK will search for these tools in the common places (/usr, /usr/bin, $HOME, etc).

You can narrow down the search as follows:
```bash
ck detect soft:tool.cmake --search_dirs={places to search for separated by comma}
ck detect soft:compiler.llvm --search_dirs={places to search for separated by comma}
ck detect soft:compiler.tvm --search_dirs={places to search for separated by comma}
```

Alternatively, you can install specific versions of these tools and plug them into CK
using "ck install package" automation as described in the next section.

## Install CK packages

*Note that you may need to install llvm 11.0.1 on Nvidia Jetson Nano board with older Ubuntu 18.04*


```bash
ck install package --tags=tool,cmake,prebuilt,v3.21.1

ck install package --tags=compiler,llvm,prebuilt,v12.0.0

ck install package --tags=compiler,tvm,dev --env.USE_OPENMP=gnu --j=8

```

TVM installation can be customized as follows:
```bash
ck install package --tags=compiler,tvm,dev \
                     --env.USE_RELAY_DEBUG=ON \
                     --env.USE_GRAPH_RUNTIME_DEBUG=ON \
                     --env.USE_GRAPH_EXECUTOR_DEBUG=ON
```

## TVM with DNNL support 
You can also install TVM with DNNL support to run MLPerf TVM2 backend as follows:
```bash
ck install package --tags=lib,dnnl,v2.2.4 --dep_add_tags.compiler=llvm
ck install package --tags=compiler,tvm,src,dev-0.8-dnnl-int8-v2-mlperf-1.1 \
      --env.USE_DNNL_CODEGEN=ON --env.USE_OPENMP=gnu --j=16
```

You can find the installation directories of TVM, LLVM, MLPerf and other packages as follows:
```bash
ck locate env --tags=compiler,tvm
ck locate env --tags=compiler,llvm
ck locate env --tags=mlperf,source
...
```

CK allows you to have multiple versions of all packages installed at the same time.
Each directory contains *env.sh* or *env.bat* with a preset environment variables
for a given version. 

CK program workflows will automatically load these files when resolving dependencies
thus allowing users to run the same MLPerf workflow with different versions
of compilers, frameworks, libraries, models and data sets.

*Note that all above steps can be automated via CK virtual environments too.
 However, we describe these manual steps to let users experiment 
 with different versions of dependencies for DSE.* 


## Check TVM backend for MLPerf v1.1

* [TVM backend with ONNX models](https://github.com/octoml/mlcommons-inference/blob/r1.1/vision/classification_and_detection/python/backend_tvm_onnx.py)
* [TVM backend with PyTorch models](https://github.com/octoml/mlcommons-inference/blob/r1.1/vision/classification_and_detection/python/backend_tvm_pytorch.py)
* [MLPerf Python wrapper for reference implementations](https://github.com/octoml/mlcommons-inference/blob/r1.1/vision/classification_and_detection/python/main.py)
