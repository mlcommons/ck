# CK specs

## CK repository

Here we describe the structure of a CK repository. 
You may want to look at any CK repository such as [ck-env](https://github.com/ctuning/ck-env)
to better understand this structure.

Note that CK creates this structure automatically when you use 
[CK CLI or Python API](commands.md).

### Root files

* *.ckr.json* : JSON meta description of this repository including UIDs and dependencies on other repositories.
                Most of this information is automatically generated when a new CK repository is created.

```Json
{
  "data_alias": # repository name (alias) such as "ck-env"
  "data_name": # user-friendly repository name such as "CK environment"
  "data_uid": # CK UID for this repository (automatically generated)
  "data_uoa": # repository alias or repository UID if alias is empty
  "dict": {
    "desc": # user-friendly description of this repository
    "repo_deps": [
      {
        "repo_uoa": # repository name
        "url": # Git URL of this repo
      }
      ...
    ],
    "shared": # =="git" if repository is shared
    "url": # Git URL of this repository
  }
}
```

### Root directories (CK modules)

Root of the CK repository can contain any sub-directories to let users gradually convert their ad-hoc projects into the CK format.
However, if a directory is related to CK entry, it should have the same name as an associated CK module and two files in the *.cm* directory:

* *CK module name*
* *.cm/alias-a-{CK module name}* : contains UID of the CK module
* *.cm/alias-u-{UID}* : contains CK module name (alias)

These 2 files in .cm help CK to understand that a given directory inside CK repository is associated with some CK entry!
They also support fast such for a given CK entry by UIDs or aliases.

However, in the future, we may want to remove such files and perform automatic indexing when CK pulls repositories (similar to Git). See [this ticket](https://github.com/mlcommons/ck/issues/118).

### Sub-directories for CK entries

If the directory in the CK repository is a valid CK module name, it can contain CK entries associated with this CK module.

If CK entry does not have a name (an alias), it will be stored as a CK UID (16 lowercase hexadecimal characters):

* *UID* : holder for some artifacts

If CK entry has a name (an alias), there will be two more files in the *.cm* directory:

* *CK entry name* : holder for some artifacts 
* *.cm/alias-a-{CK entry name}* : contains UID of the CK entry
* *.cm/alias-u-{UID}* : contains CK entry name (alias)

Once again, these .cm files allow CK to quickly find CK entries by UID and aliases in all CK repositories without the need for any indexing.

### CK entry

Each valid CK entry has at least 3 files in the *.cm* directory:

* *.cm/meta.json* : JSON meta description of a given CK entry
* *.cm/info.json* : provenance for a given CK entry (date of creation, author, copyright, license, CK used, etc)
* *.cm/desc.json* : meta description SPECs (under development)

This entry can also contain any other files and directories (for example models, data set files, algorithms, scripts, papers and any other artifacts).
