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

  * CM CLI: ```cm search repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L98))
  * CM CLI with UID: ```cm search repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L98))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'search'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L98)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### where

  * CM CLI: ```cm where repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L184))
  * CM CLI with UID: ```cm where repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L184))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'where'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L184)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### update

  * CM CLI: ```cm update repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L207))
  * CM CLI with UID: ```cm update repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L207))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'update'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L207)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### delete

  * CM CLI: ```cm delete repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L244))
  * CM CLI with UID: ```cm delete repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L244))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'delete'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L244)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### init

  * CM CLI: ```cm init repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L301))
  * CM CLI with UID: ```cm init repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L301))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'init'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L301)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### add

  * CM CLI: ```cm add repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L426))
  * CM CLI with UID: ```cm add repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L426))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'add'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L426)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### pack

  * CM CLI: ```cm pack repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L434))
  * CM CLI with UID: ```cm pack repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L434))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'pack'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L434)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### unpack

  * CM CLI: ```cm unpack repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L504))
  * CM CLI with UID: ```cm unpack repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L504))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'unpack'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L504)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### import_ck_to_cm

  * CM CLI: ```cm import_ck_to_cm repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L611))
  * CM CLI with UID: ```cm import_ck_to_cm repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L611))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'import_ck_to_cm'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L611)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### convert_ck_to_cm

  * CM CLI: ```cm convert_ck_to_cm repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L662))
  * CM CLI with UID: ```cm convert_ck_to_cm repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L662))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'convert_ck_to_cm'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L662)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### detect

  * CM CLI: ```cm detect repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L716))
  * CM CLI with UID: ```cm detect repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L716))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'detect'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L716)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### reindex

  * CM CLI: ```cm reindex repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L899))
  * CM CLI with UID: ```cm reindex repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L899))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'reindex'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L899)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)