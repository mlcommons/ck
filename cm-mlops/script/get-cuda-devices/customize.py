from cmind import utils
import os
import subprocess

def postprocess(i):

    env = i['env']
    state = i['state']

    os_info = i['os_info']

    r = utils.load_txt(file_name='tmp-run.out',
                       check_if_exists = True,
                       split = True)
    if r['return']>0: return r

    lst = r['list']

    # properties
    p = {}

    for line in lst:
        print (line)

        j = line.find(':')
        if j>=0:
           key = line[:j].strip()
           val = line[j+1:].strip()

           p[key] = val

           key_env = 'CM_CUDA_DEVICE_PROP_'+key.upper().replace(' ','_')
           env[key_env] = val

    state['cm_cuda_device_prop'] = p

    return {'return':0}
