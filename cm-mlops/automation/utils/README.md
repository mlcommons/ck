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

  * CM CLI: ```cm unzip_file utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L265))
  * CM CLI with UID: ```cm unzip_file utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L265))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'unzip_file'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L265)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### compare_versions

  * CM CLI: ```cm compare_versions utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L343))
  * CM CLI with UID: ```cm compare_versions utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L343))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'compare_versions'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L343)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### json2yaml

  * CM CLI: ```cm json2yaml utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L391))
  * CM CLI with UID: ```cm json2yaml utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L391))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'json2yaml'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L391)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### yaml2json

  * CM CLI: ```cm yaml2json utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L429))
  * CM CLI with UID: ```cm yaml2json utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L429))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'yaml2json'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L429)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### sort_json

  * CM CLI: ```cm sort_json utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L467))
  * CM CLI with UID: ```cm sort_json utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L467))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'sort_json'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L467)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### dos2unix

  * CM CLI: ```cm dos2unix utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L504))
  * CM CLI with UID: ```cm dos2unix utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L504))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'dos2unix'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L504)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### replace_string_in_file

  * CM CLI: ```cm replace_string_in_file utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L541))
  * CM CLI with UID: ```cm replace_string_in_file utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L541))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'replace_string_in_file'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L541)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### create_toc_from_md

  * CM CLI: ```cm create_toc_from_md utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L591))
  * CM CLI with UID: ```cm create_toc_from_md utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L591))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'create_toc_from_md'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L591)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### copy_to_clipboard

  * CM CLI: ```cm copy_to_clipboard utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L659))
  * CM CLI with UID: ```cm copy_to_clipboard utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L659))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'copy_to_clipboard'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L659)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### list_files_recursively

  * CM CLI: ```cm list_files_recursively utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L737))
  * CM CLI with UID: ```cm list_files_recursively utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L737))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'list_files_recursively'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L737)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### generate_secret

  * CM CLI: ```cm generate_secret utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L770))
  * CM CLI with UID: ```cm generate_secret utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L770))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'generate_secret'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L770)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### detect_tags_in_artifact

  * CM CLI: ```cm detect_tags_in_artifact utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L793))
  * CM CLI with UID: ```cm detect_tags_in_artifact utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L793))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'detect_tags_in_artifact'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L793)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### prune_input

  * CM CLI: ```cm prune_input utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L822))
  * CM CLI with UID: ```cm prune_input utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L822))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'prune_input'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L822)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### uid

  * CM CLI: ```cm uid utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L864))
  * CM CLI with UID: ```cm uid utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L864))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'uid'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L864)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### system

  * CM CLI: ```cm system utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L891))
  * CM CLI with UID: ```cm system utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L891))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'system'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L891)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### load_cfg

  * CM CLI: ```cm load_cfg utils``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L969))
  * CM CLI with UID: ```cm load_cfg utils,dc2743f8450541e3``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L969))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'load_cfg'
                 'automation':'utils,dc2743f8450541e3'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/utils/module.py#L969)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce)