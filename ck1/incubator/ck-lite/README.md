# CK Lite aka CK2

Based on user feedback, we plan to redesign the CK framework making it lighter, simpler and more pythonic.

Feel free to contribute and discuss it via [open tickets](https://github.com/mlcommons/ck/issues)! Thank you for supporting this community project!

Ideas:
* separate CK database (CK repo) and automation actions
* make a simple structure for CK database without too many .cm directories ...
* separate CK modules from CK core and share them via PyPI
  * that should help to better handle dependencies between CK modules
  * we could also use CK modules as standar Python packages
* improve CK CLI
  * add a possibility to enter lists and dictionaries from CMD
* start standardizing modules APIs and meta descriptions with the community
* drop Python 2 support to simplify the core functionality 
  * lots of effort was made to ensure compatibility between Python 2 and 3
    (ck.out functions instead of print, etc). That is not needed 
    if we drop Python 2 support.
* provide more tests for CK workflows
* simplify and standardize CK platform, env, soft, package, program, experiment modules

* enable inheritance in entries inside the CK core 
  * via dict key "_inherit":"entry"
  * or via inherit.json/inherit.yaml ?

More to come soon ;) ...
