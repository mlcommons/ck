from cmind import utils
import os
import copy

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    state = i['state']
    
    # Check selected target type (must be defined)
    target_type = env['CM_TARGET_DEVICE_ENV_TYPE'] 

    name = env.get('CM_NAME','')
    add_extra_cache_tags=[]
    if name == '':
        name = target_type
        add_extra_cache_tags.append('name-'+name)

    # Check target ENV depending on selected device
    if target_type == 'cpu':
        new_env={}
        for k in env:
            if k.startswith('CM_HOST_'):
                new_env['CM_TARGET_DEVICE_ENV_'+k[8:]]=env[k]

        if 'host_device_raw_info' in state:
                state['target_device_raw_info']=copy.deepcopy(state['host_device_raw_info'])
        
    elif target_type == 'cuda':
        new_env={}
        for k in env:
            if k.startswith('CM_CUDA_DEVICE'):
                new_env['CM_TARGET_'+k[3:]]=env[k]

        env.update(new_env)

        if 'cm_cuda_device_prop' in state:
            state['target_device_cuda_prop']=copy.deepcopy(state['cm_cuda_device_prop'])
        
    
    return {'return':0, 'add_extra_cache_tags':add_extra_cache_tags}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']

    state = i['state']

    # We are in the CM cache entry now
    env['CM_TARGET_DEVICE_PATH']=os.getcwd()

    return {'return':0}
