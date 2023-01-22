# This test covers version, variation, compilation from src, add_deps, add_deps_recursive, deps, post_deps

import cmind as cm
import check as checks

r = cm.access({'action':'run', 'automation':'script', 'tags': 'app,mlperf,inference,generic,_cpp,_retinanet,_onnxruntime,_cpu', 'adr': \
    {'python': {'version_min': '3.8'}, 'compiler': {'tags': "gcc"}, 'openimages-preprocessed': {'tags': '_500'}}, 'scenario': 'Offline', \
    'mode': 'accuracy', 'test_query_count': '10', 'rerun', 'quiet': 'yes'})
checks.check_return(r)

r = cm.access({'action':'run', 'automation':'script', 'tags': 'app,mlperf,inference,generic,_cpp,_retinanet,_onnxruntime,_cpu', 'adr': \
    {'python': {'version_min': '3.8'}, 'compiler': {'tags': "gcc"}, 'openimages-preprocessed': {'tags': '_500'}}, 'scenario': 'Offline', \
    'mode': 'performance', 'test_query_count': '10', 'rerun', 'quiet': 'yes'})
checks.check_return(r)

r = cm.access({'action':'run', 'automation':'script', 'tags': 'install,python-venv', 'version': '3.10.8', 'name': 'mlperf' })
checks.check_return(r)

r = cm.access({'action':'run', 'automation':'script', 'tags': 'run,mlperf,inference,generate-run-cmds,_submission,_short,_dashboard', 'adr': \
        {'python': {'name': 'mlperf', 'version_min': '3.8'}, 'compiler': {'tags': "gcc"}, 'openimages-preprocessed': {'tags': '_500'}}, 'submitter': 'Community', \
        'implementation': 'cpp', 'hw_name': 'default', 'model': 'retinanet', 'backend': 'onnxruntime', 'device': 'cpu', 'scenario': 'Offline', \
        'test_query_count': '10', 'clean', 'quiet': 'yes'})
checks.check_return(r)

r = cm.access({'action':'run', 'automation':'script', 'tags': 'run,mlperf,inference,generate-run-cmds', 'adr': \
        {'python': {'name': 'mlperf', 'version_min': '3.8'}}, 'submitter': 'Community', \
        'implementation': 'python', 'hw_name': 'default', 'model': 'resnet50', 'backend': 'tvm-onnx', 'device': 'cpu', 'scenario': 'Offline', \
        'mode': 'accuracy', 'test_query_count': '5', 'clean', 'quiet': 'yes'})
checks.check_return(r)

r = cm.access({'action':'run', 'automation':'script', 'tags': 'run,mlperf,inference,generate-run-cmds', 'adr': \
        {'python': {'name': 'mlperf', 'version_min': '3.8'}, 'tvm': {'tags': '_pip-install'}}, 'submitter': 'Community', \
        'implementation': 'python', 'hw_name': 'default', 'model': 'resnet50', 'backend': 'tvm-onnx', 'device': 'cpu', 'scenario': 'Offline', \
        'mode': 'accuracy', 'test_query_count': '5', 'clean', 'quiet': 'yes'})
checks.check_return(r)

r = cm.access({'action':'run', 'automation':'script', 'tags': 'run,mlperf,inference,generate-run-cmds,_submission,_dashboard', 'adr': \
        {'python': {'name': 'mlperf', 'version_min': '3.8'}}, 'submitter': 'Community', \
        'implementation': 'python', 'hw_name': 'default', 'model': 'resnet50', 'backend': 'tvm-onnx', 'device': 'cpu', 'scenario': 'Offline', \
        'test_query_count': '500', 'clean', 'quiet': 'yes'})
checks.check_return(r)

