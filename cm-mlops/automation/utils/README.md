*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

### Automation actions

#### test

  * CM CLI: ```cm test utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L15))
  * CM CLI with UID: ```cm test utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L15))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'test'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L15)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### get_host_os_info

  * CM CLI: ```cm get_host_os_info utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L54))
  * CM CLI with UID: ```cm get_host_os_info utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L54))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'get_host_os_info'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L54)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### download_file

  * CM CLI: ```cm download_file utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L156))
  * CM CLI with UID: ```cm download_file utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L156))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'download_file'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L156)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### unzip_file

  * CM CLI: ```cm unzip_file utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L256))
  * CM CLI with UID: ```cm unzip_file utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L256))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'unzip_file'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L256)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### compare_versions

  * CM CLI: ```cm compare_versions utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L334))
  * CM CLI with UID: ```cm compare_versions utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L334))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'compare_versions'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L334)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### json2yaml

  * CM CLI: ```cm json2yaml utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L382))
  * CM CLI with UID: ```cm json2yaml utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L382))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'json2yaml'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L382)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### yaml2json

  * CM CLI: ```cm yaml2json utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L420))
  * CM CLI with UID: ```cm yaml2json utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L420))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'yaml2json'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L420)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### sort_json

  * CM CLI: ```cm sort_json utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L458))
  * CM CLI with UID: ```cm sort_json utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L458))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'sort_json'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L458)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### dos2unix

  * CM CLI: ```cm dos2unix utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L495))
  * CM CLI with UID: ```cm dos2unix utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L495))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'dos2unix'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L495)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### replace_string_in_file

  * CM CLI: ```cm replace_string_in_file utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L532))
  * CM CLI with UID: ```cm replace_string_in_file utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L532))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'replace_string_in_file'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L532)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### create_toc_from_md

  * CM CLI: ```cm create_toc_from_md utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L582))
  * CM CLI with UID: ```cm create_toc_from_md utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L582))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'create_toc_from_md'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L582)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### copy_to_clipboard

  * CM CLI: ```cm copy_to_clipboard utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L644))
  * CM CLI with UID: ```cm copy_to_clipboard utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L644))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'copy_to_clipboard'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L644)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### list_files_recursively

  * CM CLI: ```cm list_files_recursively utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L722))
  * CM CLI with UID: ```cm list_files_recursively utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L722))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'list_files_recursively'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L722)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce)