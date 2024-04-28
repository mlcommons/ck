*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

### Automation actions

#### print_input

  * CM CLI: ```cm print_input automation``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/automation/module.py#L15))
  * CM CLI with UID: ```cm print_input automation,bbeb15d8f0a944a4``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/automation/module.py#L15))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'print_input'
                 'automation':'automation,bbeb15d8f0a944a4'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/automation/module.py#L15)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### add

  * CM CLI: ```cm add automation``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/automation/module.py#L39))
  * CM CLI with UID: ```cm add automation,bbeb15d8f0a944a4``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/automation/module.py#L39))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'add'
                 'automation':'automation,bbeb15d8f0a944a4'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/automation/module.py#L39)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### doc

  * CM CLI: ```cm doc automation``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/automation/module.py#L111))
  * CM CLI with UID: ```cm doc automation,bbeb15d8f0a944a4``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/automation/module.py#L111))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'doc'
                 'automation':'automation,bbeb15d8f0a944a4'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/automation/module.py#L111)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)