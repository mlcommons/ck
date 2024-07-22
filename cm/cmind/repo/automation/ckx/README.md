*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

### Automation actions

#### any

  * CM CLI: ```cm any ck``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/ck/module.py#L15))
  * CM CLI with UID: ```cm any ck,1818c39eaf3a4a78``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/ck/module.py#L15))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'any'
                 'automation':'ck,1818c39eaf3a4a78'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/ck/module.py#L15)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)