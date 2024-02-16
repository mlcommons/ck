import os
from pip._internal.operations import freeze

pip_freeze_out = os.environ.get('CM_DUMP_RAW_PIP_FREEZE_FILE_PATH', 'tmp-pip-freeze')

if os.path.isfile(pip_freeze_out):
    os.remove(pip_freeze_out)

pkgs = freeze.freeze()

x = ''

try:
    for pkg in pkgs:
        x+=pkg+'\n'
except:
    pass

if len(x)>0:
    with open(pip_freeze_out, "w") as f:
        f.write(x)
