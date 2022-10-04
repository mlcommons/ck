# Enhancements

## Automation scripts

* [Planned developments for 2022]( https://github.com/mlcommons/ck/issues/189 )
* ~[Prototyping major automations for MLOps and DevOps](https://github.com/mlcommons/ck/issues/245)~

## Ideas

### Making CM scripts completely deterministic

Script starts with a "state" dict (with "env" inside)
and must produce an updated "state" dict deterministically
to run the final command (CMD)

If "state" contains all the required information, 
script just runs the final command.

If something is missing in the "state", script and dependencies
must fill in all missing info on a given platform.

CM input to the script finds a given script
and updates the "state" uniqely. For example
--version --version_max for get-python3 will update the following variable in the state:

* CM_PYTHON_VERSION
* CM_PYTHON_VERSION_MAX

This means that we can either use state from the start and update it manually
or use local input to the script that will again update the state
before finding and running the script ...

My feeling is that it will simplify the current flow.

### Speeding up search action

In the CK1, we used explicit indexing of all entries using .cm directories. 
Such mechanism provided a very fast search but it was not very user friendly:
if a user forgot to add .cm to Git or Zip, the search function was broken.

In the CM (aka CK2), we have decided to simplify the overall architecture and removed
explicit indexing by default. Now, CM will be searching recursively for entries
based on UID and alias in their meta description (_cm.yaml | _cm.json).

We want to add implicit indexing later similar to Git to let CM auto-index repositories.

### Using sub-folders for automations (scripts)

(from Arjun) Can we also add support for putting CM scripts inside a folder? 
This will mean CM to recursively scan the script directory for all sub folders
having "_cm.json". I was considering a use case of C programs for Computer
Science subjects being organized as CM scripts (for better
reproducibility) and having them organized as sub folders 
(algorithm-lab, os-lab etc) will be better.

