[ [Back to index](README.md) ]

# CM debugging

Since CM language uses native OS scripts with python wrappers, it is relatively straightforward to debug it using your existing tools.

When you run CM language from the command line or via Python API, the most common execution flow is:

1. [cmind package access function in core.py](../cm/cmind/core.py)
2. CM automation either from the [internal CM repo](../cm/cmind/repo/automation) 
   or [mlcommons@ck](../cm-mlops/automation)
3. [CM scripts](../cm-mlops/script)
4. preprocess function from customize.py from a given CM script 
5. native OS script
6. postprocess function from customize.py from a given CM script

