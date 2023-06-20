## V1.4.1
   - added cme binary as a shortcut for "cm run experiment"

## V1.4.0
   - added cmr binary as a shortcut for "cm run script"
   - fixed minor bug with repo/automation/artifact detection in the current path with "."
   - various improvements in CM-MLOps repository to support TinyMLPerf

## V1.3.0
   - Turned on artifact indexing by default 
     (can be turned off by setting CM_INDEX to "no", "off" or "false")
   - Turned on --silent mode in "cm run script" by default
     Can be turned off via --verbose or -v flags
   - Fixed duplicate version detection for Python packages
   - added --new_tags for "cm copy" to add new tags to newly created artifacts
   - added --new_tags for "cm add" to add new tags to newly created artifacts
   - added basic check for forbidden artifact names such as "."

## V1.2.2
   - Fixed minor bug during cm detect repo (turn off indexing)

## V1.2.1
   - Fixed Bug in indexing (avoiding duplicate entries when wildcards are used)

## V1.2.0
   - Major update: transparent indexing of all artifacts 
     to speed up search and scripts by ~10..50x
     (off by default for further testing: use ENV CM_INDEX=yes|on|true to turn it on)

## V1.1.6
   - added "cm print_input automation"
   - updated link to the MLCommons taskforce on automation and reproducibility

## V1.1.5
   - added support for CLI with -- {something} . Everything after -- will be available 
     in the CM input dictionary under "unparsed_cmd" key (list).
     We need it to support universal experiments in CM:
     cm run experiment -- {any script with any command line}

## V1.1.4
   - added utils.call_internal_module to break automation modules into sub-modules

## V1.1.3
   - improved removal of CM entries on Windows
   - fixed https://github.com/mlcommons/ck/issues/574
   - improved detection of CM entries with "."
   - added --yaml option in "cm add" to save meta in YAML

## V1.1.2
   - added --save_to_json to save output to JSON (useful for web services)
   - extended "cm info {automation} {artifact}" (copy to clipboard)

## V1.1.1
   - added --checkout and --branch to "cm pull repo' for more determinism and reproducibility
   - detect if repository and its forks already exist during "cm pull repo" (#397)
   - support = inside argument of a key (--key="x=y") (#453)

## V1.0.5
   - redesigned documentation
   - added support utils to generate lists of all automations and scripts
   - '\r' is removed on Windows when writing files with meta information (json or yaml)

## V1.0.4
   - minor fix in reporting errors
   - we now do not overwrite repo alias in .cmr.yaml when pulling forks to avoid ambiguities

## V1.0.3
   - minor fix to properly self-reference running automation script

## V1.0.2
   - updated and simplified all docs

## V1.0.1
   - fixed links in PYPI docs

## V1.0.0
   - Prepared [public workgroup](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md) 
     to continue CM developments to modularize ML Systems and automate their benchmarking using the MLPerf methodology
     as a community effort!
   - Added multiple tests for CM core, scripts and "automation" script features: https://github.com/mlcommons/ck/actions
   - Extended "cm info artifact"
   - Added support to copy CID of a given CM artifact to a clipboard (cm info {artifact})
   - Updated docs and tutorials for V1.0.0 release!

# Prototyping phase

## V0.7.24
   - added link to GitHub repo with CM automation scripts

## V0.7.23
   - handle errors when loading artifact meta
   - added text output when can't detect tool version

## V0.7.22
   - Added "cm info" to print various info about artifacts
   - Fixed bug with printing help for actions when they are substituted (rm -> delete)
   - Added utils.filter_tags to filter tags starting from "-" (used in artifact add and update)
   - Added tags filter to "cm add" and "cm update"

## V0.7.21
   - fixed bug in "cm move" when moving to a repository with a prefix
   - redirect "cm version" to "cm version core"
   - redirect "cm --version" to "cm version core"

## V0.7.20
   - fixed bugs in the old "utils.list_all_files" function

## V0.7.19
   - fixed "cm copy" when copying to a repository with a prefix
   - fixed "cm copy" and "cm ren" if target artifact already exists

## V0.7.18
   - fixed bug with python_version

## V0.7.17
   - removed FullLoader from yaml load to be compatible with older Python versions
   - added cm copy & cm cp
   - added python_version to CM class to make automations more portable
   - fixed minor bug with target repo in "cm move"/"cm ren"/"cm mv"

## V0.7.16
   - fixed --help when no automation is specified 
     (to print help for the default CM database automation)
   - fixed "cm update" function (added --search-tags 
     and changed --new-tags back to tags)

## V0.7.15
   - fail by default if automation is not found
     (can be changed using cmind.cfg['fail_if_automation_not_found']=False)
   - fixed "cm update" function (added --new-tags to separate from search tags)
   - report error if automation is not defined or found

## V0.7.14
   - fixed search function when tags == ''
   - fixed cm access when automation == '' and tags!=''

## V0.7.13
   - added "-tags" in search function
   - improved "--help" option for common automations
   - enhanced common "update" function (replace tags)
   - added "utils.convert_env_to_dict" to support intelligent components
   - extended "utils.load_text" to split strings and detect versions
   - fixed bug with "no_tags" in search function

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
