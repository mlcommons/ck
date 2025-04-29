# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    misc = i['misc']
    cmind = i['cmind']
    state = i['state']
    tmp = i['tmp']
    env = i['env']
 
    cmx = state['cmx']
 
    out = misc.get('out', '')
    console = misc.get('console', False)

    task_path = misc['task_path']

    self_meta = misc['meta']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    device = _input.get('device', '')

    # Check device (either from select-compute or forced)
    if device == '':
        device = tmp['target_pytorch_device']

    env['CMX_PYTORCH_DEVICE'] = device

    # Check device (either from select-compute or forced)
    profile = _input.get('profile', False)

    cmd_prefix = ''
    if profile:
        profile_nsys = _input.get('profile_nsys', False)

        if profile_nsys:
            cmd_prefix = tmp['nsys_profile_cmd_prefix'] + ' '

    python_app = os.path.join(task_path, 'src', 'test.py')

    path_to_python = cmx['sys_tool_python']['sys_tool_python_with_path2']

    cmd = f"""{cmd_prefix}{path_to_python} {python_app}"""

    r = run_cmd(cmind, console, cmd, env, None, state = state, verbose = verbose, capture_output = False, print_cmd = True)
    if r['return']>0: return cmind.embed_error(r)

    return r
