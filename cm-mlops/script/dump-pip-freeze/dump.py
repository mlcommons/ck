import os
from pip._internal.operations import freeze

if os.path.isfile('tmp-pip-freeze'):
    os.remove('tmp-pip-freeze')

pkgs = freeze.freeze()

x = ''

try:
    for pkg in pkgs:
        x+=pkg+'\n'
except:
    pass

if len(x)>0:
    with open('tmp-pip-freeze', "w") as f:
        f.write(x)
