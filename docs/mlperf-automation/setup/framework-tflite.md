**[ [TOC](../README.md) ]**

## Pull MLOps automation repo

```bash
ck pull repo:mlcommons@ck-mlops
```

## Detect already installed tools

If you have already installed cmake and LLVM that you would like to use with MLPerf,
you can automatically plug them into CK as follows:
```bash
ck detect soft:tool.cmake
ck detect soft:compiler.llvm
```

CK will search for these tools in the common places (/usr, /usr/bin, $HOME, etc).

You can narrow down the search as follows:
```bash
ck detect soft:tool.cmake --search_dirs={places to search for separated by comma}
ck detect soft:compiler.llvm --search_dirs={places to search for separated by comma}
```

Alternatively, you can install specific versions of these tools and plug them into CK
using "ck install package" automation as described in the next section.


## Install CK packages

*Note that you may need to install llvm 11.0.1 on Nvidia Jetson Nano board with older Ubuntu 18.04*


```bash
ck install package --tags=tool,cmake,prebuilt,v3.21.1

ck install package --tags=compiler,llvm,prebuilt,v12.0.0

ck install package --tags=api,model,tensorflow,r2.3.0

ck install package --tags=lib,tflite,via-cmake,v2.4.2,with.ruy --j=2
```
