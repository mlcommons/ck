from cmind import utils
import os
import subprocess
import sys

def install(package):
    additional_install_options = []
    r = subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, capture_output=True)
    r = r.stdout.decode("utf-8")
    if "pip" in r:
        out_split = r.split(" ")
        if len(out_split) < 2:
            return {'return': 1, 'error': 'Pip version detection failed'}
        pip_version = out_split[1].split(".")
        if pip_version and len(pip_version) > 1 and int(pip_version[0]) >= 23:
            additional_install_options.append("--break-system-packages")
    run_cmd = [sys.executable, "-m", "pip", "install", package]
    run_cmd += additional_install_options
    r = subprocess.run(run_cmd, check=True)
 
    return {'return':0}

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    if env.get('CM_PIP_PACKAGE_NAME', '') != '':
        r = install(env['CM_PIP_PACKAGE_NAME'])
        if r['return'] > 0:
            return r

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
