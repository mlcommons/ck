*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

### Automation actions

#### test

  * CM CLI: ```cm test experiment``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L22))
  * CM CLI with UID: ```cm test experiment,a0a2d123ef064bcb``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L22))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'test'
                 'automation':'experiment,a0a2d123ef064bcb'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L22)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### run

  * CM CLI: ```cm run experiment``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L64))
  * CM CLI with UID: ```cm run experiment,a0a2d123ef064bcb``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L64))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'run'
                 'automation':'experiment,a0a2d123ef064bcb'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L64)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### rerun

  * CM CLI: ```cm rerun experiment``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L428))
  * CM CLI with UID: ```cm rerun experiment,a0a2d123ef064bcb``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L428))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'rerun'
                 'automation':'experiment,a0a2d123ef064bcb'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L428)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### replay

  * CM CLI: ```cm replay experiment``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L451))
  * CM CLI with UID: ```cm replay experiment,a0a2d123ef064bcb``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L451))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'replay'
                 'automation':'experiment,a0a2d123ef064bcb'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/experiment/module.py#L451)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce)