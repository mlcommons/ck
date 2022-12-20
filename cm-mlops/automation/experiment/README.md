*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

### Automation actions

#### test

  * CM CLI: ```cm test experiment``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L15))
  * CM CLI with UID: ```cm test experiment,a0a2d123ef064bcb``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L15))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'test'
                 'automation':'experiment,a0a2d123ef064bcb'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L15)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### run

  * CM CLI: ```cm run experiment``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L53))
  * CM CLI with UID: ```cm run experiment,a0a2d123ef064bcb``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L53))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'run'
                 'automation':'experiment,a0a2d123ef064bcb'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L53)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### replay

  * CM CLI: ```cm replay experiment``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L155))
  * CM CLI with UID: ```cm replay experiment,a0a2d123ef064bcb``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L155))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'replay'
                 'automation':'experiment,a0a2d123ef064bcb'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L155)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)