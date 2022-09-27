**[ [TOC](../README.md) ]**

# Ideas to improve CK

Developing backwards compatible CK2 based on our collective experience:

* simple and pythonic access to CK repos as a database (separate from actions)
* simplify CK repo structure to avoid numerous .cm directories. Use cm.json file with UID and then reindex components when pulling repo or adding/deleting entries
* implement CK actions/modules as standard Python packages with dependencies that can be installed via PIP (to ensure stability and testing)
* simplify modules program+platform with a "workflow" module that resolves all dependencies (platform+scripts+pip requirements become a part of it), 
  take env as input, run script, modifies env, and produce output - unified CK LEGO bricks
  * host/traget platform become a package rather than current separate entity - much easier to extend and provide deps!
* improve DSE + autotuner based on exposed env vars + packages + deps

