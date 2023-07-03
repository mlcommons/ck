# This test covers version, variation, compilation from src, add_deps, add_deps_recursive, deps, post_deps

import cmind as cm

from pathlib import Path
import sys
import os

sys.path.insert(1, os.path.join(Path(__file__).parent.parent.resolve(), "script"))
import check as checks

r = cm.access({'action':'run', 'automation':'script', 'tags': 'run,mlperf,inference,generate-run-cmds', 'adr': \
    {'python': {'name': 'mlperf', 'version_min': '3.8'}, 'tvm': {'tags': '_pip-install'}}, 'submitter': 'Community', \
    'implementation': 'python', 'hw_name': 'default', 'model': 'resnet50', 'backend': 'tvm-onnx', 'device': 'cpu', 'scenario': 'Offline', \
    'mode': 'accuracy', 'test_query_count': '5', 'clean': 'true', 'quiet': 'yes'})
checks.check_return(r)

r = cm.access({'action':'run', 'automation':'script', 'tags': 'run,mlperf,inference,generate-run-cmds,_submission,_short,_dashboard', 'adr': \
    {'python': {'name': 'mlperf', 'version_min': '3.8'}, 'tvm': {'tags': '_pip-install'}}, 'submitter': 'Community', \
    'implementation': 'python', 'hw_name': 'default', 'model': 'resnet50', 'backend': 'tvm-onnx', 'device': 'cpu', 'scenario': 'Offline', \
    'test_query_count': '500', 'clean': 'true', 'quiet': 'yes'})
checks.check_return(r)

