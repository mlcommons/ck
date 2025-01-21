#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

from cmind import utils
import os
import subprocess


def preprocess(i):

    env = i['env']

    if str(env.get('CM_DETECT_USING_HIP-PYTHON', '')
           ).lower() in ["1", "yes", "true"]:
        i['run_script_input']['script_name'] = 'detect'

    return {'return': 0}


def postprocess(i):

    env = i['env']
    state = i['state']

    os_info = i['os_info']

    r = utils.load_txt(file_name='tmp-run.out',
                       check_if_exists=True,
                       split=True)
    if r['return'] > 0:
        return r

    lst = r['list']

    # properties
    p = {}
    gpu = {}

    gpu_id = -1

    for line in lst:
        # print (line)

        j = line.find(':')

        if j >= 0:
            key = line[:j].strip()
            val = line[j + 1:].strip()

            if key == "GPU Device ID":
                gpu_id += 1
                gpu[gpu_id] = {}

            if gpu_id < 0:
                continue

            gpu[gpu_id][key] = val
            p[key] = val

            key_env = 'CM_ROCM_DEVICE_PROP_' + key.upper().replace(' ', '_')
            env[key_env] = val

    state['cm_rocm_num_devices'] = gpu_id + 1
    env['CM_ROCM_NUM_DEVICES'] = gpu_id + 1

    state['cm_rocm_device_prop'] = p
    state['cm_rocm_devices_prop'] = gpu

    return {'return': 0}
