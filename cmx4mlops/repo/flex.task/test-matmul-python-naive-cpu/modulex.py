# Author and developer: Grigori Fursin

from cmind import utils
import os

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']

    misc = i['misc']
    state = i['state']
    env = i['env']
    tmp = i['tmp']

    cmx = state['cmx']
    run_cmd = misc['helpers']['run_cmd']
    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    ###################################################################
    # Prepare main input
    _input = i['input']

    n = _input.get('n', '')
    if n != '':
        env['CMX_MATMUL_DIM_N'] = n
        env['CMX_MATMUL_DIM_M'] = n
        env['CMX_MATMUL_DIM_K'] = n

    # Check device (either from select-compute or forced)
    profile = _input.get('profile', False)

    if profile:
        profile_nsys = _input.get('profile_nsys', False)

        if profile_nsys:
            nsys_profile_cmd_prefix = tmp['nsys_profile_cmd_prefix']

            env['CMX_RUN_CMD_PREFIX'] = nsys_profile_cmd_prefix

    return {'return':0}
