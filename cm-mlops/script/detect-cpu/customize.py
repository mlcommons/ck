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
    # Unifying some CPU info across different platforms
    unified_env = {'CM_CPUINFO_CPUs':'CM_HOST_TOTAL_CORES',
            'CM_CPUINFO_hw.physicalcpu': 'CM_HOST_TOTAL_PHYSICAL_CORES',
            'CM_CPUINFO_hw.logicalcpu': 'CM_HOST_TOTAL_CORES',
            'CM_CPUINFO_hw.packages': 'CM_HOST_SOCKETS',
            'CM_CPUINFO_hw.memsize': 'CM_HOST_MEMSIZE',
            'CM_CPUINFO_hw.l1icachesize': 'CM_HOST_L1I_CACHE_SIZE',
            'CM_CPUINFO_hw.l1dcachesize': 'CM_HOST_L1D_CACHE_SIZE',
            'CM_CPUINFO_hw.l2cachesize': 'CM_HOST_L2_CACHE_SIZE'
            }

    if env['CM_HOST_OS_TYPE'] == 'linux':
        vkeys = [ 'Architecture', 'Model name', 'Vendor ID', 'CPU family', 'NUMA node(s)', 'CPU(s)', \
                'On-line CPU(s) list', 'Socket(s)', 'Thread(s) per core', 'L1d cache', 'L1i cache', 'L2 cache', \
                'L3 cache', 'CPU max MHz' ]
    elif env['CM_HOST_OS_FLAVOR'] == 'macos':
        vkeys = [ 'hw.physicalcpu', 'hw.logicalcpu', 'hw.packages', 'hw.ncpu', 'hw.memsize', 'hw.l1icachesize', \
                'hw.l2cachesize' ]
    if vkeys:
        for s in ss.split('\n'):
            v = s.split(':')
            key = v[0]
            if key in vkeys:
                env_key = 'CM_CPUINFO_'+key.replace(" ","_").replace('(','').replace(')','').replace('-','_').replace('.','_')
                if env_key in unified_env:
                    env[unified_env[env_key]]=v[1].strip()
                else:
                    env[env_key] = v[1].strip()

    return {'return':0}
