from cmind import utils
import os
import subprocess
import sys

def install(package):
    subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    if env.get('CM_PIP_PACKAGE_NAME', '') != '':
        install(env['CM_PIP_PACKAGE_NAME'])

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
