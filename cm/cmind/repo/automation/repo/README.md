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

#### update

  * CM CLI: ```cm update repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L177))
  * CM CLI with UID: ```cm update repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L177))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'update'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L177)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### delete

  * CM CLI: ```cm delete repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L214))
  * CM CLI with UID: ```cm delete repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L214))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'delete'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L214)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### init

  * CM CLI: ```cm init repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L271))
  * CM CLI with UID: ```cm init repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L271))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'init'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L271)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### add

  * CM CLI: ```cm add repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L395))
  * CM CLI with UID: ```cm add repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L395))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'add'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L395)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### pack

  * CM CLI: ```cm pack repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L403))
  * CM CLI with UID: ```cm pack repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L403))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'pack'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L403)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### unpack

  * CM CLI: ```cm unpack repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L473))
  * CM CLI with UID: ```cm unpack repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L473))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'unpack'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L473)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### import_ck_to_cm

  * CM CLI: ```cm import_ck_to_cm repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L580))
  * CM CLI with UID: ```cm import_ck_to_cm repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L580))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'import_ck_to_cm'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L580)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### convert_ck_to_cm

  * CM CLI: ```cm convert_ck_to_cm repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L631))
  * CM CLI with UID: ```cm convert_ck_to_cm repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L631))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'convert_ck_to_cm'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L631)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### detect

  * CM CLI: ```cm detect repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L685))
  * CM CLI with UID: ```cm detect repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L685))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'detect'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L685)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### reindex

  * CM CLI: ```cm reindex repo``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L872))
  * CM CLI with UID: ```cm reindex repo,55c3e27e8a140e48``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L872))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'reindex'
                 'automation':'repo,55c3e27e8a140e48'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm/cmind/repo/automation/repo/module.py#L872)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce)