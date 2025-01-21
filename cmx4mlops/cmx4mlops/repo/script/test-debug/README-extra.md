Demo of debugging CM scripts and wrapped apps with Visual Studio Code.


Debug customize.py using remote debugging and follow instructions on command line:

```bash
cmr "test cm-debug" --debug_uid=8d96cd9fa4734204
```

Debug Python application or tool wrapped by the CM script (see [python/main.py](python/main.py)):

```bash
cmr "test cm-debug" --debug_uid=45a7c3a500d24a63
```



Debug CM internals using standard Python debugging:
* Open _demo.py and start debugging using "Python File" default configuration.

