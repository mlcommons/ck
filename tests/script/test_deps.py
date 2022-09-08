# This test covers version, variation, compilation from src, add_deps, add_deps_recursive, deps, post_deps

import cmind as cm

def check_return(r):
    if 'return' not in r:
        raise Exception('CM access function should always return key \'return\'!')
    if 'error' in r:
        raise Exception(r['error'])

def check_list(r, str):
    check_return(r)
    if 'list' not in r:
        raise Exception('CM search should return a list!')
    if len(r['list']) < 1:
        raise Exception('CM search returned an empty list for ' + str)

r = cm.access({'action':'run', 'automation':'script', 'tags': 'generate-run-cmds,mlperf', 'add_deps_recursive':
    {'inference-src': {'tags': '_octoml'}, 'loadgen': {'version': 'r2.1'}, 'compiler': {'tags': "gcc"}}, 'env': {'CM_MODEL': 'resnet50',
        'CM_DEVICE': 'cpu', 'CM_BACKEND': 'onnxruntime'}, 'quiet': 'yes'})
check_return(r)

r = cm.access({'action':'search', 'automation': 'cache', 'tags': 'loadgen,version-r2.1,deps-python-non-virtual'})
check_list(r, "loadgen,version-r2.1,deps-python-non-virtual")

r = cm.access({'action':'search', 'automation': 'cache', 'tags': 'inference,src,version-r2.1'})
check_list(r, "inference,src,version-r2.1")

r = cm.access({'action':'run', 'automation':'script', 'tags': 'app,mlperf,inference,_resnet50,_onnxruntime,_cpu,_r2.1_default', 'quiet': 'yes'})
check_return(r)
