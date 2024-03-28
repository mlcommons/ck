*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

### Automation actions

#### test

  * CM CLI: ```cm test cfg``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cfg/module.py#L15))
  * CM CLI with UID: ```cm test cfg,88dce9c160324c5d``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cfg/module.py#L15))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'test'
                 'automation':'cfg,88dce9c160324c5d'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cfg/module.py#L15)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce)