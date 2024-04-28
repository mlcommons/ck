[ [Back to index](README.md) ]

# CM debugging

Since CM language uses native OS scripts with python wrappers, it is relatively straightforward to debug it using your existing tools.

When you run CM language from the command line or via Python API, the most common execution flow is:

1. cm/cmr binary or cmind.access function
2. ["access" function in core.py from cmind package](../cm/cmind/core.py)
3. CM automation either from the [internal CM repo](../cm/cmind/repo/automation) 
   or [mlcommons@ck](../cm-mlops/automation)
4. [CM scripts](../cm-mlops/script)
5. preprocess function from customize.py from a given CM script 
6. native OS script
7. postprocess function from customize.py from a given CM script

When running MLPerf and other benchmarks, you can often use the `--debug` flag to 
start a shell with all environment variables prepared to run/debug the final OS command manually.
You can also use GDB via environment variable `--env.CM_RUN_PREFIX="gdb --args "`

## Visual Studio Code

You can debug CM scripts using Visual Studio Code. See the [test-debug](https://github.com/mlcommons/cm4mlops/tree/main/script/test-debug) CM script 
for a demo:

* Debug CM internals and customize.py using [python entry point](https://github.com/mlcommons/cm4mlops/blob/main/script/test-debug/_demo.py#L8)
* Debug native python code wrapped by CM scripts using CM break points: [code](https://github.com/mlcommons/cm4mlops/blob/main/script/test-debug/python/main.py#L18), 
  [README](https://github.com/mlcommons/cm4mlops/blob/main/script/test-debug/README-extra.md)
