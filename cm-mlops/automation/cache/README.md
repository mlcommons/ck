*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

### Automation actions

#### test

  * CM CLI: ```cm test cache``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cache/module.py#L15))
  * CM CLI with UID: ```cm test cache,541d6f712a6b464e``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cache/module.py#L15))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'test'
                 'automation':'cache,541d6f712a6b464e'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cache/module.py#L15)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### show

  * CM CLI: ```cm show cache``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cache/module.py#L54))
  * CM CLI with UID: ```cm show cache,541d6f712a6b464e``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cache/module.py#L54))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'show'
                 'automation':'cache,541d6f712a6b464e'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cache/module.py#L54)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### search

  * CM CLI: ```cm search cache``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cache/module.py#L153))
  * CM CLI with UID: ```cm search cache,541d6f712a6b464e``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cache/module.py#L153))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'search'
                 'automation':'cache,541d6f712a6b464e'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cache/module.py#L153)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### copy_to_remote

  * CM CLI: ```cm copy_to_remote cache``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cache/module.py#L186))
  * CM CLI with UID: ```cm copy_to_remote cache,541d6f712a6b464e``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cache/module.py#L186))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'copy_to_remote'
                 'automation':'cache,541d6f712a6b464e'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/cache/module.py#L186)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce)