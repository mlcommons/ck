# Prototyping phase

## DEV
   - added "-tags" in search function
   - improved "--help" option for common automations
   - enhanced common "update" function (replace tags)

## V0.7.12
   - added "utils.sub_input"
   - added "cfg['artifact_keys']" to make it easier to create sub-inputs 
     to search for artifacts from original input

## V0.7.11
   - described CM env variables in the docs (#224)
   - moved "get_host_os_info" from CM core utils to CM automation "utils"
     to keep CM core small and simple
   - added "utils.load_python_module" function to customize
     intelligent components
   - added "utils.update_dict_if_empty" function to update
     the state in the intelligent component


## V0.7.10
   - added '\n' in save_json
   - fixed minor bug in the "find" function (when searching in the root directory of a CK repo)
   - fixed bug when pulling new repo with prefix
   - added "gen_tmp_file" from CK to utils
   - added "get_host_os_info" from CK to utils to support new "intelligent components"
   - started prototyping "intelligent component"

## V0.7.9
   - documented all internal APIs
   - changed a few ambiguous internal and environment variables
   - moved new and unstable components for MLOps to octoml@cm-mlops
     for further prototyping

## V0.7.8
   - fixed bug when detecting repo in "internal" repo
   - added dummy automations for env, ic and docker: #220
   - added dummy automation experiment
   - added support to detect current repo in artifacts in CLI: "cm add automation .:mlperf"

## V0.7.7
   - added utils.get_current_date_time
   - added utils.assemble_cm_object1

## V0.7.6
   - added "cm move/rename": https://github.com/mlcommons/ck/issues/213 
   - adding "requirements.txt" when initializing new CM repositories: https://github.com/mlcommons/ck/issues/204
   - when "cm help {automation}" print path to the automation python module: https://github.com/mlcommons/ck/issues/218
   - print equivalent Collective DB actions: https://github.com/mlcommons/ck/issues/219
   - various minor enhancements and bug fixes

## V0.7.5
   - when updating artifact, if it doesn't exist, add it
   - fixed tags processing when adding CM artifacts
   - improved CLI (change - -> _ in keys to be more user friendly)
   - added "cm update" and fixed minor bugs with cm load/update
   - fixed problems with non-serializable keys when --out=json
   - fixed major bug with inheritance (_base)
   - fixed a bug in "cm search" when automation is created without UID
   - fixed a bug with @input.json
   - fixed minior bugs in a core


## V0.7.4
   - added support to detect repo, automation and artifact in a current directory 
     when using CM CLI:
     "cm search . --tags=..."
     "cm load ."
   - added "--out=json" to print automation action output in JSON format
   - do not wait until the end of search to print entries (otherwise may be slow)
   - treat uid and alias as case insensitive (the same on Linux and Windows)
   - fixed "cm init repo" - just import when repo description already exists
   - fixed bug with printing the same error recursively
   - major fix of search with wildcards
   - fixed repository handling (search, unpack, etc)
   - changed "cm status core" to "cm test core"
   - changed ambiguous "default" repo to "internal" repo
   - changed ambiguous "default_automation" to "common_automation"
   - changed ambiguous key "name" in "repo" automation to "desc"

## V0.7.3

   - moved "parsed_cli" from core module to cli module

## V0.7.2

   - Added "cm status"
   - Changed CM CLI to "cm action automation artifact(s) flags @input.yaml @input.json"
   - Added "cm help" and "cm {action} --help"
