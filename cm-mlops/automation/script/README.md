*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

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

  * CM CLI: ```cm version script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1749))
  * CM CLI with UID: ```cm version script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1749))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'version'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1749)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### search

  * CM CLI: ```cm search script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1777))
  * CM CLI with UID: ```cm search script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1777))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'search'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1777)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### test

  * CM CLI: ```cm test script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1887))
  * CM CLI with UID: ```cm test script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1887))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'test'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1887)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### native_run

  * CM CLI: ```cm native_run script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1953))
  * CM CLI with UID: ```cm native_run script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1953))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'native_run'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L1953)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### add

  * CM CLI: ```cm add script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2026))
  * CM CLI with UID: ```cm add script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2026))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'add'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2026)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### run_native_script

  * CM CLI: ```cm run_native_script script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2624))
  * CM CLI with UID: ```cm run_native_script script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2624))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'run_native_script'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2624)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### find_file_in_paths

  * CM CLI: ```cm find_file_in_paths script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2665))
  * CM CLI with UID: ```cm find_file_in_paths script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2665))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'find_file_in_paths'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2665)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### detect_version_using_script

  * CM CLI: ```cm detect_version_using_script script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2879))
  * CM CLI with UID: ```cm detect_version_using_script script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2879))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'detect_version_using_script'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2879)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### find_artifact

  * CM CLI: ```cm find_artifact script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2952))
  * CM CLI with UID: ```cm find_artifact script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2952))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'find_artifact'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L2952)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### find_file_deep

  * CM CLI: ```cm find_file_deep script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3110))
  * CM CLI with UID: ```cm find_file_deep script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3110))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'find_file_deep'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3110)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### find_file_back

  * CM CLI: ```cm find_file_back script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3168))
  * CM CLI with UID: ```cm find_file_back script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3168))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'find_file_back'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3168)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### parse_version

  * CM CLI: ```cm parse_version script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3209))
  * CM CLI with UID: ```cm parse_version script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3209))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'parse_version'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3209)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### update_deps

  * CM CLI: ```cm update_deps script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3263))
  * CM CLI with UID: ```cm update_deps script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3263))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'update_deps'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3263)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### get_default_path_list

  * CM CLI: ```cm get_default_path_list script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3282))
  * CM CLI with UID: ```cm get_default_path_list script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3282))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'get_default_path_list'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3282)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### doc

  * CM CLI: ```cm doc script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3293))
  * CM CLI with UID: ```cm doc script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3293))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'doc'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3293)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### dockerfile

  * CM CLI: ```cm dockerfile script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3322))
  * CM CLI with UID: ```cm dockerfile script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3322))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'dockerfile'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3322)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### docker

  * CM CLI: ```cm docker script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3350))
  * CM CLI with UID: ```cm docker script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3350))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'docker'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3350)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

#### prepare

  * CM CLI: ```cm prepare script``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3403))
  * CM CLI with UID: ```cm prepare script,5b4e0237da074764``` ([add flags (dict keys) from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3403))
  * CM Python API:
    ```python
    import cmind

    r=cm.access({
                 'action':'prepare'
                 'automation':'script,5b4e0237da074764'
                 'out':'con'
    ```
    [add keys from this API](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation/script/module.py#L3403)
    ```python
                })
    if r['return']>0:
        print(r['error'])
    ```

### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce)