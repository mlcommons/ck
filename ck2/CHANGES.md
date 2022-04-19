# Prototyping phase

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
