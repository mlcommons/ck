*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

### Automation actions

#### run

  * CM CLI: ```cm run script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L77))
  * CM CLI with UID: ```cm run script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L77))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'run'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L77)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### version

  * CM CLI: ```cm version script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2199))
  * CM CLI with UID: ```cm version script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2199))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'version'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2199)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### search

  * CM CLI: ```cm search script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2227))
  * CM CLI with UID: ```cm search script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2227))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'search'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2227)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### test

  * CM CLI: ```cm test script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2346))
  * CM CLI with UID: ```cm test script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2346))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'test'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2346)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### native_run

  * CM CLI: ```cm native_run script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2412))
  * CM CLI with UID: ```cm native_run script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2412))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'native_run'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2412)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### add

  * CM CLI: ```cm add script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2485))
  * CM CLI with UID: ```cm add script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2485))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'add'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L2485)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### run_native_script

  * CM CLI: ```cm run_native_script script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3270))
  * CM CLI with UID: ```cm run_native_script script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3270))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'run_native_script'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3270)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### find_file_in_paths

  * CM CLI: ```cm find_file_in_paths script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3314))
  * CM CLI with UID: ```cm find_file_in_paths script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3314))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'find_file_in_paths'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3314)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### detect_version_using_script

  * CM CLI: ```cm detect_version_using_script script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3533))
  * CM CLI with UID: ```cm detect_version_using_script script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3533))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'detect_version_using_script'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3533)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### find_artifact

  * CM CLI: ```cm find_artifact script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3606))
  * CM CLI with UID: ```cm find_artifact script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3606))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'find_artifact'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3606)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### find_file_deep

  * CM CLI: ```cm find_file_deep script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3764))
  * CM CLI with UID: ```cm find_file_deep script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3764))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'find_file_deep'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3764)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### find_file_back

  * CM CLI: ```cm find_file_back script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3822))
  * CM CLI with UID: ```cm find_file_back script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3822))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'find_file_back'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3822)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### parse_version

  * CM CLI: ```cm parse_version script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3863))
  * CM CLI with UID: ```cm parse_version script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3863))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'parse_version'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3863)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### update_deps

  * CM CLI: ```cm update_deps script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3917))
  * CM CLI with UID: ```cm update_deps script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3917))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'update_deps'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3917)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### get_default_path_list

  * CM CLI: ```cm get_default_path_list script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3937))
  * CM CLI with UID: ```cm get_default_path_list script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3937))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'get_default_path_list'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3937)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### doc

  * CM CLI: ```cm doc script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3948))
  * CM CLI with UID: ```cm doc script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3948))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'doc'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3948)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### gui

  * CM CLI: ```cm gui script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3976))
  * CM CLI with UID: ```cm gui script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3976))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'gui'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L3976)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### dockerfile

  * CM CLI: ```cm dockerfile script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L4013))
  * CM CLI with UID: ```cm dockerfile script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L4013))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'dockerfile'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L4013)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### docker

  * CM CLI: ```cm docker script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L4041))
  * CM CLI with UID: ```cm docker script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L4041))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'docker'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L4041)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### prepare

  * CM CLI: ```cm prepare script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L4095))
  * CM CLI with UID: ```cm prepare script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L4095))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'prepare'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L4095)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### clean_some_tmp_files

  * CM CLI: ```cm clean_some_tmp_files script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L4106))
  * CM CLI with UID: ```cm clean_some_tmp_files script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L4106))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'clean_some_tmp_files'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/cm4mlops/tree/master/automation/script/module.py#L4106)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce)