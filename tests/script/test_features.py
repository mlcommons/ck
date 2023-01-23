# This test covers
# 1. python-virtual-env and update_deps inside customize.py
# 2. cache search using "-" prefix

import cmind as cm
import check as checks

r = cm.access({'action':'run', 'automation':'script', 'tags': 'install,python-venv', 'name':'test', 'quiet': 'yes'})
checks.check_return(r)

r = cm.access({'action':'search', 'automation': 'cache', 'tags': 'get,python,virtual,name-test'})
checks.check_list(r, "get,python-venv")

r = cm.access({'action':'run', 'automation':'script', 'tags': 'get,dataset,preprocessed,imagenet,_NHWC', 'quiet': 'yes'})
checks.check_return(r)

r = cm.access({'action':'search', 'automation': 'cache', 'tags': 'get,dataset,preprocessed,imagenet,-_NCHW'})
checks.check_list(r, "_NHWC")

r = cm.access({'action':'search', 'automation': 'cache', 'tags': 'get,dataset,preprocessed,imagenet,-_NHWC'})
checks.check_list(r, "_NHWC", False)
