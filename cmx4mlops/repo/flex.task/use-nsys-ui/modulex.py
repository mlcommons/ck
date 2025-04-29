# Author and developer: Grigori Fursin

from cmind import utils
import os

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']

    misc = i['misc']
    run_cmd = misc['helpers']['run_cmd']

    state = i['state']
    tmp = i['tmp']

    cmx = state['cmx']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    ###################################################################
    # Prepare aux input
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    # Prepare main input
    _input = i['input']

    # Check device (either from select-compute or forced)
    input_file = _input.get('input', '')

    ###################################################################
    # Prepare cmd
    nsys_ui_path = state['cmx']['sys_tool_nsys_ui']['sys_tool_nsys_ui_with_path2']

    cmd = nsys_ui_path

    if input_file != '':
        cmd += f' {input_file}'

    r = run_cmd(cmind, console, cmd, {}, None, state = state, verbose = verbose, capture_output = False, print_cmd = True)
    if r['return']>0: return cmind.embed_error(r)

    return {'return':0}
