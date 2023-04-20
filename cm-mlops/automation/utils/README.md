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

  * CM CLI: ```cm unzip_file utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L255))
  * CM CLI with UID: ```cm unzip_file utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L255))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'unzip_file'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L255)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### compare_versions

  * CM CLI: ```cm compare_versions utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L333))
  * CM CLI with UID: ```cm compare_versions utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L333))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'compare_versions'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L333)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### json2yaml

  * CM CLI: ```cm json2yaml utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L381))
  * CM CLI with UID: ```cm json2yaml utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L381))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'json2yaml'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L381)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### yaml2json

  * CM CLI: ```cm yaml2json utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L419))
  * CM CLI with UID: ```cm yaml2json utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L419))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'yaml2json'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L419)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### sort_json

  * CM CLI: ```cm sort_json utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L457))
  * CM CLI with UID: ```cm sort_json utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L457))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'sort_json'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L457)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### dos2unix

  * CM CLI: ```cm dos2unix utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L494))
  * CM CLI with UID: ```cm dos2unix utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L494))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'dos2unix'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L494)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### replace_string_in_file

  * CM CLI: ```cm replace_string_in_file utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L531))
  * CM CLI with UID: ```cm replace_string_in_file utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L531))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'replace_string_in_file'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L531)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### create_toc_from_md

  * CM CLI: ```cm create_toc_from_md utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L581))
  * CM CLI with UID: ```cm create_toc_from_md utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L581))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'create_toc_from_md'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L581)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### copy_to_clipboard

  * CM CLI: ```cm copy_to_clipboard utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L643))
  * CM CLI with UID: ```cm copy_to_clipboard utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L643))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'copy_to_clipboard'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L643)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)