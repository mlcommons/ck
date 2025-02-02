import sys
import os
import cmind as cm
import check as checks
import json
import yaml

files = sys.argv[1:]

for file in files:
    print(file)
    if not os.path.isfile(file) or not "script" in file:
        continue
    if not file.endswith("_cm.json") and not file.endswith("_cm.yaml"):
        continue
    script_path = os.path.dirname(file)
    f = open(file)
    if file.endswith(".json"):
        data = json.load(f)
    elif file.endswith(".yaml"):
        data = yaml.safe_load(f)
    if data.get('uid', '') == '':
        continue  # not a CM script meta
    uid = data['uid']

    ii = {
        'action': 'test', 'automation': 'script', 'artifact': uid, 'quiet': 'yes', 'out': 'con'
    }
    if os.environ.get('DOCKER_CM_REPO', '') != '':
        ii['docker_cm_repo'] = os.environ['DOCKER_CM_REPO']
    if os.environ.get('DOCKER_CM_REPO_BRANCH', '') != '':
        ii['docker_cm_repo_branch'] = os.environ['DOCKER_CM_REPO_BRANCH']
    if os.environ.get('TEST_INPUT_INDEX', '') != '':
        ii['test_input_index'] = os.environ['TEST_INPUT_INDEX']
    print(ii)
    r = cm.access(ii)

    checks.check_return(r)
