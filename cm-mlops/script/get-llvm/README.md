# Get LLVM
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/tutorial-scripts.md) detects the installed llvm on the system and if not found calls the [install script for llvm](../script/install-llvm-prebuilt).

## Exported Variables
* `CM_LLVM_CLANG_BIN`
* `CM_LLVM_CLANG_BIN_WITH_PATH` 
* `CM_C_COMPILER_BIN`
* `CM_C_COMPILER_WITH_PATH`
* `CM_CXX_COMPILER_BIN`
* `CM_CXX_COMPILER_WITH_PATH`
* `FAST_COMPILER_FLAGS`
* `FAST_LINKER_FLAGS`
* `DEBUG_COMPILER_FLAGS`
* `DEBUG_LINKER_FLAGS`
* `DEFAULT_COMPILER_FLAGS`
* `DEFAULT_LINKER_FLAGS`
## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9
