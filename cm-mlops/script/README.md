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
* Then any `prehook_deps` CM scripts mentioned in `_cm.json` are executed similar to `deps`
* After this, keys in `env` dictionary is exported as `ENV` variables and `run` file if exists is executed.
* Once run file execution is done, any `posthook_deps` CM scripts mentioned in `_cm.json` are executed similar to `deps`
* Then `postprocess` function inside customize.py is executed if present.
* After this stage any `post_deps` CM scripts mentioned in `_cm.json` is executed.

** If a script is already cached, then the `preprocess`, `run file` and `postprocess` executions won't happen and only the dependencies marked as `dynamic` will be executed from `deps`, `prehook_deps`, `posthook_deps` and `postdeps`.

### Input flags
* When we run a CM script we can also pass inputs to it and any input added in `input_mapping` dictionary inside `_cm.json` gets converted to the corresponding `ENV` variable.

### Consitional execution of any `deps`, `post_deps`
* We can use `skip_if_env` dictionary inside any `deps`, `prehook_deps`, `posthook_deps` or `post_deps` to make its executional conditional

### Versions
* [TBD]

### Variations
* Variations are used to customize CM script and each unique combination of variations uses a unique cache entry. Each variation can turn on `env` keys also any other meta including dependencies specific to it. Variations are turned on like tags but with a `_` prefix. For example, if a script is having tags `"get,myscript"`, to call the variation `"test"` inside it, we have to use tags `"get,myscript,_test"`. 
 
#### Variation groups
* `group` is a key to map variations into a group and at any time only one variation from a group can be used in the variation tags. For example, both `cpu` and `cuda` can be two variations under the `device` group, but user can at any time use either `cpu` or `cuda` as variation tags but not both.

#### Dynamic variations
* Sometimes it is difficult to add all variations needed for a script like say `batch_size` which can take many different values. To handle this case, we support dynamic variations using '#' where '#' can be dynamically replaced by any string. For example, `"_batch_size.8"` can be used as a tag to turn on the dynamic variation `"_batch_size.#"`.

### ENV flow during CM script execution
* [TBD] Issue added [here](https://github.com/mlcommons/ck/issues/382)

### How cache works?
* [TBD]

### Updating ENV from inside the run script
* [TBD]

&copy; 2022-23 [MLCommons](https://mlcommons.org)<br>
