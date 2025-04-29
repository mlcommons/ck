# Author and developer: Grigori Fursin

from cmind import utils
import os

def run(i):

    ###################################################################
    # Prepare flow

    misc = i['misc']
    run_cmd = misc['helpers']['run_cmd']

    cmind = i['cmind']
    state = i['state']
    tmp = i['tmp']

    cmx = state['cmx']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    # Prepare aux inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    quiet = _input2.get('quiet', False)

    env = _input2.get('env', {})

    # Prepare main input
    _input = i['input']

    # Check device (either from select-compute or forced)
    device = _input.get('device', '')

    if device == '':
        device = state['cmx']['use_compute']['target_device']

    hf_model_path = _input.get('hf_model_path', '')

    cur_dir = os.getcwd()

    # Prepare cmd
    python_path = state['cmx']['sys_tool_python']['sys_tool_python_with_path2']

    cmd = f'vllm serve {hf_model_path}'

    r = run_cmd(cmind, console, cmd, env, None, state = state, verbose = verbose, print_cmd = True)
    if r['return']>0: return r


    return {'return':0}
