# Prototyping phase

## Master
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
