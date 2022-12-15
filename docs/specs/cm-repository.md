[ [Back to index](README.md) ]

## CM repository structure

By default, CM repositories are stored in `$HOME/CM` on Linux and `%homepath%\CM` on Windows

They have the following structure:

```
{ROOT directory} / 
   _cmr.yaml
   {CM automation alias or Unique ID} / 
      {CM artifact alias or Unique ID } / 
         _cm.yaml and/or _cm.json
         {user scripts, files and directories}
```

Feel free to explore two main CM repositories being developed by the open MLCommons taskforce:
* [internal](https://github.com/mlcommons/ck/blob/master/cm/cmind/repo) (shared inside CM PYPI package)
* [mlcommons@ck](https://github.com/mlcommons/ck/blob/master/cm-mlops) (shared via GitHub)


### Root directory

* File *cmr.yaml* - CM repository description

```json
{
  alias (str): CM name to find this repository
  uid (str): unique ID to find this repository

  (desc) (str): user-friendly description
  (git) (bool): True, if it's a Git repository and not a local one
  (prefix) (str): sub-directory inside this repository to keep CM automations and artifacts
                  - useful to keep original software project repository intact
}
```

Example: [mlcommons@ck description](https://github.com/mlcommons/ck/blob/master/cmr.yaml) 

### First level directories

* CM automation aliases or Unique IDs

Examples: [mlcommons@ck repo](https://github.com/mlcommons/ck/tree/master/cm-mlops)

### Second level directories

* CM artifact aliases or Unique IDs

Examples: 

* [CM artifacts to wrap CM automations (including "script") in mlcommons@ck repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation) 
* [CM artifacts to wrap CM scripts in mlcommons@ck repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)

### Third level files

* *_cm.yaml and/or _cm.json* - CM meta description of this CM artifact wrapping user scripts, files and directories

```json
{
  alias (str): CM name to find this artifact
  uid (str): unique ID to find this artifact

  automation_alias (str): CM automation name for this artifact
  automation_uid (str): unique ID for the automation for this artifact

  (_base) (str): preload meta description from this base artifact in format "{automation}::{artifact}" 
                 and then merge the current meta description with the base.
                 This mechanism enables simple inheritance of artifact meta descriptions.

  tags (list): list of tags to characterize and find this artifact

  Any other keys required for a related CM automation ...
}
```

* any user scripts, files and directories wrapped by this CM artifact

Examples: 
* [CM script to install system dependencies (any Linux and macOS](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm) 
* [CM script to install system dependencies (Windows)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min) 
* [CM script to detect or install Python](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3) 
* [CM script to detect LLVM](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm) 
* [CM script to install prebuilt LLVM](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt) 
* [CM script to run image classification with ONNX](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py)
