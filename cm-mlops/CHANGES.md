Since March 2023, all updates to CM automations are submitted via PRs.
You can follow our PRs at
* https://github.com/ctuning/mlcommons-ck/commits/master
* https://github.com/mlcommons/ck/pulls?q=is%3Apr+is%3Aclosed .

---

### 20230214
 * experiment and graph gui are working now

### 20230206:
 * started prototyping cm run experiment

### 20230123:
 * added simple GUI to CM scripts

### 20221206:
 * added "script_name" to the CM "script" meta to specify any native script name
 * added "--script_name" to "cm add script {alias} --script_name=my-native-script.sh"

### 20221206:
 * added CM_SCRIPT_EXTRA_CMD to force some flags to all scripts

### 20221202:
 * major updates for Windows (CL, CUDA, etc)

### 20221111:
 * various fixes for Student Cluster Competition at SuperComputing'22

### 20221110:
 * added support to push MLPerf results to W&B dashboard

### 20221103:
 * added "cm json2yaml utils" and "cm yaml2json utils"

### 20221024:
 * added --verbose and --time to "cm run script"

### 20221017:
 * removed the need for echo-off script

### 20221010:
 * added cm run script --debug-script-tags to run cmd/bash before native script
 * added cm run script --shell to set env and run shell after script execution

* 20221007:
 * added script template (used when adding new scripts)
 * major clean up of all scripts

### 20220916:
 * treat alias as tags if spaces: 
   cm run script "get compiler" is converted to cm run script --tags=get,compiler
 * improved gcc detection
 * refactored "cm run script" to skip deps in cache if needed

### 20220906
 * added --print_env flag to "cm run script" to print aggregated env
   before running native scripts
 * various fixes to support MLPerf automation

### 20220823
 * various fixes for universal MLPerf inference submission automation

### 20220803
 * various fixes for TVM and image classification

### 20220802
 * added "run_script_after_post_deps" to script meta to run script after post deps
   (useful to activate python virtual env)
 * added "activate-python-venv" script to make it easier to debug Python deps installation

### 20220722
 * added --accept-license and --skip-system-deps 
   (converted to env CM_ACCEPT_LICENSE ("True") and CM_SKIP_SYSTEM_DEPS ("True"))

### 20220719
 * moved relatively stable MLOps automation scripts here

### 20220718
 * fixed local_env_keys in get-python3
 * added new_env_only_keys to meta to specify which env to keep
 * fixed problem with adding tags from the selected script during caching
 * added --skip-compile and --skip-run to script (converted to env CM_SKIP_COMPILE and CM_SKIP_RUN)
 * fixed local_env_keys in get-python3
 * added new_env_only_keys to get-python3

### 20220713
 * added local_env_keys to meta
 * added "env" dict to os_info

### 20220712
 * major script refactoring to support cache tags update from deps
 * fixed version min/max propagations in deps
 * improvements to support tags from deps
 * added tags from deps (python, llvm)

### 20220708
 * various fixes to handle versions (min/max/default)
 * various fixes to avoid contamination of ENV from other scripts
 * various fixes to handle versions (min/max/default)

### 20220705
 * fixes for remembered selections
 * added --skip-remembered-selections to "cm run script"

### 20220704
 * fixed a bug with searching for scripts with variations
 * added the possibility to update deps from pre/post processing
 * added --extra-cache-tags and --name for "cm run script"
 * added prototype of selection caching
 * fixed get-python-venv

### 20220701
 * added dummy "cm test script"
 * added "--env" to "cm show cache" to show env and state
 * added "cm show cache"

### 20220629
 * added "detect_version_using_script" in script used to detect python packages
 * major fix to properly support multiple scripts with the same tags, caching, selection, etc
 * fixed a bug in version comparison (converting string to int)
 * added recording of "version" to cache meta

### 20220628
 * fixed local_env with deps

### 20220623
 * important update of versions logic

### 20220621
 * added support for --quiet
 * changed CM_NEED_VERSION to CM_VERSION
 * added CM_VERSION_MIN, CM_VERSION_MAX
 * added cm compare_versions utils --version1=... --version2=...
 * added support to detect min/max/correct versions

### 20220617
 * fixed logic to handle variations (-_): https://github.com/mlcommons/ck/issues/243

### 20220616
 * changed "cached" to "cache" automation

### 20220615
 * major update of script (remove parallel env/new_env and state/new_state).
   keep global env & state and detect changes automatically
 * major simplification of "script"
 * removed "installed" to be more understandable
 * added "cached" to be more understandable

### 20220609
 * added "versions" key to the CM script meta
   it works similar to "variations" and is forced by --version
 * changed "ic" to "script" in "experiment" automation

### 20220608
 * updated "variations" logic in "script"!
   meta['default_variation'] (str): only one of many
   meta['default_variations'] (list): multiple choices
 * deprecated "ic" automation. Use "script" instead!

### 20220607
 * added strip_folders to utils/unzip_file
 * fixed minor bugs in CM script

### 20220606
 * added "name" key to deps (list of names and UIDs)
 * added "add_deps_tags" in variations and in CMD ({"name":"tag(s)"})
 * added "deps" to variations to be merged with the list of current deps
 * added --input and --output for cm run script converted to env CM_INPUT and CM_OUTPUT
   useful to create interactive CM scripts to process files
 * Added prototype-test-deps-variations-tags to play with deps, variations, tags

### 20220605
 * clean tmp files in "script" automation by default and keep them using --dirty flag

### 20220603
 * added "skip" and "deps" to postprocess to call other scripts.
   For example call install LLVM if detect LLVM fails...
 * added "script" automation to substitute less intuitive "ic"
 * Improved LLVM detection and installation
 * Added example of image corner detection
 * Added updated script entries

### 20220601
 * added version, path, skip_install and post_deps to IC 
 * added --new to IC to detect new components
 * Updating mechanisms to install and/or detect LLVM
 * added support to install prebuilt LLVM for Linux, MacOs, Windows

### 20220530
 * updated ic automation to read tmp-run-state.json 
   and merge it with the "new_state" dict

### 20220524
 * changed directory ck2-repo-mlops to cm-devops

### 20220517
 * Changed CM_PATH_LIST to +PATH
 * Added general support for +ENV that is expanded to ENV=val1;val2;...:${ENV}

### 20220511
 * Better handle exceptions in utils.download_file
 * Added support for variations in intelligent components (ic)
 * Fixed bugs in IC
 * Added "_" prefix in tags to specify variation of IC
 * Record env.sh in "installed artifacts even if bat file is not executed
 * Fixed experiment directory naming on Windows
 * Added "cm version ic" (#233)
 * Added prototype of ic::prototype-get-ml-model-resnet50-onnx with variations
 * Added prototype of ic::prototype-get-imagenet-val with variations
 * Added prototype of ic::prototype-get-imagenet-aux with variations
 * Added prototype of ic::prototype-get-llvm
 * Added prototype of ic::prototype-get-tvm
