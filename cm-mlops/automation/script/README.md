*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

### Automation actions

#### run

  * CM CLI: ```cm run script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L72))
  * CM CLI with UID: ```cm run script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L72))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'run'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L72)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### version

  * CM CLI: ```cm version script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1552))
  * CM CLI with UID: ```cm version script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1552))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'version'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1552)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### search

  * CM CLI: ```cm search script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1580))
  * CM CLI with UID: ```cm search script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1580))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'search'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1580)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### test

  * CM CLI: ```cm test script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1658))
  * CM CLI with UID: ```cm test script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1658))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'test'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1658)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### add

  * CM CLI: ```cm add script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1723))
  * CM CLI with UID: ```cm add script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1723))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'add'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1723)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### run_native_script

  * CM CLI: ```cm run_native_script script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2107))
  * CM CLI with UID: ```cm run_native_script script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2107))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'run_native_script'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2107)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### find_file_in_paths

  * CM CLI: ```cm find_file_in_paths script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2148))
  * CM CLI with UID: ```cm find_file_in_paths script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2148))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'find_file_in_paths'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2148)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### detect_version_using_script

  * CM CLI: ```cm detect_version_using_script script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2362))
  * CM CLI with UID: ```cm detect_version_using_script script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2362))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'detect_version_using_script'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2362)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### find_artifact

  * CM CLI: ```cm find_artifact script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2435))
  * CM CLI with UID: ```cm find_artifact script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2435))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'find_artifact'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2435)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### find_file_deep

  * CM CLI: ```cm find_file_deep script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2593))
  * CM CLI with UID: ```cm find_file_deep script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2593))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'find_file_deep'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2593)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### find_file_back

  * CM CLI: ```cm find_file_back script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2651))
  * CM CLI with UID: ```cm find_file_back script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2651))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'find_file_back'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2651)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### parse_version

  * CM CLI: ```cm parse_version script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2692))
  * CM CLI with UID: ```cm parse_version script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2692))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'parse_version'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2692)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### update_deps

  * CM CLI: ```cm update_deps script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2746))
  * CM CLI with UID: ```cm update_deps script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2746))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'update_deps'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2746)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### get_default_path_list

  * CM CLI: ```cm get_default_path_list script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2765))
  * CM CLI with UID: ```cm get_default_path_list script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2765))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'get_default_path_list'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2765)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### doc

  * CM CLI: ```cm doc script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2776))
  * CM CLI with UID: ```cm doc script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2776))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'doc'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2776)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)