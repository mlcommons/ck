# This test covers script installation, version, shared library install

import cmind as cm
import check as checks

r = cm.access({'action':'run', 'automation':'script', 'tags': 'python,src,install,_shared', 'version': '3.9.10', 'quiet': 'true'})
checks.check_return(r)

r = cm.access({'action':'search', 'automation':'cache', 'tags': 'python,src,install,_shared,version-3.9.10'})
checks.check_list(r, "python,src,install,_shared,version-3.9.10")
