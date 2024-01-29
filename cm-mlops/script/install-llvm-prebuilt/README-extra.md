# Get LLVM
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) detects the installed llvm on the system and if not found calls the [install script for llvm](../script/install-llvm-prebuilt).

## Exported Variables
* `CM_LLVM_CLANG_BIN`
* `CM_LLVM_CLANG_BIN_WITH_PATH` 
* `CM_C_COMPILER_BIN`
* `CM_C_COMPILER_WITH_PATH`
* `CM_CXX_COMPILER_BIN`
* `CM_CXX_COMPILER_WITH_PATH`
* `CM_COMPILER_*`

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9
3. Windows 10, 11

# CLI

## Default
```bash
cm run script "install llvm prebuilt"
```
or
```bash
cm run script --tags=get,llvm
```

## Version

```bash
cm run script "install llvm prebuilt" --version=14.0.0
```

## Version min
```bash
cm run script "install llvm prebuilt" --version_min=12.0.0
```

## Version max
```bash
cm run script "install llvm prebuilt" --version_max=13.999.999 --version_max_usable=13.0.0
```

## Force new detection even if llvm is already found and cached
```bash
cm run script "install llvm prebuilt" --new
```

## Test

```bash
cm run script "app image corner-detection"
```

## Reproducibility matrix

*Test detection and installation on different platforms*

* Windows, Linux, MacOS

### Ubuntu 22.04

* 17.0.6
* 17.0.5
* 17.0.4
* 17.0.2
* 16.0.4
* 16.0.0
  `sudo apt install libncurses5`
* 15.0.6
* 14.0.0


### RHEL 9

#### v14.0.0: &#10003; 

```bash
cm rm cache -f
cm run script "install llvm prebuilt" --version=14.0.0
cm run script "app image corner-detection"
```

#### v13.0.0: Need special command

```bash
cm rm cache -f
cm run script "install llvm prebuilt" --version=13.0.0 --env.CM_LLVM_PACKAGE=clang+llvm-13.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz
cm run script "app image corner-detection"
```

#### v12.0.0: Need special command

```bash
cm rm cache -f
cm run script "install llvm prebuilt" --version=12.0.0 --env.CM_LLVM_PACKAGE=clang+llvm-12.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz
cm run script "app image corner-detection"
```
