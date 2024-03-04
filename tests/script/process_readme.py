import sys
import os
import cmind as cm
import check as checks
import json
import yaml

files=sys.argv[1:]

for file in files:
    if not os.path.isfile(file):
        continue
    if not file.endswith("_cm.json") and not file.endswith("_cm.yaml"):
        continue
    if not file.startswith(os.path.join("cm-mlops", "script")):
        continue
    script_path = os.path.dirname(file)
    f = open(file)
    if file.endswith(".json"):
        data = json.load(f)
    elif file.endswith(".yaml"):
        data = yaml.safe_load(f)
    uid = data['uid']

    r = cm.access({'action':'doc', 'automation':'script', 'artifact': uid, 'quiet': 'yes'})
    checks.check_return(r)
