import sys
import os
import cmind as cm
import check as checks
import json
import yaml

files=sys.argv[1:]

for file in files:
    filename = os.path.basename(file)
    if not filename.endswith("_cm.json") and not filename.endswith("_cm.yaml"):
        continue
    if not str(file).startswith(os.path.join("cm-mlops", "script")):
        continue
    script_path = os.path.dirname(file)
    f = open(file)
    if f.endswith(".json"):
        data = json.load(f)
    elif f.endswith(".yaml"):
        data = yaml.safe_load(f)
    uid = data['uid']

    r = cm.access({'action':'doc', 'automation':'script', 'artifact': uid, 'quiet': 'yes'})
    checks.check_return(r)
