# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']
    tmp = i['tmp']

    misc = i['misc']
    console = misc.get('console', False)
    self_meta = misc['meta']
    run_cmd = misc['helpers']['run_cmd']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    env = _input2.get('env', {})

    cmd = _input.get('cmd', '')

    bin_docker = tmp['sys_tool_docker_with_path2']

    cmd = f'{bin_docker} images {cmd}'

    r = run_cmd(cmind, console, cmd, env, None, state = state, verbose = verbose)
    if r['return']>0: return cmind.embed_error(r)

    return {'return':0}
