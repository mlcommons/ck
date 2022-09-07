# This test covers version, variation, compilation from src, add_deps_recursive, post_deps

import cmind as cm

r = cm.access({'action':'run', 'automation':'script', 'tags': 'run,docker,container', 'add_deps_recursive':
    {'compiler': {'tags': "gcc"}}, 'env': {'CM_DOCKER_RUN_SCRIPT_TAGS': 'app,image-classification,onnx,python',
        'CM_MLOPS_REPO': 'octoml@ck', 'CM_DOCKER_IMAGE_BASE': 'ubuntu:22.04'}, 'quiet': 'yes'})
if 'return' not in r:
    raise Exception('CM access function should always return key \'return\'!')
if 'error' in r:
    raise Exception(r['error'])
