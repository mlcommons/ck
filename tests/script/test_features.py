# This test covers python-virtual-env and update_deps inside customize.py

import cmind as cm
import check as checks

r = cm.access({'action':'run', 'automation':'script', 'tags': 'install,python-venv', 'env': {'CM_NAME': 'test'}, 'quiet': 'yes'})
checks.check_return(r)
r = cm.access({'action':'search', 'automation': 'cache', 'tags': 'get,python-venv-test'})
checks.check_list(r, "get,python-venv")
