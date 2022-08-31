from cmind import utils
import os

lscpu_out = 'tmp-lscpu.out'

def preprocess(i):

    if os.path.isfile(lscpu_out):
        os.remove(lscpu_out)

    return {'return':0}


def postprocess(i):

    state = i['state']

    env = i['env']

    if not os.path.isfile(lscpu_out):
        return {'return':1, 'error':'{} was not generated'.format(lscpu_out)}

    r = utils.load_txt(file_name=lscpu_out)

    if r['return']>0: return r

    ss = r['string']

    state['cpu_info_raw'] = ss

    print ('')

    if env['CM_HOST_OS_TYPE'] == 'linux':
        vkeys = [ 'Architecture', 'Model name', 'Vendor ID', 'CPU family', 'NUMA node(s)', 'CPU(s)', \
                'On-line CPU(s) list', 'Socket(s)', 'Thread(s) per core', 'L1d cache', 'L1i cache', 'L2 cache', \
                'L3 cache', 'CPU max MHz']
        for s in ss.split('\n'):
            v = s.split(':')
            key = v[0]
            if key in vkeys:
                env['CM_CPUINFO_'+key.replace(" ","_").replace('(','').replace(')','').replace('-','_')] = v[1].strip()

    # Unifying some CPU info across different platforms
    unified_env = {'CM_CPUINFO_CPUs':'CM_HOST_TOTAL_CORES'}
    for env_key in unified_env:
        if env_key in env:
            env[unified_env[env_key]]=env[env_key]

    return {'return':0}
