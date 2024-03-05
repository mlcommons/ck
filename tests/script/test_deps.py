# This test covers version, variation, compilation from src, add_deps, add_deps_recursive, deps, post_deps

import cmind as cm
import check as checks

# MLPerf v3.0 inference is now very outdated and we are testing inference in separate tests

#r = cm.access({'action':'run', 'automation':'script', 'tags': 'generate-run-cmds,mlperf', 'adr':
#    {'loadgen': {'version': 'r3.0'}, 'compiler': {'tags': "gcc"}}, 'env': {'CM_MODEL': 'resnet50',
#        'CM_DEVICE': 'cpu', 'CM_BACKEND': 'onnxruntime'}, 'quiet': 'yes'})
#checks.check_return(r)
#
#r = cm.access({'action':'search', 'automation': 'cache', 'tags': 'loadgen,version-r3.0,deps-python-non-virtual'})
#checks.check_list(r, "loadgen,version-r3.0,deps-python-non-virtual")
#
#r = cm.access({'action':'search', 'automation': 'cache', 'tags': 'inference,src,version-r3.0'})
#checks.check_list(r, "inference,src,version-r3.0")
#
#r = cm.access({'action':'run', 'automation':'script', 'tags': 'app,mlperf,inference,generic,_python,_resnet50,_onnxruntime,_cpu,_r3.0_default', 'adr': {'mlperf-implementation': { 'version': 'master'}}, 'quiet': 'yes'})
#checks.check_return(r)
#
#r = cm.access({'action':'run', 'automation':'script', 'tags': 'app,mlperf,inference,generic,_python,_resnet50,_tf,_cpu,_r3.0_default', 'adr': {'mlperf-implementation': { 'version': 'master'}}, 'quiet': 'yes'})
#checks.check_return(r)
