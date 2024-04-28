*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

### Automation actions

#### uid

  * CM CLI: ```cm uid core``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/core/module.py#L22))
  * CM CLI with UID: ```cm uid core,60cb625a46b38610``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/core/module.py#L22))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'uid'
                 'automation':'core,60cb625a46b38610'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/core/module.py#L22)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)