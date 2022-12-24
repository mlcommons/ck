# This test covers version, variation, compilation from src, add_deps, add_deps_recursive, deps, post_deps

import cmind as cm
import check as checks

r = cm.access({'action':'run', 'automation':'script', 'tags': 'generate-run-cmds,mlperf', 'adr':
    {'loadgen': {'version': 'r2.1'}, 'compiler': {'tags': "gcc"}}, 'env': {'CM_MODEL': 'resnet50',
        'CM_DEVICE': 'cpu', 'CM_BACKEND': 'onnxruntime'}, 'quiet': 'yes'})
checks.check_return(r)

r = cm.access({'action':'search', 'automation': 'cache', 'tags': 'loadgen,version-r2.1,deps-python-non-virtual'})
checks.check_list(r, "loadgen,version-r2.1,deps-python-non-virtual")

r = cm.access({'action':'search', 'automation': 'cache', 'tags': 'inference,src,version-r2.1'})
checks.check_list(r, "inference,src,version-r2.1")

r = cm.access({'action':'run', 'automation':'script', 'tags': 'app,mlperf,inference,generic,_python,_resnet50,_onnxruntime,_cpu,_r2.1_default', 'quiet': 'yes'})
checks.check_return(r)

r = cm.access({'action':'run', 'automation':'script', 'tags': 'app,mlperf,inference,generic,_python,_resnet50,_tf,_cpu,_r2.1_default', 'quiet': 'yes'})
checks.check_return(r)
