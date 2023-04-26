*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

### Automation actions

#### pull

  * CM CLI: ```cm pull repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L15))
  * CM CLI with UID: ```cm pull repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L15))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'pull'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L15)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### search

  * CM CLI: ```cm search repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L93))
  * CM CLI with UID: ```cm search repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L93))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'search'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L93)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### update

  * CM CLI: ```cm update repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L172))
  * CM CLI with UID: ```cm update repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L172))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'update'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L172)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### delete

  * CM CLI: ```cm delete repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L209))
  * CM CLI with UID: ```cm delete repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L209))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'delete'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L209)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### init

  * CM CLI: ```cm init repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L262))
  * CM CLI with UID: ```cm init repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L262))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'init'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L262)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### add

  * CM CLI: ```cm add repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L381))
  * CM CLI with UID: ```cm add repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L381))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'add'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L381)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### pack

  * CM CLI: ```cm pack repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L389))
  * CM CLI with UID: ```cm pack repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L389))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'pack'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L389)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### unpack

  * CM CLI: ```cm unpack repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L459))
  * CM CLI with UID: ```cm unpack repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L459))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'unpack'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L459)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### import_ck_to_cm

  * CM CLI: ```cm import_ck_to_cm repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L562))
  * CM CLI with UID: ```cm import_ck_to_cm repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L562))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'import_ck_to_cm'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L562)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### convert_ck_to_cm

  * CM CLI: ```cm convert_ck_to_cm repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L613))
  * CM CLI with UID: ```cm convert_ck_to_cm repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L613))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'convert_ck_to_cm'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L613)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### detect

  * CM CLI: ```cm detect repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L667))
  * CM CLI with UID: ```cm detect repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L667))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'detect'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L667)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)