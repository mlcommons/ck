*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

### Automation actions

#### test

  * CM CLI: ```cm test contributor``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/contributor/module.py#L15))
  * CM CLI with UID: ```cm test contributor,68eae17b590d4f8f``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/contributor/module.py#L15))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'test'
                 'automation':'contributor,68eae17b590d4f8f'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/contributor/module.py#L15)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### add

  * CM CLI: ```cm add contributor``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/contributor/module.py#L54))
  * CM CLI with UID: ```cm add contributor,68eae17b590d4f8f``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/contributor/module.py#L54))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'add'
                 'automation':'contributor,68eae17b590d4f8f'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/contributor/module.py#L54)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce)