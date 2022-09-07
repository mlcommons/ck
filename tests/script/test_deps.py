# This test covers version, variation, compilation from src, add_deps_recursive, post_deps
try:
    import cmind as cm

    r = cm.access({'action':'run', 'automation':'script', 'tags': 'generate-run-cmds,mlperf', 'add_deps_recursive':
        {'inference-src': {'tags': '_octoml'}, 'loadgen': {'version': 'r2.1'}, 'compiler': {'tags': "gcc"}}, 'env': {'CM_MODEL': 'resnet50',
            'CM_DEVICE': 'cpu', 'CM_BACKEND': 'onnxruntime'}, 'quiet': 'yes'})
    if 'return' not in r:
        raise Exception('CM access function should always return key \'return\'!')
    if 'error' in r:
        raise Exception(r['error'])
    
    exit(0)

except ImportError as e:
    from sys import stderr
    print('CM module for python is not installed', file=stderr)
    exit(1)
