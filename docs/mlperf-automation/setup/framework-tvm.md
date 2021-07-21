**[ [TOC](../README.md) ]**

## Pull MLOps automation repo

```bash
ck pull repo:octoml@mlops
```

## Install CK packages

```bash
ck install package --tags=tool,cmake,prebuilt,v3.18.2

ck install package --tags=compiler,llvm,prebuilt,v12.0.0

ck install package --tags=compiler,tvm,dev --j=8

```

TVM installation can be customized as follows:
```bash
ck install package --tags=compiler,tvm,dev \
                     --env.USE_RELAY_DEBUG=ON \
                     --env.USE_GRAPH_RUNTIME_DEBUG=ON \
                     --env.USE_GRAPH_EXECUTOR_DEBUG=ON
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
