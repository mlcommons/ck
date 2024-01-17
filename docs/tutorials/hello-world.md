[ [Back to index](../README.md) ]

# Tutorial: run Python Hello World app on Linux, Windows and MacOS

```bash
python3 -m pip install cmind
```

You may need to restart bash to add `cm` and `cmr` binaries to your PATH,

```bash
cm pull repo mlcommons@ck
cm run script --tags=print,python,hello-world
cmr "print python hello-world"
```

This CM script is a simple wrapper to native scripts and tools
with a common CLI and API described by a simple declarative YAML configuration file
that specifies wrapper inputs, environment variables and dependencies on other portable
[CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script):

```yaml
alias: print-hello-world-py
uid: d83274c7eb754d90

automation_alias: script
automation_uid: 5b4e0237da074764

deps:
- tags: detect,os
- tags: get,sys-utils-cm
- names:
  - python
  tags: get,python3

tags:
- print
- hello-world
- python

```
