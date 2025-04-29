# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']

    rt_cached = state['cmx'].get('detect_pycuda_info', {})
    if len(rt_cached)>0: return rt_cached

    tmp = i['tmp']

    misc = i['misc']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']


    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    env = _input2.get('env', {})
    timeout = _input.get('timeout', None)


    # Prepare CMD to run program
    run_cmd = misc['helpers']['run_cmd']

    python_path = state['cmx']['sys_tool_python']['sys_tool_python_with_path2']

    code_path = os.path.join(self_path, 'src', 'detect.py')

    cmd = f'{python_path} {code_path}'

    r = run_cmd(cmind, console, cmd, env, timeout,
                state = state, verbose = verbose,
                cmd_prefix_from_state = [])

    rrr = {'return':0, 'raw_output':r}

    state['cmx']['detect_pycuda_info'] = rrr

    return rrr
