Checking some conditions to turn on or off deps:

```bash
cmr "test deps conditions2" -s
cmr "test deps conditions2" -s --test
cmr "test deps conditions2" -s --test=xyz
```

Note that the last two will run with the following deps,
i.e. `True` tests not only for turning flag on, 
but also for any non-empty value :
```yaml
  - tags: print,any-text,_text.RUN_IF_ENV_IS_SET_TO_TRUE
    enable_if_env:
      TEST:
      - True

```

It is useful to check if flag turns on output or output to specific file for example ...
