These portable and reusable CM scripts are being developed by the 
[MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md) 
to make MLOps and DevOps more interoperable, reusable, portable, deterministic and reproducible.

See the catalog [here](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md) (automatically generated).

## Getting started with CM scripts

* A CM script is identified by a set of tags and by unique ID. 
* Further each CM script can have multiple variations and they are identified by variation tags which are treated in the same way as tags and identified by a `_` prefix.

### CM script execution flow
* When a CM script is invoked (either by tags or by unique ID), its `_cm.json` is processed first which will check for any `deps` script and if there are, then they are executed in order.
* Once all the `deps` scripts are executed, `customize.py` file is checked and if existing `preprocess` function inside it is executed if present. 
* After the `preprocess` function is done, keys in `env` dictionary is exported as `ENV` variables and `run` file if exists is executed.
* Once run file execution is done, then `postprocess` function inside customize.py is executed if present.
* After this stage any `post_deps` CM scripts mentioned in `_cm.json` is executed.

### Input flags
* When we run a CM script we can also pass inputs to it and any input added in `input_mapping` dictionary inside `_cm.json` gets converted to the corresponding `ENV` variable.

### Consitional execution of any `deps`, `post_deps`
* We can use `skip_if_env` dictionar inside any `deps` or `post_deps` to make its executional conditional

### Versions
* [TBD]

### Variation groups
* [TBD]

### ENV flow during CM script execution
* [TBD]

### How cache works?
* [TBD]

### Updating ENV from inside the run script
* [TBD]

&copy; 2022-23 [MLCommons](https://mlcommons.org)<br>
